from PySide6 import QtWidgets, QtCore, QtGui
from libs.translate import Result
from libs.io import io
import os

TOP = QtWidgets.QAbstractItemView.ScrollHint.PositionAtTop

class BaseListWidget(QtWidgets.QListWidget):

    def update(self):
        r = self.statusTip().split()[0]
        n = self.count()
        self.setStatusTip(f'{r} ({n})' if n > 0 else r)
    
    def addItem(self, item):
        super().addItem(item)
        self.update()

class LItem(QtWidgets.QListWidgetItem):
    def __init__(self, result:Result, lang):
        super().__init__(result.word)
        self.word = result.word
        self.setBackground(QtGui.QColor(255, 100, 100, 30) if result.online else QtGui.QColor(100, 255, 255, 30))
        self.result = result
        self.lang = lang
        self.update()

    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, lang):
        self._lang = lang
        self.setToolTip(self.result.get_translation(lang))

    @property
    def top(self):
        return self.result.top
    
    @top.setter
    def top(self, value):
        self.result.top = value
        self.update()

    def update(self):
        self.setText('*'+self.word if self.top else self.word)

    def __str__(self):
        return self.result.get_translation(self.lang)

class Bank(BaseListWidget):

    def top(self):
        for item in self.selections:
            item.top = not item.top
        self.scrollToItem(self.current, TOP)

    def append(self, result:Result|list[Result]):
        if isinstance(result, list):
            for r in result:
                self.append(r)
            self.scrollToTop()
        else:
            if result in self.results:
                self.roll(result.word)
                return
            item = LItem(result, self.lang)
            self.addItem(item)
            self.scrollToItem(item, TOP)
        
    def remove(self):
        for item in self.selections:
            row = self.row(item)
            self.takeItem(row)
        self.update()

    def roll(self, word:str):
        if word:
            word = word.lower()
            for i in self.items:
                if i.word.startswith(word):
                    self.scrollToItem(i, TOP)
                    return
        self.scrollToItem(self.current, TOP)

    def clear(self):
        super().clear()
        self.update()

    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, lang):
        self._lang = lang
        for i in self.items:
            i.lang = lang

    @property
    def items(self) -> list[LItem]:
        return [self.item(i) for i in range(self.count())]

    @items.setter
    def items(self, items:LItem):
        self.clear()
        for i in items:
            self.addItem(i)
        self.scrollToTop()

    @property
    def selections(self) -> list[LItem]:
        return self.selectedItems()

    @property
    def current(self) -> LItem:
        return self.currentItem()

    @current.setter
    def current(self, item:LItem):
        self.setCurrentItem(item)

    @property
    def results(self):
        return [i.result for i in self.items]
    
    @results.setter
    def results(self, results):
        self.items = [LItem(i, self.lang) for i in results]

    @property
    def words(self):
        return [i.word for i in self.items]

class FItem(QtWidgets.QListWidgetItem):
    _results = None
    _saved = False
    _file = ''
    _name = ''
    on_display = False

    def __init__(self, file:str):
        super().__init__()
        self.file = os.path.abspath(file)
        self.setBackground(QtGui.QColor(255, 100, 255, 30))
    
    @property
    def file(self):
        return self._file
    
    @file.setter
    def file(self, file:str):
        self._file = file.replace('\\', '/')
        self.name = self.file.split('/')[-1]
        self.setToolTip(self.file)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name
        self.setText(name)

    @property
    def results(self):
        if self._results is None:
            self.load()
        return self._results
    
    @results.setter
    def results(self, results):
        self._results = results
    
    @property
    def saved(self):
        return self._saved
    
    @saved.setter
    def saved(self, value):
        self.setText(self.name if value else '*'+self.name)
        self._saved = value

    def exists(self, file=None):
        return os.path.exists(file if file else self.file)

    def load(self):
        if self.exists():
            self.results = io.read_vocabulary(self.file)
            self.saved = True
        else: self.results = []
    
    def save(self, file=None):
        if not self.saved:
            file = file if file else self.file
            if not self.exists(file):
                file = QtWidgets.QFileDialog.getSaveFileName(None, 'Save as ...', file, '*.tvf')[0]
                if file: self.file = file
                else: return
            io.save_vocabulary(self.results, file)
            self.saved = True

class Files(BaseListWidget):

    def __init__(self, parent, bank:Bank):
        super().__init__(parent)
        self.bank = bank

    def load(self, file:str|list[str]):
        if isinstance(file, list):
            return [self.load(f) for f in file]
        else:
            file = os.path.abspath(file).replace('\\', '/')
            for item in self.items:
                if item.file == file:
                    item.load()
                    return item
            item = FItem(file)
            self.addItem(item)
            return item

    def remove(self):
        self.takeItem(self.row(self.current))
        if not self.current:
            self.bank.clear()
        self.update()

    def keep(self):
        self.current.results = self.bank.results
        self.current.saved = False

    def new(self, fn=None):
        if not fn:
            fn = 'untitled%s.tvf'
            lfn = lambda fn:fn in self.names or os.path.exists(fn)
            if lfn(fn%''):
                i = 2
                while lfn(fn%f'({i})'):
                    i += 1
                fn = fn%f'({i})'
            else: fn = fn%''
        self.addItem(FItem(fn))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event:QtGui.QDropEvent):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.load(url.toLocalFile())
        else:
            event.ignore()
    
    @property
    def items(self) -> list[FItem]:
        return [self.item(i) for i in range(self.count())]

    @property
    def files(self):
        return [i.file for i in self.items]

    @property
    def names(self):
        return [i.name for i in self.items]

    @property
    def selections(self) -> list[FItem]:
        return self.selectedItems()

    @property
    def current(self) -> FItem:
        item = self.currentItem()
        if not item:
            items = self.items
            if items:
                item = items[0]
                self.current = item
        return item
    
    @current.setter
    def current(self, item:FItem):
        self.setCurrentItem(item)

    def clear(self):
        super().clear()
        self.bank.clear()



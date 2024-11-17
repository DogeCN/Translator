from PySide6.QtWidgets import QMessageBox, QMainWindow
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QAction
from libs.translate.dict import Dictionary, load_dict
from libs.ui.main import Ui_MainWindow
from libs.ui.main.base import FItem
from libs.translate import Result
from libs.config import Setting
from libs.io import dialog
from win32com.client import Dispatch
from threading import Thread
from time import sleep
import webbrowser, win32clipboard, info

class LSignal(QObject):
    set_result_singal = Signal()
    callback_singal = Signal()
    show_dicts_singal = Signal(list)
    expand_phrases_singal = Signal(Result)
    def __init__(self):
        super().__init__()

class LMain(Ui_MainWindow):
    text_changed = False
    _voice = Dispatch('SAPI.SpVoice')
    _result = Result()
    signal = LSignal()
    dl_thread = Thread()
    phrases = None
    closing = False
    parent = None
    raw = None

    def load_dicts(self):
        if self.dl_thread.is_alive(): return
        self.dl_thread = Thread(target=lambda:self.signal.show_dicts_singal.emit(load_dict(self.signal.callback_singal.emit)))
        self.dl_thread.start()
    def save_all(self, silent=True):
        for item in self.Files.items: item.save(silent)
    def append(self, result): self.Bank.append(result); self.Files.keep()
    def close(self): self.closing = True; self.parent.close()
    def remove(self): self.Bank.remove(); self.Files.keep()
    def top(self): self.Bank.top(); self.Files.keep()
    def set_expand(self, results): self.Expand.results = results

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.parent = MainWindow
        self.raw = QMainWindow(MainWindow)
        self.raw.setStyleSheet(info.StlSheets['raw'])
        Thread(target=self.handle_phrases).start()
        self.connect_actions()
    
    def connect_actions(self):
        #Menu Actions
        self.actionNew.triggered.connect(lambda:self.Files.new())
        self.actionReload.triggered.connect(lambda:(lambda item:item.load() or self._display_file(item) if item else self.load())(self.Files.current))
        self.actionDict_Reload.triggered.connect(self.load_dicts)
        self.actionLoad.triggered.connect(lambda:(lambda f:self._display_file(self.Files.load(f)[0]) if f else ...)(dialog.OpenFiles(self.parent, Setting.getTr('load'), info.ext_all_tvf)))
        self.actionSave.triggered.connect(lambda:self.Files.current.save())
        self.actionSave_All.triggered.connect(lambda:self.save_all(False))
        self.actionSave_As.triggered.connect(lambda:self.Files.current.save_as())
        self.actionRemove.triggered.connect(self.Files.remove)
        self.actionClear.triggered.connect(self.Files.clear)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(lambda:webbrowser.open(info.url_repo))
        self.actionAboutQt.triggered.connect(lambda:QMessageBox.aboutQt(self.raw))
        #Button Actions
        self.Add.clicked.connect(self.command_add)
        self.Delete.clicked.connect(self.remove)
        self.Top.clicked.connect(self.top)
        #Text
        self.Word_Entry.textChanged.connect(self.text_change)
        self.Translated_text.mouseDoubleClickEvent = self.correct
        self.Phonetic.mouseDoubleClickEvent = lambda *evt:Thread(target=lambda:self._voice.Speak(self.Word_Entry.text()) if self.result else ..., daemon=True).start()
        #List Widgets
        self.Files.itemSelectionChanged.connect(self.display_file)
        self.Bank.itemSelectionChanged.connect(self.display_selection)
        self.Exchanges.itemSelectionChanged.connect(self.display_exchanges)
        self.Expand.itemSelectionChanged.connect(self.display_phrases)
        #Signal
        self.signal.set_result_singal.connect(self.set_result)
        self.signal.show_dicts_singal.connect(self.show_dictionaries)
        self.signal.callback_singal.connect(lambda:QMessageBox.warning(self.raw, Setting.getTr('warning'), Setting.getTr('translate_function_unavailable')))
        self.signal.expand_phrases_singal.connect(self.set_expand)

    def setShotcuts(self):
        self.Add.setShortcut(Setting.Key_Add)
        self.Delete.setShortcut(Setting.Key_Del)
        self.Top.setShortcut(Setting.Key_Top)

    @property
    def result(self):
        return self._result
    
    @result.setter
    def result(self, result:Result):
        self._result = result
        word = result.word
        self.Translated_text.setText(result.get_translation(Setting.Language))
        self.Translated_text.setToolTip(result.get_definition(Setting.Language))
        self.Phonetic.setText(result.phonetic)
        if word in self.Bank.words or not result:
            self.Add.setEnabled(False)
        else:
            self.Add.setEnabled(True)

    def show_dictionaries(self, dicts:list[Dictionary]):
        for a in self.menuDicts.actions():
            if a.isCheckable():
                self.menuDicts.removeAction(a)
        for d in dicts:
            action = QAction(Setting.translateUI(d.name, dict([reversed(dn) for dn in info.dict_names])), self.parent)
            action.setCheckable(True)
            action.setChecked(True)
            action.triggered.connect(lambda *x, _d=d, a=action:_d.setEnabled(a.isChecked()))
            self.menuDicts.addAction(action)

    def correct(self, *evt):
        result = self.result
        if result.match:
            self.Word_Entry.setText(result.word)
            result.match = False
        elif result:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(result.get_translation(Setting.Language))
            win32clipboard.CloseClipboard()

    def set_result(self):
        result = self.result
        if result.match:
            self.Translated_text.setText(result.get_tip(Setting.Language))
            self.Translated_text.setToolTip(Setting.getTr('correct_hint'))
            return   
        if result:
            self.Phonetic.setToolTip(info.match_hint % Setting.getTr('speech_hint'))
        self.result = result
        self.Exchanges.results = result.exchanges
        self.phrases = result.phrases

    def handle_phrases(self):
        while info.prog_running:
            if self.parent.isActiveWindow():
                if self.phrases:
                    phrases = []
                    for p in self.phrases:
                        phrases.append(p)
                        if self.text_changed:
                            break
                    else:
                        self.signal.expand_phrases_singal.emit(phrases)
                        self.phrases = None
                sleep(0.05)
            else:
                sleep(0.5)

    def text_change(self):
        self.text_changed = True
        self.Add.setEnabled(False)
        self.Translated_text.setText('')
        self.Translated_text.setToolTip('')
        self.Phonetic.setText('')
        self.Phonetic.setToolTip('')

    def command_add(self):
        self.append(self.result)
        self.Word_Entry.setText('')
        self.Add.setEnabled(False)
        self.Files.keep()

    def load(self, file:str|list[str]=None):
        if not file:
            file = Setting.Vocabulary
        self.Files.load(file)
        self.display_file()

    def display_selection(self):
        items = self.Bank.selections
        if items:
            self.Delete.setEnabled(True)
            self.Top.setEnabled(True)
            item = self.Bank.current
            item = item if item else items[-1]
            self.Word_Entry.setText(item.word)
        else:
            self.Delete.setEnabled(False)
            self.Top.setEnabled(False)
    
    def display_exchanges(self):
        items = self.Exchanges.selections
        if items:
            item = self.Exchanges.current
            item = item if item else items[-1]
            self.Word_Entry.setText(item.word)
    
    def display_phrases(self):
        items = self.Expand.selections
        if items:
            item = self.Expand.current
            item = item if item else items[-1]
            self.Word_Entry.setText(item.word)

    def display_file(self):
        item = self.Files.current
        if not item.on_display:
            self._display_file(item)

    def _display_file(self, item:FItem):
        for i in self.Files.items:
            i.on_display = False
        item.on_display = True
        self.Bank.results = item.results

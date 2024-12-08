from PySide6.QtWidgets import QMessageBox, QMainWindow
from PySide6.QtCore import Signal, QObject
from libs.translate.dict import load_lexi
from libs.ui.main import Ui_MainWindow
from libs.ui.main.base import FItem
from libs.debris import Clipboard
from libs.translate import Result
from libs.config import Setting
from libs.io import dialog
from win32com.client import Dispatch
from threading import Thread
from time import sleep
import webbrowser, info

class LSignal(QObject):
    set_result_singal = Signal()
    callback_singal = Signal()
    set_rbenabled_signal = Signal(bool)
    show_lexis_singal = Signal()
    exchange_singal = Signal(Result)
    expand_singal = Signal(Result)
    def __init__(self):
        super().__init__()

class LMain(Ui_MainWindow):
    text_changed = False
    _voice = Dispatch('SAPI.SpVoice')
    _result = Result()
    signal = LSignal()
    lexi_thread = Thread()
    exchanges = None
    phrases = None
    parent = None
    raw = None

    def load_lexis(self):
        self.lexi_thread = Thread(target=self._load_lexis)
        self.lexi_thread.start()
    def _load_lexis(self):
        self.signal.set_rbenabled_signal.emit(False)
        load_lexi(self.signal.callback_singal.emit)
        self.signal.show_lexis_singal.emit()
        self.signal.set_rbenabled_signal.emit(True)
    def save_all(self, silent=True):
        for item in self.Files.items: item.save(silent)
    def append(self, result): self.Bank.append(result); self.Files.keep()
    def close(self): info.prog_running = False; self.parent.close()
    def remove(self): self.Bank.remove(); self.Files.keep()
    def top(self): self.Bank.top(); self.Files.keep()
    def set_expand(self, results): self.Expand.results = results
    def set_exchanges(self, results): self.Exchanges.results = results

    def __init__(self, MainWindow:QMainWindow):
        super().__init__()
        self.setupUi(MainWindow)
        self.parent = MainWindow
        self.raw = QMainWindow(MainWindow)
        self.raw.setStyleSheet(info.StlSheets['raw'])
        Thread(target=self.handle).start()
        self.connect_actions()
    
    def connect_actions(self):
        #Menu Actions
        self.actionNew.triggered.connect(lambda:self.Files.new())
        self.actionReload.triggered.connect(lambda:(lambda item:item.load() or self._display_file(item) if item else self.load())(self.Files.current))
        self.actionDict_Reload.triggered.connect(self.load_lexis)
        self.actionLoad.triggered.connect(lambda:(lambda f:self._display_file(self.Files.load(f)[0]) if f else ...)(dialog.OpenFiles(self.parent, Setting.getTr('load'), info.ext_all_voca)))
        self.actionSave.triggered.connect(lambda:self.Files.current.save())
        self.actionSave_All.triggered.connect(lambda:self.save_all(False))
        self.actionSave_As.triggered.connect(lambda:self.Files.current.save_as())
        self.actionRemove.triggered.connect(self.Files.remove)
        self.actionClear.triggered.connect(self.Files.clear)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(lambda:webbrowser.open(info.repo_url))
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
        self.signal.callback_singal.connect(lambda:QMessageBox.warning(self.raw, Setting.getTr('warning'), Setting.getTr('translate_function_unavailable')))
        self.signal.exchange_singal.connect(self.set_exchanges)
        self.signal.expand_singal.connect(self.set_expand)

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
        self.Translated_text.setText(result.get_translation())
        self.Translated_text.setToolTip(result.get_definition())
        self.Phonetic.setText(result.phonetic)
        if word in self.Bank.words or not result:
            self.Add.setEnabled(False)
        else:
            self.Add.setEnabled(True)

    def correct(self, *evt):
        result = self.result
        if result.match:
            self.Word_Entry.setText(result.word)
            result.match = False
        elif result:
            Clipboard.Write(result.get_translation())

    def set_result(self):
        result = self.result
        if result.match:
            self.Translated_text.setText(result.get_tip())
            self.Translated_text.setToolTip(Setting.getTr('correct_hint'))
        elif result:
            self.Phonetic.setToolTip(info.speech_hint % Setting.getTr('speech_hint'))
            self.exchanges = result.exchanges
            self.phrases = result.phrases
            self.result = result

    def _handle(self, generator):
        if generator:
            results = []
            for r in generator:
                results.append(r)
                if self.text_changed:
                    return
            return results

    def handle(self):
        while info.prog_running:
            print()
            if self.parent.isActiveWindow():
                if self.Exchanges.height():
                    exchanges = self._handle(self.exchanges)
                    if exchanges is not None:
                        self.signal.exchange_singal.emit(exchanges)
                    self.exchanges = None
                phrases = self._handle(self.phrases)
                if phrases is not None:
                    self.signal.expand_singal.emit(phrases)
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
        self.Exchanges.clear()
        self.Expand.clear()

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

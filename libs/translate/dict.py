from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Signal, QObject
from concurrent.futures import ThreadPoolExecutor
from requests import get
from libs.io.base import load
from libs.config import Setting
import info

pool = ThreadPoolExecutor(3)

class LSignal(QObject):
    update = Signal()

class CSignal(QObject):
    sre = Signal(bool)
    count = 0
    _lock = False

    def add(self):
        self.count += 1
        if self.count == 1 and not self._lock:
            self.sre.emit(False)

    def sub(self):
        self.count -= 1
        if not self.count and not self._lock:
            self.sre.emit(True)
    
    def lock(self):
        self._lock = True
        self.sre.emit(False)
    
    def unlock(self):
        self._lock = False
        if not self.count: self.sre.emit(True)

csignal = CSignal()

class Lexicon(dict[str, list[str, list[str]]]):
    enabled = False
    loaded = False
    failed = False
    box = None
    
    def __init__(self, fn:str):
        self.fn = fn
        self.name = self.name_zh = fn.split('\\')[-1].strip(info.ext_disabled)
        self.signal = LSignal()
    
    @property
    def text(self):
        name = self.name if Setting.Language else self.name_zh
        if self.loaded: hint = len(self)
        elif self.failed: hint = Setting.getTr('loadfailed')
        else: hint = Setting.getTr('unload')
        return f"{name} ({hint})"
    
    def setEnabled(self, enable):
        pool.submit(self._setEnabled, enable)

    def _setEnabled(self, enable):
        csignal.add()
        if enable and not self.loaded:
            try:
                l = load(self.fn)
                self.name = getattr(l, 'name')
                self.name_zh = getattr(l, 'name_zh')
                self.update(l)
                self.loaded = self.enabled = True
                self.failed = False
                self.signal.update.emit()
            except:
                self.failed = True
                self.signal.update.emit()
                csignal.sub()
                return
        fn = self.fn.strip(info.ext_disabled)
        if not enable:
            fn = fn + info.ext_disabled
            self.enabled = False
        if self.fn != fn:
            info.os.rename(self.fn, fn)
            self.fn = fn
        csignal.sub()

class LexiBox(QCheckBox):
    def __init__(self, lexicon:Lexicon, parent):
        super().__init__(parent)
        lexicon.signal.update.connect(self.update)
        self.toggled.connect(lexicon.setEnabled)
        self.lexicon = lexicon
        self.update()
    
    def update(self):
        super().setText(self.lexicon.text)
        self.setChecked(self.lexicon.enabled)
        if self.lexicon.failed: self.setStyleSheet(info.StlSheets['red'])
        elif self.lexicon.loaded: self.setStyleSheet(info.StlSheets['green'])
        else: self.setStyleSheet('')

lexicons = [] #type: list[Lexicon]

def getfile(name, dir):
    try: request = get(info.lurl_cn % name, stream=True, timeout=info.timeout)
    except: request = get(info.lurl % name, stream=True, timeout=info.timeout)
    with open(dir + name, 'wb') as f:
        for chunk in request:
            f.write(chunk)

def _load_lexis():
    files = info.os.listdir(info.lexis_dir)
    lexicons.clear()
    for f in files:
        enabled = f.endswith(info.ext_lexi)
        disabled = f.endswith(info.ext_lexi + info.ext_disabled)
        if enabled or disabled:
            fn = info.lexis_dir + f
            lexicon = Lexicon(fn)
            lexicon.setEnabled(enabled)
            lexicons.append(lexicon)
    if not lexicons: return True

def load_lexis(callback):
    if _load_lexis():
        print("Downloading ...")
        dlpool = ThreadPoolExecutor()
        csignal.lock()
        for lname in info.default_lexis:
            fname = lname + info.ext_lexi
            dlpool.submit(getfile, fname, info.lexis_dir)
        dlpool.shutdown()
        csignal.unlock()
        if _load_lexis():
            callback()

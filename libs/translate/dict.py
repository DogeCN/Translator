from PySide6.QtWidgets import QCheckBox
from concurrent.futures import ThreadPoolExecutor
from requests import get
from libs.stdout import print
from libs.io.base import load
from libs.config import Setting
import info
import os

class Lexicon(dict[str, list[str, list[str]]]):
    enabled = True
    name = 'New Lexicon'
    name_zh = '新词典'
    
    @property
    def text(self):
        return f"{self.name if Setting.Language else self.name_zh} ({len(self)})"
    
    def setEnabled(self, enable):
        self.enabled = enable

class LexiBox(QCheckBox):
    def __init__(self, lexicon:Lexicon, parent):
        super().__init__(parent)
        self.lexicon = lexicon
        self.setChecked(True)
        self.toggled.connect(lambda e: self.lexicon.setEnabled(e))
        self.retrans()
    
    def retrans(self):
        super().setText(self.lexicon.text)

lexicons = [] #type: list[Lexicon]

def getfile(name, path):
    try:
        request = get(info.lurl_cn % name, stream=True, timeout=info.timeout)
    except:
        request = get(info.lurl % name, stream=True, timeout=info.timeout)
    with open(path, 'wb') as f:
        for chunk in request:
            f.write(chunk)

def _load_lexi():
    global lexicons
    lexicons.clear()
    for f in os.listdir(info.lexis_dir):
        if f.endswith(info.ext_lexi):
            try:
                lexicons.append(load(info.lexis_dir + f))
            except: continue

def load_lexi(callback):
    _load_lexi()
    if not lexicons:
        pool = ThreadPoolExecutor()
        for lname in info.default_lexis:
            fname = lname + info.ext_lexi
            pool.submit(getfile, fname, info.lexis_dir + fname)
        pool.shutdown()
        _load_lexi()
        if not lexicons:
            callback()
        else:
            print(f"Loaded lexicons: {', '.join([d.name for d in lexicons])}", 'Bold')
    return lexicons

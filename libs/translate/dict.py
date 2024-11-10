from concurrent.futures import ThreadPoolExecutor
from requests import get
from libs.io.base import load
import info
import os

class Dictionary(dict[str, list[str, list[str]]]):
    enabled = True
    def __init__(self, dict, name):
        super().__init__(dict)
        self.name = name
    
    def setEnabled(self, enable):
        self.enabled = enable

dictionaries = [] #type: list[Dictionary]

def getfile(name, path):
    try:
        request = get(info.durl_cn % name, stream=True, timeout=3)
    except:
        request = get(info.durl % name, stream=True, timeout=3)
    with open(path, 'wb') as f:
        for chunk in request:
            f.write(chunk)

def _load_dict():
    global dictionaries
    dictionaries.clear()
    for f in os.listdir(info.dicts_dir):
        if f.endswith(info.ext_dict):
            try:
                dictionaries.append(Dictionary(load(info.dicts_dir + f), f[:-4]))
            except: continue

def load_dict(callback):
    _load_dict()
    if not dictionaries:
        pool = ThreadPoolExecutor()
        for dname in info.dnames:
            fname = dname + info.ext_dict
            pool.submit(getfile, fname, info.dicts_dir + fname)
        pool.shutdown()
        _load_dict()
        if not dictionaries:
            callback()
    return dictionaries

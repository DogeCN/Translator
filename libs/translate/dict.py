import os
from libs.io.base import load

class Dictionary(dict):
    enabled = True
    def __init__(self, dict, name):
        super().__init__(dict)
        self.name = name
    
    def setEnabled(self, enable):
        self.enabled = enable

dictionaries = [] #type: list[Dictionary[str, dict[str, list]]]

def load_dict(callback):
    global dictionaries
    dictionaries.clear()
    dpath = os.path.join(os.getcwd(), 'dictionaries')
    try:
        for f in os.listdir(dpath):
            if f.endswith('.tdf'):
                try:
                    dictionaries.append(Dictionary(load(dpath + os.sep + f), f[:-4]))
                except: continue
    except: ...
    if not dictionaries: callback()
    return dictionaries

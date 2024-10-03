from libs.io.base import load
import info
import os

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
    try:
        for f in os.listdir(info.dicts):
            if f.endswith(info.ext_dict):
                try:
                    dictionaries.append(Dictionary(load(info.dicts + os.sep + f), f[:-4]))
                except: continue
    except: ...
    if not dictionaries: callback()
    return dictionaries

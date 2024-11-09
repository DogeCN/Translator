from .io.base import load, dump
import info

data = info.public

class Public(dict):
    def __init__(self, file):
        try:
            self.update(load(file))
        except:
            self['default_path'] = None
    
    @staticmethod
    def _load(file=data):
        global Publics
        Publics = Public(file)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        try:
            dump(data, self)
            print(self['default_path'])
        except: ...

Public._load()

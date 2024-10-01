from .io.base import load, dump
from res.info import Tr
import os

data = os.getenv('AppData') + os.sep + 'setting.tsf'

class Settings:
    def __init__(self, file):
        try:
            self.__dict__ = load(file).__dict__
        except:
            self.Language = 0 #0:zh, 1:en
            self.Vocubulary = 'vocabulary.tvf'
            self.Auto_save = True
            self.Auto_save_interval = 60
            self.Key_Add = 'Ctrl+E'
            self.Key_Del = 'Del'
            self.Key_Top = 'Ctrl+T'

    def getTr(self, key):
        return Tr[key][self.Language]

    @staticmethod
    def _load(file=None):
        global Setting
        if not file:
            file = data
        Setting = Settings(file)

    @staticmethod
    def dump(file=data):
        try:
            dump(file, Setting)
        except: ...

Settings._load()
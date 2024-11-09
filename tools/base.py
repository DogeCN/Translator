from PySide6.QtWidgets import QMessageBox, QMenu
from PySide6.QtGui import QAction, QIcon
from libs.stdout import print
from libs.public import Publics
from libs.io import io, dialog
from tools._base._logic import LMainWindow
from subprocess import Popen
import info

class Action:
    tool = ... #type: Tool
    icon = None #type: QIcon
    visible = True
    enabled = True
    shortcut = ''
    def __call__(self):
        action = QAction(self.tool.get_name(), self.tool.mw)
        action.setStatusTip(self.tool.get_doc())
        action.setVisible(self.visible)
        action.setEnabled(self.enabled)
        action.setShortcut(self.shortcut)
        if self.icon:
            action.setIcon(self.icon)
        action.triggered.connect(lambda *x,_t=self.tool:_t())
        return action

class Menu:
    tool = ... #type: Tool
    tools = [] #type: list[Tool]
    icon = None #type: QIcon
    visible = True
    enabled = True
    def __call__(self):
        for tool in self.tools:
            tool.mw = self.tool.mw
            tool.lang = self.tool.lang
        menu = QMenu(self.tool.get_name(), self.tool.mw.ui.menuBar)
        menu.setVisible(self.visible)
        menu.setEnabled(self.enabled)
        for tool in self.tools:
            action = tool.action()
            action.setParent(menu)
            if tool.type: action.setMenu(action)
            else: menu.addAction(action)
        if self.icon:
            menu.setIcon(self.icon)
        menu.hide()
        return menu

class Message:
    tool = ... #type: Tool
    def _msg(self, info, icon):
        msg = QMessageBox(self.tool.mw)
        msg.setWindowTitle(self.tool.get_name())
        msg.setText(str(info))
        msg.setIcon(icon)
        return msg
    def Show(self, info):
        self._msg(info, QMessageBox.Icon.Information).exec()
    def Warn(self, info):
        self._msg(info, QMessageBox.Icon.Warning).exec()
    def Error(self, info):
        self._msg(info, QMessageBox.Icon.Critical).exec()
    def Ask(self, info):
        msg = self._msg(info, QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec() == QMessageBox.StandardButton.Yes

class Dialog:
    tool = ... #type: Tool
    def OpenDir(self, title=None, dir=None):
        if not title: title = self.tool.get_name()
        return dialog.OpenDir(self.tool.mw, title, dir)
    def OpenFile(self, title=None, type=..., dir=None):
        if not title: title = self.tool.get_name()
        return dialog.OpenFile(self.tool.mw, title, type, dir)
    def OpenFiles(self, title=None, type=..., dir=None):
        if not title: title = self.tool.get_name()
        return dialog.OpenFiles(self.tool.mw, title, type, dir)
    def SaveFile(self, title=None, type=..., dir=None):
        if not title: title = self.tool.get_name()
        return dialog.SaveFile(self.tool.mw, title, type, dir)
    @staticmethod
    def Pop(f):
        return Popen(f'"{f}"', shell=True)

class Data:
    tool = ... #type: Tool
    @property
    def name(self):
        return self.tool.name
    def Set(self, value):
        Publics[self.name] = value
    def Get(self):
        try: return Publics[self.name]
        except: ...
    def Remove(self):
        try: del Publics[self.name]
        except: ...
    def SetItem(self, key, value):
        Publics[self.name][key] = value
    def GetItem(self, key):
        try: return Publics[self.name][key]
        except: ...
    def RemoveItem(self, key):
        try: del Publics[self.name][key]
        except: ...

class Tr:
    tool = ... #type: Tool
    Tr = {}
    def __call__(self, key):
        return self.Tr[key][self.tool.lang]

class Tool:
    mw = ... #type: LMainWindow
    #Basic Infos
    name = 'New Tool'
    name_zh = ''
    doc = 'This is a new tool'
    doc_zh = ''
    lang = 1
    entrance = None
    def __init__(self, type=0):
        self.type = type
        self.action = Menu() if type else Action()
        self.action.tool = self
        self.message = Message()
        self.message.tool = self
        self.dialog = Dialog()
        self.dialog.tool = self
        self.data = Data()
        self.data.tool = self
        self.tr = Tr()
        self.tr.tool = self
    def __call__(self, *args):
        if self.entrance: self.entrance(*args)
        else: print(f"Can't find an entrance of the tool {self.name}", 'Red')
    #Get Info in Diffrent Languages
    def _get(self, attr) -> str:
        return getattr(self, attr if self.lang else f'{attr}_zh')
    def get_name(self):
        return self._get('name')
    def get_doc(self):
        return self._get('doc')

__all__ = ['Tool', 'print', 'io', 'info']
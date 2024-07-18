from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from PySide6.QtCore import QTimer
from logic.main import UILogic
from libs.ui.setting import Ui_Settings
from threading import Thread

class LogicFrame:
    def __init__(self):
        self.app = QApplication([])
        self.MainWindow = QMainWindow()
        self.ui = UILogic()
        self.setting = QDialog(self.MainWindow)
        self.setting_ui = Ui_Settings()
        self.tool_thread = Thread()
        self.online = False
        self.running = True
        self.auto_save_timer = ... #type: QTimer
    def ticker(self, func, interval): ...
    def accept(self): ...
    def retrans(self, lang=None): ...
    def auto_translate(self): ...
    def close(self, *evt): ...
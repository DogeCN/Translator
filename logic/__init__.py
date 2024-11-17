from PySide6.QtWidgets import QDialog, QMenu, QMainWindow, QSystemTrayIcon
from PySide6.QtCore import QTimer, QEvent
from libs.translate import trans
from libs.config import Setting
from libs.tool import load
from libs.io import dialog
from libs.ui.effect import acrylic
from libs.ui.setting import Ui_Settings
from .main import LMain
from threading import Thread
from time import sleep
import info

class LMainWindow(QMainWindow):
    def __init__(self, exit, file=None):
        super().__init__()
        self.exit = exit
        #Window Build
        self.ui = LMain()
        self.ui.setupUi(self)
        self.tray = QSystemTrayIcon(self.ui.icon, self)
        self.tmenu = QMenu(self.ui.raw)
        self.tmenu.addAction(self.ui.actionExit)
        self.tmenu.setStyleSheet(info.StlSheets['tmenu'])
        self.tray.setContextMenu(self.tmenu)
        self.show()
        self.tray.show()
        #Setting
        self.setting = QDialog(self)
        self.setting_ui = Ui_Settings()
        self.setting_ui.setupUi(self.setting)
        #UI
        self.connect_actions()
        self.retrans()
        self.ui.setShotcuts()
        self.ui.load_dicts()
        acrylic(self)
        #Threading
        self.argv = file
        Thread(target=lambda:self.ui.load(file)).start()
        Thread(target=self.auto_translate).start()
        self.auto_save_timer = self.ticker(lambda:self.ui.save_all() if Setting.Auto_save else ..., Setting.Auto_save_interval*1000)
        self.ticker(self.check_running, 500)

    def connect_actions(self):
        self.tray.activated.connect(self.tray_activated)
        self.ui.actionSetting.triggered.connect(self.setting_show)
        self.ui.actionOnline.triggered.connect(self.command_online)
        self.setting_ui.Lang.currentIndexChanged.connect(lambda:self.retrans(self.setting_ui.Lang.currentIndex()))
        self.ui.actionTool_Reload.triggered.connect(lambda:load() or self.show_tools())
        self.setting_ui.buttonBox.accepted.connect(self.accept)
        self.setting_ui.buttonBox.rejected.connect(self.setting.hide)
        self.setting_ui.viewVocabulary.clicked.connect(lambda:(lambda f:self.setting_ui.Vocabulary.setText(f) if f else ...)(dialog.OpenFile(self.setting, Setting.getTr('default_file'), info.ext_all_tvf)))
        self.setting_ui.Auto_Save.stateChanged.connect(lambda:self.setting_ui.Interval.setEnabled(self.setting_ui.Auto_Save.isChecked()))

    def ticker(self, func, interval):
        timer = QTimer(self)
        timer.timeout.connect(func)
        timer.start(interval)
        return timer

    def check_running(self):
        action = open(info.running).readline().strip()
        if action:
            if action != 'Show' and info.os.path.exists(action):
                self.ui.load(action)
            self.activateWindow()
            self.showNormal()
        open(info.running, 'w').write('')

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
                self.activateWindow()
                self.showNormal()

    def accept(self):
        Setting.Auto_save = self.setting_ui.Auto_Save.isChecked()
        Setting.Auto_save_interval = self.setting_ui.Interval.value()
        self.auto_save_timer.setInterval(Setting.Auto_save_interval*1000)
        Setting.Vocabulary = self.setting_ui.Vocabulary.text()
        Setting.Key_Add = self.setting_ui.Key_Add.keySequence().toString()
        Setting.Key_Del = self.setting_ui.Key_Delete.keySequence().toString()
        Setting.Key_Top = self.setting_ui.Key_Top.keySequence().toString()
        self.ui.setShotcuts()
        Setting.dump()

    def setting_show(self):
        acrylic(self.setting)
        self.setting_ui.Lang.setCurrentIndex(Setting.Language)
        self.setting_ui.Auto_Save.setChecked(Setting.Auto_save)
        self.setting_ui.Interval.setEnabled(Setting.Auto_save)
        self.setting_ui.Interval.setValue(Setting.Auto_save_interval)
        self.setting_ui.Vocabulary.setText(Setting.Vocabulary)
        self.setting_ui.Key_Add.setKeySequence(Setting.Key_Add)
        self.setting_ui.Key_Delete.setKeySequence(Setting.Key_Del)
        self.setting_ui.Key_Top.setKeySequence(Setting.Key_Top)
        self.setting.show()

    def show_tools(self):
        for action in self.ui.menuTools.actions()[2:]:
            self.ui.menuTools.removeAction(action)
        from libs.tool import Tools
        for tl in Tools.values():
            tl.mw = self
            tl.lang = Setting.Language
            action = tl.action()
            if tl.type: self.ui.menuTools.addMenu(action)
            else: self.ui.menuTools.addAction(action)

    def command_online(self):
        self.ui.menuDicts.setEnabled(info.online)
        info.online = not info.online

    def retrans(self, lang=None):
        if lang is not None:
            Setting.Language = lang
        self.setting_ui.retranslateUi(self.setting)
        self.ui.retranslateUi(self)
        for action in self.ui.menuDicts.actions()[2:]:
            text = action.text()
            for dn in info.dict_names:
                if text in dn:
                    action.setText(dn[Setting.Language])
                    break
        self.ui.Bank.lang = \
        self.ui.Exchanges.lang = \
        self.ui.Expand.lang = Setting.Language
        title = f'{self.windowTitle()} {info.version}'
        self.setWindowTitle(title)
        self.tray.setToolTip(title)
        self.show_tools()

    def auto_translate(self):
        tick = 0
        while info.prog_running:
            #Auto Translate
            if self.isActiveWindow() or self.setting.isActiveWindow():
                ticking = tick > 20
                if self.ui.text_changed or ticking:
                    tick = 0
                    self.ui.text_changed = False
                    word = self.ui.Word_Entry.text().strip()
                    if word != '':
                        if (not ticking) and (word not in self.ui.Bank.words):
                            self.ui.Bank.roll(word)
                        self.ui._result = trans(word, self.ui.Bank.results, self.ui.Exchanges.results, self.ui.Expand.results)
                        if self.ui.text_changed:
                            continue
                        self.ui.signal.set_result_singal.emit()
                tick += 1
                sleep(0.05)
            else:
                sleep(0.5)

    def closeEvent(self, evt:QEvent):
        if self.ui.closing:
            info.prog_running = False
            if Setting.Auto_save:
                self.ui.save_all(False)
            self.exit()
        else:
            self.hide()
            evt.ignore()


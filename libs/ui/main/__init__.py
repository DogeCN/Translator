from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from libs.config import Setting
from .base import Bank, Files
from . import _res

class Ui_MainWindow:
    def __init__(self):
        self.icon = QIcon()
        self.icon.addFile(u":/img/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

    def setupUi(self, MainWindow:QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowIcon(self.icon)
        self.actionReload = QAction(MainWindow)
        self.actionReload.setObjectName(u"actionReload")
        icon2 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.actionReload.setIcon(icon2)
        self.actionReload.setShortcut(u"Ctrl+R")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon(QIcon.fromTheme(u"document-save"))
        self.actionSave.setIcon(icon3)
        self.actionSave.setShortcut(u"Ctrl+S")
        self.actionSave.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        icon4 = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionLoad.setIcon(icon4)
        self.actionLoad.setShortcut(u"Ctrl+L")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon5 = QIcon(QIcon.fromTheme(u"document-save-as"))
        self.actionSave_As.setIcon(icon5)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon6 = QIcon(QIcon.fromTheme(u"edit-clear"))
        self.actionClear.setIcon(icon6)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon7 = QIcon(QIcon.fromTheme(u"system-shutdown"))
        self.actionExit.setIcon(icon7)
        self.actionExit.setShortcut(u"Ctrl+Q")
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        icon8 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.actionSetting.setIcon(icon8)
        self.actionSetting_Load = QAction(MainWindow)
        self.actionSetting_Load.setObjectName(u"actionSetting_Load")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon9 = QIcon(QIcon.fromTheme(u"system-help"))
        self.actionAbout.setIcon(icon9)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionAboutQt.setIcon(icon9)
        self.actionTool_Reload = QAction(MainWindow)
        self.actionTool_Reload.setObjectName(u"actionTool_Reload")
        self.actionTool_Reload.setIcon(icon2)
        self.actionDict_Reload = QAction(MainWindow)
        self.actionDict_Reload.setObjectName(u"actionDict_Reload")
        self.actionDict_Reload.setIcon(icon2)
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        icon10 = QIcon(QIcon.fromTheme(u"list-remove"))
        self.actionRemove.setIcon(icon10)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon11 = QIcon(QIcon.fromTheme(u"document-new"))
        self.actionNew.setIcon(icon11)
        self.actionNew.setShortcut(u"Ctrl+N")
        self.actionSave_All = QAction(MainWindow)
        self.actionSave_All.setObjectName(u"actionSave_All")
        self.actionSave_All.setIcon(icon3)
        self.actionSave_All.setShortcut(u"Ctrl+Alt+S")
        self.actionOnline = QAction(MainWindow)
        self.actionOnline.setObjectName(u"actionOnline")
        icon12 = QIcon(QIcon.fromTheme(u"applications-internet"))
        self.actionOnline.setIcon(icon12)
        self.actionOnline.setShortcut(u"Ctrl+O")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Word_Entry = QLineEdit(self.centralwidget)
        self.Word_Entry.setObjectName(u"Word_Entry")
        self.Word_Entry.setMinimumSize(QSize(100, 31))
        self.Word_Entry.setMaximumSize(QSize(16777215, 31))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(11)
        self.Word_Entry.setFont(font)
        self.Word_Entry.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Word_Entry.setStyleSheet(u"color: rgb(0, 255, 0);background-color: rgba(52, 255, 52, 50);")

        self.gridLayout.addWidget(self.Word_Entry, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Add = QPushButton(self.centralwidget)
        self.Add.setObjectName(u"Add")
        self.Add.setEnabled(False)
        self.Add.setMinimumSize(QSize(0, 32))
        self.Add.setMaximumSize(QSize(16777215, 32))
        self.Add.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Add.setStyleSheet(u"font: 10pt;color: rgb(255, 170, 0);background-color: rgba(255, 170, 20, 50);")
        icon13 = QIcon(QIcon.fromTheme(u"list-add"))
        self.Add.setIcon(icon13)

        self.verticalLayout_2.addWidget(self.Add)

        self.Top = QPushButton(self.centralwidget)
        self.Top.setObjectName(u"Top")
        self.Top.setEnabled(False)
        self.Top.setMinimumSize(QSize(0, 32))
        self.Top.setMaximumSize(QSize(16777215, 32))
        self.Top.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Top.setStyleSheet(u"font: 10pt;color: rgb(0, 170, 255);background-color: rgba(0, 170, 255, 50);")
        icon14 = QIcon(QIcon.fromTheme(u"appointment-new"))
        self.Top.setIcon(icon14)

        self.verticalLayout_2.addWidget(self.Top)

        self.Delete = QPushButton(self.centralwidget)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setEnabled(False)
        self.Delete.setMinimumSize(QSize(0, 31))
        self.Delete.setMaximumSize(QSize(16777215, 31))
        self.Delete.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Delete.setStyleSheet(u"font: 10pt;color: rgb(255, 0, 0);background-color: rgba(255, 0, 0, 50);")
        icon15 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.Delete.setIcon(icon15)

        self.verticalLayout_2.addWidget(self.Delete)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 2, 1)

        self.Bank = Bank(self.centralwidget)
        self.Bank.setObjectName(u"Bank")
        self.Bank.setMinimumSize(QSize(128, 0))
        self.Bank.setMaximumSize(QSize(128, 16777215))
        self.Bank.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Bank.setStyleSheet(u"QToolTip{background-color: rgba(30,30,30,100);color: rgb(85, 255, 255);}QListWidget{font: 10pt;color: rgb(85, 255, 255);}")
        self.Bank.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Bank.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Bank.setAutoScroll(False)
        self.Bank.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Bank.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Bank.setSortingEnabled(True)

        self.gridLayout.addWidget(self.Bank, 0, 2, 2, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.Exchanges = Bank(self.splitter)
        self.Exchanges.setObjectName(u"Exchanges")
        self.Exchanges.setMinimumSize(QSize(128, 0))
        self.Exchanges.setMaximumSize(QSize(128, 16777215))
        self.Exchanges.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Exchanges.setStyleSheet(u"QToolTip{background-color: rgba(30,30,30,100);color: rgb(170, 255, 127);}QListWidget{font: 10pt;color: rgb(170, 255, 127);}")
        self.Exchanges.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Exchanges.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Exchanges.setAutoScroll(False)
        self.Exchanges.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Exchanges.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Exchanges.setSortingEnabled(True)
        self.splitter.addWidget(self.Exchanges)
        self.Files = Files(self.splitter, self.Bank)
        self.Files.setObjectName(u"Files")
        self.Files.setMinimumSize(QSize(128, 51))
        self.Files.setMaximumSize(QSize(128, 16777215))
        self.Files.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Files.setStyleSheet(u"QToolTip{background-color: rgba(30,30,30,100);color: rgb(255, 85, 255);}QListWidget{font: 10pt;color: rgb(255, 85, 255);}")
        self.Files.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Files.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Files.setAutoScroll(False)
        self.Files.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Files.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.Files.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.splitter.addWidget(self.Files)

        self.verticalLayout_2.addWidget(self.splitter)


        self.Expand = Bank(self.centralwidget)
        self.Expand.setObjectName(u"Expand")
        self.Expand.setMinimumSize(QSize(128, 0))
        self.Expand.setMaximumSize(QSize(150, 16777215))
        self.Expand.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Expand.setStyleSheet(u"QToolTip{background-color: rgba(30,30,30,100);color: rgb(200, 200, 25);}QListWidget{font: 10pt;color: rgb(200, 200, 25);}")
        self.Expand.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Expand.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Expand.setAutoScroll(False)
        self.Expand.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Expand.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Expand.setSortingEnabled(True)

        self.gridLayout.addWidget(self.Expand, 0, 3, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Translated_text = QLabel(self.centralwidget)
        self.Translated_text.setObjectName(u"Translated_text")
        self.Translated_text.setMinimumSize(QSize(0, 117))
        self.Translated_text.setStyleSheet(u"QLabel{font: 75 12pt;color: rgb(0, 170, 255);}QToolTip{background-color: rgba(30,30,30,100);color: rgb(0, 170, 255);}")
        self.Translated_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Translated_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.Translated_text)

        self.Phonetic = QLabel(self.centralwidget)
        self.Phonetic.setObjectName(u"Phonetic")
        self.Phonetic.setMinimumSize(QSize(172, 42))
        self.Phonetic.setMaximumSize(QSize(16777215, 42))
        self.Phonetic.setStyleSheet(u"QLabel{font: 700 12pt;color: rgb(255, 170, 0);}QToolTip{background-color: rgba(30,30,30,100);color: rgb(255, 170, 0);}")
        self.Phonetic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Phonetic.setWordWrap(True)

        self.verticalLayout.addWidget(self.Phonetic)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 33))
        self.menuBar.setStyleSheet(u"QMenu{background-color: rgba(30, 30, 30, 100);border-radius:10px;}")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setToolTipsVisible(False)
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuTools.setAutoFillBackground(False)
        self.menuTools.setSeparatorsCollapsible(False)
        self.menuTools.setToolTipsVisible(False)
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuDicts = QMenu(self.menuBar)
        self.menuDicts.setObjectName(u"menuDicts")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuDicts.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemove)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionTool_Reload)
        self.menuTools.addSeparator()
        self.menuSettings.addAction(self.actionSetting)
        self.menuSettings.addAction(self.actionOnline)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAboutQt)
        self.menuDicts.addAction(self.actionDict_Reload)
        self.menuDicts.addSeparator()



    def retranslateUi(self, MainWindow:QMainWindow):
        MainWindow.setWindowTitle(Setting.translateUI('Translator'))
        self.actionReload.setText(Setting.translateUI('Reload'))
        self.actionReload.setStatusTip(Setting.translateUI('Reload File'))
        self.actionSave.setText(Setting.translateUI('Save'))
        self.actionSave.setStatusTip(Setting.translateUI('Save File'))
        self.actionLoad.setText(Setting.translateUI('Load'))
        self.actionLoad.setStatusTip(Setting.translateUI('Load Files'))
        self.actionSave_As.setText(Setting.translateUI('Save As'))
        self.actionSave_As.setStatusTip(Setting.translateUI('Save File As ...'))
        self.actionClear.setText(Setting.translateUI('Clear'))
        self.actionClear.setStatusTip(Setting.translateUI('Clear Files'))
        self.actionExit.setText(Setting.translateUI('Exit'))
        self.actionExit.setStatusTip(Setting.translateUI('Exit'))
        self.actionSetting.setText(Setting.translateUI('Settings'))
        self.actionSetting.setStatusTip(Setting.translateUI('Settings'))
        self.actionSetting_Load.setText(Setting.translateUI('Load'))
        self.actionAbout.setText(Setting.translateUI('About'))
        self.actionAbout.setStatusTip(Setting.translateUI('About This Programm'))
        self.actionAboutQt.setText(Setting.translateUI('About Qt'))
        self.actionAboutQt.setStatusTip(Setting.translateUI('About Qt Engine'))
        self.actionTool_Reload.setText(Setting.translateUI('Reload'))
        self.actionTool_Reload.setStatusTip(Setting.translateUI('Relaod Tools'))
        self.actionDict_Reload.setText(Setting.translateUI('Reload'))
        self.actionDict_Reload.setStatusTip(Setting.translateUI('Reload Dictionaries'))
        self.actionRemove.setText(Setting.translateUI('Remove'))
        self.actionRemove.setStatusTip(Setting.translateUI('Remove Current File'))
        self.actionNew.setText(Setting.translateUI('New'))
        self.actionNew.setStatusTip(Setting.translateUI('Create a New File'))
        self.actionSave_All.setText(Setting.translateUI('Save All'))
        self.actionSave_All.setStatusTip(Setting.translateUI('Save All Files'))
        self.actionOnline.setText(Setting.translateUI('Online'))
        self.actionOnline.setStatusTip(Setting.translateUI('Online Mode'))
        self.Word_Entry.setStatusTip(Setting.translateUI('Word Entry'))
        self.Word_Entry.setPlaceholderText(Setting.translateUI('Enter a word'))
        self.Add.setStatusTip(Setting.translateUI('Add into Vocabulary'))
        self.Add.setText(Setting.translateUI('Add'))
        self.Bank.setStatusTip(Setting.translateUI('Vocabulary Bank'))
        self.Translated_text.setStatusTip(Setting.translateUI('Translations'))
        self.Phonetic.setStatusTip(Setting.translateUI('Phonetic'))
        self.Top.setStatusTip(Setting.translateUI('Top the Words'))
        self.Top.setText(Setting.translateUI('Top'))
        self.Delete.setStatusTip(Setting.translateUI('Delete the Words'))
        self.Delete.setText(Setting.translateUI('Delete'))
        self.Exchanges.setStatusTip(Setting.translateUI('Exchanges'))
        self.Files.setStatusTip(Setting.translateUI('Files'))
        self.Expand.setStatusTip(Setting.translateUI('Expand'))
        self.menuFile.setTitle(Setting.translateUI('File'))
        self.menuTools.setTitle(Setting.translateUI('Tools'))
        self.menuSettings.setTitle(Setting.translateUI('Settings'))
        self.menuAbout.setTitle(Setting.translateUI('About'))
        self.menuDicts.setTitle(Setting.translateUI('Dicts'))


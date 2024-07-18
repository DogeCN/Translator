from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QCheckBox, QComboBox, QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout, QVBoxLayout, QKeySequenceEdit, QLabel, QLineEdit, QSpinBox, QToolButton

class Ui_Settings(object):
    def setupUi(self, Settings:QDialog):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(319, 234)
        icon = QIcon(QIcon.fromTheme(u"document-properties"))
        Settings.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lLang = QLabel(Settings)
        self.lLang.setObjectName(u"lLang")
        self.lLang.setMaximumSize(QSize(57, 16777215))

        self.horizontalLayout_5.addWidget(self.lLang)

        self.Lang = QComboBox(Settings)
        self.Lang.addItem(u"\u7b80\u4f53\u4e2d\u6587")
        self.Lang.addItem(u"English")
        self.Lang.setObjectName(u"Lang")

        self.horizontalLayout_5.addWidget(self.Lang)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 2, 2, 1)

        self.lFile = QLabel(Settings)
        self.lFile.setObjectName(u"lFile")
        self.lFile.setMinimumSize(QSize(218, 0))

        self.gridLayout.addWidget(self.lFile, 1, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lVoc = QLabel(Settings)
        self.lVoc.setObjectName(u"lVoc")
        self.lVoc.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_4.addWidget(self.lVoc)

        self.Vocabulary = QLineEdit(Settings)
        self.Vocabulary.setObjectName(u"Vocabulary")
        self.Vocabulary.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.Vocabulary)

        self.viewVocabulary = QToolButton(Settings)
        self.viewVocabulary.setObjectName(u"viewVocabulary")
        self.viewVocabulary.setText(u"...")

        self.horizontalLayout_4.addWidget(self.viewVocabulary)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lAuto = QLabel(Settings)
        self.lAuto.setObjectName(u"lAuto")
        self.lAuto.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_3.addWidget(self.lAuto)

        self.Auto_Save = QCheckBox(Settings)
        self.Auto_Save.setObjectName(u"Auto_Save")
        self.Auto_Save.setMaximumSize(QSize(16, 19))

        self.horizontalLayout_3.addWidget(self.Auto_Save)

        self.Interval = QSpinBox(Settings)
        self.Interval.setObjectName(u"Interval")
        self.Interval.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Interval.setMinimum(10)
        self.Interval.setMaximum(99)

        self.horizontalLayout_3.addWidget(self.Interval)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lAdd = QLabel(Settings)
        self.lAdd.setObjectName(u"lAdd")

        self.verticalLayout_2.addWidget(self.lAdd)

        self.lDel = QLabel(Settings)
        self.lDel.setObjectName(u"lDel")

        self.verticalLayout_2.addWidget(self.lDel)

        self.lTop = QLabel(Settings)
        self.lTop.setObjectName(u"lTop")

        self.verticalLayout_2.addWidget(self.lTop)


        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 3, 1)

        self.Key_Add = QKeySequenceEdit(Settings)
        self.Key_Add.setObjectName(u"Key_Add")

        self.gridLayout.addWidget(self.Key_Add, 5, 1, 1, 1)

        self.Key_Delete = QKeySequenceEdit(Settings)
        self.Key_Delete.setObjectName(u"Key_Delete")

        self.gridLayout.addWidget(self.Key_Delete, 6, 1, 1, 1)

        self.Key_Top = QKeySequenceEdit(Settings)
        self.Key_Top.setObjectName(u"Key_Top")

        self.gridLayout.addWidget(self.Key_Top, 7, 1, 1, 1)

        self.lHot = QLabel(Settings)
        self.lHot.setObjectName(u"lHot")

        self.gridLayout.addWidget(self.lHot, 4, 0, 1, 2)


        self.buttonBox.accepted.connect(Settings.accept)

        QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings:QDialog):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.lLang.setText(QCoreApplication.translate("Settings", u"Language", None))
        self.lFile.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p align=\"center\">Files</p></body></html>", None))
        self.lVoc.setText(QCoreApplication.translate("Settings", u"Vocabulary", None))
        self.lAuto.setText(QCoreApplication.translate("Settings", u"Auto Save", None))
        self.Interval.setSuffix(QCoreApplication.translate("Settings", u" Seconds", None))
        self.lAdd.setText(QCoreApplication.translate("Settings", u"Add", None))
        self.lDel.setText(QCoreApplication.translate("Settings", u"Delete", None))
        self.lTop.setText(QCoreApplication.translate("Settings", u"Top", None))
        self.lHot.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p align=\"center\">Hotkeys</p></body></html>", None))


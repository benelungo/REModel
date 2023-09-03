# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 501)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(51, 51, 76);\n"
"	color:White;\n"
"	font-weight:bold;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font-size: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    border:none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainGridLayout = QGridLayout()
        self.MainGridLayout.setObjectName(u"MainGridLayout")
        self.MainGridLayout.setHorizontalSpacing(9)
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"    border:none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OptionsLabel = QLabel(self.groupBox_5)
        self.OptionsLabel.setObjectName(u"OptionsLabel")
        font = QFont()
        font.setBold(True)
        self.OptionsLabel.setFont(font)
        self.OptionsLabel.setStyleSheet(u"margin: 0;")
        self.OptionsLabel.setMargin(7)

        self.horizontalLayout_6.addWidget(self.OptionsLabel)

        self.horizontalSpacer_3 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.ErrorLabel = QLabel(self.groupBox_5)
        self.ErrorLabel.setObjectName(u"ErrorLabel")
        self.ErrorLabel.setStyleSheet(u"color: red;")

        self.horizontalLayout_6.addWidget(self.ErrorLabel)


        self.MainGridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 50))
        self.groupBox.setStyleSheet(u"border:none;\n"
"padding: 0;\n"
"margin: 0;")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PathLineEdit = QLineEdit(self.groupBox)
        self.PathLineEdit.setObjectName(u"PathLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathLineEdit.sizePolicy().hasHeightForWidth())
        self.PathLineEdit.setSizePolicy(sizePolicy)
        self.PathLineEdit.setMinimumSize(QSize(100, 30))
        self.PathLineEdit.setAutoFillBackground(False)
        self.PathLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 5px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.PathLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.PathLineEdit)

        self.PathPushButton = QPushButton(self.groupBox)
        self.PathPushButton.setObjectName(u"PathPushButton")
        self.PathPushButton.setMinimumSize(QSize(30, 30))
        self.PathPushButton.setMaximumSize(QSize(30, 30))
        self.PathPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PathPushButton.setStyleSheet(u"QPushButton{\n"
"	border: 0px transparent;\n"
"	border-radius: 15px;\n"
"	background: rgb(152, 152, 226);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(83, 83, 124)\n"
"	\n"
"}")

        self.horizontalLayout_2.addWidget(self.PathPushButton)

        self.FindPushButton = QPushButton(self.groupBox)
        self.FindPushButton.setObjectName(u"FindPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FindPushButton.sizePolicy().hasHeightForWidth())
        self.FindPushButton.setSizePolicy(sizePolicy1)
        self.FindPushButton.setMinimumSize(QSize(70, 30))
        self.FindPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.FindPushButton.setStyleSheet(u"QPushButton{\n"
"	border: 1px transparent;\n"
"	border-radius: 15px;\n"
"	background: rgb(152, 152, 226);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(83, 83, 124)\n"
"	\n"
"}")

        self.horizontalLayout_2.addWidget(self.FindPushButton)


        self.MainGridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 50))
        self.groupBox_3.setMaximumSize(QSize(16777215, 60))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
" border:none;\n"
"padding: 0;\n"
"margin: 0;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LogoLabel = QLabel(self.groupBox_3)
        self.LogoLabel.setObjectName(u"LogoLabel")
        self.LogoLabel.setMinimumSize(QSize(200, 40))
        self.LogoLabel.setMaximumSize(QSize(200, 40))
        self.LogoLabel.setStyleSheet(u"font-size: 40px;\n"
"")

        self.horizontalLayout_4.addWidget(self.LogoLabel)

        self.horizontalSpacer = QSpacerItem(209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.MainGridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 50))
        self.groupBox_4.setMaximumSize(QSize(16777215, 50))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
" border:none;\n"
"padding: 0;\n"
"margin: 0;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.AboutLabel = QLabel(self.groupBox_4)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setStyleSheet(u"color: rgb(105, 105, 147);\n"
"margin: 1px;")

        self.horizontalLayout_5.addWidget(self.AboutLabel)

        self.horizontalSpacer_2 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.MainGridLayout.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ClassesScrollArea = QScrollArea(self.groupBox_2)
        self.ClassesScrollArea.setObjectName(u"ClassesScrollArea")
        self.ClassesScrollArea.setMinimumSize(QSize(420, 200))
        self.ClassesScrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: 1px transparent;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget {\n"
"	background: rgb(35, 35, 57);\n"
"	border: 1px rgb(25, 25, 37);\n"
"}\n"
"\n"
"QScrollArea QScrollBar {\n"
"	border: none;\n"
"	background: rgb(35, 35, 57);\n"
"	width:12px;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle{\n"
"	border: none;\n"
"	background-color: rgb(118, 118, 176);\n"
"	width:20px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:hover{\n"
"	background-color: rgb(152, 152, 226);\n"
"}\n"
"QScrollArea QScrollBar::handle:pressed {\n"
"	background-color: rgb(105, 105, 157);\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"      border: none;\n"
"      background: none;\n"
"      color: none;\n"
"}\n"
"QScrollArea QScrollBar::add-page, QScr"
                        "ollBar::sub-page {\n"
"      border: none;\n"
"      background: none;\n"
"      color: none;\n"
"}")
        self.ClassesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ClassesScrollArea.setWidgetResizable(True)
        self.ClassesScrollAreaWidgetContents = QWidget()
        self.ClassesScrollAreaWidgetContents.setObjectName(u"ClassesScrollAreaWidgetContents")
        self.ClassesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 420, 288))
        self.horizontalLayout = QHBoxLayout(self.ClassesScrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ClassesLayout = QVBoxLayout()
        self.ClassesLayout.setSpacing(0)
        self.ClassesLayout.setObjectName(u"ClassesLayout")

        self.horizontalLayout.addLayout(self.ClassesLayout)

        self.ClassesScrollArea.setWidget(self.ClassesScrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.ClassesScrollArea)


        self.MainGridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.OptionsScrollArea = QScrollArea(self.groupBox_6)
        self.OptionsScrollArea.setObjectName(u"OptionsScrollArea")
        self.OptionsScrollArea.setMinimumSize(QSize(420, 200))
        self.OptionsScrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: 1px transparent;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget {\n"
"	background: rgb(35, 35, 57);\n"
"	border: 1px rgb(25, 25, 37);\n"
"}\n"
"\n"
"QScrollArea QScrollBar {\n"
"	border: none;\n"
"	background: rgb(35, 35, 57);\n"
"	width:12px;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle{\n"
"	border: none;\n"
"	background-color: rgb(118, 118, 176);\n"
"	width:20px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:hover{\n"
"	background-color: rgb(152, 152, 226);\n"
"}\n"
"QScrollArea QScrollBar::handle:pressed {\n"
"	background-color: rgb(105, 105, 157);\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"      border: none;\n"
"      background: none;\n"
"      color: none;\n"
"}\n"
"QScrollArea QScrollBar::add-page, QScr"
                        "ollBar::sub-page {\n"
"      border: none;\n"
"      background: none;\n"
"      color: none;\n"
"}")
        self.OptionsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OptionsScrollArea.setWidgetResizable(True)
        self.OptionsScrollAreaWidgetContents = QWidget()
        self.OptionsScrollAreaWidgetContents.setObjectName(u"OptionsScrollAreaWidgetContents")
        self.OptionsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 420, 288))
        self.horizontalLayout_14 = QHBoxLayout(self.OptionsScrollAreaWidgetContents)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.OptionsLayout = QVBoxLayout()
        self.OptionsLayout.setSpacing(0)
        self.OptionsLayout.setObjectName(u"OptionsLayout")

        self.horizontalLayout_14.addLayout(self.OptionsLayout)

        self.OptionsScrollArea.setWidget(self.OptionsScrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.OptionsScrollArea)


        self.MainGridLayout.addWidget(self.groupBox_6, 2, 1, 1, 1)

        self.GenerateGroupBox = QGroupBox(self.centralwidget)
        self.GenerateGroupBox.setObjectName(u"GenerateGroupBox")
        self.GenerateGroupBox.setMinimumSize(QSize(0, 50))
        self.GenerateGroupBox.setStyleSheet(u"QGroupBox{\n"
"    border:none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.GenerateGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.ProgressBar = QProgressBar(self.GenerateGroupBox)
        self.ProgressBar.setObjectName(u"ProgressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ProgressBar.sizePolicy().hasHeightForWidth())
        self.ProgressBar.setSizePolicy(sizePolicy2)
        self.ProgressBar.setMinimumSize(QSize(305, 30))
        self.ProgressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(35, 35, 57);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: solid;\n"
"	border-color: black;\n"
"	border-radius: 14px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(118, 118, 176);	\n"
"	border: solid;\n"
"	border-radius: 14px;\n"
"}")
        self.ProgressBar.setMaximum(100)
        self.ProgressBar.setValue(30)

        self.horizontalLayout_3.addWidget(self.ProgressBar)

        self.GeneratePushButton = QPushButton(self.GenerateGroupBox)
        self.GeneratePushButton.setObjectName(u"GeneratePushButton")
        self.GeneratePushButton.setMinimumSize(QSize(100, 30))
        self.GeneratePushButton.setMaximumSize(QSize(100, 30))
        self.GeneratePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.GeneratePushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border: 1px transparent;\n"
"	border-radius: 14px;\n"
"	background: rgb(152, 152, 226);\n"
"	min-width: 100px;	\n"
"	max-width: 100px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(83, 83, 124)\n"
"	\n"
"}")

        self.horizontalLayout_3.addWidget(self.GeneratePushButton)


        self.MainGridLayout.addWidget(self.GenerateGroupBox, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.MainGridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_5.setTitle("")
        self.OptionsLabel.setText(QCoreApplication.translate("MainWindow", u"Options:", None))
        self.ErrorLabel.setText("")
        self.groupBox.setTitle("")
        self.PathLineEdit.setText("")
        self.PathLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.PathPushButton.setText("")
        self.FindPushButton.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.groupBox_3.setTitle("")
        self.LogoLabel.setText(QCoreApplication.translate("MainWindow", u"REModel", None))
        self.groupBox_4.setTitle("")
        self.AboutLabel.setText(QCoreApplication.translate("MainWindow", u"Project v0.9 by Dovhaliuk Pavlo", None))
        self.groupBox_2.setTitle("")
        self.groupBox_6.setTitle("")
        self.GenerateGroupBox.setTitle("")
        self.ProgressBar.setFormat(QCoreApplication.translate("MainWindow", u"%v/%m", None))
        self.GeneratePushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_class_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 66)
        Form.setStyleSheet(u"QWidget{background-color: rgb(136, 136, 203);\n"
"color:White;\n"
"font-weight:bold;\n"
"font-size: 14px;}\n"
"\n"
"QLineEdit {\n"
"	font-size: 14px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QGroupBox{\n"
"	border: 1px transparent;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, -1, -1, -1)
        self.ClassNameLabel = QLabel(self.groupBox)
        self.ClassNameLabel.setObjectName(u"ClassNameLabel")
        self.ClassNameLabel.setMinimumSize(QSize(70, 30))
        self.ClassNameLabel.setStyleSheet(u"padding-left: 2px;")

        self.horizontalLayout.addWidget(self.ClassNameLabel)

        self.horizontalSpacer = QSpacerItem(13, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.RandomPushButton = QPushButton(self.groupBox)
        self.RandomPushButton.setObjectName(u"RandomPushButton")
        self.RandomPushButton.setMinimumSize(QSize(30, 30))
        self.RandomPushButton.setMaximumSize(QSize(30, 30))
        self.RandomPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.RandomPushButton.setStyleSheet(u"QPushButton{\n"
"	border: 0px transparent;\n"
"	border-radius: 15px;\n"
"	background: rgb(162, 162, 236);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(83, 83, 124)\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.RandomPushButton)

        self.ClassColorLabel = QLineEdit(self.groupBox)
        self.ClassColorLabel.setObjectName(u"ClassColorLabel")
        self.ClassColorLabel.setMinimumSize(QSize(100, 30))
        self.ClassColorLabel.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")

        self.horizontalLayout.addWidget(self.ClassColorLabel)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.ClassNameLabel.setText(QCoreApplication.translate("Form", u"ObjectName", None))
        self.RandomPushButton.setText("")
        self.ClassColorLabel.setPlaceholderText(QCoreApplication.translate("Form", u"Color", None))
    # retranslateUi


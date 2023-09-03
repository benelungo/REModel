# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_regular_option_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_RegularOptionWidget(object):
    def setupUi(self, RegularOptionWidget):
        if not RegularOptionWidget.objectName():
            RegularOptionWidget.setObjectName(u"RegularOptionWidget")
        RegularOptionWidget.resize(350, 66)
        font = QFont()
        font.setBold(True)
        RegularOptionWidget.setFont(font)
        RegularOptionWidget.setStyleSheet(u"QWidget{background-color: rgb(136, 136, 203);\n"
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
        self.horizontalLayout = QHBoxLayout(RegularOptionWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainGroupBox = QGroupBox(RegularOptionWidget)
        self.MainGroupBox.setObjectName(u"MainGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainGroupBox.sizePolicy().hasHeightForWidth())
        self.MainGroupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.MainGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OptionName = QCheckBox(self.MainGroupBox)
        self.OptionName.setObjectName(u"OptionName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OptionName.sizePolicy().hasHeightForWidth())
        self.OptionName.setSizePolicy(sizePolicy1)
        self.OptionName.setMinimumSize(QSize(50, 30))
        self.OptionName.setMaximumSize(QSize(270, 30))
        self.OptionName.setCursor(QCursor(Qt.PointingHandCursor))
        self.OptionName.setStyleSheet(u"padding-left:2px")

        self.horizontalLayout_2.addWidget(self.OptionName)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.MainGroupBox)


        self.retranslateUi(RegularOptionWidget)

        QMetaObject.connectSlotsByName(RegularOptionWidget)
    # setupUi

    def retranslateUi(self, RegularOptionWidget):
        RegularOptionWidget.setWindowTitle(QCoreApplication.translate("RegularOptionWidget", u"Form", None))
        self.MainGroupBox.setTitle("")
        self.OptionName.setText(QCoreApplication.translate("RegularOptionWidget", u"CheckBox", None))
    # retranslateUi


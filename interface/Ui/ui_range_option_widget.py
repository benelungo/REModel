# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_range_option_widget.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_RangeOptionWidget(object):
    def setupUi(self, RangeOptionWidget):
        if not RangeOptionWidget.objectName():
            RangeOptionWidget.setObjectName(u"RangeOptionWidget")
        RangeOptionWidget.resize(350, 66)
        font = QFont()
        font.setBold(True)
        RangeOptionWidget.setFont(font)
        RangeOptionWidget.setStyleSheet(u"QWidget{background-color: rgb(136, 136, 203);\n"
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
        self.horizontalLayout = QHBoxLayout(RangeOptionWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainGroupBox = QGroupBox(RangeOptionWidget)
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

        self.StartLineEdit = QLineEdit(self.MainGroupBox)
        self.StartLineEdit.setObjectName(u"StartLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StartLineEdit.sizePolicy().hasHeightForWidth())
        self.StartLineEdit.setSizePolicy(sizePolicy2)
        self.StartLineEdit.setMinimumSize(QSize(50, 20))
        self.StartLineEdit.setMaximumSize(QSize(50, 30))
        self.StartLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.StartLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.StartLineEdit)

        self.DashLabel = QLabel(self.MainGroupBox)
        self.DashLabel.setObjectName(u"DashLabel")
        sizePolicy2.setHeightForWidth(self.DashLabel.sizePolicy().hasHeightForWidth())
        self.DashLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.DashLabel)

        self.EndLineEdit = QLineEdit(self.MainGroupBox)
        self.EndLineEdit.setObjectName(u"EndLineEdit")
        sizePolicy2.setHeightForWidth(self.EndLineEdit.sizePolicy().hasHeightForWidth())
        self.EndLineEdit.setSizePolicy(sizePolicy2)
        self.EndLineEdit.setMinimumSize(QSize(50, 30))
        self.EndLineEdit.setMaximumSize(QSize(50, 30))
        self.EndLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.EndLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.EndLineEdit)

        self.StepLineEdit = QLineEdit(self.MainGroupBox)
        self.StepLineEdit.setObjectName(u"StepLineEdit")
        sizePolicy2.setHeightForWidth(self.StepLineEdit.sizePolicy().hasHeightForWidth())
        self.StepLineEdit.setSizePolicy(sizePolicy2)
        self.StepLineEdit.setMinimumSize(QSize(50, 30))
        self.StepLineEdit.setMaximumSize(QSize(50, 30))
        self.StepLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.StepLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.StepLineEdit)


        self.horizontalLayout.addWidget(self.MainGroupBox)


        self.retranslateUi(RangeOptionWidget)

        QMetaObject.connectSlotsByName(RangeOptionWidget)
    # setupUi

    def retranslateUi(self, RangeOptionWidget):
        RangeOptionWidget.setWindowTitle(QCoreApplication.translate("RangeOptionWidget", u"Form", None))
        self.MainGroupBox.setTitle("")
        self.OptionName.setText(QCoreApplication.translate("RangeOptionWidget", u"CheckBox", None))
        self.StartLineEdit.setPlaceholderText(QCoreApplication.translate("RangeOptionWidget", u"Start", None))
        self.DashLabel.setText(QCoreApplication.translate("RangeOptionWidget", u"-", None))
        self.EndLineEdit.setPlaceholderText(QCoreApplication.translate("RangeOptionWidget", u"End", None))
        self.StepLineEdit.setPlaceholderText(QCoreApplication.translate("RangeOptionWidget", u"Step", None))
    # retranslateUi


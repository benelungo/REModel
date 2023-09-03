# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_resolution_option_widget.ui'
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

class Ui_ResolutionOptionWidget(object):
    def setupUi(self, ResolutionOptionWidget):
        if not ResolutionOptionWidget.objectName():
            ResolutionOptionWidget.setObjectName(u"ResolutionOptionWidget")
        ResolutionOptionWidget.resize(350, 66)
        font = QFont()
        font.setBold(True)
        ResolutionOptionWidget.setFont(font)
        ResolutionOptionWidget.setStyleSheet(u"QWidget{background-color: rgb(136, 136, 203);\n"
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
        self.horizontalLayout = QHBoxLayout(ResolutionOptionWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainGroupBox = QGroupBox(ResolutionOptionWidget)
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

        self.WidthLineEdit = QLineEdit(self.MainGroupBox)
        self.WidthLineEdit.setObjectName(u"WidthLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.WidthLineEdit.sizePolicy().hasHeightForWidth())
        self.WidthLineEdit.setSizePolicy(sizePolicy2)
        self.WidthLineEdit.setMinimumSize(QSize(70, 20))
        self.WidthLineEdit.setMaximumSize(QSize(50, 30))
        self.WidthLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.WidthLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.WidthLineEdit)

        self.DashLabel = QLabel(self.MainGroupBox)
        self.DashLabel.setObjectName(u"DashLabel")
        sizePolicy2.setHeightForWidth(self.DashLabel.sizePolicy().hasHeightForWidth())
        self.DashLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.DashLabel)

        self.HeightLineEdit = QLineEdit(self.MainGroupBox)
        self.HeightLineEdit.setObjectName(u"HeightLineEdit")
        sizePolicy2.setHeightForWidth(self.HeightLineEdit.sizePolicy().hasHeightForWidth())
        self.HeightLineEdit.setSizePolicy(sizePolicy2)
        self.HeightLineEdit.setMinimumSize(QSize(70, 30))
        self.HeightLineEdit.setMaximumSize(QSize(50, 30))
        self.HeightLineEdit.setStyleSheet(u"font-size: 14px;\n"
"padding: 5px;\n"
"border: 1px transparent;\n"
"border-radius: 6px;\n"
"background: rgb(118, 118, 176);\n"
"")
        self.HeightLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.HeightLineEdit)


        self.horizontalLayout.addWidget(self.MainGroupBox)


        self.retranslateUi(ResolutionOptionWidget)

        QMetaObject.connectSlotsByName(ResolutionOptionWidget)
    # setupUi

    def retranslateUi(self, ResolutionOptionWidget):
        ResolutionOptionWidget.setWindowTitle(QCoreApplication.translate("ResolutionOptionWidget", u"Form", None))
        self.MainGroupBox.setTitle("")
        self.OptionName.setText(QCoreApplication.translate("ResolutionOptionWidget", u"CheckBox", None))
        self.WidthLineEdit.setText("")
        self.WidthLineEdit.setPlaceholderText(QCoreApplication.translate("ResolutionOptionWidget", u"Width", None))
        self.DashLabel.setText(QCoreApplication.translate("ResolutionOptionWidget", u"x", None))
        self.HeightLineEdit.setPlaceholderText(QCoreApplication.translate("ResolutionOptionWidget", u"Height", None))
    # retranslateUi


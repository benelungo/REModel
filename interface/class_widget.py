import random

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from matplotlib import colors
from interface.Ui.ui_class_widget import Ui_Form


class ClassWidget(QWidget):
    def __init__(self, id_widget, parent=None):
        super(ClassWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.RandomPushButton.clicked.connect(self.set_random_color)
        self.additional_setup()

    def additional_setup(self):
        """Additional interface settings"""
        self.ui.RandomPushButton.setIcon(QIcon(r'icons\random.png'))

    def set_random_color(self):
        clrs = [color for color in list(colors.CSS4_COLORS.keys()) if color != 'black']
        self.ui.ClassColorLabel.setText(random.choice(clrs))

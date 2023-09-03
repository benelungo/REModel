from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from interface.Ui.ui_range_option_widget import Ui_RangeOptionWidget
from interface.Ui.ui_resolution_option_widget import Ui_ResolutionOptionWidget
from interface.Ui.ui_regular_option_widget import Ui_RegularOptionWidget
from interface.Ui.ui_folder_option_widget import Ui_FolderOptionWidget


class RangeOptionWidget(QWidget):
    def __init__(self, id_widget, parent=None):
        super(RangeOptionWidget, self).__init__(parent)
        self.ui = Ui_RangeOptionWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget


class RegularOptionWidget(QWidget):
    def __init__(self, id_widget, parent=None):
        super(RegularOptionWidget, self).__init__(parent)
        self.ui = Ui_RegularOptionWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget


class ResolutionOptionWidget(QWidget):
    def __init__(self, id_widget, parent=None):
        super(ResolutionOptionWidget, self).__init__(parent)
        self.ui = Ui_ResolutionOptionWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget


class FolderOptionWidget(QWidget):
    def __init__(self, id_widget, parent=None):
        super(FolderOptionWidget, self).__init__(parent)
        self.ui = Ui_FolderOptionWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.FolderButton.setIcon(QIcon(r'icons\folder.png'))


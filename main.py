import sys
import bpy  # required import in main
from PySide6.QtCore import QCoreApplication, QThread
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    QThread.currentThread().setPriority(QThread.HighPriority)
    window = MainWindow()
    window.setWindowTitle("REModel")
    window.show()
    sys.exit(app.exec())


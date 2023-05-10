from PySide6.QtWidgets import QApplication
import sys, os
from main_window import MainWindow

app = QApplication(sys.argv)

widget = MainWindow()
widget.show()

app.exec()

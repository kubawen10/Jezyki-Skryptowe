from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QSizePolicy, QHBoxLayout

class OpenFileWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.path_line = QLineEdit("Absolute path to log file")

        open_log_button = QPushButton("Open")
        open_log_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.addWidget(self.path_line)
        layout.addWidget(open_log_button)

        self.setLayout(layout)
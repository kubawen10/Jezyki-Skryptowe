from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QSizePolicy, QHBoxLayout

# class OpenFileWidget(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent_widget = parent

#         self.path_line = QLineEdit("/home/student/testNASA")

#         open_button = QPushButton("Open")
#         open_button.clicked.connect(self.open_file)
#         open_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

#         layout = QHBoxLayout()
#         layout.addWidget(self.path_line)
#         layout.addWidget(open_button)

#         self.setLayout(layout)

#     def open_file(self):
#         path = self.path_line.text()
#         self.parent_widget.load_file(path)

class OpenFileWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_widget = parent

        self.path_line = QLineEdit("/home/student/testNASA")

        open_button = QPushButton("Open")
        open_button.clicked.connect(self.open_file)
        open_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.addWidget(self.path_line)
        layout.addWidget(open_button)

        self.setLayout(layout)

    def open_file(self):
        path = self.path_line.text()
        self.parent_widget.load_file(path)
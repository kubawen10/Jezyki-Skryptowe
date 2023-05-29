from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QSizePolicy, QHBoxLayout, QFileDialog

class ChooseDBWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent_widget = parent

        self.path_label = QLineEdit()
        self.path_label.setReadOnly(True)

        open_button = QPushButton("Open")
        open_button.clicked.connect(self.select_db)
        open_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(open_button)

        self.setLayout(layout)

    def select_db(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec():
            path = file_dialog.selectedFiles()[0]
            self.path_label.setText(path)
            self.parent_widget.setup_db(path)
from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QWidget, QDateEdit, QVBoxLayout, QListWidget
from open_file_widget import OpenFileWidget
from date_range_widget import DateRangeWidget
from detail_widget import DetailWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("HTTP log reader")

        self.master_list = QListWidget()
        self.detail_widget = DetailWidget()
        self.previous_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        master_layout = QVBoxLayout()
        master_layout.addWidget(DateRangeWidget(self))
        master_layout.addWidget(self.master_list)
        master_layout.addLayout(button_layout)

        master_detail_layout = QHBoxLayout()
        master_detail_layout.addLayout(master_layout)
        master_detail_layout.addWidget(self.detail_widget)

        window_layout = QVBoxLayout()
        window_layout.addWidget(OpenFileWidget(self))
        window_layout.addLayout(master_detail_layout)

        window = QWidget()
        window.setLayout(window_layout)

        self.setCentralWidget(window)





from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QMessageBox
from sqlalchemy import create_engine
from master_list_widget import MasterListWidget
from choose_db_widget import ChooseDBWidget
from detail_widget import DetailWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("WRM Database explorer")
        self.resize(800, 400)

        self.master_list = MasterListWidget(self)
        self.detail_widget = DetailWidget(self)

        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.master_list.previous_station)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.master_list.next_station)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.master_list)
        master_layout.addLayout(button_layout)

        master_detail_layout = QHBoxLayout()
        master_detail_layout.addLayout(master_layout)
        master_detail_layout.addWidget(self.detail_widget)

        window_layout = QVBoxLayout()
        window_layout.addWidget(ChooseDBWidget(self))
        window_layout.addLayout(master_detail_layout)

        window = QWidget()
        window.setLayout(window_layout)
        self.setCentralWidget(window)


    def setup_db(self, path):
        self.db_path = path
        if not path.endswith('.sqlite3'):
            QMessageBox.information(self, "Could not open database", "You should create database with create_database.py")
        else:
            self.engine = create_engine('sqlite:///'+ path, echo=True)
            self.master_list.update_list()


    def row_changed(self, current_row):
        self.set_button_availability(current_row)
        print(self.master_list.currentItem().text())
        self.detail_widget.update_data(self.master_list.currentItem().text())


    def set_button_availability(self, current_row):
        num_items = self.master_list.count()
        if num_items <= 1:
            self.previous_button.setEnabled(False)
            self.next_button.setEnabled(False)
        elif current_row == 0:
            self.previous_button.setEnabled(False)
            self.next_button.setEnabled(True)
        elif current_row == num_items - 1:
            self.previous_button.setEnabled(True)
            self.next_button.setEnabled(False)
        else:
            self.previous_button.setEnabled(True)
            self.next_button.setEnabled(True)


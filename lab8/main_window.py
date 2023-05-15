from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QMessageBox
from open_file_widget import OpenFileWidget
from date_range_widget import DateRangeWidget
from detail_widget import DetailWidget
from entries import Entries
from master_list_widget import MasterListWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("HTTP log reader")
        self.resize(900, 600)

        self.entries = Entries()

        self.master_list = MasterListWidget(self)
        self.detail_widget = DetailWidget()

        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.master_list.previous_entry)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.master_list.next_entry)
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

    def load_file(self, path):
        load_result = self.entries.read_entries(path) 
        self.master_list.update_list(self.entries.entries)
        if not load_result:
            message = QMessageBox.information(self, "Could not read file", "File is either in incorrect format or it is empty.")

    def load_date_restricted(self, date_from, date_to):
        filtered = self.entries.get_entries_between(date_from, date_to)
        self.master_list.update_list(filtered)

    def entry_row_changed(self, current_row):
        self.set_button_availability(current_row)
        self.detail_widget.update_data(self.master_list.get_current_entry())

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

        





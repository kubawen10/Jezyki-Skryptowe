from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QLabel, QDateEdit
from datetime import datetime

class DateRangeWidget(QWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent_widget = parent

        label_from = QLabel("From")
        label_from.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.date_from = QDateEdit()
        self.date_from.setCalendarPopup(True)
        self.date_from.dateChanged.connect(self.date_changed)
        label_to = QLabel("To")
        label_to.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.date_to = QDateEdit()
        self.date_to.setCalendarPopup(True)
        self.date_to.dateChanged.connect(self.date_changed)

        layout = QHBoxLayout()
        layout.addWidget(label_from)
        layout.addWidget(self.date_from)
        layout.addWidget(label_to)
        layout.addWidget(self.date_to)

        self.setLayout(layout)

    def date_changed(self):
        date_from = self.date_from.date()
        date_to = self.date_to.date()
        date_from = datetime(date_from.year(), date_from.month(), date_from.day(), 0, 0, 0)
        date_to = datetime(date_to.year(), date_to.month(), date_to.day(), 23, 59, 59)
        self.parent_widget.load_date_restricted(date_from, date_to)
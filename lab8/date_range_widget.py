from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QLabel, QDateEdit

class DateRangeWidget(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        label_from = QLabel("From")
        label_from.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        date_from = QDateEdit()
        label_to = QLabel("To")
        label_to.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        date_to = QDateEdit()

        layout = QHBoxLayout()
        layout.addWidget(label_from)
        layout.addWidget(date_from)
        layout.addWidget(label_to)
        layout.addWidget(date_to)

        self.setLayout(layout)
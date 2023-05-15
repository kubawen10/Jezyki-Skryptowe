from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QFormLayout
from PySide6 import QtCore
from entry import Entry

class DescribedFramedLabel(QWidget):
    def __init__(self, description):
        super().__init__()
        self.description = QLabel(description)
        self.data = QLabel()
        self.data.setStyleSheet("border: 1px solid black; color: white")
        self.data.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
    
    def desc_data(self):
        return self.description, self.data

    def update_data(self, data):
        self.data.setText(data)


class DetailWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.host = DescribedFramedLabel("Remote host")
        self.date = DescribedFramedLabel("Date")
        self.time = DescribedFramedLabel("Time")
        self.timezone = DescribedFramedLabel("Timezone")
        self.status = DescribedFramedLabel("Status code")
        self.method = DescribedFramedLabel("Method")
        self.resource = DescribedFramedLabel("Resource")
        self.bytes = DescribedFramedLabel("Size")

        layout = QFormLayout()
        layout.addRow(*self.host.desc_data())
        layout.addRow(*self.date.desc_data())
        layout.addRow(*self.time.desc_data())
        layout.addRow(*self.timezone.desc_data())
        layout.addRow(*self.status.desc_data())
        layout.addRow(*self.method.desc_data())
        layout.addRow(*self.resource.desc_data())
        layout.addRow(*self.bytes.desc_data())

        self.setLayout(layout)


    def update_data(self, entry: Entry):
        if entry != None:
            self.host.update_data(entry.address)
            self.date.update_data(entry.date.date().isoformat())
            self.time.update_data(entry.date.time().isoformat())
            self.timezone.update_data(entry.timezone)
            self.status.update_data(entry.response_code)
            self.method.update_data(entry.method)
            self.resource.update_data(entry.resource)
            self.bytes.update_data(f'{entry.bytes} bytes')
        else:
            self.host.update_data("")
            self.date.update_data("")
            self.time.update_data("")
            self.timezone.update_data("")
            self.status.update_data("")
            self.method.update_data("")
            self.resource.update_data("")
            self.bytes.update_data("")
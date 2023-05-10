from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QSizePolicy, QGridLayout, QFormLayout
from entry import Entry

class DescribedFramedLabel(QWidget):
    def __init__(self, description):
        super().__init__()
        self.description = QLabel(description)
        self.data = QLabel()
        self.data.setStyleSheet("border: 1px solid black;")

        self.data.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    
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
        self.host.update_data(entry.address)
        self.date.update_data(entry.date.date())
        self.time.update_data(entry.date.time())
        self.timezone.update_data(entry.timezone)
        self.status.update_data(entry.response_code)
        self.method.update_data(entry.method)
        self.resource.update_data(entry.resource)
        self.bytes.update_data(f'{entry.bytes} bytes')
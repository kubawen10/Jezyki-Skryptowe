from typing import Optional
from PySide6.QtWidgets import QListWidget, QAbstractItemView
from queries import get_stations

class MasterListWidget(QListWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent_widget = parent
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.currentRowChanged.connect(self.parent_widget.row_changed)
        self.setSortingEnabled(True)
        self.clear()

    def next_station(self):
        self.setCurrentRow(self.currentRow() + 1)

    def previous_station(self):
        self.setCurrentRow(self.currentRow() - 1)

    def update_list(self):
        self.clear()
        stations = get_stations(self.parent_widget.engine)

        for station in stations:
            self.addItem(station[0].name)

        if len(stations) > 0:
            self.setCurrentRow(0)

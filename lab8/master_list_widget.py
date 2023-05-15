from typing import Optional
from PySide6.QtWidgets import QListWidget, QAbstractItemView

class MasterListWidget(QListWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.currently_displayed_entries = []
        self.parent_widget = parent
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.currentRowChanged.connect(self.parent_widget.entry_row_changed)
        self.clear()

    def next_entry(self):
        self.setCurrentRow(self.currentRow() + 1)

    def previous_entry(self):
        self.setCurrentRow(self.currentRow() - 1)

    def update_list(self, entries):
        self.clear()

        self.currently_displayed_entries = entries
        for entry in entries:
            self.addItem(repr(entry))

        if len(entries) > 0:
            self.setCurrentRow(0)

    def get_current_entry(self):
        if self.currentRow() == -1:
            return None
        
        return self.currently_displayed_entries[self.currentRow()]
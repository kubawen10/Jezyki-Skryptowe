from entry import Entry
import os
from datetime import datetime
from typing import List
class Entries:
    def __init__(self) -> None:
        self.cur_path = ''
        self.entries = []

    def read_entries(self, path) -> bool:
        if os.path.isabs(path) and os.path.isfile(path):
            with open(path) as file:
                new_entries = []
                for line in file:
                    try:
                        new_entries.append(Entry(line.rstrip()))
                    except ValueError as e:
                        pass
                if len(new_entries) > 0:
                    self.entries = new_entries
                    self.cur_path = path
                    return True
        return False
    
    def get_entries_between(self, date_start: datetime, date_end: datetime) -> List[Entry]:
        entries_between = []
        if date_start > date_end: 
            return []
        for entry in self.entries:
            if entry.is_between(date_start, date_end):
                entries_between.append(entry)
        return entries_between
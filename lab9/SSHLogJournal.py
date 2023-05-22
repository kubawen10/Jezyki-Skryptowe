from SSHFactory import SSHFactory
from SSHEntryClasses import *
from ipaddress import IPv4Address
from datetime import datetime
from typing import List, Iterator

class SSHLogJournal:
    def __init__(self) -> None:
        self.entries: List['SSHLogEntry'] = []

    def __len__(self) -> int:
        return len(self.entries)
    
    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.entries)
    
    def __contains__(self, item: 'SSHLogEntry') -> bool:
        return item in self.entries
    
    def append(self, entry_str: str) -> bool:
        entry: 'SSHLogEntry' = SSHFactory.get_entry_class(entry_str)
        if entry.validate():
            self.entries.append(entry)
            return True
        return False
    
    def get_ip_entries(self, ip: IPv4Address) -> List['SSHLogEntry']:
        return [entry for entry in self.entries if entry.has_ip and entry.get_ip() == ip]
    
    #__getattr__ for this class doesnt make sense I guess so I implemented __getitem__
    def __getattr__(self, attr) -> None:
        print(f"{attr} attribute doesnt exist for class {self.__class__.__name__}")

    def __getitem__(self, key)-> list[SSHLogEntry] | SSHLogEntry | None:
        if isinstance(key, slice):
            start: int
            stop: int
            step: int
            start, stop, step = key.indices(len(self))
            return [self.entries[i] for i in range(start, stop, step)]
        else:
            if isinstance(key, IPv4Address):
                return self.get_ip_entries(key)
            if isinstance(key, int):
                return self.entries[key]
            if isinstance(key, datetime):
                return [entry for entry in self.entries if entry.date == key]
        return None
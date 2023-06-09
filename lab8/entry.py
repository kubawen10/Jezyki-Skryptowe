import re
from datetime import datetime
import locale
class Entry:
    HTTP_ENTRY_PATTERN = re.compile(r'^(?P<address>[^\s]+)\s-\s-\s\[(?P<date>\d+\/\w+\/\d+:\d+:\d+:\d+)'
                                    r'\s(?P<timezone>-\d+)\]\s\"(?P<method>\w+)\s(?P<resource>.+)'
                                    r'\sHTTP\/1\.0\"\s(?P<response_code>\d+)\s(?P<bytes>\d+)$'
                                    )

    def __init__(self, entry_str):
        self.raw_str = entry_str

        re_match = Entry.HTTP_ENTRY_PATTERN.match(entry_str)
        if not re_match:
            raise ValueError('Entry string cannot be parsed.')
        
        self.address = re_match.group('address')
        # without this there was an error when parsing date
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        self.date = datetime.strptime(re_match.group('date'), '%d/%b/%Y:%H:%M:%S')
        self.timezone = re_match.group('timezone')
        self.method = re_match.group('method')
        self.resource = re_match.group('resource')
        self.response_code = re_match.group('response_code')
        self.bytes = re_match.group('bytes')
    
    def is_between(self, date_start: datetime, date_end: datetime) -> bool:
        return self.date >= date_start and self.date <= date_end

    def __str__(self) -> str:
        return f'{self.address}\n{self.date}\n{self.timezone}\n{self.method}\n{self.resource}\n{self.response_code}\n{self.bytes}'
    
    def __repr__(self) -> str:
        return self.raw_str[:60] + '...'
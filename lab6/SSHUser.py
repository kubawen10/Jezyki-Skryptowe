import re

class SSHUser:
    def __init__(self, username, last_login_date) -> None:
        self.username = username
        self.last_login_date = last_login_date

    def validate(self) -> bool:
        USERNAME_PATTERN = re.compile(r"^[a-z_][a-z0-9_-]{0,31}$")
        return bool(USERNAME_PATTERN.search(self.username))


from SSHFactory import *
from datetime import datetime
import ipaddress
import pytest
from SSHLogJournal import SSHLogJournal

# a
def test_time_extraction():
    entry = 'Dec 10 06:55:48 LabSZ sshd[24200]: Connection closed by 173.234.31.186 [preauth]'
    entry_class = SSHFactory.get_entry_class(entry)
    proper_date = datetime.strptime('Dec 10 06:55:48', '%b %d %H:%M:%S')
    assert entry_class.date == proper_date

# b1
def test_ipv4_extraction_proper():
    entry = 'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2'
    entry_class = SSHFactory.get_entry_class(entry)
    proper_ip = ipaddress.IPv4Address('173.234.31.186')
    assert entry_class.get_ip() == proper_ip

# b2
def test_ipv4_extraction_wrong():
    entry = 'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 666.777.88.213 port 38926 ssh2'
    entry_class = SSHFactory.get_entry_class(entry)
    with pytest.raises(ipaddress.AddressValueError):
        entry_class.get_ip()

# b3 
def test_ipv4_extraction_no_address():
    entry = 'Dec 10 07:07:38 LabSZ sshd[24206]: pam_unix(sshd:auth): check pass; user unknown'
    entry_class = SSHFactory.get_entry_class(entry)

    assert entry_class.get_ip() == None

# c
@pytest.mark.parametrize("entry, expected",[
    ('Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2', SSHFailedPassword),
    ('Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2', SSHAcceptedPassword),
    ('Dec 10 07:51:20 LabSZ sshd[24326]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]', SSHError),
    ('Dec 10 07:53:26 LabSZ sshd[24329]: Connection closed by 194.190.163.22 [preauth]', SSHOther)
])
def test_append(entry, expected):
    journal = SSHLogJournal()
    journal.append(entry)
    assert isinstance(journal[0], expected)

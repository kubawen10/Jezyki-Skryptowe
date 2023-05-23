import sys
import os
from sqlalchemy import create_engine
from models import Base


def validate_args() -> bool:
    if len(sys.argv) != 2:
        print("Incorrect argument! You should provide the name of database you want to create!")
        sys.exit(1)

    if os.path.isfile(sys.argv[1] + '.sqlite3'):
        print("Such database already exists!")
        sys.exit(1)


if __name__ == '__main__':
    validate_args()

    engine = create_engine('sqlite:///'+ sys.argv[1] +'.sqlite3', echo=True)
    Base.metadata.create_all(engine)

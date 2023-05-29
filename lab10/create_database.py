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

def create_database(database_name):
    engine = create_engine('sqlite:///'+ database_name +'.sqlite3', echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    validate_args()
    create_database(sys.argv[1])

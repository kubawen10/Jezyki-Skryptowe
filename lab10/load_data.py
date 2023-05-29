import sys
import os
import csv
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import select
from models import Station, Rental


def validate_args():
    if len(sys.argv) != 3:
        print('Incorrect arguments! You should provide filename of rentals and database you want to store them in!')
        sys.exit(1)

    csv_file = sys.argv[1]

    if not os.path.isfile(csv_file):
        print('Such file doesnt exist!')
        sys.exit(1)
    
    if not csv_file.endswith('.csv'):
        print('You should provide .csv file!')
        sys.exit(1)

    database_file = sys.argv[2] + '.sqlite3'

    if not os.path.isfile(database_file):
        print('Such database doesnt exist! You can create one with create_database.py')
        sys.exit(1)


def validate_columns(columns: List[str]):
    proper_columns = ['UID wynajmu', 'Numer roweru', 'Data wynajmu', 'Data zwrotu', 'Stacja wynajmu', 'Stacja zwrotu', 'Czas trwania']
    if sorted(proper_columns) != sorted(columns):
        print('Provided file has wrong colums!')
        sys.exit(1)


def station_provider(session):
    stations_dict = {}
    def get_station(station_name):
        if station_name in stations_dict:
            return stations_dict[station_name]
        
        station = session.scalar(select(Station).where(Station.name == station_name))
        if station is not None:
            return station
        
        station = Station(name = station_name)
        stations_dict[station_name] = station

        return station
        
    return get_station


def load_data_to_database(data, db_name):
    engine = create_engine('sqlite:///'+ db_name +'.sqlite3')
    with Session(engine) as session:
        get_station = station_provider(session)
        for row in data:
            id = int(row['UID wynajmu'])
            bike_number = int(row['Numer roweru'])

            date_fromat = '%Y-%m-%d %H:%M:%S'
            rental_date = datetime.strptime(row['Data wynajmu'], date_fromat)
            return_date = datetime.strptime(row['Data zwrotu'], date_fromat)

            rental_station = get_station(row['Stacja wynajmu'])
            return_station = get_station(row['Stacja zwrotu'])

            duration = int(row['Czas trwania'])

            session.add(Rental(id=id, 
                            bike_number=bike_number, 
                            rental_date=rental_date,
                            return_date=return_date,
                            rental_station=rental_station,
                            return_station=return_station,
                            duration=duration))
            
        session.commit()


if __name__ == '__main__':
    validate_args()
    csv_file = sys.argv[1]
    db_name = sys.argv[2]
        
    with open(csv_file, 'r') as file:
        data = csv.DictReader(file)
        validate_columns(list(data.fieldnames))
        load_data_to_database(list(data), db_name)
        


    
    

    


    

        
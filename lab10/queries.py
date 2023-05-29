from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Station, Rental


def mean_duration_at_given_rental_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rental).join(Station, Rental.rental_station_id == Station.id).where(Station.name==station_name)
        rentals = session.execute(statement).all()
        return mean_duration(rentals)


def mean_duration_at_given_return_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rental).join(Station, Rental.return_station_id == Station.id).where(Station.name==station_name)
        rentals = session.execute(statement).all()
        return mean_duration(rentals)
    

def number_of_unique_bikes_parked_at_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rental).join(Station, Rental.return_station_id == Station.id).where(Station.name==station_name)
        rentals = session.execute(statement).all()
        bikes_set = set(rental[0].bike_number for rental in rentals)
        return len(bikes_set)


def number_of_rentals_with_same_rental_and_return_station(station_name, engine):
    with Session(engine) as session:
        statement = select(Rental).join(Station, Rental.return_station_id == Station.id).where(Station.name==station_name).filter(Rental.rental_station_id == Rental.return_station_id)
        rentals = session.execute(statement).all()
        return len(rentals)
    

def mean_duration(rentals):
    if len(rentals) == 0:
        return 0
    
    duration_sum = 0
    for rental in rentals:
        duration_sum += rental[0].duration

    return duration_sum/len(rentals)

def get_stations(engine):
    with Session(engine) as session:
        statement = select(Station)
        return session.execute(statement).all()
        


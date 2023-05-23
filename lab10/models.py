from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List


class Base(DeclarativeBase):
    pass


class Rental(Base):
    __tablename__ = 'rentals'
    id: Mapped[int] = mapped_column(primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    rental_date: Mapped[datetime] = mapped_column(DateTime)
    return_date: Mapped[datetime] = mapped_column(DateTime)

    rental_station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    rental_station: Mapped['Station'] = relationship('Station', foreign_keys=[rental_station_id])

    return_station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    return_station: Mapped['Station'] = relationship('Station', foreign_keys=[return_station_id])

    duration: Mapped[int] = mapped_column(Integer)

    # def __repr__(self) -> str:
    #     return f'Rental(id={self.id!r}, bike_numer={self.bike_number!r}, rental_time={self.rental_time!r}, return_time={self.return_time!r}, duration={self.duration!r})'

    def __repr__(self) -> str:
        return f'Rental(id={self.id!r}, bike_numer={self.bike_number!r})'

class Station(Base):
    __tablename__ = 'stations'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    # rental_stations: Mapped[List['Rental']] = relationship(back_populates='rental_station')
    # return_stations: Mapped[List['Rental']] = relationship(back_populates='return_station')

    def __repr__(self) -> str:
        return f'Station(id={self.id!r}, name={self.name!r})'
    

# engine = create_engine('sqlite:///test.sqlite3', echo=True)
# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     rent_station = session.scalar(select(Station).where(Station.name == "Other"))
#     return_station = session.scalar(select(Station).where(Station.name == "Grunwald"))

#     if rent_station is None:
#         print("No rent Station")
#         rent_station = Station(name='Other')

#     if return_station is None:
#         print("No return Station")
#         return_station = Station(name='Grunwald')

#     rental = Rental(id=1, bike_number=0, rental_station = rent_station, return_station=return_station)

#     session.add(rental)
#     session.commit()

#     print(session.query(Rental).all())




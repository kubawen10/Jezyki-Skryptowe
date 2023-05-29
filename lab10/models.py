from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Rental(Base):
    __tablename__ = 'rentals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    rental_date: Mapped[datetime] = mapped_column(DateTime)
    return_date: Mapped[datetime] = mapped_column(DateTime)

    rental_station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    rental_station: Mapped['Station'] = relationship('Station', foreign_keys=[rental_station_id])

    return_station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    return_station: Mapped['Station'] = relationship('Station', foreign_keys=[return_station_id])

    duration: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f'Rental(id={self.id!r}, bike_numer={self.bike_number!r}, rental_date={self.rental_date!r}, return_time={self.return_date!r}, duration={self.duration!r})'


class Station(Base):
    __tablename__ = 'stations'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        return f'Station(id={self.id!r}, name={self.name!r})'


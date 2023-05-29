from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QFormLayout
from PySide6 import QtCore
from queries import *

class DescribedFramedLabel(QWidget):
    def __init__(self, description):
        super().__init__()
        self.description = QLabel(description)
        self.data = QLabel()
        self.data.setStyleSheet("border: 1px solid black; color: white")
        self.data.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
    
    def desc_data(self):
        return self.description, self.data

    def update_data(self, data):
        if isinstance(data, int):
            self.data.setText(str(data))
        elif isinstance(data,float):
            self.data.setText(f"{data:.2f}")
        else:
            self.data.setText(data)


class DetailWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent_widget = parent
        self.mean_started = DescribedFramedLabel("Mean duration as rental station")
        self.mean_ended = DescribedFramedLabel("Mean duration as return station")
        self.num_of_unique_bikes = DescribedFramedLabel("Number of unique bikes")
        self.num_of_same_start_and_end = DescribedFramedLabel("Number of same rental and return station")

        layout = QFormLayout()
        layout.addRow(*self.mean_started.desc_data())
        layout.addRow(*self.mean_ended.desc_data())
        layout.addRow(*self.num_of_unique_bikes.desc_data())
        layout.addRow(*self.num_of_same_start_and_end.desc_data())

        self.setLayout(layout)


    def update_data(self, station_name): 
        self.mean_started.update_data(mean_duration_at_given_rental_station(station_name, self.parent_widget.engine))
        self.mean_ended.update_data(mean_duration_at_given_return_station(station_name, self.parent_widget.engine))
        self.num_of_unique_bikes.update_data(number_of_unique_bikes_parked_at_station(station_name, self.parent_widget.engine))
        self.num_of_same_start_and_end.update_data(number_of_rentals_with_same_rental_and_return_station(station_name, self.parent_widget.engine))


from csv import reader
from datetime import datetime
from domain.aggregated_data import AggregatedData
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking
from typing import List

class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str, parking_filename: str, rows_to_return: int = 5) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename
        self.rows_to_return = rows_to_return
        pass


    def read(self) -> List[AggregatedData]:
        """Метод повертає дані отримані з датчиків"""
        list_of_data = []
        for i in range(self.rows_to_return):
            list_of_parking = next(self.parking_list_read)
            list_of_data.append(AggregatedData(Accelerometer(*next(self.accelerometer_list_reader)),Gps(*next(self.gps_list_reader)),Parking(list_of_parking[0], list_of_parking[1:]),datetime.now()))
        return list_of_data
        
    def read_file(self, path: str):
        while True:
            file_reading = open(path)
            data_reader = reader(file_reading)
            head_tabl = next(data_reader)
            for row in data_reader:
                yield row
            file_reading.close()

    def startReading(self, *args, **kwargs):
        """Метод повинен викликатись перед початком читання даних"""
        self.accelerometer_list_reader = self.read_file(self.accelerometer_filename)
        self.gps_list_reader = self.read_file(self.gps_filename)
        self.parking_list_read = self.read_file(self.parking_filename)

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
        pass
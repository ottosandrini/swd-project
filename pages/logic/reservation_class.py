import os
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import datetime
from devices import Device

class DeviceReservation(Device):
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('DeviceReservation')

    def __init__(self, device: str, user: str, date: date):
        self.device = device
        self.user = user
        self.date = date
    def __dict__(self):
        cls_dict = {"type":"reservation", "user":self.user, "date":self.date, "dev":self.device}
        return cls_dict
   
    def check_device_availability(self) -> bool:
        datetocheck = self.date
        if datetocheck.weekday() in [5, 6]:  # Saturday = 5, Sunday = 6
            return False  # Device is not available on weekends
        else:
            list_of_reservations = []
            ReservationQuery = Query()
            result = self.dbconnector.search(ReservationQuery.type == reservation)
            for i in result:
                if date_to_check == i:
                    return False
                else:
                    return True
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")


    @classmethod
    def load_data_by_reservation_name(cls, rsv_name):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'])
        else:
            return None

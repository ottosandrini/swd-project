import os
from tinydb import TinyDB, Query
from .serializer import serializer
from datetime import datetime
from .devices import Device

class DeviceReservation:
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device: str, user: str, date: str, reason: str):
        self.type = 'reservation'
        self.device = device
        self.user = user
        self.date = date
        self.reason = reason
   
    def check_device_availability(self, res_list) -> bool:
        datetocheck = self.date
        if datetocheck.weekday() in [5, 6]:  # Saturday = 5, Sunday = 6
            print("Weekend -- fail")
            return False  # Device is not available on weekends
        else:
            list_of_reservations = []
            if res_list:
                for i in res_list:
                    if datetocheck == i['date']:
                        return False
                    else:
                        return True
            else:
                print("No results")
                return True
    
    def store_data(self):
        print("Storing data...")
        self.db_connector.insert(self.__dict__)
        print("Data inserted.")


    @classmethod
    def get_all_reservations(cls):
        reservations = []
        reservationsQuery = Query()
        result = cls.db_connector.all()
        if result:
            for i in result:
                if 'type' in i:
                    reservations.append(i)
            return reservations
        else:
            print("No reservations found!")
            return None
        
    @classmethod
    def get_all_devices(cls):
        devices = []
        DeviceQuery = Query()
        result = cls.db_connector.all()

        if result:    
            for i in result:
                if i['device_name']:
                    devices.append(i["device_name"])
        else:
            print("Nothing in the Databse")
        return devices




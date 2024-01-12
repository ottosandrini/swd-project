# our version of devices.py
import os
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import datetime


class Device():
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name: str, responsible_person: str, end_of_life, next_maintenance, maintenance_interval, maintenance_cost, creation_date=datetime.now()):
        self.device_name = device_name
        self.responsible_person = responsible_person
        self.creation_date = creation_date
        self.end_of_life = end_of_life
        self.next_maintenance = next_maintenance() 
        self.maintenance_interval = maintenance_interval
        self.maintenance_cost = maintenance_cost

    def __str__(self):
        return f'Device {self.device_name} ({self.responsible_person})'

    def __repr__(self):
        return self.__str__()

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
    def load_data_by_device_name(cls, device_name):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'])
        else:
            return None


############################################################################################
############################################################################################


class DeviceReservation(Device):
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name: str, managed_by_user_id: str):
        super().__init__(device_name, managed_by_user_id)
        self.reservations_db = TinyDB('reservations.json')

    def reserve_device(self, user_id: str, reservation_date: str):
        device_available = self.check_device_availability(reservation_date)

        if not device_available:
            return "User does not exist. Reservation failed."

        # Check if the device exists
        device_exists = self.check_device_availability(self.device_name)
        if ndb_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')ot device_exists:
            return "Device does not exist. Reservation failed."
        if device_available:
            reservation_details = {
                'user_id': user_id,
                'device_name': self.device_name,
                'reservation_date': reservation_date
            }

            self.reservations_db.insert(reservation_details)
            return "Gerät erfolgreich reserviert!"
        else:
            return "Gerät ist an diesem Datum nicht verfügbar!"

    def check_device_availability(self, date_to_check: str) -> bool:

        check_date = datetime.strptime(date_to_check, "%Y-%m-%d")
        
        if check_date.weekday() in [5, 6]:  # Samstag = 5, Sonntag = 6
            return False  # Gerät ist an Wochenenden nicht verfügbar
        else:
            return True  # Gerät ist an Wochentagen verfügbar

    def check_user_existence(self, user_id: str) -> bool:
        User = Query()
        user_result = self.users_db.search(User.user_id == user_id)
        return bool(user_result)  # Return True if user exists, False otherwise

    def check_device_existence(self, device_name: str) -> bool:
        DeviceQuery = Query()
        device_result = self.db_connector.search(DeviceQuery.device_name == device_name)
        return bool(device_result)  # Return True if device exists, False otherwise

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



class MaintenancePlan(Device):
    def __init__(self, device: Device, maintenance_date: str, details: str):
        self.device = device  
        self.maintenance_date = maintenance_date
        self.details = details

if __name__ == "__main__":
    # Beispiel für die Verwendung der Klassen
    device1 = Device("Device1", "first@mci.edu")
    device2 = Device("Device2", "second@mci.edu")
    device3 = Device("Device3", "third@mci.edu")
    device1.store_data()
    device2.store_data()

    device3.store_data()
    device4 = Device("Device3", "fourth@mci.edu")
    device4.store_data()

    loaded_device = Device.load_data_by_device_name('Device2')
    if loaded_device:
        print(f"Loaded Device: {loaded_device}")
    else:
        print("Device not found.")

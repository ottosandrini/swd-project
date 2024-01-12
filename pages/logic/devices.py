import os
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import datetime


class Device():
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name: str, responsible_person: str, creation_date=datetime.now(), end_of_life, next_maintenance, maintenance_interval, maintenance_cost):
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

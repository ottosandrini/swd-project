import os
from tinydb import TinyDB, Query
if __name__ == "__main__":
    from serializer import serializer
else:
    from .serializer import serializer
from datetime import datetime

class Device():
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, id: int, device_name: str, responsible_person: str, last_update:datetime, creation_date: datetime, end_of_life:datetime, first_maintenance:datetime,
                next_maintenance:datetime, maintenance_interval:int, maintenance_cost:float):
        self.id = id
        self.device_name = device_name
        self.responsible_person = responsible_person
        self.__last_update = last_update
        self.__creation_date = creation_date
        self.end_of_life = end_of_life
        self.first_maintenance = first_maintenance
        self.next_maintenance = next_maintenance
        self.maintenance_interval = maintenance_interval
        self.maintenance_cost = maintenance_cost

    def __str__(self):
        formatted_string = (f'Device {self.id} {self.device_name} ({self.responsible_person}), '
                            f'{self.__last_update}, {self.__creation_date}, {self.end_of_life},\n '
                            f'{self.first_maintenance}, {self.next_maintenance}, {self.maintenance_interval}, '
                            f' {self.maintenance_cost}')
        return formatted_string

    def __repr__(self):
        return self.__str__()

    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.id == self.id)
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
            return cls(data["id"], data['device_name'], data['responsible_person'], data["_Device__last_update"], data["_Device__creation_date"], data["end_of_life"],
                    data['first_maintenance'], data["next_maintenance"], data["maintenance_interval"], data["maintenance_cost"])
        else:
            return None
        
    @classmethod
    def load_all_devices(cls):
        result = cls.db_connector.all()
        if result:
            devices = []
            for device_json in result:
                device = cls(device_json["id"], device_json['device_name'], device_json['responsible_person'], device_json["_Device__last_update"], device_json["_Device__creation_date"],
                            device_json["end_of_life"], device_json['first_maintenance'], device_json["next_maintenance"], device_json["maintenance_interval"], device_json["maintenance_cost"])
                devices.append(device)
            return devices
        return None
    
    @classmethod
    def delete_by_name(cls, name):
        deviceQuery = Query()
        result = cls.db_connector.remove(deviceQuery.device_name == name)
        return result


if __name__ == "__main__":
    # Beispiel für die Verwendung der Klassen
    device1 = Device(456443, "Device1", "first@mci.edu", datetime(2020, 12, 12), datetime(2020, 12, 12), datetime(2020, 12, 12), datetime(2020, 12, 12), datetime(2020, 12, 12),
                    40, 450.5)
    # device2 = Device("Device2", "second@mci.edu")
    # device3 = Device("Device3", "third@mci.edu")
    device1.store_data()
    # device2.store_data()

    # device3.store_data()
    # device4 = Device("Device3", "fourth@mci.edu")
    # device4.store_data()

    loaded_device = Device.load_data_by_device_name('Device1')
    all_loaded_devices = Device.load_all_devices()
    # if loaded_device:
    #     print(f"Loaded Device: {loaded_device}")
    # else:
    #     print("Device not found.")

    if all_loaded_devices:
        for loaded_device in all_loaded_devices:
            print(loaded_device)
    else:
        print("Device not found.")

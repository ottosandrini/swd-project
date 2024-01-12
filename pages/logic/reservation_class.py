import os
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import datetime
from devices import Device

class DeviceReservation(Device):
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name: str, managed_by_user_id: str):
        super().__init__(device_name, managed_by_user_id)
        self.reservations_db = TinyDB('reservations.json')

    def check_device_availability(self, date_to_check: str) -> bool:

        check_date = datetime.strptime(date_to_check, "%Y-%m-%d")
    
        if check_date.weekday() in [5, 6]:  # Samstag = 5, Sonntag = 6
            return False  # Gerät ist an Wochenenden nicht verfügbar
        else:
            return True  # Gerät ist an Wochentagen verfügbar


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

import streamlit as st
import pandas as pd
from logic.devices import Device
from tinydb import TinyDB, Query
import os
import os.path
from datetime import datetime
from logic.reservation_class import DeviceReservation
from logic import reservation_class as rc
from logic import serializer as myserializer
from logic.serializer import DateSerializer


devices_maintenance_costs = Device.db_connector.all()
#print(devices_maintenance_costs)

#devices_in_db =  Device.db_connector.load_data_by_device_name()#DeviceReservation.get_all_devices()
# reservations_in_db = DeviceReservation.get_all_devices()
reservations_in_db = Device.load_all_devices()
#print(reservations_in_db)

class Wartungskosten():
    #db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    #db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logic/database.json'), storage=serializer).table('devices')

    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logic\\database.json'), storage=myserializer.serializer).table('devices')

    def __init__(self, device: str, date: str, cost: float):
        #self.type = 'device'
        self.device = device
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.cost = cost

    def store_costs(self):
        print("Storing data...")
        self.db_connector.insert(self.__dict__)
        print("Data inserted.")


    @classmethod
    def get_all_costs(cls):
        costs = []
        cost_query = Query()
        result = None#cls.db_connector.search(cost_query.type == 'maintenance_cost')
        if result:
            pass
            #for i in result:
                #costs.append(i)
            #return costs
        else:
            print("No maintenance costs found!")
            return None
    @classmethod
    def load_data_by_device_name(device_reservation: DeviceReservation):
        device_name = device_reservation.device_name
        device_data = next((device for device in devices_maintenance_costs if device['device_name'] == device_name), None)
        return device_data
    
date = "2018-02-01" 

#check_=DeviceReservation.check_device_availability(reservations_in_db)

choosen_device_name = st.selectbox(label="Wähle ein Gerät für die Wartungskosten", options=[i.device_name for i in reservations_in_db])

#chosen_device = st.selectbox(label="Wähle ein Gerät für die Wartungstermine", options=[i['type'] for i in reservations_in_db])

#selected_device_data = st.table(label = "Selected device : ", value = Device.load_data_by_device_name(chosen_device))

#selected_device_data = Device.load_data_by_device_name(chosen_device)

#selected_device_data = Device.load_data_by_device_name(chosen_device)

#print(selected_device_data)

print(reservations_in_db)
choosen_device = Device.load_data_by_device_name(choosen_device_name)
maintenance_cost = choosen_device.maintenance_cost
next_maintenance = choosen_device.next_maintenance
# df = pd.DataFrame(reservations_in_db)

# df_selected_device = df[df['device'] == choosen_device_name]
# df = pd.DataFrame(df_selected_device)

# st.table(df_selected_device)


# cost_df = pd.DataFrame(reservations_in_db)
# cost_df_selected_device = df[df['date'] == choosen_device_name]
# df = pd.DataFrame(cost_df_selected_device)
df = pd.DataFrame([maintenance_cost, next_maintenance])
st.table(df)

#maintenance_cost = Wartungskosten(chosen_device, date, cost_input) 
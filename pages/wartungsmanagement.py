import streamlit as st
import pandas as pd
from logic.devices import Device
from tinydb import TinyDB, Query
import os
from datetime import datetime
from logic.reservation_class import DeviceReservation
from logic import serializer 


devices_maintenance_costs = Device.db_connector.all()
devices_in_db = DeviceReservation.get_all_devices()
reservations_in_db = DeviceReservation.get_all_reservations()

class Wartungskosten:
    def __init__(self, device: str, date: str, cost: float):
        self.type = 'maintenance_cost'
        self.device = device
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.cost = cost

    def calculate_costs(self):
        pass

    @classmethod
    def get_all_costs(cls):
        costs = []
        cost_query = Query()
        result = cls.db_connector.search(cost_query.type == 'maintenance_cost')
        if result:
            for i in result:
                costs.append(i)
            return costs
        else:
            print("No maintenance costs found!")
            return None

date = "2018-02-01" 

chosen_device = st.selectbox(label="Wähle ein Gerät für die Wartungskosten", options=devices_in_db)

#selected_device_data = st.table(label = "Selected device : ", value = Device.load_data_by_device_name(chosen_device))

selected_device_data = Device.load_data_by_device_name(chosen_device)

df_selected_device_data = pd.DataFrame([selected_device_data])

st.table(df_selected_device_data)



cost_input = st.number_input(label="Geben Sie die Wartungskosten ein", value=0.0)

maintenance_cost = Wartungskosten(chosen_device, date, cost_input)
 
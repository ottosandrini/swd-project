import streamlit as st
import pandas as pd

def get_maintenance_dates():
    pass

def calculate_costs():
    pass

dict_of_dates = {"Device 1": "8.1.2024", "Device 2":"9.1.2024", "Device 3":"10.1.2024", "Device 4":"11.1.2024"}
df = pd.DataFrame(list(dict_of_dates.items()), columns=['Device Name', 'Scheduled Maintenance Date'])

st.write("# Wartungsmanagement")

st.table(df)

st.write('# Wartungskosten')


dict_of_costs = {"Device 1": "200", "Device 2":"150", "Device 3":"200", "Device 4":"210"}
df2 = pd.DataFrame(list(dict_of_costs.items()), columns=['Device Name', 'Maintenance cost'])

st.table(df2)

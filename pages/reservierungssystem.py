import streamlit as st
import pandas as pd
from logic import reservation_class 

def get_user():
    user="Bella"
    return user

st.set_page_config(page_title="Reservierungssystem")
col1, col2 = st.columns(2)

with col1:
    dict_of_dates = {"Device 1": "8.1.2024", "Device 2":"9.1.2024", "Device 3":"10.1.2024", "Device 4":"11.1.2024"}
    df = pd.DataFrame(list(dict_of_dates.items()), columns=['device', 'reserved date'])

    st.header("Reservierungen")

    st.table(df)


with col2:

    local_usr = get_user()
    st.header("Neue Reservierung")
    list_of_available_devices=["dev1", "dev2"]

    chosen_device = st.selectbox(label="Wähle ein Gerät zum reservieren", options=list_of_available_devices)
    chosen_date = st.date_input(label="Wähle ein Startdatum:")
    reason = st.text_input(label="Reservierungsgrund:")

    if st.button(label="Reservierung speichern", key="save_reservation"):
        rsv = DeviceReservation(chosen_device, local_usr, chosen_date, reason)
        if rsv.check_device_availability():
            rsv.save_data()
        else:
            st.error("Das Gerät ist für diesen Zeitraum schon gebucht")


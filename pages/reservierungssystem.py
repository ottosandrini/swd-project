import streamlit as st
import pandas as pd
from logic import reservation_class as rc

def get_user():
    user="Bella"
    return user

devices_in_db = rc.DeviceReservation.get_all_devices()
reservations_in_db = rc.DeviceReservation.get_all_reservations()

st.set_page_config(page_title="Reservierungssystem")
col1, col2 = st.columns(2)

names_list = []
dates_list = []
if reservations_in_db:
    for i in reservations_in_db:
        names_list.append(i['device'])
        dates_list.append(i['date'])

with col1:
    df = pd.DataFrame({'device':names_list, 'reserved date':dates_list})

    st.header("Reservierungen")

    st.table(df)


with col2:

    local_usr = get_user()
    st.header("Neue Reservierung")

    chosen_device = st.selectbox(label="Wähle ein Gerät zum reservieren", options=devices_in_db)
    chosen_date = st.date_input(label="Wähle ein datum:")
    reason = st.text_input(label="Reservierungsgrund:")

    if st.button(label="Reservierung speichern", key="save_reservation"):
        rsv = rc.DeviceReservation(chosen_device, local_usr, chosen_date, reason)
        if rsv.check_device_availability(reservations_in_db):
            rsv.store_data()
        else:
            st.error("Das Gerät ist für diesen Zeitraum schon gebucht")


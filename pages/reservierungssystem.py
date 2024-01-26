import streamlit as st
import pandas as pd
from logic import reservation_class as rc
st.set_page_config(layout="wide", page_title = "Reservierungssystem")
def get_user():
    user="Bella"
    return user

def check_conditions(user, dev, date, reason, test_list):
    rsv = rc.DeviceReservation(dev, user, date, reason)
    if rsv.check_device_availability(reservations_in_db):
        pass
    else:
        st.error('Device not available on chosen date')
        return None
    if rsv.check_weekday():
        pass
    else:
        st.error('Device not available on weekends')
        return None
    if reason == "":
        st.error('Please enter a valid reason')
        return None
    return rsv


devices_in_db = rc.DeviceReservation.get_all_devices()
reservations_in_db = rc.DeviceReservation.get_all_reservations()
local_usr = get_user()

col1, col2, col3 = st.columns(3)

names_list = []
dates_list = []
myreservations = []
if reservations_in_db:
    for i in reservations_in_db:
        names_list.append(i['device'])
        dates_list.append(i['date'])
        if i['user'] == local_usr:
            lpentry = [i['device'], i['date']]
            myreservations.append(lpentry)

with col1:
    df = pd.DataFrame({'device':names_list, 'reserved date':dates_list})
    st.header("Reservierungen")
    st.table(df)


with col2:
    st.header("Neue Reservierung")

    chosen_device = st.selectbox(label="Wähle ein Gerät zum reservieren", options=devices_in_db)
    chosen_date = st.date_input(label="Wähle ein datum:")
    reason = st.text_input(label="Reservierungsgrund:")

    if st.button(label="Reservierung speichern", key="save_reservation"):
        rsv = check_conditions(local_usr, chosen_device, chosen_date, reason, reservations_in_db)
        if rsv != None:
            rsv.store_data()
            st.rerun()

with col3:
    st.header("Reservierung löschen:")
    chosen_device = st.selectbox(label="Welche Reservierung soll gelöscht werden?", options=myreservations)
    if st.button(label="Reservierung löschen", key="del_reservation"):
        rc.DeviceReservation.delete_single_res(chosen_device[0], chosen_device[1])
        st.rerun()

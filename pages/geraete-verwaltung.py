import streamlit as st
import os
import sys
from logic.devices import Device

def is_user_active():
    if 'user_active' in st.session_state.keys() and st.session_state['user_active']:
        return True
    else:
        return False

all_devices = Device.load_all_devices()
devices_names = [device.device_name for device in all_devices]

if is_user_active():
    with st.form('form'):
        
        id = st.text_input('id')
        name = st.text_input('name')
        responsible_person = st.text_input('responsible person')
        last_update = st.date_input('last update')
        creation_date = st.date_input('creation date')
        end_of_life = st.date_input('end of life')
        first_maintenance = st.date_input('first maintenance')
        next_maintenance = st.date_input('next maintenance')
        maintenance_interval = st.number_input('maintenance interval (days)', step=1, min_value=1)
        maintenance_cost = st.number_input('maintenance cost', min_value=0, step=1)

        if st.form_submit_button('submit'):
            st.text(f'{id},{name} saved')

            device_from_input =  Device(id, name, responsible_person, last_update, creation_date, end_of_life,
                first_maintenance, next_maintenance, maintenance_interval, maintenance_cost)
            device_from_input.store_data()
            st.session_state['user_active']=False

        if st.form_submit_button('exit'):
            st.session_state['user_active']=False
        
else:
    devices_list = st.selectbox(
        "Choose device to edit",
        devices_names
    )
    if st.button('Add device'):
        st.session_state['user_active']=True
        st.experimental_rerun()

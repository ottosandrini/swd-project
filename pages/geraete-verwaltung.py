import streamlit as st
from logic.devices import Device
from tinydb import TinyDB
import os

def is_form_opened():
    if 'form_opened' in st.session_state.keys() and st.session_state['form_opened']:
        return True
    else:
        return False
    
def get_all_users():
    db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logic/database.json'))
    user_data = db.table('users').all()
    return user_data
    

if __name__ == "__main__":
    st.set_page_config(layout='wide', page_title='Geräte Verwaltung')
    all_devices = Device.load_all_devices()
    devices_names = []
    if all_devices:
        devices_names = [device.device_name for device in all_devices]
    users = get_all_users()
    user_names = []
    if users:
        user_names = [user["Username"] for user in users]

    if is_form_opened():
        with st.form('form'):
            id: int
            # check if new device is created or old one is edited
            if 'edited_device' in st.session_state.keys():
                edited_device = Device.load_data_by_device_name(st.session_state['edited_device'])
                if edited_device:
                    id = edited_device.id
                    st.text(f"You're editing {id}")
            else:
                id = st.text_input('id')

            # all text fields
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
                #if necessary field not filled
                if not name or not id or not responsible_person:
                    st.warning(f"user, id or responsible person not filled in")
                # check if id of new device already exists
                # elif all_devices:
                #     if id in [device.id for device in all_devices] and 'edited_device' not in st.session_state.keys():
                #         st.warning(f'Device with id {id} already exists')
                # check if user exists
                elif responsible_person not in user_names:
                    st.warning(f"no user named {responsible_person}")
                else:
                    device_from_input =  Device(id, name, responsible_person, last_update, creation_date, end_of_life,
                        first_maintenance, next_maintenance, maintenance_interval, maintenance_cost)
                    device_from_input.store_data()
                    st.session_state['form_opened']=False
                    st.session_state['device_saved'] = True
                    st.session_state['name_of_saved_device'] = name
                    if 'edited_device' in st.session_state.keys():
                        del st.session_state['edited_device']
                    st.rerun()

            if st.form_submit_button('exit'):
                st.session_state['form_opened']=False
                if 'edited_device' in st.session_state.keys():
                        del st.session_state['edited_device']
                st.rerun()
            
    else:
        col1, col2 = st.columns([3, 1])

        with col1:
            if all_devices:
                devices_attr = [vars(device) for device in all_devices]
                devices_table = st.table(devices_attr)

        with col2:
            selected_device = st.selectbox(
                "Choose device to edit",
                devices_names
            )

            if all_devices:
                if st.button('Edit'):
                    st.session_state['form_opened']=True
                    st.session_state['edited_device']=selected_device
                    st.rerun()

            if st.button('Add device'):
                st.session_state['form_opened']=True
                st.rerun()

            if st.button('Delete'):
                result = Device.delete_by_name(selected_device)
                device_index = result[0]-1
                if device_index < len(devices_names):
                    st.session_state['deleted_device'] = devices_names[device_index]
                st.rerun()

        if 'device_saved' in st.session_state.keys() and st.session_state['device_saved']:
            st.success('Device ' + st.session_state['name_of_saved_device'] + ' saved')
            st.session_state['device_saved'] = False
            if 'name_of_saved_device' in st.session_state.keys():
                del st.session_state['name_of_saved_device']
        
        if 'deleted_device' in st.session_state.keys():
            st.success('Device ' + st.session_state['deleted_device'] + ' deleted')
            del st.session_state['deleted_device']


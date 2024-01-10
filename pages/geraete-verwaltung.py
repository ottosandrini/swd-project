import streamlit as st

def is_user_active():
    if 'user_active' in st.session_state.keys() and st.session_state['user_active']:
        return True
    else:
        return False
# if st.button('press here to edit'):
if is_user_active():
    with st.form('form'):
        
        id = st.text_input('id')
        name = st.text_input('name')
        responsible_person = st.text_input('responsible person')
        last_update = st.text_input('last update')
        creation_date = st.text_input('creation date')
        end_of_life = st.text_input('end of life')
        first_maintenance = st.text_input('first maintenance')
        next_maintenance = st.text_input('next maintenance')
        maintenance_interval = st.text_input('maintenance interval')
        maintenance_cost = st.text_input('maintenance cost')

        if st.form_submit_button('submit'):
            st.text(f'{id},{name}')
        #You can as well save your user input to a database and access later(sqliteDB will be nice)
        st.success('updated successfully')
        if st.form_submit_button('cancel'):
            st.warning('cancelled')
        
else:
    if st.button('Add device'):
        st.session_state['user_active']=True
        st.experimental_rerun()

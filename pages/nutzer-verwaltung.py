import streamlit as st
with st.form("Nutzer Verwaltung - Neuen Nutzer anlegen"):
    st.write("Input user data ")
    user_name = st.text_input('Username: ')
    user_email = st.text_input('E-mail: ')
    user_password = st.text_input('Password: ', type='password')  # Masking the password input
    submitted = st.form_submit_button('Neuen Nutzer anlegen')
    if submitted:
        pass
        # save submitted data & create user
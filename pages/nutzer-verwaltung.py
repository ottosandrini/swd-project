import streamlit as st

user_data = []

with st.form("Nutzer Verwaltung - Neuen Nutzer anlegen"):
    st.write("Input user data ")
    user_name = st.text_input('Username: ')
    user_email = st.text_input('E-mail: ')
    user_password = st.text_input('Password: ', type='password')  # Masking the password input

    submitted = st.form_submit_button('Neuen Nutzer anlegen')

    if submitted:
        #Showing  saved data
        new_user = {
            'Username': user_name,
            'E-mail': user_email,
            'Password': user_password  
        }

        #appending the new user data
        user_data.append(new_user)

        #cofirmation message
        st.success(f"Nutzer '{user_name}' wurde erfolgreich angelegt!")

# showing user dafa out of the form
if user_data:
    st.write("Gespeicherte Nutzerdaten:")
    for idx, user in enumerate(user_data, start=1):
        st.write(f"Nutzer {idx}:")
        st.write(user)

import streamlit as st
import os
import sys
from tinydb import TinyDB, Query
from datetime import datetime
from logic import nutzerverwaltung_class  # changed it due to fehlermeldung
from logic.nutzerverwaltung_class import NutzerVerwaltung
#from logic import nutzerverwaltung_class


# Add these lines at the beginning of nutzer-verwaltung.py and nutzerverwaltung_class.py

### !!! hab überall serializer.py umbennant  damit es keine Verwirrung mit serializer entsteht aber hat nicht funktioniert deswegen  hab alles zurueckgekehrt!! 

#user_data = []

# Load user data from the database
db = TinyDB('user_database.json')
user_data = db.all()

with st.form("Nutzer Verwaltung - Neuen Nutzer anlegen"):
    st.write("Input user data ")
    user_name = st.text_input('Username: ')
    user_email = st.text_input('E-mail: ')
    user_password = st.text_input('Password: ', type='password')  # Masking the password input
    submitted = st.form_submit_button('Neuen Nutzer anlegen')

    if submitted:
        # Save submitted data to the database
        new_user = {'Username': user_name, 'E-mail': user_email, 'Password': user_password}
        user_data.append(new_user)
        db.insert(new_user)


        # Display success message
        st.success(f"Nutzer '{user_name}' wurde erfolgreich angelegt!")

        # Clear input fields after successful creation
        user_name, user_email, user_password = '', '', ''

# Showing saved user data
if user_data:
    st.write("Gespeicherte Nutzerdaten:")
    for idx, user in enumerate(user_data, start=1):
        st.write(f"Nutzer {idx}:")
        st.write(user)
else:
    st.write("Keine Nutzerdaten gespeichert.")

if __name__ == "__main__":
    if user_data:
        # Instantiate NutzerVerwaltung with the last user's data
        last_user = user_data[-1]
        nutzer = NutzerVerwaltung(last_user['Username'], last_user['E-mail'], last_user['Password'])


if st.button("Delete Data"):
    # Get user name for deletion
    delete_user_name = st.text_input("User Name for Deletion:")

    # Print the user input
    print("User Input for Deletion:", delete_user_name)

    # Print the condition before deletion
    condition = Query().user_name == delete_user_name
    print("Deletion Condition Before:", condition)

    # Check if the user exists before attempting deletion
    existing_user = NutzerVerwaltung.load_data_by_user_name(delete_user_name)
    
    if existing_user:
        # Print existing user data before deletion
        print("Existing User Data Before Deletion:", existing_user.__dict__)

        # Delete data using the existing user instance
        existing_user.delete_data(condition=condition)

        # Display success message
        st.success(f"Nutzer '{delete_user_name}' wurde erfolgreich gelöscht!")

        # Print existing user data after deletion
        print("Existing User Data After Deletion:", existing_user.__dict__)
    else:
        st.warning(f"Nutzer '{delete_user_name}' existiert nicht.")

    # Print the condition after user input
    print("Deletion Condition After:", condition)
 
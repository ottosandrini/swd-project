import streamlit as st
import os
from tinydb import TinyDB, Query
from .serializer import serializer
from datetime import datetime
from .devices import Device

#from devices.py store_data and load_data nehmen###
##

class NutzerVerwaltung(Device):
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

    def __init__(self, user_name: str, user_email: str, user_password: str):
        super().__init__()  # Assuming Device class has an __init__ method
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def store_data(self):
        print("Storing data...")
        # Check if the user already exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.user_name == self.user_name)

        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update( 
                {'user_name': self.user_name, 'user_email': self.user_email, 'user_password': self.user_password},
                doc_ids=[result[0].doc_id]
            )
            print("Data updated.")
        else:
            # If the user doesn't exist, insert a new record
            self.db_connector.insert(
                {'user_name': self.user_name, 'user_email': self.user_email, 'user_password': self.user_password}
            )
            print("Data inserted.")

    @classmethod
    def load_data_by_user_name(cls, user_name):
        # Load data from the database and create an instance of the NutzerVerwaltung class
        UserQuery = Query()
        result = cls.db_connector.search(UserQuery.user_name == user_name)

        if result:
            data = result[0]
            return cls(data['user_name'], data['user_email'], data['user_password'])
        else:
            return None

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
        #super().__init__() 
        super().__init__(
            id=0,  
            device_name='',  
            responsible_person='',  
            last_update=datetime.now(),  
            creation_date=datetime.now(),  
            end_of_life=datetime.now(),  
            first_maintenance=datetime.now(),  
            next_maintenance=datetime.now(),
            maintenance_interval=0,  
            maintenance_cost=0.0  
        )
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
    @classmethod    
    def delete_data(cls, condition=None):
        # Delete data based on the specified condition or default to user_name
        if condition is None:
            condition = Query().user_name == cls.user_name

        print("Deleting data...")

        # Add a print statement to see the entire database content before deletion
        all_data_before = cls.db_connector.all()
        print("All Data Before Deletion:", all_data_before)

        result = cls.db_connector.remove(condition)

        if result:
            print(f"Data deleted based on condition: {condition}")
        else:
            print(f"No data found based on condition: {condition}")

        # Add a print statement to see the entire database content after deletion
        all_data_after = cls.db_connector.all()
        print("All Data After Deletion:", all_data_after)



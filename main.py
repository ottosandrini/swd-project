import streamlit as st
import sys
import os
from tinydb import TinyDB, Query
from logic import serializer

mystring = os.path.dirname(os.path.abspath(__file__)) + "/pages"
sys.path.append(mystring)
#print(sys.path)

#check if database works:
#db_connector1 = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')
#db_connector2 = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')



st.set_page_config(page_title="Geräte Verwaltung")


st.write("# Gerätemanagement")
st.write("## <- Wählen sie hier eine Seite")



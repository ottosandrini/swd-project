### Erste Streamlit App

import streamlit as st
from queries import find_devices
from devices import Device

st.set_page_config(page_title="Geräte Verwaltung")

st.write("# Gerätemanagement")
st.write("## <- Wählen sie hier eine Seite")



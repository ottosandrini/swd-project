import streamlit as st
import sys
import os

mystring = os.path.dirname(os.path.abspath(__file__)) + "/pages"
sys.path.append(mystring)
print(sys.path)

st.set_page_config(page_title="Geräte Verwaltung")


st.write("# Gerätemanagement")
st.write("## <- Wählen sie hier eine Seite")



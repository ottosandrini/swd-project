import streamlit as st

def get_user():
    user="Bella"
    return user

def check_if_free(device, start, end) -> bool:
    pass
    return True

def save_reservation(device, start, end, reason, user):
    if reason == "":
        st.error("Fehler beim speichern der Reservierung: Kein Grund angegeben")
    elif check_if_free(device, start, end):
        st.balloons()
        st.info("Reservierung gespeichert!")
    else:
        pass
        st.error("Fehler! Gerät für diesen Zeitraum schon gebucht")


local_usr = get_user()

st.set_page_config(page_title="Reservierungssystem")

st.write("# Reservierungssystem")

list_of_available_devices=["Device A","Device B", "5-Achs CNC"]

chosen_device = st.selectbox(label="Wähle ein Gerät zum reservieren", options=list_of_available_devices)

chosen_start = st.date_input(label="Wähle ein Startdatum:")
chosen_end = st.date_input(label="Wähle ein Enddatum:")

reason = st.text_input(label="Reservierungsgrund:")

if check_if_free(chosen_device, chosen_start, chosen_end):
    pass
else:
    st.warning("Das Gerät ist für diesen Zeitraum schon gebucht")

if st.button(label="Reservierung speichern", key="save_reservation"):
    save_reservation(chosen_device, chosen_start, chosen_end, reason, local_usr)

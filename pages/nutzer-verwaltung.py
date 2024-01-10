import streamlit as st

class UserManagementSystem:
    def __init__(self):
        self.user_data = []

    def user_exists(self, username, email):
        for user in self.user_data:
            if user['Username'] == username or user['E-mail'] == email:
                return True
        return False

    def create_user(self, username, email, password):
        if self.user_exists(username, email):
            st.error("Nutzer mit diesem Benutzernamen oder E-Mail existiert bereits!")
            return False
        else:
            new_user = {'Username': username, 'E-mail': email, 'Password': password}
            self.user_data.append(new_user)
            st.success(f"Nutzer '{username}' wurde erfolgreich angelegt!")
            return True

    def show_saved_data(self):
        if self.user_data:
            st.write("Gespeicherte Nutzerdaten:")
            for idx, user in enumerate(self.user_data, start=1):
                st.write(f"Nutzer {idx}:")
                st.write(user)
        else:
            st.write("Keine Nutzerdaten gespeichert.")

def main():
# Creating an instance of UserManagementSystem
    user_system = UserManagementSystem()

    with st.form("Nutzer Verwaltung - Neuen Nutzer anlegen"):
        st.write("Input user data ")
        user_name = st.text_input('Username: ')
        user_email = st.text_input('E-mail: ')
        user_password = st.text_input('Password: ', type='password')  # Masking the password input

        submitted = st.form_submit_button('Neuen Nutzer anlegen')

        if submitted:
            # Creating user using UserManagementSystem if it doesn't exist
            created = user_system.create_user(user_name, user_email, user_password)
            if created:
                # Clearing input fields after successful creation
                user_name, user_email, user_password = '', '', ''

    # Showing user data outside the form
    user_system.show_saved_data()

if __name__ == "__main__":
    main()
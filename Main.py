
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class DatabaseManager:
    def __init__(self):
        self.__connection = None
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "bakerydb"

    def connect(self):
        try:
            self.__connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            return True
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect:\n{e}")
            return False

    def disconnect(self):
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()

    def get_connection(self):
        return self.__connection

    def is_connected(self):
        return self.__connection and self.__connection.is_connected()


class CustomerSession:
    def __init__(self):
        # Private attributes (encapsulation)
        self.__customer_id = None
        self.__name = None
        self.__email = None
        self.__phone = None
        self.__address = None

    def set_customer_data(self, customer_id, name, email, phone, address=""):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def set_address(self, address):
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address if self.__address else 'N/A'

    def is_logged_in(self):
        return self.__customer_id is not None

    def clear_session(self):
        self.__customer_id = None
        self.__name = None
        self.__email = None
        self.__phone = None
        self.__address = None

class BakeryApplication:
    def __init__(self):
        # Private attributes (encapsulation)
        self.__db_manager = DatabaseManager()
        self.__customer_session = CustomerSession()
        self.__intro_window_obj = None

    def get_db_manager(self):
        return self.__db_manager

    def get_customer_session(self):
        return self.__customer_session

    def start(self):
        # Connect to database first
        if not self.__db_manager.connect():
            messagebox.showerror("Error", "Cannot connect to database. Application will close.")
            return

        # Launch Introduction window directly
        self.__launch_introduction()

    def __launch_introduction(self):
        # Import here to avoid circular imports
        from Introduction import IntroductionWindow
        self.__intro_window_obj = IntroductionWindow(self)

    def open_menu(self):
        from Menu import BakeryMenu
        if self.__intro_window_obj:
            self.__intro_window_obj.close()
            self.__intro_window_obj = None

        BakeryMenu(self)

    def close_application(self):
        self.__db_manager.disconnect()
        self.__customer_session.clear_session()

if __name__ == "__main__":
    app = BakeryApplication()
    app.start()
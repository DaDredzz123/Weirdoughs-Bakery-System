
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector


class IntroductionWindow:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.db_manager = app_controller.get_db_manager()
        self.customer_session = app_controller.get_customer_session()

        # Create main window (fullscreen)
        self.window = Tk()
        self.window.title("WeirDoughs Bakery System")

        # Make window fullscreen
        self.window.state('zoomed')  # For Windows
        # Alternative for other systems:
        # self.window.attributes('-zoomed', True)  # For Linux
        # self.window.attributes('-fullscreen', True)  # For macOS

        self.window.resizable(True, True)

        # Set window icon
        try:
            logo = PhotoImage(file="no bg llogo.png")
            self.window.iconphoto(True, logo)
        except:
            print("Logo file not found")

        # Load background image
        try:
            pil_bg_image = Image.open("BGP.png")
            # Get screen dimensions for fullscreen background
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            resized_bg_image = pil_bg_image.resize((screen_width, screen_height), Image.LANCZOS)
            self.tk_bg_image = ImageTk.PhotoImage(resized_bg_image)

            background_label = Label(self.window, image=self.tk_bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = self.tk_bg_image
        except FileNotFoundError:
            print("Background file not found, using solid color")
            self.window.config(bg="#F5DEB3")

        self.create_widgets()

        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Start mainloop
        self.window.mainloop()

    def create_widgets(self):
        # Main container frame (centered)
        main_container = Frame(self.window, bg="#FFFFFF", bd=0)
        main_container.place(relx=0.5, rely=0.5, anchor="center", width=500, height=700)

        # Add subtle shadow effect with multiple frames
        shadow_frame = Frame(self.window, bg="#E0E0E0", bd=0)
        shadow_frame.place(relx=0.5, rely=0.502, anchor="center", width=506, height=706)
        shadow_frame.lower()

        # Logo section
        try:
            pil_image = Image.open("no bg llogo.png")
            resized_pil_image = pil_image.resize((150, 150), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(resized_pil_image)
            image_label = Label(main_container, image=tk_image, bg="#FFFFFF", bd=0)
            image_label.place(relx=0.5, y=80, anchor="center")
            image_label.image = tk_image
        except FileNotFoundError:
            print("Logo file not found")

        # Title Label - Modern typography
        title_label = Label(main_container,
                           text="WEIRDOUGHS",
                           font=("Segoe UI", 28, "bold"),
                           fg="#2C3E50",
                           bg="#FFFFFF")
        title_label.place(relx=0.5, y=195, anchor="center")

        subtitle_label = Label(main_container,
                              text="BAKERY",
                              font=("Segoe UI", 20),
                              fg="#7F8C8D",
                              bg="#FFFFFF")
        subtitle_label.place(relx=0.5, y=230, anchor="center")

        # Welcome text
        welcome_label = Label(main_container,
                             text="Welcome! Please enter your details",
                             font=("Segoe UI", 11),
                             fg="#95A5A6",
                             bg="#FFFFFF")
        welcome_label.place(relx=0.5, y=275, anchor="center")

        # Modern input fields
        input_y_start = 320
        input_spacing = 85

        # Name Field
        name_label = Label(main_container,
                          text="Full Name",
                          font=("Segoe UI", 10),
                          fg="#7F8C8D",
                          bg="#FFFFFF",
                          anchor="w")
        name_label.place(x=70, y=input_y_start)

        self.name = Entry(main_container,
                         font=("Segoe UI", 12),
                         bg="#F8F9FA",
                         fg="#2C3E50",
                         bd=0,
                         highlightthickness=2,
                         highlightbackground="#E0E0E0",
                         highlightcolor="#D4A574",
                         relief="flat")
        self.name.place(x=70, y=input_y_start + 25, width=360, height=45)

        # Email Field
        email_label = Label(main_container,
                           text="Email Address",
                           font=("Segoe UI", 10),
                           fg="#7F8C8D",
                           bg="#FFFFFF",
                           anchor="w")
        email_label.place(x=70, y=input_y_start + input_spacing)

        self.Email = Entry(main_container,
                          font=("Segoe UI", 12),
                          bg="#F8F9FA",
                          fg="#2C3E50",
                          bd=0,
                          highlightthickness=2,
                          highlightbackground="#E0E0E0",
                          highlightcolor="#D4A574",
                          relief="flat")
        self.Email.place(x=70, y=input_y_start + input_spacing + 25, width=360, height=45)

        # Contact Field
        contact_label = Label(main_container,
                             text="Phone Number",
                             font=("Segoe UI", 10),
                             fg="#7F8C8D",
                             bg="#FFFFFF",
                             anchor="w")
        contact_label.place(x=70, y=input_y_start + input_spacing * 2)

        self.Contact = Entry(main_container,
                            font=("Segoe UI", 12),
                            bg="#F8F9FA",
                            fg="#2C3E50",
                            bd=0,
                            highlightthickness=2,
                            highlightbackground="#E0E0E0",
                            highlightcolor="#D4A574",
                            relief="flat")
        self.Contact.place(x=70, y=input_y_start + input_spacing * 2 + 25, width=360, height=45)

        # Modern Continue Button
        self.ContinueButton = Button(main_container,
                                     text="Continue",
                                     font=("Segoe UI", 12, "bold"),
                                     fg="#FFFFFF",
                                     bg="#D4A574",
                                     activebackground="#C89963",
                                     activeforeground="#FFFFFF",
                                     bd=0,
                                     relief="flat",
                                     cursor="hand2",
                                     command=self.continue_action)
        self.ContinueButton.place(x=245, y=585, width=170, height=50)

        # Hover effect for continue button
        self.ContinueButton.bind("<Enter>", lambda e: self.ContinueButton.config(bg="#C89963"))
        self.ContinueButton.bind("<Leave>", lambda e: self.ContinueButton.config(bg="#D4A574"))

        # Cancel Button
        cancel_button = Button(main_container,
                              text="Cancel",
                              font=("Segoe UI", 12, "bold"),
                              fg="#7F8C8D",
                              bg="#FFFFFF",
                              activebackground="#E0E0E0",
                              activeforeground="#7F8C8D",
                              bd=2,
                              relief="solid",
                              cursor="hand2",
                              command=self.on_closing)
        cancel_button.place(x=70, y=585, width=170, height=50)

        # Hover effect for cancel button
        cancel_button.bind("<Enter>", lambda e: cancel_button.config(bg="#E0E0E0"))
        cancel_button.bind("<Leave>", lambda e: cancel_button.config(bg="#FFFFFF"))

        # Focus sequence for Enter key navigation
        self.focus_sequence = [self.name, self.Email, self.Contact, self.ContinueButton]

        self.name.bind('<Return>', self.switch_focus)
        self.Email.bind('<Return>', self.switch_focus)
        self.Contact.bind('<Return>', self.switch_focus)

        self.name.focus_set()

    def switch_focus(self, event):
        current_widget = event.widget
        try:
            current_index = self.focus_sequence.index(current_widget)
        except ValueError:
            return

        next_index = current_index + 1

        if next_index < len(self.focus_sequence):
            self.focus_sequence[next_index].focus_set()
        else:
            if current_widget == self.Contact:
                self.ContinueButton.invoke()
        return "break"

    def validate_contact_number(self, contact):
        if not contact.isdigit():
            return False
        return True

    def save_customer_to_database(self, name, email, phone):
        try:
            connection = self.db_manager.get_connection()
            cursor = connection.cursor()
            query = """
                    INSERT INTO Customers (name, email, phone, address)
                    VALUES (%s, %s, %s, %s)
                    """
            cursor.execute(query, (name, email, phone, ""))
            connection.commit()

            customer_id = cursor.lastrowid
            cursor.close()
            return customer_id

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to save customer:\n{e}")
            return None

    def continue_action(self):
        name_val = self.name.get().strip()
        email_val = self.Email.get().strip()
        contact_val = self.Contact.get().strip()

        # Validate inputs
        if not name_val or not email_val or not contact_val:
            self.show_error_message("Please fill in all fields.")
            return

        # Validate contact number (only digits allowed)
        if not self.validate_contact_number(contact_val):
            self.show_error_message("Phone number must contain only numbers!\nPlease remove any letters or special characters.")
            return

        # Save to database
        customer_id = self.save_customer_to_database(name_val, email_val, contact_val)

        if customer_id is None:
            self.show_error_message("Failed to save customer data to database.")
            return

        # Store customer data in session (address is empty initially)
        self.customer_session.set_customer_data(customer_id, name_val, email_val, contact_val, "")

        # Show success message and proceed to menu
        self.show_success_message_and_proceed()

    def show_success_message_and_proceed(self):
        info_window = Toplevel(self.window)
        info_window.title("Success")
        info_window.geometry("400x250")
        info_window.config(bg="#FFFFFF")
        info_window.resizable(False, False)
        info_window.grab_set()

        # Center the window
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        win_width = 400
        win_height = 250
        x = (screen_width // 2) - (win_width // 2)
        y = (screen_height // 2) - (win_height // 2)
        info_window.geometry(f'{win_width}x{win_height}+{x}+{y}')

        # Success icon (checkmark)
        success_icon = Label(info_window,
                            text="✓",
                            font=("Segoe UI", 50, "bold"),
                            fg="#27AE60",
                            bg="#FFFFFF")
        success_icon.pack(pady=(30, 10))

        success_label = Label(info_window,
                              text="Registration Successful!",
                              font=("Segoe UI", 16, "bold"),
                              fg="#2C3E50",
                              bg="#FFFFFF")
        success_label.pack(pady=5)

        success_msg = Label(info_window,
                           text="Your information has been saved",
                           font=("Segoe UI", 10),
                           fg="#7F8C8D",
                           bg="#FFFFFF")
        success_msg.pack(pady=5)

        proceed_button = Button(info_window,
                                text="Proceed to Menu",
                                command=lambda: self.proceed_to_menu(info_window),
                                font=("Segoe UI", 11, "bold"),
                                bg="#D4A574",
                                fg="#FFFFFF",
                                activebackground="#C89963",
                                activeforeground="#FFFFFF",
                                bd=0,
                                relief="flat",
                                cursor="hand2")
        proceed_button.place(relx=0.5, y=200, anchor="center", width=300, height=45)

        proceed_button.bind("<Enter>", lambda e: proceed_button.config(bg="#C89963"))
        proceed_button.bind("<Leave>", lambda e: proceed_button.config(bg="#D4A574"))
        proceed_button.focus_set()

    def show_error_message(self, message):
        message_window = Toplevel(self.window)
        message_window.title("Error")
        message_window.geometry("400x220")
        message_window.config(bg="#FFFFFF")
        message_window.resizable(False, False)
        message_window.grab_set()

        # Center the window
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        win_width = 400
        win_height = 220
        x = (screen_width // 2) - (win_width // 2)
        y = (screen_height // 2) - (win_height // 2)
        message_window.geometry(f'{win_width}x{win_height}+{x}+{y}')

        # Error icon
        error_icon = Label(message_window,
                          text="⚠",
                          font=("Segoe UI", 20, "bold"),
                          fg="#E74C3C",
                          bg="#FFFFFF")
        error_icon.pack(pady=(20, 10))

        error_label = Label(message_window,
                            text=message,
                            font=("Segoe UI", 11),
                            fg="#2C3E50",
                            bg="#FFFFFF",
                            wraplength=350,
                            justify="center")
        error_label.pack(pady=5, padx=20)

        close_button = Button(message_window,
                              text="OK",
                              command=message_window.destroy,
                              font=("Segoe UI", 11, "bold"),
                              bg="#E74C3C",
                              fg="#FFFFFF",
                              activebackground="#C0392B",
                              activeforeground="#FFFFFF",
                              bd=0,
                              relief="flat",
                              cursor="hand2")
        close_button.place(relx=0.5, y=170, anchor="center", width=200, height=40)

        close_button.bind("<Enter>", lambda e: close_button.config(bg="#C0392B"))
        close_button.bind("<Leave>", lambda e: close_button.config(bg="#E74C3C"))

    def proceed_to_menu(self, popup_window):
        popup_window.destroy()
        self.window.destroy()
        self.app_controller.open_menu()

    def on_closing(self):
        self.app_controller.close_application()
        self.window.destroy()

    def close(self):
        try:
            self.window.destroy()
        except:
            pass
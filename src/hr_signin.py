from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from dashboard import create_dashboard

# Global session dictionary to track logged-in user
session = {}

def create_hr_login(parent):
    login_window = Toplevel(parent)
    login_window.title("HR Signin")
    login_window.configure(background="#FFDD95")

    # Positioning the application
    window_width = 460
    window_height = 480
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    login_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the font
    font_login = ('Arial', 30, 'italic')
    font_username = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_login_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    # Setting up the "login" label
    login_label = Label(login_window, text="LOGIN", fg='#3468C0', bg='#FFDD95', font=font_login)
    login_label.pack(padx=50, pady=50)

    # Username Label
    username_label = Label(login_window, text="Organization Email:", fg='#3468C0', bg='#FFDD95', font=font_username,
                           anchor="w")
    username_label.pack(padx=10, pady=4, anchor="w")

    # Username Field
    username_field = Entry(login_window, width=50, justify="left")
    username_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Password Label
    Password_label = Label(login_window, text="Password:", fg='#3468C0', bg='#FFDD95', font=font_password, anchor="w")
    Password_label.pack(padx=10, pady=4, anchor="w")

    # Password Field
    Password_field = Entry(login_window, width=50, justify="left", show="*")
    Password_field.pack(pady=7, padx=(7, 0), anchor="w")

    # **MySQL Login Functionality**
    def verify_login():
        email = username_field.get()
        password = Password_field.get()

        if not email or not password:
            messagebox.showerror("Login Failed", "Please enter both email and password.")
            return

        try:
            # Connect to MySQL Database
            conn = mysql.connector.connect(host="localhost", user="root", password="CHIR2502004|", database="hrassistance")
            cursor = conn.cursor()

            # Verify credentials
            query = "SELECT * FROM corporate_register WHERE email_of_the_organization = %s AND password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                session["email"] = email  # Store session for filtering
                messagebox.showinfo("Login Successful", "Welcome!")
                login_window.withdraw()  # Hide login window
                dashboard_window = create_dashboard(login_window)  # Open dashboard

                if dashboard_window:
                    dashboard_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(login_window, dashboard_window))

            else:
                messagebox.showerror("Login Failed", "Invalid Email or Password")

            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # Setting up the login button
    Login = Button(login_window, text="Login", foreground='#f7f7f7', background='#D24545',
                   activeforeground='#E43A19', activebackground='#FFDD95', font=font_login_button,
                   command=verify_login)
    Login.pack(padx=10, pady=20)

    # Function to close both windows
    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    # Back button function
    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    # Setting up the back button
    Back = Button(login_window, text="Back", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#FFDD95', font=font_button,
                  command=lambda: feature_back(login_window, parent))
    Back.pack(padx=10, anchor='sw')

    return login_window


if __name__ == "__main__":
    window = Tk()
    create_hr_login(window)
    window.mainloop()

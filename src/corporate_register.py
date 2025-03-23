from tkinter import *
from tkinter import messagebox
import mysql.connector
from dashboard import create_dashboard


def create_register(parent):
    register_window = Toplevel(parent)
    register_window.geometry("460x440")
    register_window.title("Register")
    register_window.configure(background="#FFDD95")

    window_width = 460
    window_height = 480
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    register_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    font_Register = ('Arial', 30, 'italic')
    font_Registerinfo = ('Arial', 10, 'italic')
    font_name = ('Arial', 13, 'bold')
    font_email = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_register_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    Label(register_window, text="REGISTER", fg='#3468C0', bg='#FFDD95', font=font_Register).pack(padx=10, pady=10)
    Label(register_window, text="Fill the details below", fg='#3468C0', bg='#FFDD95', font=font_Registerinfo).pack()

    Label(register_window, text="Name of the organization:", fg='#3468C0', bg='#FFDD95', font=font_name,
          anchor="w").pack(padx=10, pady=4, anchor="w")
    name_field = Entry(register_window, width=50, justify="left")
    name_field.pack(pady=7, padx=(7, 0), anchor="w")

    Label(register_window, text="Email of the organization:", fg='#3468C0', bg='#FFDD95', font=font_email,
          anchor="w").pack(padx=10, pady=4, anchor="w")
    email_field = Entry(register_window, width=50, justify="left")
    email_field.pack(pady=7, padx=(7, 0), anchor="w")

    Label(register_window, text="A UNIQUE KEY FOR ORGANIZATION:", fg='#3468C0', bg='#FFDD95', font=font_email,
          anchor="w").pack(padx=10, pady=4, anchor="w")
    key_field = Entry(register_window, width=50, justify="left")
    key_field.pack(pady=7, padx=(7, 0), anchor="w")

    Label(register_window, text="Password:", fg='#3468C0', bg='#FFDD95', font=font_password, anchor="w").pack(padx=10,
                                                                                                              pady=4,
                                                                                                              anchor="w")
    password_field = Entry(register_window, width=50, justify="left", show="*")
    password_field.pack(pady=7, padx=(7, 0), anchor="w")

    def register_corporation():
        company_id = key_field.get().strip()
        name = name_field.get().strip()
        email = email_field.get().strip()
        password = password_field.get().strip()

        if not company_id or not name or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="CHIR2502004|",
                                           database="hrassistance")
            cursor = conn.cursor()

            # Check if the email already exists
            cursor.execute(
                "SELECT email_of_the_organization FROM corporate_register WHERE email_of_the_organization = %s",
                (email,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Email already registered!")
                return

            # Check if the company_id already exists
            cursor.execute(
                "SELECT company_id FROM corporate_register WHERE company_id = %s",
                (company_id,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Company ID already in use! Please use a different unique key.")
                return

            # Insert data along with the timestamp
            cursor.execute(
                "INSERT INTO corporate_register (company_id, name_of_the_organization, email_of_the_organization, password, registration_time) "
                "VALUES (%s, %s, %s, %s, NOW())",
                (company_id, name, email, password))
            conn.commit()
            messagebox.showinfo("Success", f"Registration successful for {name}!")

            # Store company details in a session-like variable
            register_window.company_data = {
                "company_id": company_id,
                "company_name": name,
                "email": email
            }

            # Open dashboard with company_id
            feature_dashboard(company_id)

            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def feature_dashboard(company_id=None):
        register_window.withdraw()
        dashboard_window = create_dashboard(register_window, company_id)
        if dashboard_window:
            dashboard_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(register_window, dashboard_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    Button(register_window, text="Register", fg='#3468C0', bg='#D24545', activeforeground='#E43A19',
           activebackground='#111F4D', command=register_corporation, font=font_register_button).pack(padx=10, pady=20)
    Button(register_window, text="Back", fg='#f7f7f7', bg='#D24545', activeforeground='#D24545',
           activebackground='#A94438', command=lambda: feature_back(register_window, parent), font=font_button).pack(
        padx=10, anchor='sw')

    def feature_back(current_window, previous_window):
        current_window.withdraw()
        previous_window.deiconify()

    return register_window


if __name__ == "__main__":
    window = Tk()
    create_register(window)
    window.mainloop()
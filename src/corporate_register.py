from tkinter import *
from tkinter import messagebox

def create_register(parent):
    # Setting Up the window
    register_window = Toplevel(parent)
    register_window.geometry("460x440")
    register_window.title("Register")
    register_window.configure(background="#FFDD95")

    # Positioning the application
    window_width = 460
    window_height = 480

    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    register_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the font
    font_Register = ('Arial', 30, 'italic')
    font_Registerinfo = ('Arial', 10, 'italic')
    font_name = ('Arial', 13, 'bold')
    font_email = ('Arial', 13, 'bold')
    font_username = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_register_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    # Setting up the "Register" label
    Register_label = Label(register_window,
                           text="REGISTER",
                           fg='#3468C0',
                           bg='#FFDD95',
                           font=font_Register)
    Register_label.pack(padx=10, pady=10)

    # Setting up the "Register" label info
    Registerinfo_label = Label(register_window,
                               text="Fill the details below",
                               fg='#3468C0',
                               bg='#FFDD95',
                               font=font_Registerinfo)
    Registerinfo_label.pack()

    # Name label
    Name_label = Label(register_window,
                       text="Name of the organization:",
                       fg='#3468C0',
                       bg='#FFDD95',
                       font=font_name,
                       anchor="w")
    Name_label.pack(padx=10, pady=4, anchor="w")

    # Name field
    name_field = Entry(register_window, width=50, justify="left")
    name_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Email Label
    Email_label = Label(register_window,
                        text="Email of the organization:",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_email,
                        anchor="w")
    Email_label.pack(padx=10, pady=4, anchor="w")

    # Email field
    email_field = Entry(register_window, width=50, justify="left")
    email_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Username Label
    username_label = Label(register_window,
                           text="Preferred name for the organization:",
                           fg='#3468C0',
                           bg='#FFDD95',
                           font=font_username,
                           anchor="w")
    username_label.pack(padx=10, pady=4, anchor="w")

    # Username field
    username_field = Entry(register_window, width=50, justify="left")
    username_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Password Label
    Password_label = Label(register_window,
                           text="Password:",
                           fg='#3468C0',
                           bg='#FFDD95',
                           font=font_password,
                           anchor="w")
    Password_label.pack(padx=10, pady=4, anchor="w")

    # Password field
    Password_field = Entry(register_window, width=50, justify="left", show="*")
    Password_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Register Button (No Functionality)
    Register = Button(register_window,
                      text="Register",
                      foreground='#3468C0',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      font=font_register_button)
    Register.pack(padx=10, pady=20)

    # Back Button (No Functionality)
    Back = Button(register_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  font=font_button)
    Back.pack(padx=10, anchor='sw')

    return register_window  # Return the created window


if __name__ == "__main__":
    window = Tk()
    create_register(window)
    window.mainloop()
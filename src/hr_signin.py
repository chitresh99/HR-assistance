from tkinter import *
import tkinter as tk


def create_login(parent):
    login_window = Toplevel(parent)
    # login_window.geometry("460x440")
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

    # Setting up the icon for the window
    # icon = PhotoImage(file='logo.png')
    # login_window.iconphoto(True, icon)

    # Setting up the font
    font_login = ('Arial', 30, 'italic')
    font_username = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_login_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    # Setting up the "login" label
    login_label = Label(login_window,
                        text="LOGIN",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_login)
    login_label.pack(padx=50, pady=50)

    # Username Label
    username_label = Label(login_window,
                           text="Organization Name:",
                           fg='#3468C0',
                           bg='#FFDD95',
                           font=font_username,
                           anchor="w")
    username_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the age field
    username_field = Entry(login_window,
                           width=50,
                           justify="left",
                           # anchor="w"
                           )
    username_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Password Label
    Password_label = Label(login_window,
                           text="Password:",
                           fg='#3468C0',
                           bg='#FFDD95',
                           font=font_password,
                           anchor="w")
    Password_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the age field
    Password_field = Entry(login_window,
                           width=50,
                           justify="left",
                           # anchor="w",
                           show="*"
                           )
    Password_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Setting up the button to login

    # Setting up the button to enter a new window

    # def feature_mainwindow():
    #     login_window.withdraw()  # Hide the main window
    #     dashboard_window = create_dashboard(login_window)
    #     if dashboard_window:
    #         dashboard_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(register_window, dashboard_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    Login = Button(login_window,
                   text="Login",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#FFDD95',
                   # command=feature_mainwindow,
                   font=font_login_button
                   )
    Login.pack(padx=10, pady=20)

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(login_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#FFDD95',
                  command=lambda: feature_back(login_window, parent),
                  # command=back,
                  font=font_button
                  )
    Back.pack(padx=10, anchor='sw')

    return login_window


if __name__ == "__main__":
    window = Tk()
    create_login(window)
    window.mainloop()

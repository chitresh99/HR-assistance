from tkinter import *
import tkinter as tk

def create_dashboard(parent):
    dashboard_window = Toplevel(parent)
    # main_window.geometry("1000x600")
    dashboard_window.title("Dashboard")
    dashboard_window.configure(background="#FFDD95")

    # Positioning the application

    window_width = 1000
    window_height = 600

    screen_width = dashboard_window.winfo_screenwidth()
    screen_height = dashboard_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    dashboard_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    # icon = PhotoImage(file='logo.png')
    # dashboard_window.iconphoto(True, icon)

    # Setting up the font
    font_info1 = ('Arial', 30, 'italic')
    font_info2 = ('Arial', 15, 'italic')
    font_button = ('Arial', 15, 'bold')

    info1_label = Label(dashboard_window,
                        text="HR ASSISTANCE",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_info1)
    info1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    info2_label = Label(dashboard_window,
                        text="Make your HR Operations more efficient by starting here",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_info2)
    info2_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    employee_managment = Label(dashboard_window,
                     text="Employee Management",
                     foreground='#3468C0',
                     background='#FFDD95',
                     font=font_button
                     )
    employee_managment.grid(row=2, columnspan=4, sticky='n')

    employee_managment = Button(dashboard_window,
                      text="Employee Management",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      # command=feature_mainwindow,
                      font=font_button
                      )
    employee_managment.grid(row=3, columnspan=4,pady=5,sticky='n')

    payroll_managment = Label(dashboard_window,
                        text="Payroll Management",
                        foreground='#3468C0',
                        background='#FFDD95',
                        font=font_button
                        )
    payroll_managment.grid(row=4, columnspan=4,pady=10,sticky='n')

    payroll_managment = Button(dashboard_window,
                   text="Payroll Management",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   # command=feature_placewindow,
                   font=font_button
                   )
    payroll_managment.grid(row=5, columnspan=4,pady=10, sticky='n')

    recruitment = Label(dashboard_window,
                              text="Recruitment",
                              foreground='#3468C0',
                              background='#FFDD95',
                              font=font_button
                              )
    recruitment.grid(row=6, columnspan=4, pady=10, sticky='n')

    recruitment = Button(dashboard_window,
                      text="Recruitment",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      font=font_button
                      )
    recruitment.grid(row=7, columnspan=4,pady=10, sticky='n')

    performance_management = Label(dashboard_window,
                        text="Performance Management",
                        foreground='#3468C0',
                        background='#FFDD95',
                        font=font_button
                        )
    performance_management.grid(row=8, columnspan=4,padx=20, pady=10, sticky='sw')

    performance_management = Button(dashboard_window,
                         text="Performance Management",
                         foreground='#f7f7f7',
                         background='#D24545',
                         activeforeground='#E43A19',
                         activebackground='#111F4D',
                         font=font_button
                         )
    performance_management.grid(row=9, columnspan=4, padx=20, pady=10, sticky='sw')

    Skillup_tracking = Label(dashboard_window,
                                   text="Skillup Tracking",
                                   foreground='#3468C0',
                                   background='#FFDD95',
                                   font=font_button
                                   )
    Skillup_tracking.grid(row=8, columnspan=4, padx=20, pady=10, sticky='ne')

    skillup_tracking = Button(dashboard_window,
                                    text="Skillup Tracking",
                                    foreground='#f7f7f7',
                                    background='#D24545',
                                    activeforeground='#E43A19',
                                    activebackground='#111F4D',
                                    font=font_button
                                    )
    skillup_tracking.grid(row=9, columnspan=4, padx=20, pady=10, sticky='ne')

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(dashboard_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(dashboard_window, parent),
                  font=font_button
                  )
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')



    # Configure column sizes
    dashboard_window.grid_columnconfigure(0, weight=1, uniform="group1")
    dashboard_window.grid_columnconfigure(1, weight=1, uniform="group1")
    dashboard_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    dashboard_window.grid_rowconfigure(2, weight=0)
    dashboard_window.grid_rowconfigure(3, weight=0)
    dashboard_window.grid_rowconfigure(4, weight=0)
    dashboard_window.grid_rowconfigure(5, weight=0)
    dashboard_window.grid_rowconfigure(6, weight=0)
    dashboard_window.grid_rowconfigure(7, weight=0)
    dashboard_window.grid_rowconfigure(8, weight=0)
    dashboard_window.grid_rowconfigure(9, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_dashboard(window)
    window.mainloop()

from tkinter import *
import tkinter as tk
from employee_managment import employee_management
from payroll_managment import payroll_management
from recruitment import recruitment_management
from performane_management import performance_management
from upskilling import upskilling_management
from greviance_check import grievance_check


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

    org_name_label = Label(dashboard_window,
                        text=" ",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_info1)
    org_name_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    info2_label = Label(dashboard_window,
                        text="Make your HR Operations more efficient by starting here",
                        fg='#3468C0',
                        bg='#FFDD95',
                        font=font_info2)
    info2_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    employee_managment = Label(dashboard_window,
                               text="Efficient way to manage your employee data down here",
                               foreground='#3468C0',
                               background='#FFDD95',
                               font=font_button
                               )
    employee_managment.grid(row=2, columnspan=4, sticky='n')

    def feature_employee_management():
        dashboard_window.withdraw()  # Hide the main window
        employee_window = employee_management(dashboard_window)
        if employee_window:
            employee_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, employee_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    employee_managment = Button(dashboard_window,
                                text="Employee Management",
                                foreground='#f7f7f7',
                                background='#D24545',
                                activeforeground='#E43A19',
                                activebackground='#111F4D',
                                command=feature_employee_management,
                                font=font_button
                                )
    employee_managment.grid(row=3, columnspan=4, pady=5, sticky='n')

    payroll_managment = Label(dashboard_window,
                              text="Manage your organization's payroll here",
                              foreground='#3468C0',
                              background='#FFDD95',
                              font=font_button
                              )
    payroll_managment.grid(row=4, columnspan=4, padx=(20, 0), pady=10, sticky='sw')

    def feature_payroll_management():
        dashboard_window.withdraw()  # Hide the main window
        payroll_window = payroll_management(dashboard_window)
        if payroll_window:
            payroll_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, payroll_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    payroll_managment = Button(dashboard_window,
                               text="Payroll Management",
                               foreground='#f7f7f7',
                               background='#D24545',
                               activeforeground='#E43A19',
                               activebackground='#111F4D',
                               command=feature_payroll_management,
                               font=font_button
                               )
    payroll_managment.grid(row=5, columnspan=4, padx=(40, 0), pady=10, sticky='sw')

    recruitment = Label(dashboard_window,
                        text="Check your organization's recruitment status",
                        foreground='#3468C0',
                        background='#FFDD95',
                        font=font_button
                        )
    recruitment.grid(row=6, columnspan=4, pady=10, sticky='n')

    def feature_recruitment_management():
        dashboard_window.withdraw()  # Hide the main window
        recruitment_window = recruitment_management(dashboard_window)
        if recruitment_window:
            recruitment_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, recruitment_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    recruitment = Button(dashboard_window,
                         text="Recruitment",
                         foreground='#f7f7f7',
                         background='#D24545',
                         activeforeground='#E43A19',
                         activebackground='#111F4D',
                         command=feature_recruitment_management,
                         font=font_button
                         )
    recruitment.grid(row=7, columnspan=4, pady=10, sticky='n')

    performancee_management = Label(dashboard_window,
                                    text="Check your employee's performance here",
                                    foreground='#3468C0',
                                    background='#FFDD95',
                                    font=font_button
                                    )
    performancee_management.grid(row=8, columnspan=4, padx=20, pady=10, sticky='sw')

    def feature_performance_management():
        dashboard_window.withdraw()  # Hide the main window
        recruitment_window = performance_management(dashboard_window)
        if recruitment_window:
            recruitment_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, recruitment_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    performancee_management = Button(dashboard_window,
                                     text="Performance Management",
                                     foreground='#f7f7f7',
                                     background='#D24545',
                                     activeforeground='#E43A19',
                                     activebackground='#111F4D',
                                     command=feature_performance_management,
                                     font=font_button
                                     )
    performancee_management.grid(row=9, columnspan=4, padx=50, pady=10, sticky='sw')

    Skillup_tracking = Label(dashboard_window,
                             text="Check your employee's skillup status",
                             foreground='#3468C0',
                             background='#FFDD95',
                             font=font_button
                             )
    Skillup_tracking.grid(row=8, columnspan=4, padx=20, pady=10, sticky='ne')

    def feature_skillup_management():
        dashboard_window.withdraw()  # Hide the main window
        skillup_window = upskilling_management(dashboard_window)
        if skillup_window:
            skillup_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, skillup_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    skillup_tracking = Button(dashboard_window,
                              text="Skillup Tracking",
                              foreground='#f7f7f7',
                              background='#D24545',
                              activeforeground='#E43A19',
                              activebackground='#111F4D',
                              command=feature_skillup_management,
                              font=font_button
                              )
    skillup_tracking.grid(row=9, columnspan=4, padx=(0, 50), pady=10, sticky='ne')

    greviance_tracking = Label(dashboard_window,
                              text="Solve your employee's grievance's here",
                              foreground='#3468C0',
                              background='#FFDD95',
                              font=font_button
                              )
    greviance_tracking.grid(row=4, columnspan=4, padx=(0, 20), pady=10, sticky='ne')

    def feature_greviance_management():
        dashboard_window.withdraw()  # Hide the main window
        greviance_window = grievance_check(dashboard_window)
        if greviance_window:
            greviance_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(dashboard_window, greviance_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    greviance_tracking = Button(dashboard_window,
                                text="Grievance Tracking",
                                foreground='#f7f7f7',
                                background='#D24545',
                                activeforeground='#E43A19',
                                activebackground='#111F4D',
                                command=feature_greviance_management,
                                font=font_button
                                )
    greviance_tracking.grid(row=5, columnspan=4, padx=(0, 50), sticky='ne')

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

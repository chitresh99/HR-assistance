from tkinter import *
import tkinter as tk




def create_dashboard(parent):
    dashboard_window = Toplevel(parent)
    # main_window.geometry("1000x600")
    dashboard_window.title("Dashboard")
    dashboard_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 1000
    window_height = 600

    screen_width = dashboard_window.winfo_screenwidth()
    screen_height = dashboard_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    dashboard_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    dashboard_window.iconphoto(True, icon)

    # Setting up the font
    font_info1 = ('Arial', 30, 'italic')
    font_info2 = ('Arial', 15, 'italic')
    font_button = ('Arial', 15, 'bold')
    font_from = ('Arial', 20, 'bold')
    font_to = ('Arial', 20, 'bold')
    font_map_view_button = ('Arial', 10, 'bold')

    # Setting up the first info label stating 'Enter your destination'
    info1_label = Label(dashboard_window,
                        text="Trip Planner",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_info1)
    info1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    info2_label = Label(dashboard_window,
                        text="Embark on adventures effortlessly with our intuitive trip planner app.",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_info2)
    info2_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    iternary = Label(dashboard_window,
                     text="Iternary",
                     foreground='#f7f7f7',
                     background='#111F4D',
                     font=font_button
                     )
    iternary.grid(row=2, columnspan=4, padx=(0, 200), pady=10, sticky='ne')

    def feature_mainwindow():
        dashboard_window.withdraw()  # Hide the main window
        mainfeature_window = create_mainwindow(dashboard_window)
        if mainfeature_window:
            mainfeature_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(window, mainfeature_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    iternary = Button(dashboard_window,
                      text="Iternary",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      command=feature_mainwindow,
                      font=font_button
                      )
    iternary.grid(row=3, columnspan=4, padx=(0, 200), pady=10, sticky='ne')

    suggestions = Label(dashboard_window,
                        text="Suggestions",
                        foreground='#f7f7f7',
                        background='#111F4D',
                        font=font_button
                        )
    suggestions.grid(row=4, columnspan=4, padx=(0, 180), pady=10, sticky='ne')

    def feature_placewindow():
        dashboard_window.withdraw()  # Hide the main window
        suggestionfeature_window = create_suggestionwindow(dashboard_window)
        if suggestionfeature_window:
            suggestionfeature_window.protocol("WM_DELETE_WINDOW",
                                              lambda: close_windows(window, suggestionfeature_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    place = Button(dashboard_window,
                   text="Place",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   command=feature_placewindow,
                   font=font_button
                   )
    place.grid(row=5, columnspan=4, padx=(0, 200), pady=10, sticky='ne')

    def feature_accomodationwindow():
        dashboard_window.withdraw()  # Hide the main window
        dashboard_window_window = create_accomodationwindow(dashboard_window)
        if dashboard_window_window:
            dashboard_window_window.protocol("WM_DELETE_WINDOW",
                                                lambda: close_windows(window, dashboard_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    iternary = Button(dashboard_window,
                      text="Accomodations",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      command=feature_accomodationwindow,
                      font=font_button
                      )
    iternary.grid(row=6, columnspan=4, padx=(0, 150), pady=10, sticky='ne')

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


if __name__ == "__main__":
    window = Tk()
    create_dashboard(window)
    window.mainloop()

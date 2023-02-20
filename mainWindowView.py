#View for the main page (deals with only view things)

import tkinter as tk

class MainWindowView():
    main_window = None
    
    menu_frame = None
    
    plot_frame = None 
    plot_slider_frame = None
    
    trace_frame = None
    trace_slider_frame = None

    def __init__(self, MW):
        self.setup_main_window(MW)
        self.setup_menu()
    
    def setup_main_window(self, MW):
        main_window = MW

        main_window.title('My First GUI') 

        main_window.minsize(1000,560)
        main_window.maxsize(1920,1080)
        
        main_window.config(bg="lightgrey")
    
    def setup_menu(self):
        menu_frame = tk.Frame(self.main_window, width=1550, height=40, bg='white')
        menu_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        menu_frame.pack_propagate(False)
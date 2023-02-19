#View for the main page (deals with only view things)

import tkinter as tk

class MainWindowView():
    def __init__(self, MW):
        self.MW = MW

        MW.title('My First GUI') 

        MW.minsize(1000,560)
        MW.maxsize(1920,1080)
        
        MW.config(bg="lightgrey")

        menu_frame = tk.Frame(MW, width=1550, height=40, bg='white')
        menu_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        menu_frame.pack_propagate(False)
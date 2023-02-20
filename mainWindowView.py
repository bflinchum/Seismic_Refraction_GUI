#View for the main page (deals with only view things)

import tkinter as tk
import mainWindowController as mwc

class MainWindowView():
    main_window = None
    
    menu_frame = None
    
    plot_frame = None 
    plot_slider_frame = None
    
    trace_frame = None
    trace_slider_frame = None

    def __init__(self, MW):
        self.init_main_window(MW)
        self.init_menu()
        self.init_trace()
        self.init_plot()
    
    def init_main_window(self, MW):
        main_window = MW

        main_window.title('My First GUI') 

        main_window.minsize(1000,560)
        main_window.maxsize(1920,1080)
        
        main_window.config(bg="lightgrey")

        self.main_window = main_window
    
    #TODO: add menu items like: file (save, save as, open, etc), view (apperance, etc), help (about, etc), etc
    def init_menu(self):
        menu_frame = tk.Frame(self.main_window, width=1550, height=40, bg='white')
        menu_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        menu_frame.pack_propagate(False)

        self.menu_frame = menu_frame
    
    def init_plot(self):
        plot_frame = tk.Frame(self.main_window, width=1300, height=500, bg='white')
        plot_frame.grid(row=1, column=0, padx=5, sticky="WN")
        plot_frame.pack_propagate(False)
        
        #mwc.MainPageController.plot_graph()

        self.plot_frame = plot_frame

    def init_trace(self):
        pass

#Class for frames with graphs and sliders 
class GraphFrame():
    full_frame = None
    
    canvas = None

    sliders_frame = None
    #list of sliders 
    sliders = []
    #list of variables associated with sliders 
    slider_variables = []

    slider_orient = 'horizontal'
    slider_length = 1000

    def __init__(self):
        pass 

    def init_graph(self):
        pass 
    
    #add slider at the end
    def add_slider(self, root, label, f, t, r, c):
        self.add_slider(self.sliders.length, root, label, f, t, r, c)
        pass 
    
    #add slider at index i 
    def add_slider(self, i, root, label, f, t, r, c):
        #bounds checking 
        if (i > self.sliders.length or i < 0):
            return
        
        #set variable to start at the middle
        self.slider_variables.insert(i, (f + t)/ 2)

        slider = tk.Scale(root, variable=var, label=label, from_=f, to=1, resolution=r, 
            length=self.slider_length, orient=self.slider_orient)
        self.sliders.insert(i, slider)

    #remove slider at index i 
    def remove_slider(self, i):
        pass 
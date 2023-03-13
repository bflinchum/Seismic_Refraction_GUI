#View for the main page (deals with only view things)

import tkinter as tk
from tkinter import filedialog
import os

from matplotlib.widgets import SliderBase
import mainWindowController as mwc

#MAIN/SHOT WINDOW VARIABLES
shotWin_colorMap = 'gray' #colormap for pcolorfast(cmap=XX)
shotWin_vmin = 0 #lower amplitude clip (vmin) in pcolor **update with slider
shotWin_vmax = 1 #upper amplitude clip (vmax) in pcolor **update with slider
shotWin_tmin = 0 #lower time in ms (time*1000) value set_ylim([tmin,tmax]) **update with slider
shotWin_tmax = 300 #upper time in ms (time*1000) value set_ylim([tmin,tmax]) **update with slider
shotWin_xLabel = 'Distance (m)' #Label for plot, set_xlabel()
shotWin_yLabel = 'Time (ms)' #label for plot, set_ylabel()
shotWin_currentSymbol = 1 #this is a horizontal flat bar marker=XX in scatter()
shotWin_currentSize = 50 #this is the size of the flat bar size=XX in scatter()
shotWin_currentPickColor = 'tab:blue' #this is the color of the flat bar c=XX in scatter()
shotWin_modeledSymbol = 1 #this is a horizontal flat bar marker=XX in scatter()
shotWin_modeledSize = 50 #this is the size of the flat bar size=XX in scatter()     
shotWin_modeledPickColor = 'tab:orange' #this is the color of the flat bar c=XX in scatter()
shotWin_recipSymbol = '+' #this is a + symbol for marker=XX in scatter()
shotWin_recipSize = 50 #this is the size of the + in size=XX in scatter()     
shotWin_recipSymbolColor = 'magenta'   #this is the color of the + in c=XX in scatter()

#MAIN/SHOT WINDOW VARIABLES
traceWin_fillColor = 'k' #This is the fill color in the trace window
traceWin_fillDir = 'positive' #this is the direction we want to fill shoudl be 'positive' or 'negative'
traceWin_lineWidth = 2 #Thickness of the trace lineWidth= in plot()
traceWin_vmin = -0.5 #Sets the x-scale set_xlim([vmin,vmax]) in plot() **update with slider
traceWin_vmax = 0.5 #Sets the x-scale set_xlim([vmin,vmax]) in plot() **update with slider
traceWin_tmin = 0 #Sets the y-scale (in miliseconds!!) set_ylim([tmin,tmax]) in plot() **update with slider
traceWin_tmax = 100 #Sets the y-scale (in miliseconds!!) set_ylim([tmin,tmax]) in plot() **update with slider
traceWin_minAmp = 0 #Sets the amplitude (assumes trace is normalized!) vmin=minAmp or vmin=maxAmp in plot() **update with slider
traceWin_maxAmp = 0.5 #Sets the amplitude (assumes trace is normalized!) vmin=minAmp or vmin=maxAmp in plot() **update with slider
traceWin_xLabel = 'Distance (m)' #Label for plot, set_xlabel()
traceWin_yLabel = 'Time (ms)' #label for plot, set_ylabel()

class MainWindowView():
    #class variable declaration
    main_window = None
    menu_frame = None
    shot = None
    trace = None

    def __init__(self, MW):
        self.init_main_window(MW)
        self.init_menu()
        self.init_trace()
        self.init_shot()
    
    def init_main_window(self, MW):
        main_window = MW

        main_window.title('My First GUI') 

        main_window.minsize(1000,560)
        main_window.maxsize(1920,1080)
        
        main_window.config(bg="lightgrey")

        #Allow items in column 1, 2 and rows 1, 2 to change size with the window
        main_window.columnconfigure(0, weight=1)
        main_window.columnconfigure(1, weight=1)
        main_window.rowconfigure(0, weight=1)
        main_window.rowconfigure(1, weight=1)

        self.main_window = main_window
    
    #TODO: add menu items like: file (save, save as, open, etc), view (apperance, etc), help (about, etc), etc
    def init_menu(self):
        menu_frame = tk.Frame(self.main_window, width=1550, height=40, bg='white')
        menu_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        menu_frame.pack_propagate(False)

        btn_file = tk.Button(menu_frame, text="File", command = lambda self = self: self.open_file_explorer())
        btn_file.grid(row = 0, column = 0)

        btn_plot = tk.Button(menu_frame, text="Plot", command = lambda self = self: mwc.controller.plot_graph())
        btn_plot.grid(row=0, column=1)

        self.menu_frame = menu_frame
    
    def init_shot(self):
        #create and add shot graph frame to main window
        shot = GraphFrame(self.main_window, 1300, 500, 'white', 1, 0)
        #shot.full_frame.grid(row=1, column=0, padx=5, pady=5, sticky = tk.W + tk.N)
        #shot.full_frame.pack_propagate(False)

        #add graph 

        #add shot sliders 

        #set local shot to class shot 
        self.shot = shot

    def init_trace(self):
        #create and add trace graph frame to main window
        self.trace = GraphFrame(self.main_window, 250, 500, 'white', 1, 1)
        #trace.full_frame.grid(row=1, column=1, padx=5, pady=5, sticky = tk.W + tk.N)
        #trace.full_frame.pack_propagate(False)

        #add graph

        #add sliders 
        var = 0.5
        #trace.add_slider('Amplitude', 0, 1, 0.01, lambda self = self: self.test, var)
        self.trace.create_slider('Amplitude', 0, 1, 0.01, lambda self = self: self.test, var)
        #x = 5
        #test = Slider(trace.sliders_frame, 'test', 0, 10, 0.5, lambda x = x: self.test(), x)
        #trace.add_slider(test)
    
    def test(self):
        print("This is a test :0")

    def open_file_explorer(self):
        filename = filedialog.askopenfile(initialdir = "/", title = "Select a File", 
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        os.startfile(os.path.abspath(filename))

#Class for frames with graphs and sliders 
class GraphFrame():
    full_frame = None
    
    canvas_frame = None
    canvas = None

    sliders_frame = None
    sliders = []

    def __init__(self, MW, w, h, b, r, c):
        self.full_frame = tk.Frame(MW, width=w, height=h, bg=b)
        self.full_frame.grid(row=r, column=c, padx=5, pady=5)
        self.full_frame.pack_propagate(False)

        self.canvas_frame = tk.Frame(self.full_frame, width=w, height = h / 2, bg = 'white')
        self.canvas_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.canvas_frame.pack_propagate(False)

        self.sliders_frame = tk.Frame(self.full_frame, width=w, height = h / 2, bg='white')
        self.sliders_frame.grid(row=1, column=0, padx=5, pady=5)
        self.sliders_frame.pack_propagate(False)

    def init_graph(self):
        pass 
    
    #add slider at the end
    def add_slider(self, s):
        self.add_slider_index(s, len(self.sliders))
    
    #add slider at index i 
    #TODO figure out how python overloading fucntions works >:(
    def add_slider_index(self, s, i):
        #bounds checking 
        if (i > len(self.sliders) or i < 0):
            return
        
        self.sliders.insert(i, s)
        self.sliders[i].slider.grid(row=i, column=0, padx=5, pady=5)

    def create_slider(self, l, f, t, r, c, v):
        temp = Slider(self.sliders_frame, l, f, t, r, c, v)
        self.sliders.insert(len(self.sliders), temp)
        self.sliders[len(self.sliders) - 1].grid(len(self.sliders) - 1)
        #self.sliders[len(self.sliders) - 1].slider.grid(row=len(self.sliders) - 1, column=0, padx=5, pady=5)

    #remove slider with label l
    def remove_slider_label(self, l):
        pass

    #remove slider at index i 
    def remove_slider_index(self, i: int):
        #bounds checking 
        if (i > self.sliders.length or i < 0):
            return
        del self.sliders[i]
    
    def plot_graph(self, plot, x, t, data):
        pass

class Slider():
    slider = None #tkinter slider 
    entry = None #textbox
    var = None #variable it links to
    label = None #name of this slider

    def __init__(self, root: tk.Frame, l, f, t, r, c, v):
        self.slider = tk.Scale(root, label=l, from_=f, to=t, resolution=r, command=c,
            orient='horizontal')
        self.var = v
        self.entry = tk.Entry(root, width=10, textvariable=self.var)
        self.label=l
    
    def grid(self, r):
        self.slider.grid(row=r, column=0, padx=5, pady=5)
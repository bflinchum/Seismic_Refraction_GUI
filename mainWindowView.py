#View for the main page (deals with only view things)

import tkinter as tk

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

        #Create trace frame and add sliders 
        self.init_trace()

        #Create shot frame and add sliders
        self.init_shot()
    
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
    
    def init_shot(self):
        #create and add shot graph frame to main window
        shot = GraphFrame(self.main_window, 1300, 500, 'white')
        shot.full_frame.grid(row=2, column=0, padx=5, pady=5, sticky = tk.W + tk.N)
        shot.full_frame.pack_propagate(False)
        
        #add graph 

        #add shot sliders 

        #set local shot to class shot 
        self.shot = shot

    def init_trace(self):
        #create and add trace graph frame to main window
        trace = GraphFrame(self.main_window, 250, 500, 'white')
        trace.full_frame.grid(row=2, column=1, padx=5, pady=5, sticky = tk.W + tk.N)
        trace.full_frame.pack_propagate(False)

        #add graph

        #add sliders 

        #set local shot to class shot 
        self.trace = trace

#Class for frames with graphs and sliders 
class GraphFrame():
    full_frame = None
    
    canvas = None

    sliders_frame = None
    sliders = []

    slider_orient = 'horizontal'
    slider_length = 1000

    def __init__(self, MW, w, h, b):
        self.full_frame = tk.Frame(MW, width=w, height=h, bg=b)
        self.sliders_frame = tk.Frame(MW, width=1200, height=0, bg='white')

    def init_graph(self):
        pass 
    
    #add slider at the end
    def add_slider(self, root, label, f, t, r, c):
        self.add_slider(self.sliders.length, root, label, f, t, r, c)
    
    #add slider at index i 
    def add_slider(self, i, root, label, f, t, r, c, v):
        #bounds checking 
        if (i > self.sliders.length or i < 0):
            return
        temp = Slider(root, label, f, t, c, v[0])
        self.sliders.insert(i, temp)

    #remove slider with label l
    def remove_slider(self, l):
        pass

    #remove slider at index i 
    def remove_slider(self, i):
        #bounds checking 
        if (i > self.sliders.length or i < 0):
            return
        del self.sliders[i]

class Slider():
    slider = None #tkinter slider 
    entry = None #textbox
    var = None #variable it links to
    label = None #name of this slider

    def __init__(self, root, l, f, t, r, c, v):
        self.slider = tk.Scale(root, label=l, from_=f, to=t, resolution=r, command=c)
        self.var = v[0]
        self.entry = tk.Entry(root, width=10, textvariable=self.var)
        self.label=l
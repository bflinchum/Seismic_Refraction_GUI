#View for the main page (deals with only view things)

import tkinter as tk
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
    
    shot_frame = None 
    shot_slider_frame = None
    
    trace_frame = None
    trace_slider_frame = None

    def __init__(self, MW):
        self.init_main_window(MW)
        self.init_menu()
        self.init_trace()
        self.init_shot()
        self.init_browse_button()
        self.init_mainSliderFrame()
        self.init_traceSliderFrame()
    
        
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
    
    #TODO: add menu items like: file (save, save as, open, etc), view (apperance, etc), help (about, etc), etc
   
    def init_shot(self):
        shot_frame = tk.Frame(self.main_window, width=1300, height=500, bg='white')
        shot_frame.grid(row=1, column=0, padx=5, sticky="WN")
        shot_frame.pack_propagate(False)
        
        #mwc.MainPageController.shot_graph()

        self.shot_frame = shot_frame
    
    def init_mainSliderFrame(self):
        mainSlider_frame = tk.Frame(self.main_window, width=1300, height=100, bg='white')
        mainSlider_frame.grid(row=2, column=0, padx=5, sticky="WN")
        mainSlider_frame.pack_propagate(False)
        
        #mwc.MainPageController.shot_graph()

        self.mainSlider_frame = mainSlider_frame
        
        
    def init_trace(self):
        trace_frame = tk.Frame(self.main_window, width=250, height=500, bg='white')
        trace_frame.grid(row=1, column=1, padx=5, sticky="WN")
        trace_frame.pack_propagate(False)
        
        #mwc.MainPageController.shot_graph()

        self.trace_frame = trace_frame
        
    def init_traceSliderFrame(self):
        traceSlider_frame = tk.Frame(self.main_window, width=250, height=100, bg='white')
        traceSlider_frame.grid(row=2, column=1, padx=5, sticky="WN")
        traceSlider_frame.pack_propagate(False)
        
        #mwc.MainPageController.shot_graph()

        self.traceSlider_frame = traceSlider_frame
        
    def init_browse_button(self):
        browse_button = tk.Button(self.main_window,text='Browse',highlightcolor='gray',height=1,width=3)
        browse_button.grid(row=0,column=0,padx=5,sticky="W")
        #browse_button.pack_propogate(False)
        self.browse_button = browse_button
    """
    HOW BUTTON WILL MODIFY MAIN WINDOW CONTROLLER:
        GET INFO -> PASS TO CONTROLER -> CONTROLLER FILTER PASS REALAVENT INFO -> VIEWER
    def on_press_browse(self):
        dirName = COME FROM THE BUTTON
        mwc.MainPageController.get_file_info_from_directory(self, dirName)
        
        each widget is an object --> Widget is a subject ->
        [our job what happens define whats happens on buttons press and what is returned 
         to the screen] -> screen is observer
    """
#Class for frames with graphs and sliders 
class GraphFrame():
    full_frame = None
    
    canvas = None

    sliders_frame = None
    #Dictonary of sliders (key = name and value = Slider class object)
    #Maybe change to a list? 
    slider_dict = None

    slider_orient = 'horizontal'
    slider_length = 1000

    def __init__(self):
        pass 

    def init_graph(self):
        pass 
    
    #add slider at the end
    def add_slider(self, root, label, f, t, r, c):
        self.add_slider(self.sliders.length, root, label, f, t, r, c)
    
    #add slider at index i 
    def add_slider(self, i, root, label, f, t, r, c):
        #bounds checking 
        if (i > self.sliders.length or i < 0):
            return

    #remove slider at index i 
    def remove_slider(self, i):
        pass 

class Slider():
    slider = None
    entry = None #textbox
    var = None 

    def __init__(self):
        pass 
#View for the main page (deals with only view things)

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

from matplotlib.widgets import SliderBase
import mainWindowController as mwc


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
        
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

#style variables 
#TODO: Move to a seperate file labled color_scheme or something like that
title = 'Seismic Refactor'

min_window_width = 1000
min_window_height = 560
max_window_width = 1920
max_window_height = 1080

menu_height = 30

split_shash_width = 5

min_graph_frame_width = (min_window_width - split_shash_width) / 3
min_canvas_height = 50
min_sliders_height = 50
entry_width = 10

frame_padx = 5
frame_pady = 5

color_background = 'lightgrey'
color_frame = 'white'
color_menu = 'grey'

pad_frame = 5

class MainWindowView():
    main_window = tk.Tk
    menu_frame = tk.Frame
    split_window = tk.PanedWindow
    shot_frame = tk.Frame
    trace_frame = tk.Frame

    amp = None
    time = None
    currentTraceIndex = 5 #NEEDS TO BE AN INTEGER!

    def __init__(self, root):
        self.init_main_window(root)
        self.init_menu()
        self.init_split()
        


    
    def init_main_window(self, root):
        self.main_window = root
        self.main_window.title('Seismic Refactor')
        self.main_window.minsize(min_window_width, min_window_height)
        self.main_window.maxsize(max_window_width, max_window_height)
        self.main_window.config(bg=color_background)
        
        self.main_window.bind('<Left>',self.shiftTraceLeft)
        self.main_window.bind('<Right>',self.shiftTraceRight)
        self.main_window.focus_set()
        
        
    def init_menu(self):
        self.menu_frame = tk.Frame(self.main_window, height=menu_height, bg=color_menu, padx = frame_padx, pady= frame_pady)
        self.menu_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        btn_file = tk.Button(self.menu_frame, text="File", command = lambda self = self: self.open_file_explorer())
        btn_file.grid(row = 0, column = 0)

    def init_split(self):
        #init split_window
        self.split_window = tk.PanedWindow(self.main_window, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=split_shash_width)

        self.init_trace()
        self.init_shot()

        self.split_window.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # configure the rows and columns to resize properly
        self.main_window.grid_rowconfigure(1, weight=1)
        self.main_window.grid_columnconfigure(0, weight=1)
        self.main_window.grid_columnconfigure(1, weight=1)


    def init_trace(self):
        self.trace_frame = GraphFrame(self.split_window, (min_window_width - split_shash_width) / 2, min_window_height - menu_height)
        init_amplitude = 0.3
        init_window_length = 0.1
        init_min_time = 0.0
        
        self.trace_frame.add_slider('Amplitude', 0, 1, 0.01, lambda x = init_amplitude : self.trace_get_amplitude_from_slider(x), init_amplitude) #First slider in list [0]
        self.trace_frame.add_slider('Min Time (s)', 0, 1, 0.01, lambda x = init_min_time: self.trace_get_min_time_from_slider(x), init_min_time) #Second slider in the list [1]
        self.trace_frame.add_slider('Window Length (s)', 0, 1, 0.01, lambda x = init_window_length: self.trace_get_window_length_from_slider(x), init_window_length) #Second slider in the list [1]
            
        self.split_window.add(self.trace_frame.full_frame, minsize=min_graph_frame_width)

    def init_shot(self):
        self.shot_frame = GraphFrame(self.split_window, (min_window_width - split_shash_width) / 2, min_window_height - menu_height)    
        #self.shot_frame.plot_frame() #This is an instance of Graphframe
        
        #If init_amplitude == init_window_length the sliders are linked... can't figure out why... python is weird.
        init_amplitude = 0.45
        init_window_length = 0.5
        self.shot_frame.add_slider('Amplitude', 0, 1, 0.01, lambda x = init_amplitude : self.shot_get_amplitude_from_slider(x), init_amplitude) #First slider in list [0]
        #x = 'This is a test :)'
        self.shot_frame.add_slider('Max Time (s)', 0, 1, 0.01, lambda x = init_window_length: self.shot_get_time_from_slider(x), init_window_length) #Second slider in the list [1]
        #init_window_length.trace("w", lambda name, index,mode, init_window_length=init_window_length: self.shot_get_time_from_slider(init_window_length) )
        self.split_window.add(self.shot_frame.full_frame, minsize=min_graph_frame_width)
        
    #Trace slider functions 
    def shiftTrace(self, traceNumber):
        max_amplitude = self.trace_frame.sliders[0].slider.get()
        min_time = self.trace_frame.sliders[1].slider.get()
        window_length = self.trace_frame.sliders[2].slider.get()
        self.trace_frame.update_wiggleTrace(traceNumber,min_time,window_length,max_amplitude)
        self.currentTraceIndex = traceNumber
        
        max_time = self.shot_frame.sliders[1].slider.get()

        max_amplitude = self.shot_frame.sliders[0].slider.get()
        print('MAXIMUM TIME')
        print(max_time)
        print(max_amplitude)
        print('************')
        self.shot_frame.update_pcolorFast(max_time,max_amplitude,self.currentTraceIndex)
        
    def shiftTraceLeft(self, event):
        #print(self.currentTraceIndex-1)
        self.shiftTrace(self.currentTraceIndex-1)
        
        
    def shiftTraceRight(self, event):
        self.shiftTrace(self.currentTraceIndex+1)
        #print(self.currentTraceIndex+1)
        
        
        
        
    def shot_get_amplitude_from_slider(self,init_amplitude):
        max_amplitude = float(init_amplitude)
        max_time = self.shot_frame.sliders[1].slider.get() # gets curent value of slider in positon 1 = time slider
        
        print('Hello World!')
        print(max_amplitude)
        print(max_time)
        self.shot_frame.update_pcolorFast(max_time,max_amplitude,self.currentTraceIndex)

    def shot_get_time_from_slider(self, max_time):
        max_time = float(max_time)
        #print('testing ')
        #print(max_time)
        max_amplitude = self.shot_frame.sliders[0].slider.get()  #gets curent value of slider in positon 0 = ampltiude slider
        self.shot_frame.update_pcolorFast(max_time,max_amplitude,self.currentTraceIndex)
        
    def trace_get_amplitude_from_slider(self,init_amplitude):
        max_amplitude = float(init_amplitude)
        min_time = self.trace_frame.sliders[1].slider.get() # gets curent value of slider in positon 1 = time slider
        #print(min_time)
        window_length = self.trace_frame.sliders[2].slider.get() # gets curent value of slider in positon 1 = time slider
        #print(max_amplitude)
        #print('Hello World!')
        self.trace_frame.update_wiggleTrace(self.currentTraceIndex,min_time,window_length,max_amplitude)
    #Shot slider functions 
    
    def trace_get_min_time_from_slider(self,init_min_time):
        min_time = float(init_min_time)
        max_amplitude = self.trace_frame.sliders[0].slider.get() # gets curent value of slider in positon 1 = time slider
        print(min_time)
        window_length = self.trace_frame.sliders[2].slider.get() # gets curent value of slider in positon 1 = time slider
        #print(max_amplitude)
        #print('Hello World!')
        self.trace_frame.update_wiggleTrace(self.currentTraceIndex,min_time,window_length,max_amplitude)
        
    def trace_get_window_length_from_slider(self,init_window_length):
        window_length = float(init_window_length)
        max_amplitude = self.trace_frame.sliders[0].slider.get() # gets curent value of slider in positon 1 = time slider
        min_time = self.trace_frame.sliders[1].slider.get() # gets curent value of slider in positon 1 = time slider
        #print(max_amplitude)
        #print('Hello World!')
        self.trace_frame.update_wiggleTrace(self.currentTraceIndex,min_time,window_length,max_amplitude)
            
    #Shot slider functions 
    

    def open_file_explorer(self):
        filename = filedialog.askopenfile(initialdir = "/", title = "Select a File")
        #print(filename.name)
        #os.startfile(os.path.abspath(filename))
        
        mwc.controller.read_segy_file(filename.name)
        default_max_time = 0.5
        default_max_amplitude = 0.45
        default_min_time = 0
        default_window_length = 0.05
        self.shot_frame.add_pcolorFast(default_max_time,default_max_amplitude,self.currentTraceIndex)
        self.trace_frame.add_wiggleTrace(self.currentTraceIndex,default_min_time,default_window_length,default_max_amplitude)
    def set_color_scheme(self):
        pass

class GraphFrame():
    full_frame = tk.PanedWindow

    canvas_frame = None
    canvas = None
    
    #The object that holds the matplotlib axes
    dataAxes = None
    
    sliders_frame = None



    def __init__(self, root, w, h):
        self.sliders = []
        self.full_frame = tk.PanedWindow(root, orient=tk.VERTICAL, sashrelief=tk.RAISED, sashwidth=split_shash_width)

        self.canvas_frame = tk.Frame(self.full_frame, width=w, height = h / 2, bg = 'red')
        self.full_frame.add(self.canvas_frame, minsize=min_canvas_height)

        self.sliders_frame = tk.Frame(self.full_frame, width=w, height = h / 2, bg='blue')
        self.sliders_frame.columnconfigure(0, weight=1)
        self.full_frame.add(self.sliders_frame, minsize=min_sliders_height)
        
        
        
    def add_slider(self, l, f, t, r, c, v):
        temp = Slider(self.sliders_frame, l, f, t, r, c, v)
        self.sliders.insert(len(self.sliders), temp)
        self.sliders[len(self.sliders) - 1].grid(len(self.sliders) - 1)
        print(l)
        print(len(self.sliders) - 1)
    
    #Version two rename a bit better
    def add_pcolorFast(self,max_time,max_amplitude,currentTraceIndex):
    
        #Create the Matplotlib figure         
        fig = Figure() #Create the figure        
        self.dataAxes = fig.add_subplot(111) #add axis to figure      
        self.dataAxes.pcolorfast(mwc.controller.seismicDataContainer.geoLocs,mwc.controller.seismicDataContainer.twtt,
                       mwc.controller.seismicDataContainer.data,cmap='gray',vmin=-max_amplitude,vmax=max_amplitude)
        xTemp = mwc.controller.seismicDataContainer.geoLocs[currentTraceIndex]
        yTemp = mwc.controller.seismicDataContainer.twtt
        self.dataAxes.plot([xTemp,xTemp],[yTemp[0],yTemp[-1]],'r--')
        self.dataAxes.set_ylim([0,max_time])
        self.dataAxes.set_xlabel('X-axis') #add labels to x-axis
        self.dataAxes.set_ylabel('Y-axis') #add label to y-axis 
        self.dataAxes.invert_yaxis()
        
        self.canvas = FigureCanvasTkAgg(fig,master=self.canvas_frame) #place matploitlib object on GUI canvas object
        self.canvas.draw() #Update the canvas
        self.canvas.get_tk_widget().pack(side='top') #
    
    def update_pcolorFast(self,max_time,max_amplitude,currentTraceIndex):
        #print(max_time)
        self.dataAxes.clear()
        self.dataAxes.pcolorfast(mwc.controller.seismicDataContainer.geoLocs,mwc.controller.seismicDataContainer.twtt,
                       mwc.controller.seismicDataContainer.data,cmap='gray',vmin=-max_amplitude,vmax=max_amplitude) 
        xTemp = mwc.controller.seismicDataContainer.geoLocs[currentTraceIndex]
        yTemp = mwc.controller.seismicDataContainer.twtt
        self.dataAxes.plot([xTemp,xTemp],[yTemp[0],yTemp[-1]],'r--')
        self.dataAxes.set_ylim([0,max_time])
        self.dataAxes.set_xlabel('X-axis') #add labels to x-axis
        self.dataAxes.set_ylabel('Y-axis') #add label to y-axis 
        self.dataAxes.invert_yaxis()
        self.canvas.draw()
        # ax1 = self.canvas.figure.axes(0)
        # ax1.set_ylim([0,max_time])
        # ax1.draw()
        pass
    
    def add_wiggleTrace(self,currentLocation_index,min_time,window_length,max_amplitude):
        #currentLocation_index = integer defining the column of the trace
        
        #CREATES THE MATPLOTLIB PLOT
        fig = Figure() #Create the figure        
        self.dataAxes = fig.add_subplot(111) #add axis to figure      
        self.dataAxes.plot(mwc.controller.seismicDataContainer.data[:,currentLocation_index],mwc.controller.seismicDataContainer.twtt)
        self.dataAxes.set_ylim([min_time,min_time+window_length])
        self.dataAxes.set_xlim([-max_amplitude,max_amplitude])
        self.dataAxes.set_xlabel('X-axis') #add labels to x-axis
        self.dataAxes.set_ylabel('Y-axis') #add label to y-axis 
        self.dataAxes.invert_yaxis()
        
        #Places the plot on the GUI
        self.canvas = FigureCanvasTkAgg(fig,master=self.canvas_frame) #place matploitlib object on GUI canvas object
        self.canvas.draw() #Update the canvas
        self.canvas.get_tk_widget().pack(side='top') #
        pass
    
    def update_wiggleTrace(self,currentLocation_index,min_time,window_length,max_amplitude):
        self.dataAxes.clear()
        self.dataAxes.plot(mwc.controller.seismicDataContainer.data[:,currentLocation_index],mwc.controller.seismicDataContainer.twtt)
        self.dataAxes.set_ylim([min_time,min_time+window_length])
        self.dataAxes.set_xlim([-max_amplitude,max_amplitude])
        self.dataAxes.set_xlabel('X-axis') #add labels to x-axis
        self.dataAxes.set_ylabel('Y-axis') #add label to y-axis 
        self.dataAxes.invert_yaxis()
        self.canvas.draw()
        # ax1 = self.canvas.figure.axes(0)
        # ax1.set_ylim([0,max_time])
        # ax1.draw()
        pass
    
    
    def plot_frame(self):
        pass
        
         
        
class Slider():
    slider = None #tkinter slider 
    entry = None #textbox
    var = None #variable it links to
    label = None #name of this slider

    def __init__(self, root: tk.Frame, l, f, t, r, c, v):
        self.var = v
        self.label = l
        self.slider = tk.Scale(root, variable=self.var, label=self.label, from_=f, to=t, resolution=r, command=c,
            orient='horizontal')
        self.slider.set(self.var)
        self.entry = tk.Entry(root, width=entry_width, textvariable=self.var)
        #self.entry.bind_class('KeyRelease',c)
        #print()
        #print(self.slider.get())
        #print(self.t)
    def grid(self, r):
        self.slider.grid(row=r, column=0, sticky='nsew')
        self.entry.grid(row=r, column=1, sticky='ne')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 07:36:35 2023

@author: bflinch
"""
import numpy as np

class pickData: 
    def __init__(self):
        #PICKS
        self.pick_shotLocs = np.array([],dtype=float)
        self.pick_geoLocs = np.array([],dtype=float)
        self.pick_travelTimes = np.array([],dtype=float)
        self.pick_modeledTravelTimes = np.array([],dtype=float)
        
        #FOR PLOTTING MODELED TRAVEL TIMES
        self.pick_modelTraveTimesExists = False
        self.pick_modelTraveTimePath = ''
        self.pick_modelTraveTimeFile = ''
        
        def delete_pick(self):
            pass
        def write_picks(self):
            pass
        def find_recipValue(self):
            pass
class seismicData:    
    def __init__(self):          
        #AFTER READING SEGY FILE INFORMATION ABOUT CURRENT SHOT
        self.geoLocs = np.array([],dtype=float) 
        self.twtt = np.array([],dtype=float)
        self.data = np.array([],dtype=float)
        self.offset = np.array([],dtype=float)
        self.dx_geo = float #Default to 2 m but needs to get calculated upon reading data
        
        
        
class plottingSeismicDataParameters():
    def __init__(self):        
        #MAIN/SHOT WINDOW VARIABLES
        self.shotWin_colorMap = 'gray' #colormap for pcolorfast(cmap=XX)
        self.shotWin_vmin = 0 #lower amplitude clip (vmin) in pcolor **update with slider
        self.shotWin_vmax = 1 #upper amplitude clip (vmax) in pcolor **update with slider
        self.shotWin_tmin = 0 #lower time in ms (time*1000) value set_ylim([tmin,tmax]) **update with slider
        self.shotWin_tmax = 300 #upper time in ms (time*1000) value set_ylim([tmin,tmax]) **update with slider
        self.shotWin_xLabel = 'Distance (m)' #Label for plot, set_xlabel()
        self.shotWin_yLabel = 'Time (ms)' #label for plot, set_ylabel()
        self.shotWin_currentSymbol = 1 #this is a horizontal flat bar marker=XX in scatter()
        self.shotWin_currentSize = 50 #this is the size of the flat bar size=XX in scatter()
        self.shotWin_currentPickColor = 'tab:blue' #this is the color of the flat bar c=XX in scatter()
        self.shotWin_modeledSymbol = 1 #this is a horizontal flat bar marker=XX in scatter()
        self.shotWin_modeledSize = 50 #this is the size of the flat bar size=XX in scatter()     
        self.shotWin_modeledPickColor = 'tab:orange' #this is the color of the flat bar c=XX in scatter()
        self.shotWin_recipSymbol = '+' #this is a + symbol for marker=XX in scatter()
        self.shotWin_recipSize = 50 #this is the size of the + in size=XX in scatter()     
        self.shotWin_recipSymbolColor = 'magenta'   #this is the color of the + in c=XX in scatter()
        
        #MAIN/SHOT WINDOW VARIABLES
        self.traceWin_fillColor = 'k' #This is the fill color in the trace window
        self.traceWin_fillDir = 'positive' #this is the direction we want to fill shoudl be 'positive' or 'negative'
        self.traceWin_lineWidth = 2 #Thickness of the trace lineWidth= in plot()
        self.traceWin_vmin = -0.5 #Sets the x-scale set_xlim([vmin,vmax]) in plot() **update with slider
        self.traceWin_vmax = 0.5 #Sets the x-scale set_xlim([vmin,vmax]) in plot() **update with slider
        self.traceWin_tmin = 0 #Sets the y-scale (in miliseconds!!) set_ylim([tmin,tmax]) in plot() **update with slider
        self.traceWin_tmax = 100 #Sets the y-scale (in miliseconds!!) set_ylim([tmin,tmax]) in plot() **update with slider
        self.traceWin_minAmp = 0 #Sets the amplitude (assumes trace is normalized!) vmin=minAmp or vmin=maxAmp in plot() **update with slider
        self.traceWin_maxAmp = 0.5 #Sets the amplitude (assumes trace is normalized!) vmin=minAmp or vmin=maxAmp in plot() **update with slider
        self.traceWin_xLabel = 'Distance (m)' #Label for plot, set_xlabel()
        self.traceWin_yLabel = 'Time (ms)' #label for plot, set_ylabel()
        
                
        
if __name__ == "__main__":
    sd = seismicData()

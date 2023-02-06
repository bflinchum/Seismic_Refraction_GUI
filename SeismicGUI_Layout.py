#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:50:08 2023

@author: bflinch
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
import matplotlib.pyplot as plt

class windowLayout():    
    def __init__(self, MW):        
        #DEFINE CLASS VARIBLES
        self.MW = MW
        
        #CLOSE WINDOW WITH q (PERSONAL PREFERENCE)
        #I am still a bit confused with this command. The GUI is constantly
        #listing so basically if press lower case q then the it will close the
        #window with the destroy() method. e is the event?
        self.MW.bind('<q>', lambda e: MW.destroy())
        
        # def resize(event):
        #     print("widget", event.widget)
        #     print("height", event.height, "width", event.width)
        # self.MW.bind("<Configure>", resize)
        #Set up so that it scales when rezied
        
        
        #DEFINE CLASS METHODS
        
        #SET LAYOUT UP
        MW.title('My First GUI') #Text at top of window
        MW.minsize(1000,560) #Minimum "opening" size
        #MW.minsize(1920,1080) #Minimum "opening" size
        
        MW.maxsize(1920,1080) #Maximum size allowed
        MW.config(bg="lightgray") #Background color of main window
        #BUTTON BAR AT THE TOP
        mainButtonFrame = tk.Frame(MW,width=1300, height=40, bg='white') #make it white to see iti
        mainButtonFrame.grid(row=0, column=0, padx=10, pady=5) #You need to position the frame on the window
        mainButtonFrame.pack_propagate(False) #This keeps it from collapsing around new widgets (buttons,labels, etc)
        
        #Create a large frame where main plot will go
        mainPlotFrame = tk.Frame(MW,width=1300,height=500,bg='white') #create frame
        mainPlotFrame.grid(row=1,column=0,padx=10,pady=5,sticky="WN") #place the frame on the main window
        mainPlotFrame.pack_propagate(False)
        
        #Place a frame where sliders will go
        mainSliderFrame = tk.Frame(MW,width=1300,height=100,bg='white')
        mainSliderFrame.grid(row=2,column=0,padx=10,pady=5,sticky=tk.W+tk.N)
        mainSliderFrame.pack_propagate(False)        
        
        fig = plt.Figure(figsize = (13,5),dpi=100) #Create the figure        
        ax1 = fig.add_subplot(111) #add axis to figure
        ax1.set_xlabel('Distance') #add labels to x-axis
        ax1.set_ylabel('Time') #add label to y-axis
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,master=mainPlotFrame) #place matploitlib object on GUI canvas object
        canvas.draw() #Update the canvas
        canvas.get_tk_widget().pack(side=tk.TOP)         
        
        traceButtonFrame = tk.Frame(MW,width=250, height=40, bg='white') #make it white to see iti
        traceButtonFrame.grid(row=0, column=1, padx=10, pady=5) #You need to position the frame on the window
        traceButtonFrame.pack_propagate(False) #This keeps it from collapsing around new widgets (buttons,labels, etc)        
        
        #Create a smaller frame where trace plot will go
        tracePlotFrame = tk.Frame(MW,width=250,height=500,bg='white') #create frame
        tracePlotFrame.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W) #place the frame on the main window
        tracePlotFrame.pack_propagate(False)
        
        #Place a frame where sliders will go
        traceSliderFrame = tk.Frame(MW,width=250,height=100,bg='white')
        traceSliderFrame.grid(row=2,column=1,padx=10,pady=5,sticky=tk.W+tk.N)
        traceSliderFrame.pack_propagate(False)        
        
        fig2 = plt.Figure(figsize = (2.5,5),dpi=100) #Create the figure        
        ax2 = fig2.add_subplot(111) #add axis to figure
        ax2.set_xlabel('Distance') #add labels to x-axis
        ax2.set_ylabel('Time') #add label to y-axis
        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")
        canvas2 = FigureCanvasTkAgg(fig2,master=tracePlotFrame) #place matploitlib object on GUI canvas object
        canvas2.draw() #Update the canvas
        canvas2.get_tk_widget().pack(side=tk.TOP) 
        fig2.tight_layout() 
        
        
        MW.grid_columnconfigure(0,weight=1)
        MW.grid_columnconfigure(1,weight=1)
        MW.grid_columnconfigure(2,weight=2)
        MW.grid_columnconfigure(3,weight=2)
        
        #CLASS VARIBLES That need to be passed out for manipulation later
        self.mainButtonFrame = mainButtonFrame
        self.mainPlotFrame = mainPlotFrame
        self.mainSliderFrame = mainSliderFrame
        self.traceSliderFrame = traceSliderFrame
        self.traceButtonFrame = traceButtonFrame
        self.mainAxis = ax1
        self.mainCanvas = canvas
        self.traceAxis = ax2
        self.traceCanvas = canvas2

        
#EXECUTE THE PROGRAM
if __name__ == "__main__":
    root = tk.Tk() #Create a tkinter object (emtpy window for manipuation)
    my_gui = windowLayout(root) #pass the new window to the class to create the layout.
    
    
    
    
    
    
    
    
    
    
        
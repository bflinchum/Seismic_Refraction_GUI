#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:50:08 2023

@author: bflinch, sand583
"""

import tkinter as tk
from matplotlib import gridspec
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
import seismicProcessingMethods as spm

class WindowLayout():
    amp = 0.5

    def __init__(self, MW):
        #Main menu set up
        self.MW = MW

        MW.iconbitmap('imgs/windows_12813.ico')
        MW.title('My First GUI') 

        MW.minsize(1000,560)
        MW.maxsize(1920,1080)
        
        MW.config(bg="lightgrey")

        #Menu bar 
        menuBar = tk.Frame(MW, width=1550, height=40, bg='white')
        menuBar.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        menuBar.pack_propagate(False)

        #Main plot frame
        plot = tk.Frame(MW, width=1300, height=500, bg='white')
        plot.grid(row=1, column=0, padx=5, sticky="WN")
        plot.pack_propagate(False)

        #Plot graph
        x, t, data, gx, shotLocation = spm.getData("segy", "70_extracted.sgy")
        self.plot_graph(plot, x, t, data)

        #Main plot sliders 
        plotSlider = tk.Frame(MW, width=1300, height=100, bg='white')
        plotSlider.grid(row=2, column=0, padx=5, pady=5, sticky = tk.W + tk.N)
        plotSlider.pack_propagate(False)

        #lambda i = i: button_click(i))
        #graphPlot = lambda x, t, data, plot: self.graph_plot(x, t, data, plot)
        #graphPlot(x, t, data, plot)

        ampSlider = tk.Scale(plotSlider, variable=self.amp, label="Amplitude", from_=0, to=1, resolution=0.01, 
            length=1000, orient='horizontal', command=lambda x = x: self.plot_graph(x, t, data, plot))
        ampSlider.grid(row=0, column=0, padx=5, pady=5)
        ampEntry = tk.Entry(plotSlider, width=10, textvariable=self.amp)
        ampEntry.grid(row=0, column=1, padx=5, pady=5)

        maxTime = 0.5
        timeSlider = tk.Scale(plotSlider, variable=maxTime, label="Max Time", from_=0, to=1, resolution=0.01, length=1000, orient='horizontal')
        timeSlider.grid(row=1, column=0, padx=5, pady=5)
        timeEntry = tk.Entry(plotSlider, width=10, textvariable=maxTime)
        timeEntry.grid(row=1, column=1, padx=5, pady=5)

        #Trace plot
        trace = tk.Frame(MW, width=250, height=500, bg='white')
        trace.grid(row=1, column=1, padx=5, pady=5)
        trace.pack_propagate(False)

        #Plot trace 
        fig2 = plt.Figure(figsize = (2.5,5), dpi=100)     
        ax2 = fig2.add_subplot(111)
        ax2.plot(data[:, 48],t)
        ax2.set_xlabel('Distance') 
        ax2.set_ylabel('Time')
        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")
        canvas2 = FigureCanvasTkAgg(fig2, master=trace) 
        canvas2.draw() 
        canvas2.get_tk_widget().pack(side=tk.TOP) 
        fig2.tight_layout() 

        #Trace plot sliders 
        traceSlider = tk.Frame(MW, width=250, height=100, bg='white')
        traceSlider.grid(row=2, column=1, padx=5, pady=5, sticky = tk.W + tk.N)
        traceSlider.pack_propagate(False)

        #Short-cuts 
        self.MW.bind('<q>', lambda e: MW.destroy())

    def plot_graph(self, plot, x, t, data):
        data = spm.normalizeTraces(data)

        fig = plt.Figure(figsize = (13, 5), dpi=100)      
        ax1 = fig.add_subplot(111) 
        ax1.pcolorfast(x, t, data, vmin=0, vmax=self.amp)
        ax1.set_xlabel('Distance') 
        ax1.set_ylabel('Time') 
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=plot) 
        canvas.draw() 
        canvas.get_tk_widget().pack(side=tk.TOP)

#EXECUTE THE PROGRAM
if __name__ == "__main__":
    root = tk.Tk() #Create a tkinter object (emtpy window for manipuation)
    my_gui = WindowLayout(root) #pass the new window to the class to create the layout.
    root.mainloop() #Needed for running it outside of spyder 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:56:20 2023

@author: bflinch
"""

from tkinter import *
#from matplotlib.figure import Figure
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np

class mainPickingGUI():
    
    def __init__(self, MW):
        
        #DEFINE CLASS VARIABLES
        self.MW = MW
        
        #CLOSE WINDOW WITH q (PERSONAL PREFERENCE)
        #I am still a bit confused with this command. The GUI is constantly
        #listing so basically if press lower case q then the it will close the
        #window with the destroy() method. e is the event?
        MW.bind('<q>', lambda e: MW.destroy())
        
        """
        Crash course in Python. I have used the lambda function a few times in 
        my scripts to replace a function call. For example to calcualte the 
        area of a circle you could do it the tradtioanl way:
        
            def area(r):
                A = 2*np.pi*r
                return A
        
        then call this: area = area(4)
        
        You could also replace this with a lambda statement:
            A = lambda r: 2*np.pi*r
        
        then call this: A(4)
        
        """
        
        #DEFINE METHODS
        """
        I am not exactly sure how to make these accesible to the class. For 
        example once the class object is created below you can see my_gui.MW
        because has self in front of it. You should be able to access this call
        somehow too
        """
        
        
        def plotExponentialFunction(a,b,canvas,axis):
            """
            
            Parameters
            ----------
            a : the entry object from the GUI
                You can run the .get() method to get the string in the box
            b : the entry object from the GUI
                You can run the .get() method to get the string in the box.
            canvas : a GUI (tk) object where you can place things
                This is the designated space for the matplotlib axis
            axis : Axis of the matplotlib object
                This gets passed through so you can then access matplotlib like
                usual

            Returns
            -------
            None.

            """
            
            #Convert the string to a float (assuming no user input errors)
            # Probably should check to make sure it's a number and then do something...
            a = float(a.get())
            b = float(b.get())
            
            
            #Check to see if there is already a line plotted on the axis object
            #If a line already exists then remove it
            if len(axis.get_lines()) > 0:
                axis.lines.pop(0) #Remove the line object
                
            #This is what I am familar with. Use Numpy to calcaute function
            x = np.linspace(0,2,100)
            y = a*x**b
            
            #Rename the axis object passed into the method to my familar notaiton
            ax = axis
            
            #Plot the data on the axis           
            ax.plot(x,y,'k',linewidth=2)
            
            #Reset the limits to make sure the plot "auto zooms"
            ax.relim()      # make sure all the data fits
            ax.autoscale()
            
            #Update the canvas. Without this the plot will not update
            canvas.draw()                   
        
        
        #Create the window
        MW.title('My First GUI') #Text at top of window
        MW.minsize(1000,560) #Minimum "opening" size
        MW.maxsize(1920,1080) #Maximum size allowed
        MW.config(bg="lightgray") #Background color of main window
        
        #**************************GUI LAYOUT**********************************
        
        #Create a bar accros the window for all the buttons
        buttonFrame = Frame(MW,width=1000, height=40, bg='white') #make it white to see iti
        buttonFrame.grid(row=0, column=0, padx=20, pady=5) #You need to position the frame on the window
        buttonFrame.pack_propagate(False) #This keeps it from collapsing around new widgets (buttons,labels, etc)
        
      

        #Create a large frame where main plot will go
        mainPlotFrame = Frame(MW,width=500,height=500,bg='white') #create frame
        mainPlotFrame.grid(row=1,column=0,padx=20,pady=5,sticky=W+N) #place the frame on the main window
        mainPlotFrame.pack_propagate(False)
        
        #Place a frame where sliders will go
        mainSliderFrame = Frame(MW,width=500,height=100,bg='white')
        mainSliderFrame.grid(row=2,column=0,padx=20,pady=5,sticky=W+N)
        mainSliderFrame.pack_propagate(False)
        
        #PLACE HOLDER
        sliderLabel = Label(mainSliderFrame,text='PLACE HOLDER FOR SLIDERS',
                            font=("Times New Roman", 24),bg='White')
        sliderLabel.pack(side = TOP)
        #********************* MAKE PLOT BUTTONS AND LABELS*******************
        
        #Create teh "canvas" object that will house the matplotlib figure
        #CANVAS OBJECT FOR MATPLOTLIB
        
        fig = Figure(figsize = (5,5),dpi=100) #Create the figure        
        ax1 = fig.add_subplot(111) #add axis to figure
        ax1.set_xlabel('X-axis') #add labels to x-axis
        ax1.set_ylabel('Y-axis') #add label to y-axis
        canvas = FigureCanvasTkAgg(fig,master=mainPlotFrame) #place matploitlib object on GUI canvas object
        canvas.draw() #Update the canvas
        canvas.get_tk_widget().pack(side=TOP) #Place the canvas in the frame (wihtout this it will not show up...)
        
        #STILL NEED TO WORK THIS OUT.... This is the default toolbar for matplotlib
        #toolbar = NavigationToolbar2Tk(canvas,mainPlotFrame)
        #toolbar.pack(side=BOTTOM)
        #toolbar.update()
        #canvas.get_tk_widget().pack()
        
        #CREATE BUTTONS AND INPUTS FOR PLOT
        Label(buttonFrame,text = 'y = ax**b: ',bg='white').pack(side=LEFT) #add label
        
        Label(buttonFrame,text = 'a = ',bg='white').pack(side=LEFT) #add label (could have combinded with text above)
        aEntry = Entry(buttonFrame,width=5,highlightbackground='white') #Create entry box object
        aEntry.insert(END,'2') #set default entry for entry box. Not sure why END is there (stackOverflow)
        aEntry.pack(side=LEFT) #Place the entry box on the frame (without this it does not show up..)
        
        Label(buttonFrame,text = 'b = ',bg='white',padx=5).pack(side=LEFT) #add label for b
        bEntry = Entry(buttonFrame,width=5,highlightbackground='white') #Create entry box object
        bEntry.insert(END,'3') #set default entry for entry box. Not sure why END is there (stackOverflow)
        bEntry.pack(side=LEFT) #Place the entry box on the frame (without this it does not show up..)
        
        #Create button for some action!
        
        #Create button object with labels.
        """
        I had to unpack the command a bit more.
        Command = is the method it's going to call. The only way I found to 
        pass it arguments is using the lambda funciton. I still have to think 
        about why this is. However with this notation you can then pass anything
        you want to the method
        Here when the button is pressed i call the plotExponentialFunction method 
        defined above. It takes the a entry object, bentry object the gui canvas
        where the plot is housed and the matplotlib axes obejct where the plots
        will go.
        
        This updates the plot when the button is pressed
        """
        plotButton = Button(buttonFrame,text='Plot Function',
                            highlightbackground='white',
                            command = lambda: plotExponentialFunction(aEntry,bEntry,canvas,ax1))
        
        plotButton.pack(side=LEFT) #place the buttton on the frame (wihtout this it does not work)
        

#EXECUTE THE PROGRAM
if __name__ == "__main__":
    root = Tk() #Create a tkinter object (emtpy window for manipuation)
    my_gui = mainPickingGUI(root) #pass the new window to the class to create the layout.


#%%
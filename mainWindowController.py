#Controller for the main page (handels communication between view(s) and model(s))

import tkinter as tk
#import seismicProcessingMethods as spm
import mainWindowView as mpv

class MainPageController():
    #file info 
    sgy_filename = None
    pick_filename = None

    #seismic refraction info
    x = None
    t = None
    data = None
    gx = None
    shot_location = None

    def plot_graph(self, plot, x, t, data):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = mpv.MainWindowView(root)
    root.mainloop()
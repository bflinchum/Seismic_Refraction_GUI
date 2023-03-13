#Controller for the main page (handels communication between view(s) and model(s))

import tkinter as tk
import seismicProcessingMethods as spm
import mainWindowView as mpv

class MainPageController():
    #file info 
    sgy_filename = None
    pick_filename = None

    #seismic refraction info
    seismic_data = None 
    pick_data = None

    def shot_graph(self):
        pass

    def read_seismic_file(self):
        pass 

    def read_pick_data(self):
        pass

    def write_pick_data(self):
        pass

    def plot_graph(self):
        print("hello world!")

controller = MainPageController()

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = mpv.MainWindowView(root)
    root.mainloop()
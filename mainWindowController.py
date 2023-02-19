#Controller for the main page (handels communication between view(s) and model(s))

import tkinter as tk
#import seismicProcessingMethods as spm
import mainWindowView as mpv

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = mpv.MainWindowView(root)
    root.mainloop()
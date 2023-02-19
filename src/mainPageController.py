#Controller for the main page (handels communication between view(s) and model(s))

import src.seismicProcessingMethods as spm
import src.mainPageView as mpv

#Execute the program
class MainPageController():
    input_file = "input/70_extracted.sgy"

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = MainPageView(root)
    root.mainLoop()
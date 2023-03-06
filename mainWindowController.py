#Controller for the main page (handels communication between view(s) and model(s))

import tkinter as tk
import seismicProcessingMethods as spm
import mainWindowView as mpv

#For getFile Info
import glob as glb
import os
import segyio

class MainPageController():
    #file info 
    sgy_filename = None
    pick_filename = None

    #seismic refraction info
    seismic_data = None 
    pick_data = None

    def shot_graph(self):
        pass

    def getFileInfo(self,dirName):
        """
        This function will read all of the *.segy or & *.sgy files in a given 
        directory. It returns a list with the file name and the shot location.
        This information will be passed to the GUI to display the file names. At
        a latter time it might be worth extracting other things from the headers
        and storing them in this list.
        
        DEPENDENCIES:
            GLOB - this is used to get the file names in the directory
            segyio - this is used to read the segy files and extract header info
        INPUTS:
            dirName (str) = this is a string to the directory that contains all of 
            the segy files from the survey.
        OUTPUTS:
            fileInfo is a list that is total Files by 2.
            Column 1 (str) = file name
            Column 2 (float) = shot location (units assumed to be m)
            
        NOTES:
            At this stage I use two if statemetns to check for segy files. If there
            are no segy files fileInfo will be an empty list and the user will get 
            an error. Though I am not sure where error goes in a GUI?
             - It depends, but we will be able to use try-except blocks for them
            
            It might be worth adding columns to this list if we need more info from
            the files later on
        """
        files = glb.glob(os.path.join(dirName, "*.sgy"))
        if files == []:
            files = glb.glob(os.path.join(dirName, "*.segy"))
    
        if files == []:
            print("No files with *.sgy or *.segy exist in this directory")
        # Column 1: File Name (str)
        # Column 2: SX (float)
        fileInfo = []
    
        for file in files:
            filename = os.path.basename(file)
            # print(filename)
            with segyio.open(file, strict=False) as f:
                shotLoc = f.header[0][segyio.TraceField.SourceX]
                # print(shotLoc)
            fileInfo.append([filename, shotLoc])
        return fileInfo
    
    
    def read_seismic_file(self):
        pass 

    def read_pick_data(self):
        pass

    def write_pick_data(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = mpv.MainWindowView(root)
    root.mainloop()
#Controller for the main page (handels communication between view(s) and model(s))

import tkinter as tk
#import seismicProcessingMethods as spm
import mainWindowView as mpv

#Class that will hold seismic refraciton data
import seismicData 

#For get_file_info_from_directory Info
import glob as glb
import os
import segyio

#For read_seismic File
import numpy as np

class MainPageController():
    
    def __init__(self):
        #Varibles that will be accessible in the class
        
        #file info varibles
        self.current_shotLocation = 0 #Default to zero unless overwritten
        self.seismic_directory_path = '' #Path to directory that holds seisimc data
        self.current_segy_fileName = '' #Depends on the shot location 
        
        #Create Instance of Seismic Data for access
        #Holds Data, geoLocs, dx_geoLocs, twtt
        self.seismicDataContainer = seismicData.seismicData() 
        
        #Create instance of container that will hold pickign data
        #Holds Pick Data -- ShotLoc, GeoLoc, Pick Time
        #Holds information related to modeled travel times
        self.pickDataContainer = seismicData.pickData()
        
        #Create Instance of container holding all the plotting info
        self.seismicPlotParameters = seismicData.plottingSeismicDataParameters()
        
        

    def shot_graph(self):
        pass

    def get_file_info_from_directory(self,dirName):
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
    
    def read_segy_file(self, file):
        """
        Read data from segy or su file written to read a single file right now. 
        Could modify to extract shot location from a compiled file (or give file 
        list??) Options but segyio made it pretty easy.
        
        INPUTS
        File type = Str with either segy or su
        file = str with file name with path
        
        OUTPUTS
        x = 1D array with reciever locations in m
        t = 1D array with the time values in s
        data = trace data in an np array that is nt x ns
        gx = reciever spacing (calcualted from header) in m
        shotLoc = Shot Location in m
        """

        with segyio.open(file, strict=False) as f:
            t = f.samples / 1000
            x = f.attributes(segyio.TraceField.GroupX)[:]
            #shotLoc = f.header[0][segyio.TraceField.SourceX]
            gx = np.diff(x)[0]
            ngx = len(x)
            data = np.zeros((len(t), ngx))
            for i in range(0, ngx):
                data[:, i] = f.trace[i]
            
        self.seismicDataContainer.data = data
        self.seismicDataContainer.geoLocs = x
        self.seismicDataContainer.twtt = t
        self.seismicDataContainer.dx_geo = gx
    
    

    def read_pick_data(self):
        pass

    def write_pick_data(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    mainPage = mpv.MainWindowView(root)
    root.mainloop()
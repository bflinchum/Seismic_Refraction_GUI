# Seismic_Refraction_GUI
GEOL-4110: Creating a GUI for Seismic Refraction Picking Software

## ABOUT
This is a python based open source first-arrial picker for seismic refraciton data. This software package does not do any inversion, it is strictly for visualizing and picking the first arrival data. The data needs to be in segy format. The data are outputed in a three-column format: shot location, geophone location, and travel-time (s). These values can then be used in other open source codes.

## HOW TO INSTALL AND RUN
Packages include: glob, os, segyio, numpy, scipy
When running outside of a virtual environment (like Spyder), you need to include "root.mainloop"

## HOW TO USE
Sliders bars control the amplitude and y-axis time scale.
Picking is done in teh trace window by left-clicking.
Picks are deleted by rigth clicking.

## KNOWN ISSUES

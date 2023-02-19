#View for the main page (try to keep to only layout stuff)

import tkinter as tk
from matplotlib import gridspec
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
import src.seismicProcessingMethods as spm

class MainPageView():
    def _init_(self, MW):
        x = 5

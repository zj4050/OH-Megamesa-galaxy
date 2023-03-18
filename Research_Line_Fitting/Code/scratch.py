'''
    This is just a scratch place, where you can try your code when you are not sure the output.

'''


import numpy as np
import random
import matplotlib.pyplot as plt
import os


import line_fitting_code as lfc

output_directory = '../'

directory = 'Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_fit_data.dat'

file = np.loadtxt(directory)

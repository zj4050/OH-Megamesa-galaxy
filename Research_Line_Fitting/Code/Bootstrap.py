import numpy as np
import random
import os

##
#This one is the bootstrap method code, which is going to be used to create new spectra with more reasonable line ratios and errors corresponding to them.


folder = 'PA158'


List_label        = []

if folder == 'PA158':

    index1 = 'iras-158-p0'
    index2 = 'iras11-158-p0'

    for i in range(20):
        if i >= 15:
            i += 1
        List_label.append(i)

elif folder == 'PA261':
    index1 = index2 = 'iras11-569-pa261'

    for i in range(14):
        List_label.append(i+1)

elif folder == 'PA239':
    index1 = index2 = 'iras11-239-15'

    for i in range(19):
        List_label.append(i)



for i in List_label:
    sigma_file = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-{:s}/e-ap{:s}-{:s}/e-ap0-{:s}_sigmaspec.txt'\
    .format(folder, str(i), index1, index2)

    flux_file = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-{:s}/e-ap{:s}-{:s}/e-ap0-{:s}_PPXFfit.txt'\
        .format(folder, str(i), index1, index2)

    sigma   = np.loadtxt(sigma_file, skiprows= 1, usecols= 1)

    mu      = np.loadtxt(flux_file, skiprows= 3, usecols= 5)
    n       = len(mu)
    x       = np.random.normal(mu, sigma, size = (1000,n))
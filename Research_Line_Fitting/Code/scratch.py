import numpy as np
import random
import matplotlib.pyplot as plt
import os


import line_fitting_code as lfc

'''folder = 'PA158'


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



i = 0
sigma_file = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-{:s}/e-ap{:s}-{:s}/e-ap{:s}-{:s}_sigmaspec.txt'\
.format(folder, str(i), index1, str(i),index2)

flux_file = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-{:s}/e-ap{:s}-{:s}/e-ap{:s}-{:s}_fit_without_spurious_lines.txt'\
    .format(folder, str(i), index1, str(i), index2)

#sigma   = np.loadtxt(sigma_file, skiprows=1, max_rows= ,usecols= 1)
#print(sigma)
mu      = np.loadtxt(flux_file, skiprows= 1, usecols= 1)

n       = len(mu)
sigma   = np.loadtxt(sigma_file, skiprows= 1, max_rows= n, usecols= 1)
print(sigma)
x       = np.random.normal(mu, sigma, size = (1000,n))


bins = np.linspace(min(mu), max(mu), 50)
hist, edges = np.histogram(x, bins=bins, density=True)
plt.plot(edges[:-1], hist)

# Find the x-axis and y-axis of the peak point
peak_x = edges[np.argmax(hist)]
peak_y = hist.max()
print("Peak x: ", peak_x)
print("Peak y: ", peak_y)

# Show the plot
plt.show()'''


'''#'/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_sigmaspec.txt'
# /Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_sigmaspec.txt
file1 = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_fit_data.dat'

file = np.loadtxt(file1, skiprows= 1, usecols= 2)

print(len(file))
'''

print(__file__)

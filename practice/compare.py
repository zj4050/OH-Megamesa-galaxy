import numpy as np

file1 = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/line_fitting/fit_data/iras11-239-p15_1_PPXFfit.txt'
file2 = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/line_fitting/fit_data/iras11-239-p15_PPXFfit.txt'

df1 = np.loadtxt(file1, skiprows= 1)
df2 = np.loadtxt(file2, skiprows=1)


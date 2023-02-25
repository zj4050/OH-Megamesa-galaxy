import numpy as np

import matplotlib.pyplot as plt



#File reading 
file_name = 'e-ap14-iras11-569-pa261'

try:
    a = int(file_name[5])

except (TypeError, ValueError):
   b = file_name[4]

else:
    b = file_name[4] + file_name[5]


file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/' + file_name + '/' \
     + file_name + '_fit_without_spurious_lines.txt'



df1 = np.loadtxt(file, skiprows=1)



wlen = df1[:, 0]
newgal_spec = df1[:, 1]



#data plot 
plt.plot(wlen, newgal_spec)
plt.title(file_name)
plt.xlabel('Wavelength [$\mathrm{\AA}$]')
plt.ylabel('Flux')
plt.show()

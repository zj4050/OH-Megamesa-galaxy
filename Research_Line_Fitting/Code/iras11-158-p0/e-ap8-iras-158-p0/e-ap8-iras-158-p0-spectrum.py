import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap8-iras-158-p0/e-ap8-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap8-iras-158-p0/'
output_file = 'e-ap8-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

#data reduction

for i in range(len(wlen)):
    if 4240.914 < wlen[i] < 4247.776  or 4600.476 < wlen[i] < 4607.092 or 4816.993 < wlen[i] < 4827.388 or 5574.510 < wlen[i] < 5579.519 or  6157.863 < wlen[i] < 6163.397 or 6178.918 < wlen[i] < 6183.360 \
        or 6723.293 < wlen[i] < 6730.544 :
        wlen_delete.append(i)
        newgal_spec_delete.append(i)

wlen=np.delete(wlen, wlen_delete)
newgal_spec=np.delete(newgal_spec, newgal_spec_delete) 



with open(output_direct + output_file + '_fit_without_spurious_lines' + '.txt', 'w') as f:
    f.write('wlen \t newgal_spectrum \n')
    for i in range(np.size(wlen)):
        f.write('{:10.3f} \t {:10.3f}\n'.format(wlen[i], newgal_spec[i]))

    f.close()





#data plot 
plt.plot(wlen, newgal_spec)
plt.title(output_file)
plt.xlabel('Wavelength [$\mathrm{\AA}$]')
plt.ylabel('Flux')
plt.show()

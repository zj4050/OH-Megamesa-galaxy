import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap6-iras-158-p0/e-ap6-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap6-iras-158-p0/'
output_file = 'e-ap6-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

#data reduction

for i in range(len(wlen)):
    if 4196.201 < wlen[i] < 4199.217 or 4380.293 < wlen[i] < 4385.017 or  5242.322 < wlen[i] < 5255.523 or 5383.574 < wlen[i] < 5394.223 or 5472.308 < wlen[i] < 5480.179 or 5928.812 < wlen[i] < 5959.781 \
        or 6157.863 < wlen[i] < 6162.290 or 6180.028 < wlen[i] < 6183.360 or 6734.173 < wlen[i] < 6740.224:
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

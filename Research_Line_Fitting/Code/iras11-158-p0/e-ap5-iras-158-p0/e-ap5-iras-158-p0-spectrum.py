import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap5-iras-158-p0/e-ap5-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap5-iras-158-p0/'
output_file = 'e-ap5-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

#data reduction

for i in range(len(wlen)):
    if 4379.506 < wlen[i] < 4386.593 or 4427.763 < wlen[i] < 4434.928 or 5245.148 < wlen[i] < 5253.635 or 5325.857 < wlen[i] < 5330.643 or 5375.842 < wlen[i] < 5395.192 or 5929.878 < wlen[i] < 5967.280 \
        or 6050.399 < wlen[i] < 6055.836 or 6157.863 < wlen[i] < 6167.828 or 6735.383 < wlen[i] < 6743.858:
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

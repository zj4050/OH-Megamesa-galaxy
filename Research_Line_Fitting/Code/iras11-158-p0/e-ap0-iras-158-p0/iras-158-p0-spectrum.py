import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/'
output_file = 'e-ap0-iras11-158-p0'


df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

#data reduction
for i in range(len(wlen)):
    if 4381.080 < wlen[i] < 4390.535 or 5211.3335 < wlen[i] < 5231.032 or 5247.975 < wlen[i] < 5259.301 or 5385.509 < wlen[i] < 5393.254 or \
    5448.765 < wlen[i] < 5454.641 or 6016.797 < wlen[i] < 6029.782 or 6156.757 < wlen[i] < 6163.397:
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

plt.savefig(output_direct + output_file + 'spectrum_without_spurious_lines' + '.png')

plt.show()

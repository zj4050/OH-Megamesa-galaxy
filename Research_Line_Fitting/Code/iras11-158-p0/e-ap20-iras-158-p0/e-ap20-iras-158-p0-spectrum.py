import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap20-iras-158-p0/e-ap20-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap20-iras-158-p0/'
output_file = 'e-ap20-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4631.989 < wlen[i] < 4646.992  or 6720.878 < wlen[i] < 6728.127 or 6808.376 < wlen[i] < 6820.618 or 7008.173 < wlen[i] < 7022.036 or 7049.844 < wlen[i] < 7057.447 \
            or 7149.326 < wlen[i] < 7154.465 or 7271.081 < wlen[i] < 7277.616:
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

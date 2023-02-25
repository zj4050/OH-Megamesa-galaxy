import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap14-iras-158-p0/e-ap14-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap14-iras-158-p0/'
output_file = 'e-ap14-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4382.654 < wlen[i] < 4390.535  or 4521.003 < wlen[i] < 4525.065 or 4537.276 < wlen[i] < 4541.353 or 4638.651 < wlen[i] <  4643.654 or 5113.954 < wlen[i] <  5124.991 \
            or 5385.509 < wlen[i] < 5394.223 or  5456.601 < wlen[i] < 5461.505 or 5935.206 < wlen[i] < 5966.209 or 6306.767 < wlen[i] < 6311.3  :
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

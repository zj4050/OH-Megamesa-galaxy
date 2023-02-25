import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA239/e-ap8-iras11-239-p15/e-ap8-iras11-239-p15_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA239/e-ap8-iras11-239-p15/'
output_file = 'e-ap8-iras11-239-p15'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4378.71 < wlen[i] < 4385.788 or  5880.487 < wlen[i] < 5888.936 or 6115.131 < wlen[i] < 6160.296 or 6247.143 < wlen[i] < 6307.984 or 6810.422 < wlen[i] < 6864.418:
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

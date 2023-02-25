import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap17-iras-158-p0/e-ap17-iras11-158-p0_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap17-iras-158-p0/'
output_file = 'e-ap17-iras11-158-p0'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4383.442 < wlen[i] < 4391.324  or 4526.692 < wlen[i] < 4538.091 or 4634.486 < wlen[i] < 4641.152 or 4883.212 < wlen[i] < 4896.388 or 5118.55 < wlen[i] <  5129.596 \
            or 5380.673 < wlen[i] < 5394.223 or 5847.364 < wlen[i] < 5854.722 or 5933.074 < wlen[i] < 5960.852 or 6824.295 < wlen[i] < 6831.654:
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

import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap7-iras11-569-pa261/e-ap7-iras11-569-pa261_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap7-iras11-569-pa261/'
output_file = 'e-ap7-iras11-569-pa261'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4374.105 < wlen[i] < 4395.114  or 4724.981 < wlen[i] < 4732.794 or 4971.66 < wlen[i] < 4979.881 or 5572.961 < wlen[i] < 5583.099  \
            or 5883.321 < wlen[i] < 5901.819 or 6294.648 < wlen[i] < 6313.396 or  6824.344 < wlen[i] < 6959.854:
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

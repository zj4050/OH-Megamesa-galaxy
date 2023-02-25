import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap14-iras11-569-pa261/e-ap14-iras11-569-pa261_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap14-iras11-569-pa261/'
output_file = 'e-ap14-iras11-569-pa261'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'N'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if  5335.092 < wlen[i] < 5342.149 or 5354.521 < wlen[i] < 5364.262 or 5572.04 < wlen[i] < 5583.099 or 5884.293 < wlen[i] < 5903.77 or 6218.152 < wlen[i] < 6354.211 or 6465 < wlen[i] < 6610.156 \
            or 6823.217 < wlen[i] < 6869.597 :
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

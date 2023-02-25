import numpy as np

import matplotlib.pyplot as plt



#File reading 
file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap8-iras11-569-pa261/e-ap8-iras11-569-pa261_PPXFfit.txt'
output_direct = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap8-iras11-569-pa261/'
output_file = 'e-ap8-iras11-569-pa261'

df1 = np.loadtxt(file, skiprows=3)
wlen = df1[:, 0]
newgal_spec = df1[:, 5]
wlen_delete = []
newgal_spec_delete = []

data_reduction = 'Y1'

#data reduction
if data_reduction == 'Y':
    for i in range(len(wlen)):
        if 4370.493 < wlen[i] < 4399.473  or 4633.75 < wlen[i] < 4639.113  or 5217.406 < wlen[i] < 5228.625  \
            or 5276.357 < wlen[i] < 5290.324 or 5572.961 < wlen[i] < 5583.099 or 5862.942 < wlen[i] < 5904.746 or  5963.574 < wlen[i] < 5975.41\
            or 6231.523 < wlen[i] < 6241.828 or 6253.183 < wlen[i] < 6263.523 or 6282.179 < wlen[i] < 6342.672 or 6293.608 < wlen[i] < 6315.483\
            or 6326.972 < wlen[i] < 6334.294 or 6824.344 < wlen[i] < 6989.817:
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

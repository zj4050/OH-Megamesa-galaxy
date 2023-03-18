'''
    This code is used to plot and save all the original spectra. 

    Code route updated --Ziming 03.18.2023
'''

import numpy as np

import matplotlib.pyplot as plt

data_folder = ['PA158', 'PA239', 'PA261']


for folder in data_folder:

    if folder == 'PA158':
        index1 = 'iras-158-p0'
        index2 = 'iras11-158-p0'

    elif folder == 'PA239':
        index1 = index2 = 'iras11-239-p15'

    elif folder == 'PA261':
        index1 = index2 = 'iras11-569-pa261'

    List_label        = []

    if folder == 'PA158':
        for i in range(20):
            if i >= 15:
                i += 1
            List_label.append(i)

    elif folder == 'PA261':
        for i in range(14):
            List_label.append(i+1)

    elif folder == 'PA239':
        for i in range(19):
            List_label.append(i)



    #File reading 
    for i in List_label:
        file = 'Research_Line_Fitting/Output/iras11-{:s}/e-ap{:s}-{:s}/e-ap{:s}-{:s}_PPXFfit.txt'.format(folder, str(i), index1, str(i), index2)

        df1 = np.loadtxt(file, skiprows=3)
        wlen = df1[:, 0]
        newgal_spec = df1[:, 5]
        wlen_delete = []
        newgal_spec_delete = []
        
        save_direct = 'Research_Line_Fitting/Original_spectrum/' + folder + '/'

        #data plot 
        plt.plot(wlen, newgal_spec)
        plt.title('e-ap{:s}-{:s}'.format(str(i), index2))
        plt.xlabel('Wavelength [$\mathrm{\AA}$]')
        plt.ylabel('Flux')
        plt.savefig(save_direct + 'original_spectrum_{:s}_ap{:s}_ppxf.png'.format(folder, str(i)))

        plt.clf()

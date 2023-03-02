import os 
import subprocess
# Define the paths of the folders containing the scripts:
folder_paths = []

machine = 'laptop' #['laptop', 'mac-mini']
#/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code/run.py
if machine  == 'laptop':
    dir     = '/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Code/'

elif machine == 'mac-mini':
    dir     = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code/'

folder_list = ['PA158', 'PA239', 'PA261']


for folder in folder_list:
#for folder in ['PA158', 'PA239', 'PA261']:
    List_label        = []

    if folder == 'PA158':

        index1 = 'iras11-158-p0'
        index2 = 'iras-158-p0'
        index3 = 'iras11-158.p0'

        for i in range(20):
            if i >= 15:
                i += 1
            List_label.append(i)

    elif folder == 'PA261':
        index1 = 'iras11-PA261'
        index2 = 'iras-569-pa261'
        index3 = 'iras11-569-pa261'

        for i in range(14):
            List_label.append(i+1)

    elif folder == 'PA239':
        index1 = 'iras11-PA239'
        index2 = 'iras-239-p15'
        index3 = 'iras11-239-p15'

        for i in range(19):
            List_label.append(i)

    #/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Code/iras11-158-p0/e-ap0-iras-158-p0/e-ap0-iras11-158.p0-linefitting.py
    for i in List_label:
        #path = '~/Code/iras11-158-p0/e-ap0-iras-158-p0/~ iras11-158.p0'
        #path = '~/Code/iras11-PA239/~ iras-239-p15/~ iras11-239-p15'
        #path = '~/Code/iras11-PA261/~ iras-569-pa261/ ~ iras11-569-pa261'
        path = dir + '{:s}/e-ap{:s}-{:s}/e-ap{:s}-{:s}-linefitting.py'\
                .format(index1, str(i), index2, str(i), index3)

        folder_paths.append(path)


    for paths in folder_paths:
        subprocess.run(['python3', paths])
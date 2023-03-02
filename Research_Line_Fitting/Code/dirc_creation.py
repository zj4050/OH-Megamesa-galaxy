import os 
import shutil

# This code is to copy and remove files. Because there are too many data files in the output, writing a code to ask computer to do it for you is faster.


hint = 'copy_261'
if hint == 158:
    for i in range(5, 14):
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap{:s}-iras-158-p0/e-ap{:s}-iras11-158-p0_fit_data.dat'.format(str(i), str(i))
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap{:s}-iras-158-p0/e-ap{:s}-iras11-158-p0_fit_data.dat'.format(str(i), str(i))
        os.remove(file)

elif hint == 239:
    for i in range(19):
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA239/e-ap{:s}-iras11-239-p15/e-ap{:s}-iras11-239-p15_fit_data.dat'.format(str(i), str(i))
        os.remove(file)

elif hint == 569:
    for i in range(1, 15):
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap{:s}-iras11-569-pa261/e-ap{:s}-iras11-569-pa261_fit_data.dat'.format(str(i), str(i))

elif hint == 'copy_158':
    for i in range(21):
        if i == 15:
            continue
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap{:s}-iras-158-p0/e-ap{:s}-iras11-158-p0_fit_data.dat'.format(str(i), str(i))
        des = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/parameters information/iras11-PA158/data/'
        shutil.copy(file, des)

elif hint == 'copy_239':
    des = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/parameters information/iras11-PA239/data/'
    if not os.path.isdir(des):
        os.makedirs(des)

    for i in range(19):
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA239/e-ap{:s}-iras11-239-p15/e-ap{:s}-iras11-239-p15_fit_data.dat'.format(str(i), str(i))
                
        shutil.copy(file, des)

elif hint == 'copy_261':
    des = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/parameters information/iras11-PA261/data/'
    if not os.path.isdir(des):
        os. makedirs(des)

    for i in range(1, 15):
        file = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA261/e-ap{:s}-iras11-569-pa261/e-ap{:s}-iras11-569-pa261_fit_data.dat'.format(str(i), str(i))
                
        shutil.copy(file, des)
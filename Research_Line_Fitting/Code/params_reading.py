'''
    This code is to read the data. 
    
    Code route updated --Ziming 03.18.2023
'''



import numpy as np
import matplotlib.pyplot as plt
import os 

data_folder      = ['PA158', 'PA239', 'PA261']


for folder in data_folder:
    if folder == 'PA158':
        index = '158-p0'
    elif folder == 'PA239':
        index = '239-p15'
    elif folder == 'PA261':
        index = '569-pa261'



    output_directory = 'Research_Line_Fitting/parameters information/iras11-{:s}/'.format(folder)







    OI_file           =  output_directory + "flux_ratio_data/{:s}_OI6300_fit_data.dat".format(folder)
    Halpha_file       =  output_directory + "flux_ratio_data/{:s}_Halpha_fit_data.dat".format(folder)
    Hbeta_file        =  output_directory + "flux_ratio_data/{:s}_Hbeta_fit_data.dat".format(folder)
    NII_file          =  output_directory + "flux_ratio_data/{:s}_NII6584_fit_data.dat".format(folder)
    SII_file          =  output_directory + "flux_ratio_data/{:s}_SII_fit_data.dat".format(folder)
    OIII_file         =  output_directory + "flux_ratio_data/{:s}_OIII5007_fit_data.dat".format(folder)
    SII_a_file        =  output_directory + "flux_ratio_data/{:s}_SII_a_fit_data.dat".format(folder)
    SII_b_file        =  output_directory + "flux_ratio_data/{:s}_SII_b_fit_data.dat".format(folder)


    OI_position = []
    OI_velocity = []
    OI_fwhm     = []
    OI6300_flux = []
    OI6300_flux_err = []
    OI_position_err = []
    OI_velocity_err = []
    OI_fwhm_err     = []

    Halpha_position = []
    Halpha_velocity = []
    Halpha_fwhm     = []
    Halpha_flux     = []
    Halpha_position_err = []
    Halpha_velocity_err = []
    Halpha_fwhm_err     = []
    Halpha_flux_err     = []

    NII_position = []
    NII_velocity = []
    NII_fwhm     = []
    NII6584_flux = []
    NII_position_err = []
    NII_velocity_err = []
    NII_fwhm_err     = []
    NII6584_flux_err = []

    SII_position = []
    SII_velocity = []
    SII_fwhm     = []
    SII_flux     = []
    SII_position_err = []
    SII_velocity_err = []
    SII_fwhm_err     = []
    SII_flux_err     = []


    SII_a_flux     = []
    SII_b_flux     = []
    SII_a_flux_err     = []
    SII_b_flux_err     = []




    Hbeta_position      = []
    Hbeta_velocity      = []
    Hbeta_fwhm          = []
    Hbeta_fwhm_err      = []
    Hbeta_flux          = []
    Hbeta_position_err  = []
    Hbeta_velocity_err  = []
    Hbeta_fwhm          = []
    Hbeta_flux_err      = []

    OIII_position       = []
    OIII_velocity       = []
    OIII_fwhm           = []
    OIII5007_flux       = []
    OIII_position_err   = []
    OIII_velocity_err   = []
    OIII_fwhm_err       = []
    OIII5007_flux_err   = []

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

    for i in List_label:
        file = 'Research_Line_Fitting/parameters information/iras11-{:s}/data/e-ap{:s}-iras11-{:s}_fit_data.dat'.format(folder,str(i), index)
        
        df_position     = np.loadtxt(file, skiprows = 1, usecols= 10)
        df_velocity     = np.loadtxt(file, skiprows= 1, usecols= 12)
        df_flux         = np.loadtxt(file,skiprows= 1, usecols= 8)
        df_fwhm         = np.loadtxt(file, skiprows= 1, usecols= -1)
        df_position_err = np.loadtxt(file, skiprows= 1, usecols= 11)
        df_velocity_err = np.loadtxt(file, skiprows= 1, usecols= 14)
        df_flux_err     = np.loadtxt(file, skiprows= 1, usecols= 9)
        df_fwhm_err     = 2.3548 * np.loadtxt(file, skiprows= 1, usecols= 7)

    

        OI_position.append(df_position[0])
        OI_velocity.append(df_velocity[0])
        OI_fwhm.append(df_fwhm[0])
        OI_fwhm_err.append(df_fwhm_err[0])
        OI_position_err.append(df_position_err[0])
        OI_velocity_err.append(df_velocity_err[0])
        OI6300_flux.append(df_flux[0])
        OI6300_flux_err.append(df_flux_err[0])

        Halpha_position.append(df_position[3])
        Halpha_velocity.append(df_velocity[3])
        Halpha_fwhm.append(df_fwhm[3])
        Halpha_fwhm_err.append(df_fwhm_err[3])
        Halpha_flux.append(df_flux[3])
        Halpha_flux_err.append(df_flux_err[3])
        Halpha_position_err.append(df_position_err[3])
        Halpha_velocity_err.append(df_velocity_err[3])

        NII_position.append(df_position[4])
        NII_velocity.append(df_velocity[4])
        NII_fwhm.append(df_fwhm[4])
        NII_fwhm_err.append(df_fwhm_err[4])
        NII6584_flux.append(df_flux[4])
        NII6584_flux_err.append(df_flux_err[4])
        NII_position_err.append(df_position_err[4])
        NII_velocity_err.append(df_velocity_err[4])

        SII_position.append(df_position[5])
        SII_velocity.append(df_velocity[5])
        SII_fwhm.append(df_fwhm[5])
        SII_fwhm_err.append(df_fwhm_err[5])
        SII_flux.append(df_flux[5]+ df_flux[6])
        SII_flux_err.append(np.sqrt((df_flux_err[5])**2 + (df_flux_err[6])**2))
        SII_position_err.append(df_position_err[5])
        SII_velocity_err.append(df_velocity_err[5])

        SII_a_flux.append(df_flux[5])
        SII_b_flux.append(df_flux[6])
        SII_a_flux_err.append(df_flux_err[5])
        SII_b_flux_err.append(df_flux_err[6])


        Hbeta_position.append(df_position[7])
        Hbeta_velocity.append(df_velocity[7])
        Hbeta_fwhm.append(df_fwhm[7])
        Hbeta_fwhm_err.append(df_fwhm_err[7])
        Hbeta_flux.append(df_flux[7])
        Hbeta_flux_err.append(df_flux_err[7])
        Hbeta_position_err.append(df_position_err[7])
        Hbeta_velocity_err.append(df_velocity_err[7])


        OIII_position.append(df_position[9])
        OIII_velocity.append(df_velocity[9])
        OIII_fwhm.append(df_fwhm[9])
        OIII_fwhm_err.append(df_fwhm_err[9])
        OIII5007_flux.append(df_flux[9])
        OIII5007_flux_err.append(df_flux_err[9])
        OIII_position_err.append(df_position_err[9])
        OIII_velocity_err.append(df_velocity_err[9])


    # Generating the information of seven parameters
    OI_info     = (OI_position, OI_position_err, OI_velocity, OI_velocity_err, OI_fwhm, OI_fwhm_err, OI6300_flux, OI6300_flux_err)
    Hbeta_info  = (Hbeta_position, Hbeta_position_err, Hbeta_velocity, Hbeta_velocity_err, Hbeta_fwhm, Hbeta_fwhm_err, Hbeta_flux, Hbeta_flux_err)
    Halpha_info = (Halpha_position, Halpha_position_err, Halpha_velocity, Halpha_velocity_err, Halpha_fwhm, Halpha_fwhm_err, Halpha_flux, Halpha_flux_err)
    NII_info    = (NII_position, NII_position_err, NII_velocity, NII_velocity_err, NII_fwhm, NII_fwhm_err, NII6584_flux, NII6584_flux_err)
    SII_info    = (SII_position, SII_position_err, SII_velocity, SII_velocity_err, SII_fwhm, SII_fwhm_err, SII_flux, SII_flux_err)
    OIII_info   = (OIII_position, OIII_position_err, OIII_velocity, OIII_velocity_err, OIII_fwhm, OIII_fwhm_err, OIII5007_flux, OIII5007_flux_err)
    SII_a_info  = (SII_position, SII_position_err, SII_velocity, SII_velocity_err, SII_fwhm, SII_fwhm_err, SII_a_flux, SII_a_flux_err)
    SII_b_info  = (SII_position, SII_position_err, SII_velocity, SII_velocity_err, SII_fwhm, SII_fwhm_err, SII_b_flux, SII_b_flux_err)

    if os.path.exists(OI_file):
        os.remove(OI_file)

    if os.path.exists(Halpha_file):
        os.remove(Halpha_file)

    if os.path.exists(Hbeta_file):
        os.remove(Hbeta_file)

    if os.path.exists(NII_file):
        os.remove(NII_file)

    if os.path.exists(SII_file):
        os.remove(SII_file)

    if os.path.exists(OIII_file):
        os.remove(OIII_file)

    if os.path.exists(SII_a_file):
        os.remove(SII_a_file)

    if os.path.exists(SII_b_file):
        os.remove(SII_b_file)
    #Recording the information of seven parameters into a text file.
    titles = ['Position', 'dPosition', 'Velocity', 'dVelocity', 'fwhm', 'dfwhm', 'flux', 'dflux']

    with open(OI_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, OI_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(OI_info, max_widths)]) + "\n")

    with open(Halpha_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, Halpha_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(Halpha_info, max_widths)]) + "\n")
    
    with open(Hbeta_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, Hbeta_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(Hbeta_info, max_widths)]) + "\n")
        
    with open(NII_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, NII_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(NII_info, max_widths)]) + "\n")

        

    with open(SII_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, SII_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(SII_info, max_widths)]) + "\n")

    with open(OIII_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, OIII_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(OIII_info, max_widths)]) + "\n")


    with open(SII_a_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, SII_a_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(SII_a_info, max_widths)]) + "\n")

    with open(SII_b_file,'a') as f:
        max_widths = [max(len(title), len('{:.4e}'.format(np.max(column)))) for title, column in zip(titles, SII_b_info)]
        
        f.write("  ".join([title.ljust(width) for title, width in zip(titles, max_widths)]) + "\n")
        
        for i in range(len(OI_position)):
            f.write("  ".join([("{:." + str(width - 7) + "e}").format(column[i]).ljust(width) for column, width in zip(SII_b_info, max_widths)]) + "\n")





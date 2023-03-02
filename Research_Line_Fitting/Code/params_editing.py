'''
    This code is for data manipulation. What I am doing here basically is:

    (1) Calculating the emission line ratio
    (2) Plotting the several important diagrams as shown in the comment in the plotting part



'''




import numpy as np
import matplotlib.pyplot as plt
import functions as f
import os

data_folder      = ['PA158', 'PA239', 'PA261']

machine          = 'mac-mini' #['laptop', 'mac-mini']

for folder in data_folder:
    # Determine the route of files
    if machine == 'laptop':
        output_directory = '/Users/kamiori/Desktop/Research_project/Research Project/OH Megamesa/Research_Line_Fitting/parameters information/iras11-{:s}/'.format(folder) #laptop
    elif machine == 'mac-mini':
        output_directory = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/parameters information/iras11-{:s}/'.format(folder)  #mac-mini directory

    #Generate the emission line files
    OI_file     = output_directory + 'flux_ratio_data/{:s}_OI6300_fit_data.dat'.format(folder)
    OIII_file   = output_directory + 'flux_ratio_data/{:s}_OIII5007_fit_data.dat'.format(folder)
    Halpha_file = output_directory + 'flux_ratio_data/{:s}_Halpha_fit_data.dat'.format(folder)
    Hbeta_file  = output_directory + 'flux_ratio_data/{:s}_Hbeta_fit_data.dat'.format(folder)
    NII_file    = output_directory + 'flux_ratio_data/{:s}_NII6584_fit_data.dat'.format(folder)
    SII_file    = output_directory + 'flux_ratio_data/{:s}_SII_fit_data.dat'.format(folder)
    SII_a_file  = output_directory + 'flux_ratio_data/{:s}_SII_a_fit_data.dat'.format(folder)
    SII_b_file  = output_directory + 'flux_ratio_data/{:s}_SII_b_fit_data.dat'.format(folder)

    # Create skip list:
    ## The skip list contains bad fits that are supposed to be cleared. The number refers to apxx. 
    if folder == 'PA158':
        skip = [14, 17-1, 18-1, 19-1, 20-1] #PA158 [OI]
        #skip2 = [17-1]                #PA158 H_alpha
    elif folder == 'PA239':
        skip = [5, 6, 7, 8, 9, 10, 16, 17, 18] # PA239 [OI]
        #skip2 = [9, 10, 16, 18]
    #skip_239    = [9, 10, 16, 18]
    elif folder == 'PA261':
        skip = []

    # Create data list


    OI_flux         = np.loadtxt(OI_file, skiprows=1 , usecols= 6)
    OIII_flux       = np.loadtxt(OIII_file, skiprows=1 , usecols= 6)
    Halpha_flux     = np.loadtxt(Halpha_file, skiprows=1 , usecols= 6)
    Hbeta_flux      = np.loadtxt(Hbeta_file, skiprows=1 , usecols= 6)
    NII_flux        = np.loadtxt(NII_file, skiprows=1 , usecols= 6)
    SII_flux        = np.loadtxt(SII_file, skiprows=1 , usecols= 6)
    SII_a_flux      = np.loadtxt(SII_a_file, skiprows= 1, usecols= 6)
    SII_b_flux      = np.loadtxt(SII_b_file, skiprows=1, usecols=6)


    position        = np.loadtxt(OI_file, skiprows= 1, usecols= 0)
    position_err    = np.loadtxt(OI_file, skiprows= 1, usecols= 1)

    OI_flux_err     = np.loadtxt(OI_file, skiprows= 1, usecols= 7)
    OIII_flux_err   = np.loadtxt(OIII_file, skiprows= 1, usecols= 7)
    Halpha_flux_err = np.loadtxt(Halpha_file, skiprows= 1, usecols= 7)
    Hbeta_flux_err  = np.loadtxt(Hbeta_file, skiprows= 1, usecols= 7)
    NII_flux_err    = np.loadtxt(NII_file, skiprows= 1, usecols= 7)
    SII_flux_err    = np.loadtxt(SII_file, skiprows= 1, usecols= 7)
    SIIa_flux_err   = np.loadtxt(SII_a_file, skiprows=1, usecols= 7)
    SIIb_flux_err   = np.loadtxt(SII_b_file, skiprows=1, usecols= 7)

    Halpha_fwhm     = np.loadtxt(Halpha_file, skiprows= 1, usecols= 4)
    NII_fwhm        = np.loadtxt(NII_file,    skiprows= 1, usecols= 4)
    SII_fwhm        = np.loadtxt(SII_file,    skiprows= 1, usecols= 4)

    Halpha_fwhm_err = np.loadtxt(Halpha_file, skiprows= 1, usecols= 5)
    NII_fwhm_err    = np.loadtxt(NII_file,    skiprows= 1, usecols= 5)
    SII_fwhm_err    = np.loadtxt(SII_file,    skiprows= 1, usecols= 5)
   
    Halpha_velocity     = np.loadtxt(Halpha_file, skiprows= 1, usecols= 2)
    NII_velocity        = np.loadtxt(NII_file,    skiprows= 1, usecols= 2)
    SII_velocity        = np.loadtxt(SII_file,    skiprows= 1, usecols= 2)
    Halpha_velocity_err = np.loadtxt(Halpha_file, skiprows= 1, usecols= 3)
    NII_velocity_err    = np.loadtxt(NII_file,    skiprows= 1, usecols= 3)
    SII_velocity_err    = np.loadtxt(SII_file,    skiprows= 1, usecols= 3)

    #Generating the flux ratio and the corresponding errors

    OI6300_Halpha_flux_ratio    = np.log10(OI_flux/Halpha_flux)
    NII_Halpha_flux_ratio       = np.log10(NII_flux/Halpha_flux)
    SII_Halpha_flux_ratio       = np.log10(SII_flux/Halpha_flux)
    OIII_5007_Hbeta_flux_ratio  = np.log10(OIII_flux/Hbeta_flux)
    SIIab_ratio                 = SII_a_flux/SII_b_flux
    Balmer_decrement            = Halpha_flux/Hbeta_flux

    OI_ratio_err                          = f.log_err(OI_flux, Halpha_flux, OI_flux_err, Halpha_flux_err)
    NII_ratio_err                         = f.log_err(NII_flux, Halpha_flux, NII_flux_err, Halpha_flux_err)
    SII_ratio_err                         = f.log_err(SII_flux, Halpha_flux, SII_flux_err, Halpha_flux_err)
    OIII5007_ratio_err                    = f.log_err(OIII_flux, Hbeta_flux, OIII_flux_err, Hbeta_flux_err)
    SIIab_ratio_err                       = f.ratio_err(SII_a_flux, SII_b_flux, SIIa_flux_err, SIIb_flux_err)
    Balmer_decrement_err                  = f.ratio_err(Halpha_flux, Hbeta_flux, Halpha_flux_err, Hbeta_flux_err)


    #Generate the total position dictionary
    total_dict = {}
    total_dict['position']                              = np.delete(position, skip) - position[0]
    total_dict['position_err']                          = np.delete(position_err, skip) 
    total_dict['OI_Halpha_flux_ratio']                  = np.delete(OI6300_Halpha_flux_ratio, skip)
    total_dict['OI_Halpha_flux_ratio_err']              = np.delete(OI_ratio_err, skip)

    total_dict['NII_Halpha_flux_ratio']                 = np.delete(NII_Halpha_flux_ratio, skip)
    total_dict['NII_Halpha_flux_ratio_err']             = np.delete(NII_ratio_err, skip)
    total_dict['SII_Halpha_flux_ratio']                 = np.delete(SII_Halpha_flux_ratio, skip)
    total_dict['SII_Halpha_flux_ratio_err']             = np.delete(SII_ratio_err, skip)
    total_dict['OIII_Hbeta_flux_ratio']                 = np.delete(OIII_5007_Hbeta_flux_ratio, skip)
    total_dict['OIII_Hbeta_flux_ratio_err']             = np.delete(OIII5007_ratio_err, skip)
    total_dict['SIIab_flux_ratio']                      = np.delete(SIIab_ratio, skip)
    total_dict['SIIab_flux_ratio_err']                  = np.delete(SIIab_ratio_err, skip)
    total_dict['Balmer_decrement']                      =  np.delete(Balmer_decrement, skip)
    total_dict['Balmer_decrement_err']                  =  np.delete(Balmer_decrement_err, skip)

    total_dict['Halpha_flux']                           = np.delete(Halpha_flux, skip)
    total_dict['Halpha_flux_err']                       = np.delete(Halpha_flux_err, skip)

    #Velocity
    total_dict['Halpha_velocity']                       = np.delete(Halpha_velocity, skip)
    total_dict['Halpha_velocity_err']                   = np.delete(Halpha_velocity_err, skip)
    total_dict['NII_velocity']                          = np.delete(NII_velocity, skip)
    total_dict['NII_velocity_err']                      = np.delete(NII_velocity_err, skip)
    total_dict['SII_velocity']                          = np.delete(SII_velocity, skip)
    total_dict['SII_velocity_err']                      = np.delete(SII_velocity_err, skip)
    
    #Calculation Part:
    if folder == 'PA261':
        remove_list     = [6-1, 7-1, 8-1]
        SII_remove_list = [7]
    else:
        remove_list     = []
        SII_remove_list = []

    average_SIIab_ratio         = np.average([x for x in np.delete(total_dict['SIIab_flux_ratio'], SII_remove_list)])
    average_Balmer_decrement    = np.average([x for x in total_dict['Balmer_decrement'] if x >= 2.86])
    average_Halpha_flux         = np.average([x for x in np.delete(total_dict['Halpha_flux'], remove_list)])

    log_e_density               = f.log_e_density(average_SIIab_ratio)
    Halpha_init_flux, excess    = f.init_Halpha_flux(average_Balmer_decrement, average_Halpha_flux)

    params_info_file            = output_directory + '{:s}_param_info'.format(folder)

    
    if os.path.exists(params_info_file):
        os.remove(params_info_file)

    with open(params_info_file, 'a') as file: 
        file.write('The average electron number density in log-scale is {:.3f}'.format(log_e_density) + '\n')
        file.write('The average electron number density is {:.3f} cm^-3'.format(10**log_e_density) + '\n')
        file.write('The average Halpha flux is {:.6e} erg/s.'.format(Halpha_init_flux) + '\n')
        file.write('The excess E(B-V) is {:.6f}'.format(excess) + '\n')



    # Generating the label for each points in plots below.
    List_label = []

    for i in range(len(NII_flux)):
        if folder == 'PA261':
            if i in skip:
                continue
            else:
                List_label.append(str(i+1))
        
        elif folder == 'PA158':
            if i in skip:
                continue
            else:
                if i >= 15:
                    i += 1
                List_label.append(str(i))
        else:
            if i in skip:
                continue
            else:
                List_label.append(str(i))



    position = position - position[0] 
    # Plotting part:
    
    #Generating BPT Diagrams (NII, SII, OIII, OI, respectively) 

    plt.scatter(total_dict['NII_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'])
    plt.errorbar(total_dict['NII_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'],\
                 xerr= total_dict['NII_Halpha_flux_ratio_err'], yerr= total_dict['OIII_Hbeta_flux_ratio_err'], fmt= 'o', ecolor='black')

    xmax   =  max(total_dict['NII_Halpha_flux_ratio']) + total_dict['NII_Halpha_flux_ratio_err'][np.where(max(total_dict['NII_Halpha_flux_ratio']))]
    xmin   = -0.7
    ymin, ymax  = (-3.5, 2.2)

    # [NII] starburst line data generation and plot 
    x_step = np.linspace(xmin, 0.34, num = 50)
    plt.plot(x_step, f.NII_Starburst(x_step), color = 'red')
    # [NII] starburst modified line plot
    x_step = np.linspace(xmin, -0.077, num= 50)
    plt.plot(x_step, f.NII_modified_starburst(x_step), linestyle = 'dashed', color = 'black')
    plt.xlabel(r'$\log{([NII]6584/H_{\alpha})}$')
    plt.ylabel(r'$\log{([OIII]5007/H_{\beta})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['NII_Halpha_flux_ratio'][i], total_dict['OIII_Hbeta_flux_ratio'][i]))

    plt.xlim(xmin, max(xmax, 0.34+0.1))
    plt.ylim(ymin, ymax)
    plt.savefig(output_directory + 'BPT Diagram/BPT(NII)_{:s}.png'.format(folder))

    plt.clf()

    #SII BPT Diagram
    # (1) Data plot
    plt.scatter(total_dict['SII_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'])
    plt.errorbar(total_dict['SII_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'], \
                xerr = total_dict['SII_Halpha_flux_ratio_err'], yerr = total_dict['OIII_Hbeta_flux_ratio_err'], fmt='o', ecolor='black')

    # (2.1) Starburst line data generation
    xmax  = max(total_dict['SII_Halpha_flux_ratio']) + total_dict['SII_Halpha_flux_ratio_err'][np.where(max(total_dict['SII_Halpha_flux_ratio']))]
    xmin  = -1.2
    x_step = np.linspace(xmin, 0.17, num = 50)
    fig_xmax = max(xmax, 0.17) + 0.1
    # (2.2) Starburst line plot
    plt.plot(x_step, f.SII_Starburst(x_step), color = 'red')

    # (3) Seyfert separation line data generation and figure plot
    x_step = np.linspace(-0.315, fig_xmax, num= 50)
    plt.plot(x_step, f.SII_Seyfert_separation_line(x_step), linestyle = '-.', color = 'blue')


    plt.xlabel(r'$\log{([SII]/H_{\alpha})}$')
    plt.ylabel(r'$\log{([OIII]5007/H_{\beta})}$')

    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['SII_Halpha_flux_ratio'][i], total_dict['OIII_Hbeta_flux_ratio'][i]))

    plt.xlim(xmin, fig_xmax)
    plt.ylim(ymin, ymax)
    plt.savefig(output_directory + 'BPT Diagram/BPT(SII)_{:s}.png'.format(folder))

    plt.clf()


    # OI BPT Diagram
    plt.scatter(total_dict['OI_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'])
    plt.errorbar(total_dict['OI_Halpha_flux_ratio'], total_dict['OIII_Hbeta_flux_ratio'],\
                 xerr= total_dict['OI_Halpha_flux_ratio_err'], yerr= total_dict['OIII_Hbeta_flux_ratio_err'], fmt= 'o', ecolor='black')

    # Plot size generation
    xmin       = -2.25
    xmax       = max(total_dict['OI_Halpha_flux_ratio']) + total_dict['OI_Halpha_flux_ratio_err'][np.where(max(total_dict['OI_Halpha_flux_ratio']))]
    fig_xmax   = xmax + 0.2

    # OI Starburst line data generation and figure plot
    x_step     = np.linspace(xmin, -0.60, num= 50)
    plt.plot(x_step, f.OI_Starburst(x_step), color = 'red')

    # OI Seyfert Separation line data generation and figure plot
    x_step     = np.linspace(-1.127, fig_xmax, num= 50)
    plt.plot(x_step, f.OI_Seyfert_separation_line(x_step), linestyle = '-.', color = 'blue')

    plt.xlabel(r'$\log{([OI]6300/H_{\alpha})}$')
    plt.ylabel(r'$\log{([OIII]5007/H_{\beta})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['OI_Halpha_flux_ratio'][i], total_dict['OIII_Hbeta_flux_ratio'][i]))

    plt.xlim(xmin,fig_xmax)
    plt.ylim(ymin, ymax)
    plt.savefig(output_directory + 'BPT Diagram/BPT(OI)_{:s}.png'.format(folder))

    plt.clf()


    #Generate the position vs. Flux-ratio plots
    ## [SII]/H_alpha flux ratio vs position plot 
    plt.scatter(total_dict['position'], total_dict['SII_Halpha_flux_ratio'])
    plt.errorbar(total_dict['position'], total_dict['SII_Halpha_flux_ratio'],\
                 xerr= total_dict['position_err'], yerr= total_dict['SII_Halpha_flux_ratio_err'], fmt= 'o', ecolor= 'black')
    plt.xlabel('Distance')
    plt.ylabel(r'$\log{([SII]/H_{\alpha})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['SII_Halpha_flux_ratio'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/SII_flux_ratio_position_{:s}.png'.format(folder))

    plt.clf()

    # [OI]6300/H_alpha flux ratio vs position plot
    plt.scatter(total_dict['position'], total_dict['OI_Halpha_flux_ratio'])
    plt.errorbar(total_dict['position'], total_dict['OI_Halpha_flux_ratio'], \
                xerr= total_dict['position_err'], yerr= total_dict['OI_Halpha_flux_ratio_err'], fmt='o', ecolor= 'black')
    plt.xlabel('Distance')
    plt.ylabel(r'$\log{([OI]6300/H_{\alpha})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['OI_Halpha_flux_ratio'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/OI6300_flux_ratio_position_{:s}.png'.format(folder))

    plt.clf()

    # [NII]/H_alpha flux ratio vs position plot
    plt.scatter(total_dict['position'], total_dict['NII_Halpha_flux_ratio'])
    plt.errorbar(total_dict['position'], total_dict['NII_Halpha_flux_ratio'], \
                xerr= total_dict['position_err'], yerr= total_dict['NII_Halpha_flux_ratio_err'], fmt='o', ecolor= 'black')
    plt.xlabel('Distance')
    plt.ylabel(r'$\log{([NII]6584/H_{\alpha})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['NII_Halpha_flux_ratio'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/NII6584_flux_ratio_position_{:s}.png'.format(folder))

    plt.clf()

    # [OIII]/H_beta flux ratio vs. position plot
    plt.scatter(total_dict['position'], total_dict['OIII_Hbeta_flux_ratio'])
    plt.errorbar(total_dict['position'], total_dict['OIII_Hbeta_flux_ratio'], \
                xerr= total_dict['position_err'], yerr= total_dict['OIII_Hbeta_flux_ratio_err'], fmt='o', ecolor= 'black')
    plt.xlabel('Distance')
    plt.ylabel(r'$\log{([OIII]5007/H_{\beta})}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['OIII_Hbeta_flux_ratio'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/Hbeta_flux_ratio_position_{:s}.png'.format(folder))

    plt.clf()

    # Plot of flux of Halpha in terms of position
    plt.scatter(total_dict['position'], total_dict['Halpha_flux'])
    plt.errorbar(total_dict['position'], total_dict['Halpha_flux'], \
                xerr= total_dict['position_err'], yerr= total_dict['Halpha_flux_err'], fmt='o', ecolor= 'black')
    plt.xlabel('Position')
    plt.ylabel(r'$H_{\alpha}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['Halpha_flux'][i]))
    plt.savefig(output_directory + 'flux_{:s}.png'.format(folder))

    plt.clf()


    # Plot of Balmer Decrement in terms of position
    plt.scatter(total_dict['position'], total_dict['Balmer_decrement'])
    plt.errorbar(total_dict['position'], total_dict['Balmer_decrement'], \
                xerr= total_dict['position_err'], yerr= total_dict['Balmer_decrement_err'], fmt= 'o', ecolor= 'black')
    plt.xlabel('Position')
    plt.ylabel(r'$H_{\alpha}/H_{\beta}$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['Balmer_decrement'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/Balmer_decrement_{:s}.png'.format(folder))

    plt.clf()

    # Plot of SIIa/SIIb in terms of position
    plt.scatter(total_dict['position'], total_dict['SIIab_flux_ratio'])
    plt.errorbar(total_dict['position'], total_dict['SIIab_flux_ratio'], \
                xerr= total_dict['position_err'], yerr= total_dict['SIIab_flux_ratio_err'], fmt= 'o', ecolor= 'black')
    plt.xlabel('Position')
    plt.ylabel(r'$[SII]a/[SII]b$')
    for i, label in enumerate(List_label):
        plt.annotate(label, (total_dict['position'][i], total_dict['SIIab_flux_ratio'][i]))
    plt.savefig(output_directory + 'flux_ratio_position/SIIab_ratio_{:s}.png'.format(folder))

    plt.clf()

    # Plot of fwhm in terms of position
    plt.scatter(position, Halpha_fwhm, label = r'$H_{\alpha}$')
    plt.scatter(position, NII_fwhm, label = '[NII]')
    plt.scatter(position, SII_fwhm, label = '[SII]')
    plt.errorbar(position, Halpha_fwhm, xerr= position_err, yerr= Halpha_fwhm_err, fmt = 'o', ecolor= 'black')
    plt.errorbar(position, NII_fwhm, xerr=position_err, yerr= NII_fwhm_err, fmt= 'o', ecolor= 'black')
    plt.errorbar(position, SII_fwhm, xerr= position_err, yerr= SII_fwhm_err, fmt= 'o', ecolor= 'black')

    plt.legend()
    plt.xlabel('Position')
    plt.ylabel('Velocity (km/s)')
    plt.savefig(output_directory + 'FWHM_{:s}.png'.format(folder))

    plt.clf()

    # Plot of velocity in terms of positions
    plt.scatter(total_dict['position'], total_dict['Halpha_velocity'], label = r'$H_{\alpha}$')
    plt.scatter(total_dict['position'], total_dict['NII_velocity'], label = '[NII]')
    plt.scatter(total_dict['position'], total_dict['SII_velocity'], label = '[SII]')
    plt.errorbar(total_dict['position'], total_dict['Halpha_velocity'], \
                xerr= total_dict['position_err'], yerr= total_dict['Halpha_velocity_err'], fmt= 'o', ecolor= 'black')
    plt.errorbar(total_dict['position'], total_dict['NII_velocity'], \
                 xerr= total_dict['position_err'], yerr= total_dict['NII_velocity_err'], fmt= 'o', ecolor= 'black')
    plt.errorbar(total_dict['position'], total_dict['SII_velocity'], \
                xerr = total_dict['position_err'], yerr = total_dict['SII_velocity_err'], fmt= 'o', ecolor= 'black')

    plt.legend()
    plt.xlabel('Position')
    plt.ylabel('Velocity (km/s)')
    plt.savefig(output_directory + 'Velocity_{:s}'.format(folder))

    plt.clf()

    
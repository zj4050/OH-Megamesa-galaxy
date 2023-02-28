#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sigmaSpec(wv, flux, region):
    import numpy as np
    wv_ind = []
    wv_ind2 = []
    
    # check the actual wavelength values nearest to the wavelengths specified in region
    for ind, i in enumerate(wv):
        if abs(i - region[0]) < 0.7:
            wv_ind.append(ind)
            
        elif abs(i - region[1]) < 0.7:
            wv_ind2.append(ind)
    
    # calculate the standard deviation of the flux values in a flat part of the spectrum
    sigma = np.std(flux[wv_ind[0]: wv_ind2[0]])
    
    # calculate mean flux in the region
    mean_flux = np.mean(flux[wv_ind[0]: wv_ind2[0]])
    
    # calculate the error spectrum
    sigma_spec = np.sqrt(abs(flux)/abs(mean_flux))*sigma
    
    # look for values of zeo and replace them
    for ind, i in enumerate(sigma_spec):
        if i == 0:
            # print('zero')
            sigma_spec[ind] = sigma_spec[ind-1]
            
    return sigma_spec
    
def lineFit(spectrum1, spectrum2, guesses, tied, limits, limited, output_filename, filename, output_directory,
            sigma_region, z, rest, lines, exclude, center, order = 5):
    
    '''
    Spectrum: String - the path to the text file contining the spectrum to fit
    guesses: List: - the initial guesses for the amplitude, center, and width of emission lines to fit
    tied: List: - same length as guesses
    limits: List: - same length as tied
    limited: List: - same length as limits
    output_filename: String: - prefix for the name of the text file - might suggest it be the slit position being fit
    '''
    
    import pyspeckit
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    import matplotlib as mpl
    from matplotlib.ticker import AutoMinorLocator
    
    # retrieve spectrum from the ppxf output file
    data= np.loadtxt(spectrum1, skiprows = 1)
    wv = data[:,0]
    norm_flux = data[:,1] # the continuum subtract gas spectrum
    
    # creating output directory and sub-directories to save data files and plots
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    
    # directory for plots of the bare spectrum and various info in legend
    if not os.path.isdir(output_directory + '/spectra/'):
        os.makedirs(output_directory + '/spectra/')
    
    # directory for the plots of the spectra with fits plotted and info in legend
    if not os.path.isdir(output_directory + '/fit_spectra/'):
        os.makedirs(output_directory + '/fit_spectra/')
    
    # getting bin location in arcseconds - will work as long as the ppxf text file format was unchanged
    aperture = np.loadtxt(spectrum2, skiprows = 1, max_rows = 1, delimiter = ' ')
    bin_loc = float(((aperture[2] - center) * 0.1614 + (aperture[3]- center)*0.1614)/2) #aperture location in arcsec relative to central bin
    dpos = ((aperture[3]-aperture[2])*0.1614*0.5)
    ap_width = ((aperture[3]-aperture[2])*0.1614) # aperture width in arcsec
    
    # retrieve aperture number for later reference
    if len(str(aperture[0])) > 1:
        aperture_number = str(int(aperture[0]))
        
    else:
        aperture_number = '0' + str(int(aperture[0]))
        
    output_filename = output_filename + '_' + aperture_number
    
    # retrieve flux normalizaiton factor used in ppxf from the output ppxf text file
    norm = np.loadtxt(spectrum2, max_rows = 1)
    
    # estimating the error spectrum
    sigma_spec = sigmaSpec(wv, norm_flux, sigma_region)
    
    # writing error spectrum to a file
    os.remove(output_directory + filename + '_' + 'sigmaspec' + ".txt")
    
    with open(output_directory + filename + '_' + 'sigmaspec' + ".txt",'a') as f:
        f.write(f"{format('WV','8.8s')}\t {format('Sigma','8.8s')}\n")
                
        for ind, i in enumerate(sigma_spec):
            f.write(f"{format(wv[ind],'8.3f')}\t {format(i,'8.3f')}\n")
        f.close()
    
    # initializing the spectrum, plotter, and baseline for fitting
    spec = pyspeckit.Spectrum(data = norm_flux, xarr = wv, error = sigma_spec,
                          xarrkwargs={'unit':'AA'},
                          unit='erg/s/cm^2/AA')
    
    # calculating limits of plot in angstrom
    xmin_plot = min(guesses[1::3]) - 20
    xmin = min(guesses[1::3]) - 30
    xmax_plot = max(guesses[1::3]) + 20
    xmax = max(guesses[1::3]) + 30
    ymin = -1
    wv_ind = [ind for ind, i in enumerate(wv) if i > xmin_plot and i < xmax]
    ymax = max(norm_flux[min(wv_ind):max(wv_ind)])
    
    # initialize plotter
    spec.plotter(xmin = xmin_plot, xmax = xmax_plot, ymin = ymin, ymax = ymax)
    
    #adding in a baseline fit of the background - needs to be done over a 'small'
    # wavelength range since it is hard to describe the baseline continuum over the 
    # whole spectrum with one fit
    spec.baseline(xmin=xmin, xmax=xmax,
        exclude=exclude, 
        subtract=False, reset_selection=False, 
        highlight_fitregion=False, order=order)
    
    # initialize fitting using guesses
    spec.specfit(guesses = guesses, tied = tied,
                 limits = limits, limited = limited, annotate = False)
    
    # retrieve chi square value for the fit
    chi = spec.specfit.optimal_chi2(reduced=True, threshold='auto')
    
    spec.plotter.refresh()
    spec.baseline.clearlegend()
    
    # adding axis labels and a legend with filename and chi^2
    spec.plotter.axis.set_xlabel(r'Wavelength $(\AA)$', fontsize = 14)
    spec.plotter.axis.set_ylabel(f"{format(norm,'.3e')}  "r'Flux $(\mathrm{erg/s/cm^2/\AA})$',fontsize = 14)
    spec.plotter.refresh()
    plt.plot([],[],' ', label = f"{aperture_number}")
    plt.plot([],[],' ', label = f"$\chi^{2}$ = {format(chi,'.4f')}")
    plt.plot([],[], ' ', label = f"ap_width = {format(ap_width,'.1f')} arcsec")
    plt.plot([],[], ' ', label = f"ap_position = {format(bin_loc, '.1f')} arcsec")
    plt.legend(fontsize = 14)
    
    # plotting residuals
    spec.specfit.plotresiduals(axis=spec.plotter.axis,clear=False,yoffset=-0.75,label=False)
    
    # saving the output figure from pyspeckit
    spec.plotter.figure.savefig(output_directory + '/fit_spectra/' + output_filename + '_fitplot' + '.png', dpi = 250)
     
    # plotting the spectrum and sigma spectrum to check
    fig, ax1 = plt.subplots(nrows = 2, sharex = True, sharey = True, gridspec_kw={'hspace': 0})
    ax1[0].plot(wv, norm_flux, 'black', lw = 0.7)
    ax1[0].set_ylabel("Flux Density", fontsize = 14)
    
    ax1[1].plot(wv, sigma_spec, 'black', lw = 0.7)
    ax1[1].set_ylabel("Uncertainty", fontsize = 14)
    ax1[1].set_xlabel("Wavelength", fontsize = 14)
    plt.tight_layout()
    
    # saving sigmaspectrum if it doesn't already exist
    if not os.path.isdir(output_directory + '/spectra/' + filename + '_sigma_spec' + '.png'):
        plt.savefig(output_directory + '/spectra/' + filename + '_sigma_spec' + '.png')
    
    # plotting the full spectrum with info like aperture position, number, and width
    plt.figure()
    plt.plot(wv, norm_flux*norm, c = 'black', lw = .8)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().tick_params(bottom = True, top = True, left = True, right = True, which = 'both', direction = 'in')
    plt.ylabel('Flux (erg/$cm^{2}/s/\AA$)', fontsize = 14)
    plt.xlabel('Wavelength ($\AA$)', fontsize = 14)
    plt.plot([],[],' ', label = f"{aperture_number}")
    plt.plot([],[],' ', label = f"dist = {format(bin_loc,'.3f')} arcsec")
    plt.plot([],[], ' ', label = f"ap_width = {format(ap_width,'.3f')}")
    plt.legend(fontsize = 12)
    plt.tight_layout()
    
    # save the info plot if it doesn't already exist for the same filename
    if not os.path.isdir(output_directory + '/spectra/' + filename + '_infoplot' + '.png'):
        plt.savefig(output_directory + '/spectra/' + filename + '_infoplot' + '.png')
    
    # doing line calculations / accessing best fit parameters
    spec.measure(z = z, fluxnorm = norm) # returns some model parameters and some calculated values like total flux, and luminosity
    
    center=[]# empty array for line wavelengths
    amp=[] # for amplitudes
    flux=[] # for integrated line fluxes
    flux_err=[]
    fwhm=[] # for the FWHM of the lines
    lum=[] # for the calculated line luminosities
    vel=[] # unsubtracted velocities
    rel_vel=[] # subtracted velocities
    dvel=[] # for velocity uncertainty
    
    # retrieve model parameters
    model_pars = spec.specfit.modelpars 
    model_errs = spec.specfit.modelerrs
    
    amplitude = model_pars[0::3]
    damplitude = model_errs[0::3]
    sigma = model_pars[2::3]
    dsigma = model_errs[2::3]
    dcenter = model_errs[1::3]
    
    c = 299792.458 # km/s
    
    # iterate through the values for each emission line
    for line in spec.measurements.lines.keys():
        # pulls these measurements from the model pars, appending the values to the empty lists
        center.append(spec.measurements.lines[line]['pos'])
        amp.append(spec.measurements.lines[line]['amp'])
        flux.append(spec.measurements.lines[line]['flux'])
        fwhm.append(spec.measurements.lines[line]['fwhm'])
        lum.append(spec.measurements.lines[line]['lum'])
        
    # calculating velocities, flux err
    for j in rest:
        ind = rest.index(j) # gets indicy of rest frame value
        
        delta = ((center[ind]- j)/j + 1)**2 # calculates part of the relativistic doppler shift
        velocity = ((delta -1)/(delta+1))*c # final calculation
        vel.append(velocity)
        rel_vel.append(velocity) # subtracting a central velocity can be done later
        
        # propogation of error for flux
        dflux = np.sqrt(2*np.pi*norm**2*((sigma[ind]*damplitude[ind])**2 + (amplitude[ind]*dsigma[ind])**2))
        flux_err.append(dflux)
        
        velocity_uncertainty = ((4*j**2*center[ind])/(center[ind]**2+j**2)**2)*dcenter[ind]*c
        
        dvel.append(velocity_uncertainty)
    
    flux_per = []
    
    # calculating percent error on flux and appending to list
    for ind, i in enumerate(flux):
        flux_per.append((flux_err[ind]/flux[ind])*100)
        
    # applying flux normalization to amplitude uncertainties
    damplitude = damplitude * norm
    dpos = np.full_like(rel_vel,dpos)
    bin_loc = np.full_like(rel_vel,bin_loc)
    
    # Gathering model paramters and calculated values to add to a text file 
    info = zip(lines,rest,center,dcenter,amp,damplitude,sigma,dsigma,flux,flux_err,bin_loc,dpos,vel,rel_vel,dvel,flux_per,fwhm)
    
    # if the output file doesn't already exist - open it, append the header (column names), and then append the data for each line.     
    if not os.path.exists(output_directory + filename + '_fit_data.dat'): 
          
        with open(output_directory + filename + '_fit_data.dat','a') as f:
            f.write(f"{format('Line','8.8s')}\t {format('Rest_wv','8.8s')}\t {format('Center','8.8s')}\t {format('dCenter','8.8s')}\t {format('Amp','8.8s')}\t \
    {format('dAmp','8.8s')}\t {format('Sigma','8.8s')} \t {format('dSig','8.8s')} \t {format('Flux','8.8s')}\t \
    {format('dFlux','8.8s')}\t {format('Pos','8.8s')}\t {format('dPos','8.8s')}\t {format('Vel','8.8s')}\t {format('Rel_Vel','8.8s')}\t \
    {format('dVel','8.8s')}\t {format('flu_per','8.8s')}\t {format('fwhm', '8.8s')}\n")
                        
            for i in info:
                f.write(f"{format(i[0],'8.8s')}\t {format(i[1],'8.3f')}\t {format(i[2],'8.3f')}\t {format(i[3],'8.3f')}\t {format(i[4],'8.3e')}\t \
    {format(i[5],'8.3e')}\t {format(i[6],'8.3f')}\t {format(i[7],'8.3f')}\t {format(i[8],'8.3e')}\t {format(i[9],'8.3e')}\t {format(i[10],'8.3f')}\t \
    {format(i[11],'8.3f')}\t {format(i[12],'8.3f')}\t {format(i[13],'8.3f')}\t {format(i[14],'8.3f')}\t {format(i[15],'8.3f')}\t {format(i[16],'8.3f')}\n")
                            
         
    
    # if the file already exists, just append the data for new lines that have been fit
    else:
        file1 = np.loadtxt(output_directory + filename + '_fit_data.dat', skiprows= 1, usecols= 2)
        if len(file1) > 18:
            os.remove(output_directory + filename + '_fit_data.dat')

            with open(output_directory + filename + '_fit_data.dat','a') as f:
                f.write(f"{format('Line','8.8s')}\t {format('Rest_wv','8.8s')}\t {format('Center','8.8s')}\t {format('dCenter','8.8s')}\t {format('Amp','8.8s')}\t \
        {format('dAmp','8.8s')}\t {format('Sigma','8.8s')} \t {format('dSig','8.8s')} \t {format('Flux','8.8s')}\t \
        {format('dFlux','8.8s')}\t {format('Pos','8.8s')}\t {format('dPos','8.8s')}\t {format('Vel','8.8s')}\t {format('Rel_Vel','8.8s')}\t \
        {format('dVel','8.8s')}\t {format('flu_per','8.8s')}\t {format('fwhm', '8.8s')}\n")
                            
                for i in info:
                    f.write(f"{format(i[0],'8.8s')}\t {format(i[1],'8.3f')}\t {format(i[2],'8.3f')}\t {format(i[3],'8.3f')}\t {format(i[4],'8.3e')}\t \
        {format(i[5],'8.3e')}\t {format(i[6],'8.3f')}\t {format(i[7],'8.3f')}\t {format(i[8],'8.3e')}\t {format(i[9],'8.3e')}\t {format(i[10],'8.3f')}\t \
        {format(i[11],'8.3f')}\t {format(i[12],'8.3f')}\t {format(i[13],'8.3f')}\t {format(i[14],'8.3f')}\t {format(i[15],'8.3f')}\t {format(i[16],'8.3f')}\n")
    
        else:
            with open(output_directory + filename + '_fit_data.dat' , 'a') as f:
                for i in info:
                    f.write(f"{format(i[0],'8.8s')}\t {format(i[1],'8.3f')}\t {format(i[2],'8.3f')}\t {format(i[3],'8.3f')}\t {format(i[4],'8.3e')}\t \
        {format(i[5],'8.3e')}\t {format(i[6],'8.3f')}\t {format(i[7],'8.3f')}\t {format(i[8],'8.3e')}\t {format(i[9],'8.3e')}\t \
        {format(i[10],'8.3f')}\t {format(i[11],'8.3f')}\t {format(i[12],'8.3f')}\t {format(i[13],'8.3f')}\t {format(i[14],'8.3f')}\t \
        {format(i[15],'8.3f')}\t {format(i[16],'8.3f')}\n")
                            
            
            




from time import perf_counter as clock
from os import path
import glob 
import numpy as np
import ppxf as ppxf_package
from ppxf.ppxf import ppxf
import ppxf.ppxf_util as util
import ppxf.miles_util as lib
import matplotlib.pyplot as plt
from astropy.io import fits
import os
import scipy.ndimage

###############################################################################
def fitspec(spectrum_file, miles_dir, z, fwhm, mask_between, output_file, output_direct):
    '''
    

    Parameters
    ----------
    spectrum_file : string
        The FITS file with the spectrum
    miles_dir : string
        The file location for MILES stellar library
    z : float
        The redshift of the system/galaxy.
    fwhm : float
        detector FWHM as measured from the arc lamp spectrum
    mask_between: list of tuple
        a list of tuples, (lower, upper), to define the lower and upper bounds, in units of wavelength (angstrom), of features to be excluded from the fit
    output_file : string
        Desired filename for the output data file, exclude the file extension ( i.e. .png, .txt)

    Returns
    -------
    None.

    '''
    
    # ------------------ Load Galaxy Spectrum -------------------------------------
    print(spectrum_file)
    file = str(spectrum_file) # makes sure the filename is a string, this is recquired for fits.open to read them. 
    hdu = fits.open(file)
    gal_lin = hdu[0].data # loads the actual image/spectrum data
    h1 = hdu[0].header
    
    
    # redshift of galaxy
    z = z
    
    #fwhm
    FWHM_gal = fwhm 
    
    lamRange = h1['CRVAL1'] + np.array([0., h1['CDELT1']*(h1['NAXIS1'] - 1)])        
    
#-------------------------Log re-bin the data ---------------------------------
    galaxy1, logLam1, velscale = util.log_rebin(lamRange, gal_lin) # logrithmic rebin of the flux and wavelength
    galaxy = galaxy1/np.median(galaxy1)  # Normalize spectrum to avoid numerical issues
    lam = np.exp(logLam1) # obtain array of linear wavelengths
    wave = lam
    
    # define the mask for to take chip gaps or other erroneous features out of the fit
    
    
    for i in mask_between:
        lam = np.ma.masked_inside(lam, i[0], i[1])
    
    mask = ~np.ma.getmask(lam) # get the inverted mask
    
    # using randomly selected noise
    # Could potentially make this the noise spectrum rather than constant noise
    noise = np.full_like(galaxy, 0.0456)
    
    # min/max of wavelength 
    lam_range_gal = np.array([np.min(wave), np.max(wave)])/(z+1)
            
    #------------------- Setup templates -----------------------
    
    ## RW - didn't change this section much from SDSS example. 
    
    pathname = str(miles_dir) + 'Eun1.30*.fits' 
    miles = lib.miles(pathname, velscale, FWHM_gal)

    # The stellar templates are reshaped into a 2-dim array with each spectrum
    # as a column, however we save the original array dimensions, which are
    # needed to specify the regularization dimensions
    reg_dim = miles.templates.shape[1:]
    stars_templates = miles.templates.reshape(miles.templates.shape[0], -1)

    # See the pPXF documentation for the keyword REGUL,
    regul_err = 0.013  # Desired regularization error

    # Construct a set of Gaussian emission line templates.
    # Estimate the wavelength fitted range in the rest frame.
#            lam_range_gal = np.array([np.min(wave), np.max(wave)])/(1 + z) # I put this in earlier in the code under Galaxy Wavelength Range
    gas_templates, gas_names, line_wave = \
        util.emission_lines(miles.ln_lam_temp, lam_range_gal, FWHM_gal, tie_balmer = False)

    # Combines the stellar and gaseous templates into a single array.
    # During the PPXF fit they will be assigned a different kinematic
    # COMPONENT value
    #
    templates = np.column_stack([stars_templates, gas_templates])

    #-----------------------------------------------------------
    
    c = 299792.458
#            dv = 4455
    dv = c*(miles.ln_lam_temp[0] - np.log(wave[0])) # km/s
    
    vel = c*np.log(1 + z)   # eq.(8) of Cappellari (2017)
    start = [vel, 180.]  # (km/s), starting guess for [V, sigma]
    
# --------------- Emission Lines ----------------------------------------------
    
    n_temps = stars_templates.shape[1]
    ### RW - the following need to be changed based on how many emission lines are present, such as whether hbeta is detected or not
    n_balmer = 3  # Number of Balmer lines included in the fit
    n_forbidden = 5 
    n_lines = 6
    #n_forbidden = 7 #[OII] lines included

#            n_forbidden = np.sum(["[" in a for a in gas_names])  # forbidden lines contain "[*]" 
#            n_balmer = len(gas_names) - n_forbidden

    # Assign component=0 to the stellar templates, component=1 to the Balmer
    # gas emission lines templates and component=2 to the forbidden lines.
    
#            component = [0]*n_temps + [1]*n_lines
    component = [0]*n_temps + [1]*n_balmer + [2]*n_forbidden
    print(len(component))
    gas_component = np.array(component) > 0
    
    moments = [4, 2, 2]

    # Adopt the same starting value for the stars and the two gas components
    start = [start, start, start]
    
    t = clock()
    reddening = 0.780
    
    # this runs the actual fit, there are variables here that can be changed to get different fits
    # Check the ppxf documentation for what those are
    pp = ppxf(templates, galaxy, noise, velscale, start,
              moments=moments, degree=-1, vsyst=dv, lam=wave,
              regul=1./regul_err, reg_dim=reg_dim, component=component,
              gas_component=gas_component, gas_names=gas_names, mask = None, reddening = reddening)
    
    # pp = ppxf(templates, galaxy, noise, velscale, start,
    #                   plot=False, moments=moments, degree=-1, mdegree=10, vsyst=dv, lam=wave,
    #                   clean=False, regul=1./regul_err, reg_dim=reg_dim, component=component,
    #                   gas_component=gas_component, gas_names=gas_names)
    
    print('Desired Delta Chi^2: %.4g' % np.sqrt(2*galaxy.size))
    print('Current Delta Chi^2: %.4g' % ((pp.chi2 - 1)*galaxy.size))
    print('Elapsed time in PPXF: %.2f s' % (clock() - t))

    weights = pp.weights[~gas_component]  # Exclude weights of the gas templates
    weights = weights.reshape(reg_dim)/weights.sum()  # Normalized

    miles.mean_age_metal(weights)
    miles.mass_to_light(weights, band="r")
    plt.figure()

    # Plot fit results for stars and gas.
    plt.clf()
    pp.plot()
    
    # extract fitted spectra
    wlen = pp.lam  #wavelength
    gal_spectrum = pp.galaxy   #spectrum (input data)
    specfit = pp.bestfit  # best fit spectrum
    gas = pp.gas_component # number of gas components
    spectra = pp.matrix[:, pp.degree + 1 :]
    gas_spectrum = spectra[:, gas].dot(pp.weights[gas]) #emiision line spectrum
    stars_spectrum = specfit - gas_spectrum 
    newgal_spectrum = gal_spectrum - stars_spectrum # subtract fit to stellar component from original spectrum
    Nwlen = np.size(wlen)
    
    out_direc = output_direct
    if not os.path.isdir(out_direc):
        os.makedirs(out_direc)
    
    #write spectra to output file
    
    plt.savefig(output_direct + output_file + '_PPXFspectrum' + '.png')
    
    with open(output_direct + output_file + '_PPXFfit' + '.txt','w') as f:
        f.write(f"{format(np.median(galaxy1),'7.5e')}\n") # writing the normalization factor to the header
        f.write(h1["APNUM1"]+"\n") # writing aperture number to the header
        f.write("wlen\tgal_spec\tfit_spec\tstar_spec\tline_spec\tnewgal_spectrum\n") # column names
        for k in range(np.size(wlen)):
            f.write("{:10.3f}\t{:10.3f}\t{:10.3f}\t{:10.3f}\t{:10.3f}\t{:10.3f}\n"\
                    .format(wlen[k],gal_spectrum[k],specfit[k],stars_spectrum[k],gas_spectrum[k],newgal_spectrum[k]))
        f.close()
     
        
    # adding information from the emission line fits to a text file
    gas = pp.gas_component
    gas_velocity = []
    gas_sig = []
    for l, comp in enumerate(pp.component[gas]):
        gas_velocity.append(pp.sol[comp][:2][0])
        gas_sig.append(pp.sol[comp][:2][1])
        print(pp.sol[comp][:2],'\n')
        
    
    with open(output_direct + output_file + 'emissionlines' + '.txt','w') as f:
        f.write(h1["APNUM1"]+"\n") # write aperture number to header
        f.write(f"{format(pp.chi2,'.4f')} \n") # write the chi-square of the fit to the header
        f.write(f"{format(pp.reddening,'.4f')} \n") # write the reddening to the header
        f.write("name    flux    f_err    vel    sig\n")
        for k in range(len(pp.gas_names)):
            f.write("{:12.12s}\t{:10.5f}\t{:10.2f}\t{:10.4f}\t{:10.2f}\n"\
                    .format(pp.gas_names[k], pp.gas_flux[k], pp.gas_flux_error[k],gas_velocity[k], gas_sig[k]))
        f.close()
            
            
##############################################################################

# specfile = '/home/ryan/Desktop/OHMG_longslit/test_ppxf_fit/PA90.03001.fits' # spectrum from disk of IRAS09320
specfile = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/OHMG-IRAS11506-longslit-spectra/iras11-PA158/e-ap1-iras11-158-p0.fits'
output_directory = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/e-ap1-iras-158-p0/'
output_file = 'e-ap1-iras11-158-p0' 
# output_file = 'iras09320_test'
miles_dir = '/Users/kamiori/Desktop/Python/env/lib/python3.10/site-packages/ppxf/miles_models/'
# wavelengths to mask for IRAS05414
#mask_locations = [(4377, 4389), (4900, 4915), (5188, 5245),(5208, 5253), (5568, 5585),(6267,6325), (6859, 6928), (5960, 5997), (5571, 5582), (4397, 4417), (5881,5901)]
mask_locations = []
z = 0.01078 #redshift for IRAS11506
#z = 0.01486 # redshift for IRAS05414
# z = 0.039367  # redshift for IRAS09320
fwhm = 3.838 # fwhm for IRAS05414 data arcs


if __name__ == '__main__':

    fitspec(specfile, miles_dir,z,fwhm, mask_locations, output_file, output_directory)
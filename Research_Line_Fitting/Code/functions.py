import numpy as np

def log_err(f1, f2, df1, df2 ):
    # f1: the log of the flux_ratio 1
    # f2: the log of the flux_ratio 2
    
    dlogf1 = (1/np.log(10))*(df1/f1)
    dlogf2 = (1/np.log(10))*(df2/f2)

    a = np.log10(f1)/np.log10(f2)
    error  = a*np.sqrt(dlogf1 ** 2 + dlogf2 **2)

    return error 

def ratio_err(f1, f2, df1, df2):
    # f1: the flux_ratio 1
    # f2: the flux_ratio 2

    a = f1/f2

    error = a*np.sqrt((df1/f1)**2 + (df2/f2)**2)

    return error

def NII_Starburst(NII_flux_ratio):
    a = NII_flux_ratio - 0.47
    y = 0.61/a + 1.19

    return y

def SII_Starburst(SII_flux_ratio):
    a = SII_flux_ratio - 0.32
    y = 0.72/a + 1.30

    return y

def OI_Starburst(OI_flux_ratio):
    a = OI_flux_ratio + 0.59
    y = 0.73/a + 1.33

    return y

def NII_modified_starburst(NII_flux_ratio):
    a = NII_flux_ratio - 0.05
    y = 0.61/a + 1.30

    return y

def SII_Seyfert_separation_line(SII_flux_ratio):
    a = SII_flux_ratio
    y = 1.89*a + 0.76
    
    return y

def OI_Seyfert_separation_line(OI_flux_ratio):
    a = OI_flux_ratio
    y = 1.18*a + 1.30
    
    return y
    
def log_e_density(x):
    log_e_density = 0.0846*np.tan(-2.1453*x + 4.9367) + 5.17 - 3.16118*x +2.7206*x**2 - 1.211*x**3
    
    return log_e_density

def init_Halpha_flux(Balmer_decre, Halpha_flux):
    E = 1.97 * np.log10(Balmer_decre/2.86)
    A = 3.33 * E
    Halpha_init = Halpha_flux * 10**(0.4*A)

    return (Halpha_init, E)


import sys
import os 

sys.path.append('/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code')
import line_fitting_code as lfc 

if __file__ == '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code/iras11-158-p0/e-ap0-iras-158-p0/e-ap0-iras11-158.p0-linefitting.py':
        spectrum1 = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_fit_without_spurious_lines.txt'
        spectrum2 = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/e-ap0-iras11-158-p0_PPXFfit.txt'
elif __file__ == '':
        spectrum1 = ''
        spectrum2 = ''

filename = 'e-ap0-iras11-158-p0'

output_directory = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/'


run_region = ['OI', 'Halpha', 'Hbeta']

for run in run_region:
        # H_alpha region fitting
        # each of these lists must be in the same order as the other - typically listed from 'bluest' to reddest line


        if run == 'Halpha':
                NII_6548 = 6548.1
                H_alpha = 6562.8
                NII_6583 = 6583.5
                SII_6716 =  6716.4
                SII_6730 = 6730.8

                rest = [NII_6548, H_alpha, NII_6583, SII_6716, SII_6730] # NII_1, H_alpha, NII_2, SII_1, SII_2

                NII_6548_amp = 1.04
                NII_6548_lam = 6614.3
                NII_6548_sig = 1.5

                H_alpha_amp = 4.59
                H_alpha_lam = 6629.1
                H_alpha_sig = 1.5

                NII_6583_amp = 3.08
                NII_6583_lam = 6650
                NII_6583_sig = 1.5

                SII_6716_amp = 0.76
                SII_6716_lam = 6784.6
                SII_6716_sig = 1.5

                SII_6730_amp = 0.65
                SII_6730_lam = 6798.5
                SII_6730_sig = 1.5

        # amplitude, lambda center, sigma [normalized flux units, angstrom, angstrom]

                guesses = [NII_6548_amp, NII_6548_lam, NII_6548_sig, #[NII]6548
                        H_alpha_amp,  H_alpha_lam,   H_alpha_sig, #H_alpha
                        NII_6583_amp, NII_6583_lam, NII_6583_sig, # [NII]6583
                        SII_6716_amp, SII_6716_lam, SII_6716_sig, # [SII]6716
                        SII_6730_amp, SII_6730_lam, SII_6730_sig # [SII]6730
                        ]

        # certain parameters are 'tied' to others - such as the amplitude and widths of the doublets - this removes some of the free parameters
                tied =  ['(1/2.9) * p[6]',f'{rest[0]/rest[2]} * p[7]',f'{6548.1/6583.5}*p[8]', # NII_a, 
                '','','', # Halpha
                '','','', # NII_b
                '',f'{rest[3]/rest[4]}*p[13]',f'{6716.4/6730.8}*p[14]', # SII_a
                '','','' # SII_b
                ]

        # limits lets you set ranges that that each parameter is allowed to take
                limits = [(0,0), (0,0), (0,0),
                        (0,0), (0,0), (0,0),
                        (0,0), (0,0), (0,0),
                        (0,0), (0,0), (0,0),
                        (0,0), (0,0), (0,0),
                        ]

        # this controls whether each limit is applied, so as this stands, the lower limit of zero on all of the parameters is respected
                limited = [(True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False)
                        ]

                output_filename = filename + '_Halpha_fitting'

                sigma_region = [6700,6806]



        # list of the lines being fit - needs to be in the same order as the above variables as well
                lines = ['[NII]b', 'Halpha','[NII]a','[SII]a','[SII]b']

        # the region to exclude from the baseline fit - this region should cover emission lines and spurious features 
                exclude = [6632,6697,6809, 6838]



        elif run == 'Hbeta':
                #H_beta region fitting

                Hbeta = 4861
                OIII_4959 = 4959  
                OIII_5007 = 5007

                rest = [Hbeta, OIII_4959, OIII_5007]



                guesses = [0.502, 4911.34, 1.5, # Amplitude, lambda center, sigma
                0.0526, 5009.38, 2.0,
                0.191, 5057.31, 1.5]

                tied = ['', '', '',  # Hbeta
                '1/3 * p[6]', '4958.9/5006.9 * p[7]', 'p[8]',  # OIII_4959     
                '', '', ''   # OIII_5007
                ]

                limits = [(0, 0), (0, 0), (0, 0),
                        (0, 0), (0, 0), (0, 0),
                        (0, 0), (0, 0), (0, 0)
                        ]

                limited=[(True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False)
                        ]

                output_filename = filename + '_Hbeta_fitting'

                sigma_region = [4920, 5090]

                lines = ['Hbeta','[OIII]4959','[OIII]5007']

                exclude = None 

        elif run == 'OI':
                OI_6300 = 6300.3
                OI_6364 = 6363.8

                rest = [OI_6300, OI_6364]

                guesses = [0.342, 6364.1, 1.0, #[OI]6300
                        0.155, 6429.14, 1.5 # [OI]6364
                        ]

                tied = ['', '', '', #[OI]6300
                '1/3.1 * p[0]', f'{OI_6364/OI_6300} * p[1]', 'p[2]' #[OI]6364
                ]

                limits = [(0,0), (0,0), (0,0),
                        (0,0), (0,0), (0,0)]

                limited = [(True,False), (True,False), (True,False),
                        (True,False), (True,False), (True,False)]

                output_filename = filename + '_OI_fitting'

                sigma_region = [6389, 6464]

                lines = ['[OI]a','[OI]b']

                exclude = None


        z = 0.01078

        #output_directory = '/Users/kamiori/Desktop/Python/line_fitting/fit_data/pa253/'

        #output_directory = '/Users/kamiori/Desktop/Python/Research Project/OH Megamesa/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0/' #mac_mini_directory

        
        center = 1136.44 # center pixel for PA253 extractions

        lfc.lineFit(spectrum1, spectrum2, guesses, tied, limits, limited, output_filename, filename, output_directory, sigma_region, z, rest, lines, exclude, center)


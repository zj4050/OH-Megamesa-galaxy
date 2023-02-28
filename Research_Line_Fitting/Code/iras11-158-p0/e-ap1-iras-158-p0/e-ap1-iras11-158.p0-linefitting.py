import sys
import os

index = os.path.basename(__file__)[4]

filename = 'e-ap{:s}-iras11-158-p0'.format(index)
filename2 = 'e-ap{:s}-iras-158-p0'.format(index)
filename3 = 'e-ap{:s}-iras11-158.p0'.format(index)


if __file__ == '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code/iras11-158-p0/{:s}/{:s}-linefitting.py'\
                .format(filename2, filename3):
        spectrum1 = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/{:s}_fit_without_spurious_lines.txt'\
                        .format(filename2, filename)
        spectrum2 = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/{:s}_PPXFfit.txt'\
                        .format(filename2, filename)
        output_directory = '/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/'.format(filename2)
        
        sys.path.append('/Users/kamiori/Desktop/Research Project/OH Megamesa galaxy/Research_Line_Fitting/Code')
        import line_fitting_code as lfc 

elif __file__ == '/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Code/iras11-158-p0/{:s}/{:s}-linefitting.py'.format(filename2, filename3):
        spectrum1 = '/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/{:s}_fit_without_spurious_lines.txt'.format(filename2, filename)
        spectrum2 = '/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/{:s}_PPXFfit.txt'.format(filename2, filename)
        output_directory = '/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Output/iras11-PA158/{:s}/'.format(filename2)
        #/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Output/iras11-PA158/e-ap0-iras-158-p0
        sys.path.append('/Users/kamiori/Desktop/OH-Megamesa-galaxy/Research_Line_Fitting/Code')
        import line_fitting_code as lfc 

#run = 'Hbeta' #Choice to fit region ['Halpha', 'Hbeta', 'OI']
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

        # amplitude, lambda center, sigma [normalized flux units, angstrom, angstrom]

                guesses = [0.719, 6612.7, 1.5, #[NII]6548
                        3.4, 6627.3,1.5, #H_alpha
                        2.015,6648.3,1.5, # [NII]6583
                        0.61,6782.3,1.5, # [SII]6716
                        0.501,6797,1.5 # [SII]6730
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



                guesses = [0.371, 4909.7, 1.5, # Amplitude, lambda center, sigma
                0.048, 5008.6, 1.5,
                0.192, 5056.1, 1.5]

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

                guesses = [0.336, 6363, 1.5, #[OI]6300
                        0.165, 6427.1, 1.5 # [OI]6364
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



        center = 1136.44 # center pixel for PA253 extractions

        lfc.lineFit(spectrum1, spectrum2, guesses, tied, limits, limited, output_filename, filename, output_directory, sigma_region, z, rest, lines, exclude, center)


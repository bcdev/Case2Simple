import math
__author__ = 'Carole, Gunnar, Ana'
"""
Created on Thur Mar 03 2016
version 1.0
version 2.0 May 2017

@author: Carole
List of function containing the different algorithms used in the in water C2X processing
Place your algorithm definition here

"""


# TODO implement Sampsa's algorithm
# TODO make the algos callable for specific sensor, i.e. have the rrs and coeffs specifided in if loops for each seonsor
# the call only asks ofr the sensor not the coeff and rrs.
# should make it be possible to override

# There are two CDOM syke algos with different bands and coefficients but same format
def cdom1_syke(rhow, cdom1_coeff=[0.11149, 1.9231, 0.023628], bandnames=["band708", "band490"]):
    """
    Function to calculate CDOM (2 options)
    :param cdom1_syke: function name
    :param band: reflectance (or other Lw or whatever)
    :param coeff: coefficient to be applied
    :return:
    """

    cdom1_ratio = rhow[bandnames[0]] / rhow[bandnames[1]]
    res = (cdom1_coeff[0] * (cdom1_ratio ** 2)) + (cdom1_coeff[1] * cdom1_ratio) + (cdom1_coeff[2])
    return res


def cdom2_syke(rhow, cdom2_coeff=[0.29631, 0.78671, 0.060684], bandnames=["band708", "band442"]):
    """
    Function to calculate CDOM (2 options)
    :param cdom2_syke: function name
    :param band: reflectance (or other Lw or whatever)
    :param coeff: coefficient to be applied
    :return:
    """
    cdom2_ratio = rhow[bandnames[0]] / rhow[bandnames[1]]
    res = (cdom2_coeff[0] * (cdom2_ratio ** 2)) + (cdom2_coeff[1] * cdom2_ratio) + (cdom2_coeff[2])
    return res

#### TSM algos ####
def tsm_syke(rhow, tsm_coeff=[2566.2, -0.2616], bandnames=["band708"]):
    """

    :param tsm_syke: function name
    :param band: reflectance (or other Lw or whatever)
    :param coeff: coefficient to be applied
    :return:
    """
    res = tsm_coeff[0] * rhow[bandnames[0]] + tsm_coeff[1]
    return res


def tsm_nechad_MERIS_665(rhow, coeff=[352.6, 0.1728], bandnames=["band665"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MERIS_680(rhow, coeff=[406.9, 0.1792], bandnames=["band680"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MERIS_708(rhow, coeff=[537.1, 0.1887], bandnames=["band708"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MERIS_753(rhow, coeff=[1810.8, 0.1997], bandnames=["band753"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MERIS_779(rhow, coeff=[1827.1, 0.2046], bandnames=["band779"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MERIS_865(rhow, coeff=[3365, 0.2115], bandnames=["band865"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res

'''
def tsm_nechad_MODIS_667(rhow, coeff=[362.1, 0.1736], bandnames=["band667"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MODIS_678(rhow, coeff=[400.8, 0.1778], bandnames=["band678"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MODIS_748(rhow, coeff=[1768.6, 0.1988], bandnames=["band748"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MODIS_858(rhow, coeff=[2846.9, 0.2112], bandnames=["band858"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res


def tsm_nechad_MODIS_869(rhow, coeff=[3031.5, 0.2117], bandnames=["band869"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = A * math.pi * RRs / (1. - math.pi * RRs / C)
    return res
'''

def tsm_shen_560(rhow, coeff=[0.0566, 0.0493], bandnames=["band560"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = (A * RRs/C) / (1. - RRs/C) ** 2
    return res


def tsm_shen_620(rhow, coeff=[0.09767, 0.0652], bandnames=["band620"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = (A * RRs / C) / (1. - RRs / C) ** 2
    return res


def tsm_shen_709(rhow, coeff=[0.18898, 0.076], bandnames=["band708"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = (A * RRs / C) / (1. - RRs / C) ** 2
    return res


def tsm_shen_779(rhow, coeff=[0.57099, 0.0904], bandnames=["band779"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs = rhow[bandnames[0]]
    A = coeff[0]
    C = coeff[1]
    res = (A * RRs / C) / (1. - RRs / C) ** 2
    return res


def tsm_dox_meris(rhow, coeff=[12.733, 3.2567, 95.883], bandnames=["band779", "band560"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    A = coeff[0]
    B = coeff[1]
    C = coeff[2]
    res = (A * (RRs1 / RRs2)) + (C * (RRs1 / RRs2) ** 2) + B
    return res


def tsm_dox_oli_1(rhow, coeff=[2.389, 3.082], bandnames=["band825", "band482"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    A = coeff[0]
    B = coeff[1]
    res = (A * math.exp(RRs1 / RRs2)) + B
    return res


def tsm_dox_oli_2(rhow, coeff=[3.880, 3.057], bandnames=["band825", "band565"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    A = coeff[0]
    B = coeff[1]
    res = (A * math.exp(RRs1 / RRs2)) + B
    return res

'''
##TODO: add coefficients here, this is semi-analytical algo with weights
def tsm_han_msi(rhow, coeff=[0, 0], bandnames=["band560", "band665"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    A = coeff[0]
    B = coeff[1]
    res = (A * (math.log(RRs2) * (1 + RRs2 / RRs1)) + B)
    return res
'''

def tsm_qiu_meris(rhow, coeff=[1.932, 0.875], bandnames=["band708", "band560"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    A = coeff[0]
    C = coeff[1]
    res = (A * (RRs1 / RRs2)) + (C * (RRs2 / RRs2) ** 2) ##+B (???)
    return res


#### Chlorophyll algos adapated ###

def OC3_meris(rhow, coeff=[0.252, 2.215, 1.519, -0.77, -0.429], bandnames=["band442", "band490", "band560"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    a0 = coeff[0]
    a1 = coeff[1]
    a2 = coeff[2]
    a3 = coeff[3]
    a4 = coeff[4]
    X = max(RRs1, RRs2)/ RRs3
    X = math.log10(X)
    res = 10. ** (a0 + X * (a1 + X * (a2 + X * (a3 + X * a4))))
    return res


def OC4_meris(rhow, coeff=[0.326, -2.768, 2.442, -1.129, 0.499],
              bandnames=["band442", "band490", "band510", "band560"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    RRs4 = rhow[bandnames[3]]
    a0 = coeff[0]
    a1 = coeff[1]
    a2 = coeff[2]
    a3 = coeff[3]
    a4 = coeff[4]
    X = max(RRs1, RRs2, RRs3)/ RRs4
    res = 10. ** (a0 + X * (a1 + X * (a2 + X * (a3 + X * a4))))
    return res


def chl_clark_meris(rhow, coeff=[0.789, -3.926, 11.638, -27.158, 27.937, -10.399],
                    bandnames=["band442n", "band490n", "band560n"]):
    ###nLw and not RRs###
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    a0 = coeff[0]
    a1 = coeff[1]
    a2 = coeff[2]
    a3 = coeff[3]
    a4 = coeff[4]
    a5 = coeff[5]
    X = math.log10((RRs1 + RRs2) / RRs3)
    res = 10. ** (a0 + X * (a1 + X * (a2 + X * (a3 + X * (a4 + X * a5)))))
    return res

'''
###Review bands + IOPs to match names###
def chl_ruddick_meris(rhow, coeff=["iop_atot", "iop_btot, "iop_apig"], bandnames=["band665", "band753"]):
    ##or band672 + band704 or band748 + band830-900

    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    a0 = coeff[0]
    a1 = coeff[1]
    a2 = coeff[2]
    res = (RRs2 / RRs1(a1 + a1) - a0 - a1) / a2
    return res'''

###Lw778---review###
def chl_gons(rhow,coeff=None, bandnames=["band708", "band665", "band779n"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    RM = RRs1 / RRs2
    bb = (1.61 * RRs3) / ((0.82 - 0.6) * RRs3)
    res = (RM * (0.70 + bb) - 0.40 - (bb ** 1.06)) / 0.016
    return res


####Adjusted to MERIS####
def chl_zimba_1_meris (rhow,coeff=None, bandnames=["band665", "band708", "band753"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    res = (1/RRs1 - 1/RRs2) * RRs3
    return res


def chl_zimba_2_meris (rhow, coeff=None, bandnames=["band708", "band753"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    res = (RRs1 / RRs2)
    return res


def chl_gitelson_meris (rhow,coeff=None, bandnames=["band665", "band708", "band753"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    RRs3 = rhow[bandnames[2]]
    res = (1/RRs1 - 1/RRs2) * RRs3
    return res


def chl_gitelson_2 (rhow,coeff=None, bandnames=["band726", "band650"]):
    """
    :param rhow: dictionary containing all bands
    :param coeff: [wavelength, A_lamdba, C_lambda]
    :return: result
    """
    RRs1 = rhow[bandnames[0]]
    RRs2 = rhow[bandnames[1]]
    res = (RRs1 / RRs2)
    return res

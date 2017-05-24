from snappy import ProductData

from c2x.inwater_algorithms import cdom1_syke, cdom2_syke, tsm_syke, tsm_nechad_MERIS_665, tsm_nechad_MERIS_680, \
    tsm_nechad_MERIS_708, tsm_nechad_MERIS_753, tsm_nechad_MERIS_779, tsm_nechad_MERIS_865, tsm_shen_560, tsm_shen_620, \
    tsm_shen_709, tsm_shen_779, tsm_dox_meris, tsm_qiu_meris
#chl_zimba_1_meris, chl_zimba_2_meris, chl_gitelson_meris
#OC3_meris, OC4_meris,chl_clark_meris,chl_gons


MERIS = {
    "Name": "MERIS",
    "wavelengths": [442,490,510, 560, 620, 665, 680, 708, 753, 779, 865],
    #"band442": "reflec_2",
    #"band620": "reflec_6",
    #"band665": "reflec_7",
    #"band708": "reflec_9",

    ##c2rcc_rrs##
    "band442": "rrs_2",
    "band490": "rrs_3",
    "band510": "rrs_4",
    "band560": "rrs_5",
    "band620": "rrs_6",
    "band665": "rrs_7",
    "band680": "rrs_8",
    "band708": "rrs_9",
    "band753": "rrs_10",
    "band779": "rrs_12",
    "band865": "rrs_13",
    ##c3rcc_rhown##
    #"band442n": "rhown_2",
    #"band490n": "rhown_3",
    #"band510n": "rhown_4",
    #"band560n": "rhown_5",
    #"band779n": "rhown_12",

    ##Polymer##,
    #"band442": "Rw442",
    #"band490": "Rw490",
    #"band510": "Rw510",
    #"band560": "Rw560",
    #"band620": "Rw620",
    #"band665": "Rw665",
    #"band753": "Rw754",
    #"band779": "Rw779",
    #"band865": "Rw865",
    ###c2rcc_iop###
    #"iop_apig": "iop_apig",
    #"iop_adet": "iop_adet",
    #"iop_agelb": "iop_agelb",
    #"iop_bpart": "iop_bpart",
    #"iop_bwit": "iop_bwit" ,
    #"iop_adg": "iop_adg",
    #"iop_atot": "iop_atot",
    #"iop_btot": "iop_btot",


    "outputs": [('cdom1_syke', ProductData.TYPE_FLOAT32, cdom1_syke, 'Syke cdom 1', [0.11149, 1.9231, 0.023628],
                ["band708", "band442"]),
                ('cdom2_syke', ProductData.TYPE_FLOAT32, cdom2_syke, 'SYKE cdom 2', [0.29631, 0.78671, 0.060684],
                ["band665", "band442"]),
                ('tsm_syke', ProductData.TYPE_FLOAT32, tsm_syke, 'SYKE TSM', [2566.2, -0.2616], ["band708"]),
                ('tsm_nechad_665', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_665, 'TSM Nechad 1', [352.6, 0.1728],
                 ["band665"]),
                ('tsm_nechad_680', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_680, 'TSM Nechad 2', [406.9, 0.1792],
                 ["band680"]),
                ('tsm_nechad_708', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_708, 'TSM Nechad 3', [537.1, 0.1887],
                 ["band708"]),
                ('tsm_nechad_753', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_753, 'TSM Nechad 4', [1810.8, 0.1997],
                 ["band753"]),
                ('tsm_nechad_779', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_779, 'TSM Nechad 5', [1827.1, 0.2046],
                 ["band779"]),
                ('tsm_nechad_865', ProductData.TYPE_FLOAT32, tsm_nechad_MERIS_865, 'TSM Nechad 6', [3365, 0.2115],
                 ["band865"]),
                ('tsm_shen_560', ProductData.TYPE_FLOAT32, tsm_shen_560, 'TSM Shen 1', [0.0566, 0.0493],
                 ["band560"]),
                ('tsm_shen_620', ProductData.TYPE_FLOAT32, tsm_shen_620, 'TSM Shen 2', [0.09767, 0.0652],
                 ["band620"]),
                ('tsm_shen_709', ProductData.TYPE_FLOAT32, tsm_shen_709, 'TSM Shen 3', [0.18898, 0.076],
                 ["band708"]),
                ('tsm_shen_779', ProductData.TYPE_FLOAT32, tsm_shen_779, 'TSM Shen 4', [0.57099, 0.0904],
                 ["band779"]),
                ('tsm_dox_meris', ProductData.TYPE_FLOAT32, tsm_dox_meris, 'TSM Doxaran', [12.733, 3.2567, 95.883],
                 ["band779", "band560"]),
                ('tsm_qiu_meris', ProductData.TYPE_FLOAT32, tsm_qiu_meris, 'TSM Qiu', [1.932, 0.875],
                 ["band708", "band560"]),
                #('OC3_meris', ProductData.TYPE_FLOAT32, OC3_meris, 'CHL OC3', [0.252, 2.215, 1.519, -0.77, -0.429],
                 #["band442", "band490", "band560"]),
                #('OC4_meris', ProductData.TYPE_FLOAT32, OC4_meris, 'CHL OC4', [0.326, -2.768, 2.442, -1.129, 0.499],
                 #["band442", "band490", "band510", "band560"]),
                #('chl_clark_meris', ProductData.TYPE_FLOAT32, chl_clark_meris, 'CHL Clark', [0.789, -3.926, 11.638, -27.158, 27.937, -10.399],
                #["band442n", "band490n", "band560n"]),
                #('chl_gons', ProductData.TYPE_FLOAT32, chl_gons, 'CHL Gons',["band708", "band665", "band779n"]),
                #('chl_zimba_1_meris', ProductData.TYPE_FLOAT32, chl_zimba_1_meris, 'CHL Zimba 1',[], ["band665", "band708", "band753"]),
                #('chl_zimba_2_meris', ProductData.TYPE_FLOAT32, chl_zimba_2_meris, 'CHL Zimba 2 ',[], ["band708", "band753"]),
                #('chl_gitelson_meris', ProductData.TYPE_FLOAT32, chl_gitelson_meris, 'CHL Gitelson',[], ["band665", "band708", "band753"])
]
}

'''
OLCI = {
    "Name": "OLCI",
    "wavelengths": [442, 490, 510, 560, 620, 665, 673, 681, 708, 754, 779, 865],
    "band442": "rhow_3",
    "band490": "rhow_4",
    "band510": "rhow_5",
    "band560": "rhow_6",
    "band620": "rhow_7",
    "band665": "rhow_8",
    "band673": "rhow_9",
    "band681": "rhow_10",
    "band708": "rhow_11",
    "band754": "rhow_12,
    "band779": "rhow_13",
    "band865": "rhow_14",


    ###c2rcc##

    "outputs": [('cdom1_syke', ProductData.TYPE_FLOAT32, cdom1_syke, 'Syke cdom 1', [0.11149, 1.9231, 0.023628],
                 ["band708", "band442"]),
                ('cdom2_syke', ProductData.TYPE_FLOAT32, cdom2_syke, 'SYKE cdom 2', [0.29631, 0.78671, 0.060684],
                 ["band665", "band442"]),
                ('tsm_syke', ProductData.TYPE_FLOAT32, tsm_syke, 'SYKE TSM', [2566.2, -0.2616], ["band708"])]
     #           ('tsm_nechad', ProductData.TYPE_FLOAT32, tsm_nechad_, 'TSM Nechad', [352.6, 0.1728], ["band665"])]
}

MODIS = {
    "Name": "MODIS",
    "wavelengths": [667, 678],
    "band667": "Rrs_667",
    "band678": "Rrs_678",
    "outputs": [('tsm_nechad', ProductData.TYPE_FLOAT32, tsm_nechad_MODIS_667, 'TSM Nechad', [352.6, 0.1728], ["band667"])]
}

MSI = {
    "Name": "MSI",
    "wavelengths": [443, 490, 560, 665, 705, 740, 783, 865],
    "band443": "rhow_B1",
    "band490": "rhow_B2",
    "band560": "rhow_B3",
    "band665": "rhow_B4",
    "band705": "rhow_B5",
    "band740": "rhow_B6",
    "band783": "rhow_B7",
    "band865": "rhow_B8",
    "outputs": [('cdom1_syke', ProductData.TYPE_FLOAT32, cdom1_syke, 'Syke cdom 1', [0.11149, 1.9231, 0.023628],
                 ["band708", "band442"]),
                ('cdom2_syke', ProductData.TYPE_FLOAT32, cdom2_syke, 'SYKE cdom 2', [0.29631, 0.78671, 0.060684],
                 ["band665", "band442"]),
                ('tsm_syke', ProductData.TYPE_FLOAT32, tsm_syke, 'SYKE TSM', [2566.2, -0.2616], ["band708"]),
                ('tsm_nechad', ProductData.TYPE_FLOAT32, tsm_nechad, 'TSM Nechad', [352.6, 0.1728], ["band665"])]
}

OLI= {
    "Name": "OLI",
    "wavelengths": [442, 620, 665, 708],
    "band442": "reflec_2",
    "band620": "reflec_6",
    "band665": "reflec_7",
    "band708": "reflec_9",
    "outputs": [('cdom1_syke', ProductData.TYPE_FLOAT32, cdom1_syke, 'Syke cdom 1', [0.11149, 1.9231, 0.023628],
                 ["band708", "band442"]),
                ('cdom2_syke', ProductData.TYPE_FLOAT32, cdom2_syke, 'SYKE cdom 2', [0.29631, 0.78671, 0.060684],
                 ["band665", "band442"]),
                ('tsm_syke', ProductData.TYPE_FLOAT32, tsm_syke, 'SYKE TSM', [2566.2, -0.2616], ["band708"]),
                ('tsm_nechad', ProductData.TYPE_FLOAT32, tsm_nechad, 'TSM Nechad', [352.6, 0.1728], ["band665"])]
}'''

Supported_Sensors = [MERIS]

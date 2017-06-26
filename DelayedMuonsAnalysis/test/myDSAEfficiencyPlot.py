#!/usr/bin/env python                                                                                                                                                                                    
intLumi = 2460
cutName = 'reco'
input_sources = [
    {   'condor_dir' : 'NoBPTX2016Data_DSArecoTagAndProbe',
        'dataset' : 'NoBPTX_2016BCDEFGH_23Sep2016_Ntuple',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'NoBPTX 2016 Rereco Data',
        'color' : 'black',
        #'fill' : '',
        'marker' : 'circle',
        },
    {   'condor_dir' : 'CosmicData_CosmicMC80X_DSArecoTagAndProbe',
        'dataset' : 'NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom_Ntuple',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'Cosmic Data',
        'color' : 'blue',
        'fill' : 'hollow', #solid
        'marker' : 'triangle',
        },
    {   'condor_dir' : 'CosmicData_CosmicMC80X_DSArecoTagAndProbe',
        'dataset': 'cosmicMC_0To25Timing_Ntuple_2016_v2',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'Cosmic Simulation, 2016',
        'color' : 'red',
        #'fill' : '',
        'marker' : 'square',
        },
    
]

#!/usr/bin/env python                                                                                                                                                                                    
intLumi = 2460
cutName = 'reco'
input_sources = [
    {   'condor_dir' : 'NoBPTX2015Data_CosmicMC76X_DSArecoTagAndProbe_withoutBackToBack',
        'dataset' : 'NoBPTX_16Dec2015_Ntuple',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'NoBPTX 2015 Rerecoed Data',
        'color' : 'black',
        #'fill' : '',
        'marker' : 'circle',
        },
    {   'condor_dir' : 'NoBPTX2016Data_DSArecoTagAndProbe_withoutBackToBack',
        'dataset' : 'NoBPTX_2016BCDEFGH_23Sep2016_Ntuple',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'NoBPTX 2016 Rerecoed Data',
        'color' : 'red',
        #'fill' : '',
        'marker' : 'circle',
        },
    {   'condor_dir' : 'CosmicData_CosmicMC80X_DSArecoTagAndProbe_withoutBackToBack',
        'dataset' : 'NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom_Ntuple',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'Cosmic Data',
        'color' : 'blue',
        'fill' : 'hollow', #solid
        'marker' : 'circle',
        },
    {   'condor_dir' : 'NoBPTX2015Data_CosmicMC76X_DSArecoTagAndProbe_withoutBackToBack',
        'dataset': 'cosmicMC_0To25Timing_Ntuple_v2',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'Cosmic Simulation, 2015',
        'color' : 'green',
        'fill' : 'hollow',
        'marker' : 'square',
        },
    {   'condor_dir' : 'CosmicData_CosmicMC80X_DSArecoTagAndProbe_withoutBackToBack',
        'dataset': 'cosmicMC_0To25Timing_Ntuple_2016_v2',
        'den_channel' : 'TagAndProbeDen',
        'num_channel' : 'TagAndProbeNum',
        'legend_entry' : 'Cosmic Simulation, 2016',
        'color' : 'purple',
        'fill' : 'hollow',
        'marker' : 'triangle',
        },
    
]
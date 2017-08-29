#!/usr/bin/env python

intLumi = 2460
cutName = 'trigger'
input_sources = [
    {      
        'condor_dir' : 'NoBPTX2017Data_OnlyJetTriggers_TurnOnCurve_29Aug2017',
        'dataset' :   'NoBPTX_2017_PromptReco_OnlyJetTriggers_Ntuple',
        'den_channel' : 'LooseTurnOnDen',
        'num_channel' : 'LooseTurnOnNum40',
        'legend_entry' : 'Run2017, L2Mu40',
        'color' : 'black',
        #'fill' : '',
        'marker' : 'circle',
        },    
    {      
        'condor_dir' : 'NoBPTX2017Data_OnlyJetTriggers_TurnOnCurve_29Aug2017',
        'dataset' :   'NoBPTX_2017_PromptReco_OnlyJetTriggers_Ntuple',
        'den_channel' : 'LooseTurnOnDen',
        'num_channel' : 'LooseTurnOnNum45',
        'legend_entry' : 'Run2017, L2Mu45',
        'color' : 'red',
        #'fill' : '',
        'marker' : 'square',
        },
    
    #{ 
        #'condor_dir' : 'TriggerTurnOn_2016Systematic_2016ReReco',
        #'dataset' :   'cosmicMC_0To25Timing_onlyControlTriggers_Ntuple_2016',
        #'den_channel' : 'LooseTurnOnDen',
        #'num_channel' : 'LooseTurnOnNum40',
        #'legend_entry' : 'Cosmic Simulation, 2016, L2Mu40',
        #'color' : 'green',
        #'fill' : 'hollow',
        #'marker' : 'square',
        #},

]

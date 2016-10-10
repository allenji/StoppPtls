#!/usr/bin/env python                                                                                                                                                                                    
intLumi = 2460
cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'NoBPTX2015Data_TriggerTurnOn',
      'dataset' :   'NoBPTX_16Dec2015_OnlyControlTriggers_Ntuple',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum35',
      'legend_entry' : 'Run2015, L2Mu35',
      'color' : 'black',
      #'fill' : '',
      'marker' : 'circle',
      },
    { 'condor_dir' : 'NoBPTX2015Data_TriggerTurnOn',
      'dataset' :   'NoBPTX_16Dec2015_OnlyControlTriggers_Ntuple',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum40',
      'legend_entry' : 'Run2015, L2Mu40',
      'color' : 'red',
      #'fill' : '',
      'marker' : 'square',
      },
]

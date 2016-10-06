#!/usr/bin/env python                                                                                                                                                                                    
intLumi = 2460
cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'NoBPTX2016Data_TriggerTurnOn',
      'dataset' :   'NoBPTX_2016BCD_PromptReco_OnlyControlTriggers_Ntuple',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum35',
      'legend_entry' : 'Run2016B-D, L2Mu35',
      'color' : 'black',
      #'fill' : '',
      'marker' : 'circle',
      },
    { 'condor_dir' : 'NoBPTX2016Data_TriggerTurnOn',
      'dataset' :   'NoBPTX_2016BCD_PromptReco_OnlyControlTriggers_Ntuple',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum40',
      'legend_entry' : 'Run2016B-D, L2Mu40',
      'color' : 'red',
      #'fill' : '',
      'marker' : 'square',
      },
]

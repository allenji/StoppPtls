#!/usr/bin/env python                                                                                                                                                                                    
intLumi = 2460
cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'TriggerTurnOn_2016Systematic',
      'dataset' :   'cosmicMC_0To25Timing_onlyControlTriggers_Ntuple_2016',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum35',
      'legend_entry' : 'Cosmic Simulation, 2016, L2Mu35',
      'color' : 'blue',
      'fill' : 'hollow',
      'marker' : 'circle',
      },

    { 'condor_dir' : 'TriggerTurnOn_2016Systematic',
      'dataset' :   'NoBPTX_2016BCDEFG_PromptReco_OnlyControlTriggers_Ntuple',
      'den_channel' : 'PreSelectionUpperLowerTurnOnDen',
      'num_channel' : 'PreSelectionUpperLowerTurnOnNum35',
      'legend_entry' : 'Run2016B-G, L2Mu35',
      'color' : 'black',
      #'fill' : '',
      'marker' : 'circle',
      },

]
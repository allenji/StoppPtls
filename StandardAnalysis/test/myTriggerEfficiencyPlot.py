#!/usr/bin/env python

intLumi = 2460
cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'NoBPTX2016Data_Jets_TriggerTurnOn',
      'dataset' :   'NoBPTX_2016BCDEFGH_PromptReco_Jets_OnlyControlTriggers_Ntuple',
      #'dataset' :   'NoBPTX_2016C_PromptReco_Jets_OnlyControlTriggers_Ntuple',
      'den_channel' : 'DenominatorTriggerTurnOnSelection2016',
      'num_channel' : 'NumeratorTriggerTurnOnSelection2016',
      'legend_entry' : 'Run 2016C-G',
      #'legend_entry' : 'Run 2016C',
      'color' : 'black',
      #'fill' : '',
      'marker' : 'circle',
      },

]

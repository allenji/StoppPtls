from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460


config_file = "delayedMuonsCandiate_cosmicMC_2016_cfg.py"
#config_file = "delayedMuonsCandiate_cosmicMC_2016_controlTriggersOnly_cfg.py"
#config_file = "delayedMuonsCandiate_cosmicMC_2016_OnlyJetTriggers_cfg.py"

datasets = [
    #'cosmicMC_0To25Timing_Reco_2016'
    'cosmicMC_0To25Timing_Reco_2016_v2'
]
    
InputCondorArguments = {}

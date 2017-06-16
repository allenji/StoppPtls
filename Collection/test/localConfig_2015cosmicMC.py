from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460


#config_file = "delayedMuonsCandiate_cosmicMC_2015_cfg.py"
#config_file = "delayedMuonsCandiate_cosmicMC_2015_controlTriggersOnly_cfg.py"
config_file = "delayedMuonsCandiate_cosmicMC_2015_OnlyJetTriggers_cfg.py"

datasets = [
    #'cosmicMC_0To25Timing_Reco'
    #'cosmicMC_0To25Timing_Reco_v2'
    'cosmicMC_JetsChannelCosmicPreselection_reco_2015'
]
    
InputCondorArguments = {}

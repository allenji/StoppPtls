from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2830

#config_file = "delayedMuonsCandiate2016_23Sep2016BCDEFGReReco_cfg.py"
config_file = "delayedMuonsCandiate2016_PromptRecoH_cfg.py"

#config_file = "delayedMuonsCandiate_cfg.py"

#config_file = "delayedMuonsCandiate2016_OnlyControlTriggers_cfg.py"

datasets = [
    #"NoBPTX_2016BCDEFG_23Sep2016",
    "NoBPTX_2016H_PromptReco",

    #"NoBPTX_16Dec2015",

    #"NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom",
]
    
InputCondorArguments = {}

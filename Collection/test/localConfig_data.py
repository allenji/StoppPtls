from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2830

config_file = "delayedMuonsCandiate2016_cfg.py"
#config_file = "delayedMuonsCandiate_cfg.py"

datasets = [
    "NoBPTX_2016BCDEFG_PromptReco",
    #"NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom",
    #"NoBPTX_16Dec2015",
    #"NoBPTX_2015BCDE_PromptReco",
]
    
InputCondorArguments = {}

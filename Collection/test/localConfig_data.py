from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2830

config_file = "delayedMuonsCandiate2017_PromptReco_cfg.py"

#config_file = "delayedMuonsCandiate2016_23Sep2016BCDEFGReReco_cfg.py"
#config_file = "delayedMuonsCandiate2016_PromptRecoH_cfg.py"

#config_file = "delayedMuonsCandiate_cfg.py"

#config_file = "delayedMuonsCandiate2016_OnlyControlTriggers_cfg.py"
#config_file = "delayedMuonsCandiate2016_OnlyControlTriggers_23Sep2016BCDEFGReReco_cfg.py"
#config_file = "delayedMuonsCandiate2016_OnlyControlTriggers_PromptRecoH_cfg.py"

#config_file = "delayedMuonsCandiate2016_OnlyJetTriggers_23Sep2016BCDEFGReReco_cfg.py"
#config_file = "delayedMuonsCandiate2016_OnlyJetTriggers_PromptRecoH_cfg.py"

#config_file = "delayedMuonsCandiate_OnlyJetTriggers_cfg.py"

#config_file = "delayedMuonsCandiate2015_ZMuMu_80To100_cfg.py"
#config_file = "delayedMuonsCandiate2016_PromptRecoH_ZMuMu_80To100_cfg.py"

datasets = [
    "NoBPTX_2017_PromptReco_RECO",

    #"NoBPTX_2016BCDEFG_23Sep2016",
    #"NoBPTX_2016H_PromptReco",

    #"NoBPTX_2016H_PromptReco_AOD_v2",
    #"NoBPTX_2016H_PromptReco_AOD_v3",

    #"NoBPTX_16Dec2015",

    #"NoBPTX_2015C_16Dec2015_AOD",
    #"NoBPTX_2015D_16Dec2015_AOD",

    #"NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom",

    #"ZMuSkim_2015D_16Dec2015_RAWRECO",
    #"ZMuSkim_2016H_PromptReco_RAWRECO_v2",
]
    
InputCondorArguments = {}

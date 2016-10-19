from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

config_file = "DelayedMuonsAnalysis.py"
#config_file = "dumpedConfig.py"

datasetsSig = [
    'mchamp100_NtupleSeparateEvents',
    'mchamp600_NtupleSeparateEvents',
    'mchamp1000_NtupleSeparateEvents',
    'mchamp2600_NtupleSeparateEvents',
    
    'gluino100_NtupleSeparateEvents',
    'gluino600_NtupleSeparateEvents',
    'gluino1000_NtupleSeparateEvents',
    'gluino2000_NtupleSeparateEvents',
    'gluino2600_NtupleSeparateEvents',
]

datasetsData = [
    #'NoBPTX_16Dec2015_Ntuple', #2015 rereco

    #'NoBPTX_16Dec2015_OnlyControlTriggers_Ntuple', #2015 rereco with only control triggers
    
    'NoBPTX_2016BCDEFGH_PromptReco_Ntuple', #2016 prompt reco
    #'NoBPTX_2016B_PromptReco_Ntuple', #2016 prompt reco
    #'NoBPTX_2016C_PromptReco_Ntuple', #2016 prompt reco
    #'NoBPTX_2016D_PromptReco_Ntuple', #2016 prompt reco
    #'NoBPTX_2016E_PromptReco_Ntuple', #2016 prompt reco
    
    #'NoBPTX_2016BCDEFGH_PromptReco_OnlyControlTriggers_Ntuple', #2016 prompt reco with only control triggers
    #'NoBPTX_2016B_PromptReco_OnlyControlTriggers_Ntuple', #2016 prompt reco with only control triggers
    #'NoBPTX_2016C_PromptReco_OnlyControlTriggers_Ntuple', #2016 prompt reco with only control triggers
    #'NoBPTX_2016D_PromptReco_OnlyControlTriggers_Ntuple', #2016 prompt reco with only control triggers
    #'NoBPTX_2016F_PromptReco_OnlyControlTriggers_Ntuple', #2016 prompt reco with only control triggers
]

datasetsCosmicData = [
    'NoBPTX_2016DE_PromptReco_Cosmic_TopAndBottom_Ntuple', #2016 top and bottom cosmics
]

datasetsCosmicMC = [
    #'cosmic_preselection',
]

    
datasets = datasetsSig + datasetsData + datasetsCosmicData
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig + datasetsCosmicData
#datasets = datasetsSig
#datasets = datasetsData
#datasets = datasetsCosmicData
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicData + datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}

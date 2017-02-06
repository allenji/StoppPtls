from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

#config_file = "DelayedMuonsAnalysis.py"
#config_file = "dumpedConfig.py"
config_file = "ToyMCRunLbPlotMaking.py"

datasetsSig = [
    #2015 MC
    #'mchamp100_NtupleSeparateEvents',
    #'mchamp200_NtupleSeparateEvents',
    #'mchamp400_NtupleSeparateEvents',
    'mchamp600_NtupleSeparateEvents',
    #'mchamp800_NtupleSeparateEvents',
    #'mchamp1000_NtupleSeparateEvents',
    #'mchamp1400_NtupleSeparateEvents',
    #'mchamp1800_NtupleSeparateEvents',
    #'mchamp2200_NtupleSeparateEvents',
    #'mchamp2600_NtupleSeparateEvents',
    
    #'gluino100_NtupleSeparateEvents',
    #'gluino200_NtupleSeparateEvents',
    #'gluino400_NtupleSeparateEvents',
    #'gluino600_NtupleSeparateEvents',
    #'gluino800_NtupleSeparateEvents',
    'gluino1000_NtupleSeparateEvents',
    #'gluino1200_NtupleSeparateEvents',
    #'gluino1400_NtupleSeparateEvents',
    #'gluino1600_NtupleSeparateEvents',
    #'gluino1800_NtupleSeparateEvents',
    #'gluino2000_NtupleSeparateEvents',
    #'gluino2200_NtupleSeparateEvents',
    #'gluino2400_NtupleSeparateEvents',
    #'gluino2600_NtupleSeparateEvents',

    #2016 MC
    #'mchamp100_NtupleSeparateEvents_2016',
    #'mchamp200_NtupleSeparateEvents_2016',
    #'mchamp400_NtupleSeparateEvents_2016',
    #'mchamp600_NtupleSeparateEvents_2016',
    #'mchamp800_NtupleSeparateEvents_2016',
    #'mchamp1000_NtupleSeparateEvents_2016',
    #'mchamp1400_NtupleSeparateEvents_2016',
    #'mchamp1800_NtupleSeparateEvents_2016',
    #'mchamp2200_NtupleSeparateEvents_2016',
    #'mchamp2600_NtupleSeparateEvents_2016',
    
    #'gluino100_NtupleSeparateEvents_2016',
    #'gluino200_NtupleSeparateEvents_2016',
    #'gluino400_NtupleSeparateEvents_2016',
    #'gluino600_NtupleSeparateEvents_2016',
    #'gluino800_NtupleSeparateEvents_2016',
    #'gluino1000_NtupleSeparateEvents_2016',
    #'gluino1200_NtupleSeparateEvents_2016',
    #'gluino1400_NtupleSeparateEvents_2016',
    #'gluino1600_NtupleSeparateEvents_2016',
    #'gluino1800_NtupleSeparateEvents_2016',
    #'gluino2000_NtupleSeparateEvents_2016',
    #'gluino2200_NtupleSeparateEvents_2016',
    #'gluino2400_NtupleSeparateEvents_2016',
    #'gluino2600_NtupleSeparateEvents_2016',
]

datasetsData = [
    #'NoBPTX_16Dec2015_Ntuple', #2015 rereco

    #'NoBPTX_16Dec2015_OnlyControlTriggers_Ntuple', #2015 rereco with only control triggers
    
    'NoBPTX_2016BCDEFGH_23Sep2016_Ntuple', #2016 rereco
    
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
    'cosmicMC_0To25Timing_Ntuple',
    #'cosmicMC_0To25Timing_Ntuple_2016',

    #'cosmicMC_0To25Timing_onlyControlTriggers_Ntuple',
    #'cosmicMC_0To25Timing_onlyControlTriggers_Ntuple_2016',
]

    
#datasets = datasetsSig + datasetsData + datasetsCosmicData + datasetsCosmicMC
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig + datasetsCosmicData
#datasets = datasetsSig
datasets = datasetsData
#datasets = datasetsCosmicData
#datasets = datasetsCosmicMC
#datasets = datasetsCosmicMC + datasetsData
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicData + datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}
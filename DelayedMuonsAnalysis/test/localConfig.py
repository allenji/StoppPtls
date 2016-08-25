from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

config_file = "DelayedMuonsAnalysis.py"
#config_file = "dumpedConfig.py"

datasetsSig = [
    'mchamp600_NtupleSeparateEvents',
    'gluino2000_NtupleSeparateEvents',
]

datasetsData = [
   'NoBPTX_16Dec2015_Ntuple', #2015 rereco
   'NoBPTX_2016BCDEFG_PromptReco_Ntuple', #2016 prompt reco
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

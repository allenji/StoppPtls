from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

config_file = "DelayedMuonsAnalysis.py"

datasetsSig = [
    'mchamp600_NtupleSeparateEventsParticle0',
]

datasetsData = [
   'NoBPTX_16Dec2015_Ntuple',
]

datasetsCosmicData = [
    'NoBPTX_2015BCDE_PromptReco_Cosmic_Ntuple',
]

datasetsCosmicMC = [
    #'cosmic_preselection',
]

    
#datasets = datasetsSig + datasetsData + datasetsCosmicData
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig
#datasets = datasetsData
datasets = datasetsCosmicData
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicData + datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsCosmicMC + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}

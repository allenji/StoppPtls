from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

#config_file = "SecondJetAnalysis.py"
config_file = "StoppedParticlesAnalysis.py"

datasetsSig = [
  'GluinoToUUbarChi0_1200_200',
  'GluinoToUUbarChi0_1200_600',
  'GluinoToUUbarChi0_1200_1000',
  'GluinoToGChi0_1200_200',
  'GluinoToGChi0_1200_400',
  'GluinoToGChi0_1200_600',
  'GluinoToGChi0_1200_800',
  'GluinoToGChi0_1200_1000',
]

datasetsData = [
  'NoBPTX_2015D_v3',
  'NoBPTX_2015D_v4',
]

#datasets = datasetsSig + datasetsData
#datasets = datasetsSig
datasets = datasetsData

InputCondorArguments = {}

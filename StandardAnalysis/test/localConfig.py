from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

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
  'NoBPTX_2015D',
]

#data control sample
datasetsControl = [
    'StpPtls_controlSample_2015',
]

#cosmic MC with MET with pt>15GeV, a barrel jet, and 0 cscSegments
datasetsCosmic = [
    'cosmic_preselection',
]

datasetsSig_2BodyDecay = [
    'GluinoToGChi0_1200_200',
    'GluinoToGChi0_1200_400',
    'GluinoToGChi0_1200_600',
    'GluinoToGChi0_1200_800',
    'GluinoToGChi0_1200_1000',
]
    
#datasets = datasetsSig + datasetsData + datasetsControl
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig
#datasets = datasetsData
#datasets = datasetsControl
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsControl + datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsDummy

InputCondorArguments = {}

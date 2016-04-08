from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

#config_file = "CosmicBackground.py"
config_file = "HaloBackground.py"

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
    #'NoBPTX_2015Dv3_controlSample',
    #'NoBPTX_2015Dv4_controlSample'
]

#cosmic MC with MET with pt>15GeV, a barrel jet, and 0 cscSegments
datasetsCosmic = [
    'cosmic_preselection',
]

datasetsSig_2BodyDecay = [
    'GluinoToGChi0_1200_200',
    'GluinoToGChi0_1200_1000',
]

datasetsRpcStudy = [
    'GluinoToGChi0_1200_1000_noiseFrate0p4',
    'GluinoToGChi0_1200_1000_noiseFrate0p6',
    'GluinoToGChi0_1200_1000_noiseFrate0p8',
    'GluinoToGChi0_1200_1000_noiseFrate1p0',
    'GluinoToGChi0_1200_1000_nonoise',
]
    
#datasets = datasetsSig + datasetsData + datasetsControl
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig
datasets = datasetsData
#datasets = datasetsControl
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsControl + datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}

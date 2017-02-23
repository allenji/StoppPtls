from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

config_file = "CosmicBackground_2016.py"

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

datasetsEnergyScanG600 = [
    'GluinoToGChi0_600_309',
    'GluinoToGChi0_600_354',
    'GluinoToGChi0_600_424',
    'GluinoToGChi0_600_483',
    'GluinoToGChi0_600_495',
    'GluinoToGChi0_600_507',
    'GluinoToGChi0_600_519',
    'GluinoToGChi0_600_547',
]
datasetsEnergyScanG1200 = [
    'GluinoToGChi0_1200_848',
    'GluinoToGChi0_1200_903',
    'GluinoToGChi0_1200_954',
    'GluinoToGChi0_1200_997',
    'GluinoToGChi0_1200_1044',
    'GluinoToGChi0_1200_1089',
    'GluinoToGChi0_1200_1100',
    'GluinoToGChi0_1200_1111',
    'GluinoToGChi0_1200_1122',
    'GluinoToGChi0_1200_1148',
]
datasetsEnergyScanG1800 = [
    'GluinoToGChi0_1800_1047',
    'GluinoToGChi0_1800_1122',
    'GluinoToGChi0_1800_1200',
    'GluinoToGChi0_1800_1272',
    'GluinoToGChi0_1800_1341',
    'GluinoToGChi0_1800_1407',
    'GluinoToGChi0_1800_1469',
    'GluinoToGChi0_1800_1529',
]
datasetsEnergyScanS400 = [
    'StopToTChi0_400_75',
    'StopToTChi0_400_150',
    'StopToTChi0_400_199',
    'StopToTChi0_400_250',
    'StopToTChi0_400_285',
    'StopToTChi0_400_300',
]
datasetsEnergyScanS600 = [
    'StopToTChi0_600_100',
    'StopToTChi0_600_300',
    'StopToTChi0_600_400',
    'StopToTChi0_600_500',
]
datasetsEnergyScanS1000 = [
    'StopToTChi0_1000_100',
    'StopToTChi0_1000_173',
    'StopToTChi0_1000_360',
    'StopToTChi0_1000_480',
    'StopToTChi0_1000_574',
    'StopToTChi0_1000_656',
    'StopToTChi0_1000_728',
]

datasetsData = [
  #'NoBPTX_2015D',
  'NoBPTX_Jet_2016BCD_ReReco'
  #'NoBPTX_Jet_2016BCDEFGH_ReReco'
]

#data control sample
datasetsControl = [
    'StpPtls_controlSample_2015',
]

datasetsCommissioning = [
    'Commissioning2015_controlSample',
]
datasetsControlAllDatasets = [
    'Commissioning2015_controlSample',
    'NoBPTX_2015B_controlSample',
    'NoBPTX_2015C_controlSample',
]
datasetsAdditionalControlDatasets = [
    'NoBPTX_2015Dv3_controlSample',
    'NoBPTX_2015Dv4_controlSample',
]
datasetsSearchAllDatasets = [
    'NoBPTX_2015D_v3',
    'NoBPTX_2015D_v4',
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
#    'GluinoToGChi0_1200_1000_noiseFrate0p4',
    'GluinoToGChi0_1200_1000_noiseFrate0p6',
#    'GluinoToGChi0_1200_1000_noiseFrate0p7',
    'GluinoToGChi0_1200_1000_noiseFrate0p8',
    'GluinoToGChi0_1200_1000_noiseFrate1p0',
#    'GluinoToGChi0_1200_1000_nonoise',
    'GluinoToGChi0_1200_200',
]
    
#datasets = datasetsSig + datasetsData + datasetsControl
#datasets = datasetsSig + datasetsData
#datasets = datasetsSig
#datasets = datasetsData + datasetsEnergyScanS600
#datasets = datasetsAdditionalControlDatasets
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsControl + datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy
#datasets = datasetsControl + datasetsRpcStudy
#datasets = datasetsCommissioning
#datasets = datasetsRpcStudy + datasetsCosmic
#datasets = datasetsCosmic
#datasets = datasetsControlAllDatasets
#datasets = datasetsSearchAllDatasets
#datasets = ['GluinoToGChi0_1200_1000']
#datasets = ['cosmic_preselection']
#datasets = datasetsRpcStudy
#datasets = datasetsControlAllDatasets + datasetsAdditionalControlDatasets
#datasets = ['NoBPTX_2015Dv4_controlSample']
#datasets = ['NoBPTX_2015B_controlSample']
#datasets = datasetsControl
#datasets = datasetsAdditionalControlDatasets
#datasets = datasetsEnergyScanG600
#datasets = datasetsEnergyScanS400
#datasets = datasetsData + datasetsEnergyScanG1200
datasets = datasetsData
#datasets = ['NoBPTX_2015D_v4']

InputCondorArguments = {}

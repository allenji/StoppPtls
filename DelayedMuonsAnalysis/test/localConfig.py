from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

#config_file = "SecondJetAnalysis.py"
config_file = "StoppedParticlesAnalysis.py"

datasetsSig = [
    'mchamp600',
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

    
#datasets = datasetsSig + datasetsData + datasetsControl
#datasets = datasetsSig + datasetsData
datasets = datasetsSig
#datasets = datasetsData
#datasets = datasetsControl
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsControl + datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}

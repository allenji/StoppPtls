from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

#config_file = "SecondJetAnalysis.py"
#config_file = "StoppedParticlesAnalysis.py"
config_file = "StoppedParticlesAnalysis_2016.py"

datasetsSig = [
    #'Stop2TChi0_400_214_2016Run2_80x',
    #'Stop2TChi0_600_417_2016Run2_80x',
    #'Stop2TChi0_1200_1018_2016Run2_80x',
    #'Gluino2GChi0_600_489_2016Run2_80x',
    #'Gluino2GChi0_1200_1095_2016Run2_80x',
    #'Gluino2GChi0_1800_1697_2016Run2_80x',
    'GluinoToQQbarChi0_1800_1325_2016Simulation',
    'GluinoToQQbarChi0_1000_100_2016Simulation',

  #'GluinoToUUbarChi0_1200_200',
  #'GluinoToUUbarChi0_1200_600',
  #'GluinoToUUbarChi0_1200_1000',
  #'GluinoToGChi0_1200_200',
  #'GluinoToGChi0_1200_400',
  #'GluinoToGChi0_1200_600',
  #'GluinoToGChi0_1200_800',
  #'GluinoToGChi0_1200_1000',
]

datasetsData = [
    #'NoBPTX_2015D',
    #'NoBPTX_Jet_2016BCD_PromptReco'
    #'NoBPTX_Jet_2016FG_PromptReco'
    #'NoBPTX_2016B_PromptReco_Jets_BxStudy_Ntuple',
    #'NoBPTX_2016D_PromptReco_Jets_BxStudy_Ntuple',
    #'NoBPTX_2016BCDEFGH_PromptReco_Jets_OnlyControlTriggers_Ntuple',
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
datasets = datasetsSig
#datasets = datasetsData
#datasets = datasetsControl
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsControl + datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsCosmic + datasetsSig_2BodyDecay
#datasets = datasetsDummy
#datasets = datasetsData + datasetsRpcStudy

InputCondorArguments = {}

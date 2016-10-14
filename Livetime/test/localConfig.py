from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

#config_file = "getLivetime_cfg.py"
config_file = "getLivetime_2016_cfg.py"


datasetsData = [
    #'NoBPTX_2015D',
    #'NoBPTX_2015D_v3',
    #'NoBPTX_2015D_v4'
    'NoBPTX_Jet_2016FG_PromptReco'
    ]

#data control sample
datasetsControl = [
    #'StpPtls_controlSample_2015',
    'Commissioning2015_controlSample',
    'NoBPTX_2015B_controlSample',
    'NoBPTX_2015C_controlSample',
    'NoBPTX_2015Dv3_controlSample',
    'NoBPTX_2015Dv4_controlSample'
]
    
#datasets = datasetsData + datasetsControl
datasets = datasetsData
#datasets = datasetsControl

InputCondorArguments = {}

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.GENSIMSamples import *

intLumi = 2460

config_file = "stage2GENSIM_mchampXXX_separateEvents_particle0_cfg.py"
#config_file = "stage2GENSIM_mchampXXX_separateEvents_particle1_cfg.py"
#config_file = "stage2GENSIM_mchampXXX_sameEvent_cfg.py"

datasets = [
    #'mchamp100',
    #'mchamp200',
    #'mchamp400',
    'mchamp600',
    #'mchamp800',
    #'mchamp1000',
    #'mchamp1400',
    #'mchamp1800',
    #'mchamp2200',
    #'mchamp2600',
]
    
InputCondorArguments = {}

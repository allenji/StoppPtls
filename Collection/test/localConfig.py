from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460

config_file = "delayedMuonsCandiate_MC_cfg.py"

datasets = [
    #'mchamp100_RecoSeparateEventsParticle0',
    #'mchamp200_RecoSeparateEventsParticle0',
    #'mchamp400_RecoSeparateEventsParticle0',
    #'mchamp600_RecoSeparateEventsParticle0',
    #'mchamp800_RecoSeparateEventsParticle0',
    #'mchamp1000_RecoSeparateEventsParticle0',
    #'mchamp1400_RecoSeparateEventsParticle0',
    #'mchamp1800_RecoSeparateEventsParticle0',
    #'mchamp2200_RecoSeparateEventsParticle0',
    #'mchamp2600_RecoSeparateEventsParticle0',

    #'mchamp100_RecoSeparateEventsParticle1',
    #'mchamp200_RecoSeparateEventsParticle1',
    #'mchamp400_RecoSeparateEventsParticle1',
    #'mchamp600_RecoSeparateEventsParticle1',
    #'mchamp800_RecoSeparateEventsParticle1',
    #'mchamp1000_RecoSeparateEventsParticle1',
    #'mchamp1400_RecoSeparateEventsParticle1',
    #'mchamp1800_RecoSeparateEventsParticle1',
    #'mchamp2200_RecoSeparateEventsParticle1',
    #'mchamp2600_RecoSeparateEventsParticle1',

    #'gluino100_RecoSeparateEventsParticle0',
    #'gluino200_RecoSeparateEventsParticle0',
    #'gluino400_RecoSeparateEventsParticle0',
    #'gluino600_RecoSeparateEventsParticle0',
    #'gluino800_RecoSeparateEventsParticle0',
    #'gluino1000_RecoSeparateEventsParticle0', 
    #'gluino1200_RecoSeparateEventsParticle0', 
    #'gluino1400_RecoSeparateEventsParticle0', 
    #'gluino1600_RecoSeparateEventsParticle0', 
    #'gluino1800_RecoSeparateEventsParticle0', 
    #'gluino2000_RecoSeparateEventsParticle0', 
    #'gluino2200_RecoSeparateEventsParticle0',  
    #'gluino2400_RecoSeparateEventsParticle0',  
    #'gluino2600_RecoSeparateEventsParticle0', 

    #'gluino100_RecoSeparateEventsParticle1',
    #'gluino200_RecoSeparateEventsParticle1',
    #'gluino400_RecoSeparateEventsParticle1',
    #'gluino600_RecoSeparateEventsParticle1',
    #'gluino800_RecoSeparateEventsParticle1',
    #'gluino1000_RecoSeparateEventsParticle1', 
    #'gluino1200_RecoSeparateEventsParticle1', 
    #'gluino1400_RecoSeparateEventsParticle1', 
    #'gluino1600_RecoSeparateEventsParticle1', 
    #'gluino1800_RecoSeparateEventsParticle1', 
    'gluino2000_RecoSeparateEventsParticle1', 
    #'gluino2200_RecoSeparateEventsParticle1',  
    #'gluino2400_RecoSeparateEventsParticle1',  
    #'gluino2600_RecoSeparateEventsParticle1', 
]
    
InputCondorArguments = {}

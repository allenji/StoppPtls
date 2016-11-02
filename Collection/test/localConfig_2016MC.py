from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RECOSamples import *

intLumi = 2460


config_file = "delayedMuonsCandiate_2016MC_cfg.py"

datasets = [
    'mchamp100_RecoSeparateEventsParticle0_2016',
    'mchamp200_RecoSeparateEventsParticle0_2016',
    'mchamp400_RecoSeparateEventsParticle0_2016',
    'mchamp600_RecoSeparateEventsParticle0_2016',
    'mchamp800_RecoSeparateEventsParticle0_2016',
    'mchamp1000_RecoSeparateEventsParticle0_2016',
    'mchamp1400_RecoSeparateEventsParticle0_2016',
    'mchamp1800_RecoSeparateEventsParticle0_2016',
    'mchamp2200_RecoSeparateEventsParticle0_2016',
    'mchamp2600_RecoSeparateEventsParticle0_2016',

    'mchamp100_RecoSeparateEventsParticle1_2016',
    'mchamp200_RecoSeparateEventsParticle1_2016',
    'mchamp400_RecoSeparateEventsParticle1_2016',
    'mchamp600_RecoSeparateEventsParticle1_2016',
    'mchamp800_RecoSeparateEventsParticle1_2016',
    'mchamp1000_RecoSeparateEventsParticle1_2016',
    'mchamp1400_RecoSeparateEventsParticle1_2016',
    'mchamp1800_RecoSeparateEventsParticle1_2016',
    'mchamp2200_RecoSeparateEventsParticle1_2016',
    'mchamp2600_RecoSeparateEventsParticle1_2016',

    'gluino100_RecoSeparateEventsParticle0_2016',
    'gluino200_RecoSeparateEventsParticle0_2016',
    'gluino400_RecoSeparateEventsParticle0_2016',
    'gluino600_RecoSeparateEventsParticle0_2016',
    'gluino800_RecoSeparateEventsParticle0_2016',
    'gluino1000_RecoSeparateEventsParticle0_2016', 
    'gluino1200_RecoSeparateEventsParticle0_2016', 
    'gluino1400_RecoSeparateEventsParticle0_2016', 
    'gluino1600_RecoSeparateEventsParticle0_2016', 
    'gluino1800_RecoSeparateEventsParticle0_2016', 
    'gluino2000_RecoSeparateEventsParticle0_2016', 
    'gluino2200_RecoSeparateEventsParticle0_2016',  
    'gluino2400_RecoSeparateEventsParticle0_2016',  
    'gluino2600_RecoSeparateEventsParticle0_2016', 

    'gluino100_RecoSeparateEventsParticle1_2016',
    'gluino200_RecoSeparateEventsParticle1_2016',
    'gluino400_RecoSeparateEventsParticle1_2016',
    'gluino600_RecoSeparateEventsParticle1_2016',
    'gluino800_RecoSeparateEventsParticle1_2016',
    'gluino1000_RecoSeparateEventsParticle1_2016', 
    'gluino1200_RecoSeparateEventsParticle1_2016', 
    'gluino1400_RecoSeparateEventsParticle1_2016', 
    'gluino1600_RecoSeparateEventsParticle1_2016', 
    'gluino1800_RecoSeparateEventsParticle1_2016', 
    'gluino2000_RecoSeparateEventsParticle1_2016', 
    'gluino2200_RecoSeparateEventsParticle1_2016',  
    'gluino2400_RecoSeparateEventsParticle1_2016',  
    'gluino2600_RecoSeparateEventsParticle1_2016', 

]
    
InputCondorArguments = {}

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RAWSIMSamples import *

intLumi = 2460

config_file = "stage2RECO_2016.py"

datasets = [
    'mchamp100_DigiHltSeparateEventsParticle0_2016',
    'mchamp200_DigiHltSeparateEventsParticle0_2016',
    'mchamp400_DigiHltSeparateEventsParticle0_2016',
    'mchamp600_DigiHltSeparateEventsParticle0_2016',
    'mchamp800_DigiHltSeparateEventsParticle0_2016',
    'mchamp1000_DigiHltSeparateEventsParticle0_2016',
    'mchamp1400_DigiHltSeparateEventsParticle0_2016',
    'mchamp1800_DigiHltSeparateEventsParticle0_2016',
    'mchamp2200_DigiHltSeparateEventsParticle0_2016',
    'mchamp2600_DigiHltSeparateEventsParticle0_2016',

    'mchamp100_DigiHltSeparateEventsParticle1_2016',
    'mchamp200_DigiHltSeparateEventsParticle1_2016',
    'mchamp400_DigiHltSeparateEventsParticle1_2016',
    'mchamp600_DigiHltSeparateEventsParticle1_2016',
    'mchamp800_DigiHltSeparateEventsParticle1_2016',
    'mchamp1000_DigiHltSeparateEventsParticle1_2016',
    'mchamp1400_DigiHltSeparateEventsParticle1_2016',
    'mchamp1800_DigiHltSeparateEventsParticle1_2016',
    'mchamp2200_DigiHltSeparateEventsParticle1_2016',
    'mchamp2600_DigiHltSeparateEventsParticle1_2016',

    'gluino100_DigiHltSeparateEventsParticle0_2016',
    'gluino200_DigiHltSeparateEventsParticle0_2016',
    'gluino400_DigiHltSeparateEventsParticle0_2016',
    'gluino600_DigiHltSeparateEventsParticle0_2016',
    'gluino800_DigiHltSeparateEventsParticle0_2016',
    'gluino1000_DigiHltSeparateEventsParticle0_2016',
    'gluino1200_DigiHltSeparateEventsParticle0_2016',
    'gluino1400_DigiHltSeparateEventsParticle0_2016',
    'gluino1600_DigiHltSeparateEventsParticle0_2016',
    'gluino1800_DigiHltSeparateEventsParticle0_2016',
    'gluino2000_DigiHltSeparateEventsParticle0_2016',
    'gluino2200_DigiHltSeparateEventsParticle0_2016',
    'gluino2400_DigiHltSeparateEventsParticle0_2016',
    'gluino2600_DigiHltSeparateEventsParticle0_2016',

    'gluino100_DigiHltSeparateEventsParticle1_2016',
    'gluino200_DigiHltSeparateEventsParticle1_2016',
    'gluino400_DigiHltSeparateEventsParticle1_2016',
    'gluino600_DigiHltSeparateEventsParticle1_2016',
    'gluino800_DigiHltSeparateEventsParticle1_2016',
    'gluino1000_DigiHltSeparateEventsParticle1_2016',
    'gluino1200_DigiHltSeparateEventsParticle1_2016',
    'gluino1400_DigiHltSeparateEventsParticle1_2016',
    'gluino1600_DigiHltSeparateEventsParticle1_2016',
    'gluino1800_DigiHltSeparateEventsParticle1_2016',
    'gluino2000_DigiHltSeparateEventsParticle1_2016',
    'gluino2200_DigiHltSeparateEventsParticle1_2016',
    'gluino2400_DigiHltSeparateEventsParticle1_2016',
    'gluino2600_DigiHltSeparateEventsParticle1_2016',
]
    
InputCondorArguments = {}

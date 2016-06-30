from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.RAWSIMSamples import *

intLumi = 2460

config_file = "stage2RECO.py"

datasets = [
    #'mchamp100_DigiHltSeparateEventsParticle0',
    #'mchamp200_DigiHltSeparateEventsParticle0',
    #'mchamp400_DigiHltSeparateEventsParticle0',
    #'mchamp600_DigiHltSeparateEventsParticle0',
    #'mchamp800_DigiHltSeparateEventsParticle0',
    #'mchamp1000_DigiHltSeparateEventsParticle0',
    #'mchamp1400_DigiHltSeparateEventsParticle0',
    #'mchamp1800_DigiHltSeparateEventsParticle0',
    #'mchamp2200_DigiHltSeparateEventsParticle0',
    #'mchamp2600_DigiHltSeparateEventsParticle0',

    #'gluino100_DigiHltSeparateEventsParticle0',
    #'gluino200_DigiHltSeparateEventsParticle0',
    #'gluino400_DigiHltSeparateEventsParticle0',
    #'gluino600_DigiHltSeparateEventsParticle0',
    #'gluino800_DigiHltSeparateEventsParticle0',
    #'gluino1000_DigiHltSeparateEventsParticle0'
    #'gluino1200_DigiHltSeparateEventsParticle0'
    #'gluino1400_DigiHltSeparateEventsParticle0'
    #'gluino1600_DigiHltSeparateEventsParticle0'
    #'gluino1800_DigiHltSeparateEventsParticle0'
    'gluino2000_DigiHltSeparateEventsParticle0',
    #'gluino2200_DigiHltSeparateEventsParticle0',
    #'gluino2400_DigiHltSeparateEventsParticle0',
    #'gluino2600_DigiHltSeparateEventsParticle0',
]
    
InputCondorArguments = {}

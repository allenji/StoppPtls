mass_mchamp = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
mass_mchamp_runLimits = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
#mass_mchamp_runLimits = [100, 200]

mass_gluino = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mass_gluino_runLimits = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]

mchamp_stopEff = [0.33, 0.29, 0.28, 0.25, 0.30, 0.32, 0.35, 0.41, 0.48, 0.54]
gluino_stopEff = [0.19, 0.17, 0.17, 0.17, 0.18, 0.20, 0.21, 0.22, 0.23, 0.25, 0.25, 0.26]

mchamp_reco_2015 = [0.0051, 0.044, 0.050, 0.048, 0.041, 0.039, 0.038, 0.031, 0.031, 0.030]
gluino_reco_2015 = [0.0019, 0.0025, 0.0046, 0.0031, 0.0033, 0.0039, 0.0033, 0.0030, 0.0025, 0.0033, 0.0030, 0.0033]
mchamp_reco_2016 = [0.0059, 0.041, 0.045, 0.042, 0.038, 0.035, 0.032, 0.027, 0.026, 0.026]
gluino_reco_2016 = [0.0015, 0.0024, 0.0037, 0.0029, 0.0025, 0.0031, 0.0029, 0.0023, 0.0020, 0.0028, 0.0025, 0.0025]

mchamp2015ToyMC = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/2015/toymc.txt"
gluino2015ToyMC = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/2015/toymc.txt"
mchamp2015Params = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/2015/parameters.txt"
gluino2015Params = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/2015/parameters.txt"

mchamp2016ToyMC = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/2016/toymc.txt"
gluino2016ToyMC = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/2016/toymc.txt"
mchamp2016Params = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/2016/parameters.txt"
gluino2016Params = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/2016/parameters.txt"

combine = 'True'
year = '2016'
onlyOneSec = 'True'

bkg_list = ['bkg']
# currently lnN only, parameters in the list are in the order: central estimate, stat. error, syst. error
bkg_estimate_2015 = {'bkg':['lnN', 0.0400022 , 0.0, 0.03], 'total': 0.0400022 }
bkg_estimate_2016 = {'bkg':['lnN', 0.500099  , 0.02, 0.40], 'total': 0.500099  }

effLumi_2016 = 13673.9
effLumi_2015 = 0

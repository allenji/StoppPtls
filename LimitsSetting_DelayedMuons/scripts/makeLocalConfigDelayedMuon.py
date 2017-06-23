############# Parameter Setting #############
#mass_mchamp = [100, 200, 400, 600, 800, 1000, 1800, 2600]
mass_mchamp = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
#mass_mchamp_ref2015 = [100, 200, 400, 600, 800, 1000, 1400, 1400, 1400, 1400]
#mass_mchamp_ref2016 = [100, 200, 400, 600, 800, 1000, 1000, 1800, 1800, 2600]
mass_gluino = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
#mass_gluino_ref2015 = [400, 600, 600, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000]
#mass_gluino_ref2016 = [400, 600, 600, 1000, 1200, 1200, 1600, 1800, 2000, 2000, 2400, 2400]

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

outputdir = "nimei"
combine = 'True'
year = '2016'
onlyOneSec = 'True'

bkg_list = ['bkg']
# currently lnN only, parameters in the list are in the order: central estimate, stat. error, syst. error
bkg_estimate_2015 = {'bkg':['lnN', 0.0400022 , 0.0, 0.03], 'total': 0.0400022 }
bkg_estimate_2016 = {'bkg':['lnN', 0.500099  , 0.02, 0.40], 'total': 0.500099  }


############# MAIN PART #############
import os
import sys
if os.path.exists(outputdir):
    print "Output directory already exists, aborting...."
    sys.exit(0)
else:
    os.mkdir(outputdir)

mchamp_sigEff_2015 = []
gluino_sigEff_2015 = []
mchamp_sigEff_2016 = []
gluino_sigEff_2016 = []
for i in range(0, len(mass_mchamp)):
    mchamp_sigEff_2015.append(mchamp_stopEff[i]*mchamp_reco_2015[i])
    mchamp_sigEff_2016.append(mchamp_stopEff[i]*mchamp_reco_2016[i])
for i in range(0, len(mass_gluino)):
    gluino_sigEff_2015.append(gluino_stopEff[i]*gluino_reco_2015[i])
    gluino_sigEff_2016.append(gluino_stopEff[i]*gluino_reco_2016[i])

for mmchamp in mass_mchamp:
    
    if not os.path.isfile(mchamp2015ToyMC):
        print mchamp2015ToyMC + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(mchamp2016ToyMC):
        print mchamp2016ToyMC + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(mchamp2015Params):
        print mchamp2015Params + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(mchamp2016Params):
        print mchamp2016Params + "doesn't exist, shame on you!"
        sys.exit(0)
    
    os.system("rm -rf "+outputdir+"/"+"localConfig_DMMchampCombined_"+str(mmchamp)+".py")
    localConfig = open(outputdir+"/"+"localConfig_DMMchampCombined_"+str(mmchamp)+".py", "w")
    localConfig.write("combine = %s\n\n"%(combine))
    localConfig.write("year = %s\n\n"%(year))
    localConfig.write("onlyOneSec = %s\n\n"%(onlyOneSec))

    localConfig.write("toymc1 = '"+mchamp2015ToyMC+"'\n")
    localConfig.write("toymc2 = '"+mchamp2016ToyMC+"'\n")
    localConfig.write("toymc = [toymc1, toymc2]\n\n")
    localConfig.write("param1 = '"+mchamp2015Params+"'\n")
    localConfig.write("param2 = '"+mchamp2016Params+"'\n")
    localConfig.write("param = [param1, param2]\n\n")
    localConfig.write("signal_eff = [%-15f, %-15f]\n\n"%(mchamp_sigEff_2015[mass_mchamp.index(mmchamp)], mchamp_sigEff_2016[mass_mchamp.index(mmchamp)]))

    localConfig.write('dataset_name = "DelayedMuonCombineMchamp'+ str(mmchamp)+'"\n\n')
    localConfig.write("bkg = %s\n"%(bkg_list))
    localConfig.write("bkg_estimate_1 = %s\n"%(bkg_estimate_2015))
    localConfig.write("bkg_estimate_2 = %s\n"%(bkg_estimate_2016))
    localConfig.close()

for mgluino in mass_gluino:

    if not os.path.isfile(gluino2015ToyMC):
        print gluino2015ToyMC + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(gluino2016ToyMC):
        print gluino2016ToyMC + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(gluino2015Params):
        print gluino2015Params + "doesn't exist, shame on you!"
        sys.exit(0)
    if not os.path.isfile(gluino2016Params):
        print gluino2016Params + "doesn't exist, shame on you!"
        sys.exit(0)
    os.system("rm -rf "+outputdir+"/"+"localConfig_DMGluinoCombined_"+str(mgluino)+".py")
    localConfig = open(outputdir+"/"+"localConfig_DMGluinoCombined_"+str(mgluino)+".py", "w")
    localConfig.write("combine = %s\n\n"%(combine))
    localConfig.write("year = %s\n\n"%(year))
    localConfig.write("onlyOneSec = %s\n\n"%(onlyOneSec))
    localConfig.write("toymc1 = '"+gluino2015ToyMC+"'\n")
    localConfig.write("toymc2 = '"+gluino2016ToyMC+"'\n")
    localConfig.write("toymc = [toymc1, toymc2]\n\n")
    localConfig.write("param1 = '"+gluino2015Params+"'\n")
    localConfig.write("param2 = '"+gluino2016Params+"'\n")
    localConfig.write("param = [param1, param2]\n\n")
    localConfig.write("signal_eff = [%-15f, %-15f]\n\n"%(gluino_sigEff_2015[mass_gluino.index(mgluino)], gluino_sigEff_2016[mass_gluino.index(mgluino)]))

    localConfig.write('dataset_name = "DelayedMuonCombineGluino'+ str(mgluino)+'"\n\n')
    localConfig.write("bkg = %s\n"%(bkg_list))
    localConfig.write("bkg_estimate_1 = %s\n"%(bkg_estimate_2015))
    localConfig.write("bkg_estimate_2 = %s\n"%(bkg_estimate_2016))
    localConfig.close()

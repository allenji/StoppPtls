#!/usr/bin/python
############# Parameter Setting #############
#mass_mchamp = [100, 200, 400, 600, 800, 1000, 1800, 2600]
mass_mchamp = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
mass_mchamp_ref2015 = [100, 200, 400, 600, 800, 1000, 1400, 1400, 1400, 1400]
mass_mchamp_ref2016 = [100, 200, 400, 600, 800, 1000, 1000, 1800, 1800, 2600]
mass_gluino = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mass_gluino_ref2015 = [400, 600, 600, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000]
mass_gluino_ref2016 = [400, 600, 600, 1000, 1200, 1200, 1600, 1800, 2000, 2000, 2400, 2400]

mchamp_stopEff = [0.33, 0.29, 0.28, 0.25, 0.30, 0.32, 0.35, 0.41, 0.48, 0.54]
gluino_stopEff = [0.19, 0.17, 0.17, 0.17, 0.18, 0.20, 0.21, 0.22, 0.23, 0.25, 0.25, 0.26]

mchamp_reco_2015 = [0.0028, 0.035, 0.038, 0.039, 0.032, 0.029, 0.029, 0.025, 0.024, 0.023]
gluino_reco_2015 = [0.0017, 0.0021, 0.0040, 0.0030, 0.0030, 0.0038, 0.0039, 0.0034, 0.0028, 0.0032, 0.0031, 0.0038]
mchamp_reco_2016 = [0.0050, 0.039, 0.042, 0.039, 0.035, 0.030, 0.030, 0.026, 0.024, 0.023]
gluino_reco_2016 = [0.0015, 0.0025, 0.0036, 0.0034, 0.0024, 0.0033, 0.0035, 0.0029, 0.0027, 0.0033, 0.0031, 0.0034]

mchamp_toyMCDir_2015 = "/home/weifengji/StoppedParticles_Run2/SPAnalysis_2017_Jan11/CMSSW_7_4_7/src/DelayedMuon_ToyMCResult_Apr27/ToyMC_2015mchamps_27April2017_unblinded"
gluino_toyMCDir_2015 = "/home/weifengji/StoppedParticles_Run2/SPAnalysis_2017_Jan11/CMSSW_7_4_7/src/DelayedMuon_ToyMCResult_Apr27/ToyMC_2015gluinos_27April2017_unblinded"
mchamp_toyMCDir_2016 = "/home/weifengji/StoppedParticles_Run2/SPAnalysis_2017_Jan11/CMSSW_7_4_7/src/DelayedMuon_ToyMCResult_Apr27/ToyMCmchamps2016_27April_unblinded"
gluino_toyMCDir_2016 = "/home/weifengji/StoppedParticles_Run2/SPAnalysis_2017_Jan11/CMSSW_7_4_7/src/DelayedMuon_ToyMCResult_Apr27/ToyMCgluinos2016_27April_unblinded"

mchamp_subDir_prefix_2015 = "mchamp2015"
gluino_subDir_prefix_2015 = "gluino2015"
mchamp_subDir_prefix_2016 = "mchamp2016"
gluino_subDir_prefix_2016 = "gluino2016"

outputdir = "DelayedMuon_2016_AllLifeTime_Apr30"
combine = 'False'
year = '2016'
onlyOneSec = 'False'


############# MAIN PART #############
import os
import sys
#mchamp_sigEff_2015 = []
mchamp_sigEff_2015 = [0.00092, 0.01015, 0.01064, 0.00975, 0.00990, 0.00960, 0.01015, 0.01025, 0.01152, 0.01296]
#gluino_sigEff_2015 = []
gluino_sigEff_2015 = [0.00034, 0.00036, 0.00071, 0.00053, 0.00058, 0.00080, 0.00084, 0.00079, 0.00067, 0.00080, 0.00080, 0.00101]
#mchamp_sigEff_2016 = []
mchamp_sigEff_2016 = [0.00172, 0.01131, 0.01176, 0.00975, 0.01050, 0.00960, 0.01050, 0.01066, 0.01152, 0.01296]
#gluino_sigEff_2016 = []
gluino_sigEff_2016 = [0.00029, 0.00043, 0.00065, 0.00060, 0.00045, 0.00070, 0.00076, 0.00064, 0.00064, 0.00085, 0.00080, 0.00091]
'''
for i in range(0, len(mass_mchamp)):
    mchamp_sigEff_2015.append(mchamp_stopEff[i]*mchamp_reco_2015[i])
    mchamp_sigEff_2016.append(mchamp_stopEff[i]*mchamp_reco_2016[i])
for i in range(0, len(mass_gluino)):
    gluino_sigEff_2015.append(gluino_stopEff[i]*gluino_reco_2015[i])
    gluino_sigEff_2016.append(gluino_stopEff[i]*gluino_reco_2016[i])
    '''

for mmchamp in mass_mchamp:
    mchamp2015ToyMC = mchamp_toyMCDir_2015 + '/' + mchamp_subDir_prefix_2015 + '_' + str(mass_mchamp_ref2015[mass_mchamp.index(mmchamp)]) +'/'+'toymc.txt'
    mchamp2016ToyMC = mchamp_toyMCDir_2016 + '/' + mchamp_subDir_prefix_2016 + '_' + str(mass_mchamp_ref2016[mass_mchamp.index(mmchamp)]) +'/'+'toymc.txt'
    mchamp2015Params = mchamp_toyMCDir_2015 + '/' + mchamp_subDir_prefix_2015 + '_' + str(mass_mchamp_ref2015[mass_mchamp.index(mmchamp)]) +'/'+'parameters.txt'
    mchamp2016Params = mchamp_toyMCDir_2016 + '/' + mchamp_subDir_prefix_2016 + '_' + str(mass_mchamp_ref2016[mass_mchamp.index(mmchamp)]) +'/'+'parameters.txt'
    
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
    bkg = []
    bkgN = []
    bkgalpha = []
    Toymc2015 = open(mchamp2015ToyMC)
    for line in Toymc2015:
        split_line = line.split()
        if split_line[0] == "1":
            bkg.append(split_line[3])
            bkgN.append(split_line[5])
            bkgalpha.append(split_line[6])
    Toymc2016 = open(mchamp2016ToyMC)
    for line in Toymc2016:
        split_line = line.split()
        if split_line[0] == "1":
            bkg.append(split_line[3])
            bkgN.append(split_line[5])
            bkgalpha.append(split_line[6])
   

    
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
    localConfig.write("bkg = ['bkg']\n")
    print bkg, bkgN, bkgalpha
    localConfig.write("bkg_estimate_1 = {'bkg':['gmN', %-10s,%-10s,%-10s], 'total': %-10s}\n"%(bkg[0], bkgN[0], bkgalpha[0], bkg[0]))
    localConfig.write("bkg_estimate_2 = {'bkg':['gmN', %-10s,%-10s,%-10s], 'total': %-10s}\n"%(bkg[1], bkgN[1], bkgalpha[1], bkg[1]))
    localConfig.close()

for mgluino in mass_gluino:
    gluino2015ToyMC = gluino_toyMCDir_2015 + '/' + gluino_subDir_prefix_2015 + '_' + str(mass_gluino_ref2015[mass_gluino.index(mgluino)]) +'/'+'toymc.txt'
    gluino2016ToyMC = gluino_toyMCDir_2016 + '/' + gluino_subDir_prefix_2016 + '_' + str(mass_gluino_ref2016[mass_gluino.index(mgluino)]) +'/'+'toymc.txt'
    gluino2015Params = gluino_toyMCDir_2015 + '/' + gluino_subDir_prefix_2015 + '_' + str(mass_gluino_ref2015[mass_gluino.index(mgluino)]) +'/'+'parameters.txt'
    gluino2016Params = gluino_toyMCDir_2016 + '/' + gluino_subDir_prefix_2016 + '_' + str(mass_gluino_ref2016[mass_gluino.index(mgluino)]) +'/'+'parameters.txt'

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
    bkg = []
    bkgN = []
    bkgalpha = []
    Toymc2015 = open(gluino2015ToyMC)
    for line in Toymc2015:
        split_line = line.split()
        if split_line[0] == "1":
            bkg.append(split_line[3])
            bkgN.append(split_line[5])
            bkgalpha.append(split_line[6])
    Toymc2016 = open(gluino2016ToyMC)
    for line in Toymc2016:
        split_line = line.split()
        if split_line[0] == "1":
            bkg.append(split_line[3])
            bkgN.append(split_line[5])
            bkgalpha.append(split_line[6])
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
    localConfig.write("bkg = ['bkg']\n")
    print bkg, bkgN, bkgalpha
    localConfig.write("bkg_estimate_1 = {'bkg':['gmN', %-10s,%-10s,%-10s], 'total': %-10s}\n"%(bkg[0], bkgN[0], bkgalpha[0], bkg[0]))
    localConfig.write("bkg_estimate_2 = {'bkg':['gmN', %-10s,%-10s,%-10s], 'total': %-10s}\n"%(bkg[1], bkgN[1], bkgalpha[1], bkg[1]))
    localConfig.close()

#!/usr/bin/python
############# Parameter Setting #############
#mass_mchamp = [100, 200, 400, 600, 800, 1000, 1800, 2600]
mass_mchamp = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
mass_mchamp_ref2015 = [100, 200, 400, 600, 600, 1000, 1400, 1400, 1400, 1400]
mass_mchamp_ref2016 = [100, 200, 200, 600, 800, 1000, 1000, 1800, 1800, 2600]
mass_gluino = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mass_gluino_ref2015 = [400, 600, 600, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000]
mass_gluino_ref2016 = [400, 600, 600, 1000, 1200, 1200, 1600, 1800, 2000, 2000, 2400, 2400]

mchamp_stopEff = [0.33, 0.29, 0.28, 0.25, 0.30, 0.32, 0.35, 0.41, 0.48, 0.54]
gluino_stopEff = [0.19, 0.17, 0.17, 0.17, 0.18, 0.20, 0.21, 0.22, 0.23, 0.25, 0.25, 0.26]

mchamp_reco_2015 = [0.0028, 0.035, 0.038, 0.039, 0.032, 0.029, 0.029, 0.025, 0.024, 0.023]
gluino_reco_2015 = [0.0017, 0.0021, 0.0040, 0.0030, 0.0030, 0.0038, 0.0039, 0.0034, 0.0028, 0.0032, 0.0031, 0.0038]
mchamp_reco_2016 = [0.0050, 0.039, 0.042, 0.039, 0.035, 0.030, 0.030, 0.026, 0.024, 0.023]
gluino_reco_2016 = [0.0015, 0.0025, 0.0036, 0.0034, 0.0024, 0.0033, 0.0035, 0.0029, 0.0027, 0.0033, 0.0031, 0.0034]

mchamp_toyMCDir_2015 = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/ToyMC_2015mchamps_21April2017_unblinded"
gluino_toyMCDir_2015 = "/home/jalimena/StoppedParticles2015_2/CMSSW_7_6_6/src/ToyMC_2015gluinos_21April2017_unblinded"
mchamp_toyMCDir_2016 = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/ToyMCmchamps2016_21April_unblinded"
gluino_toyMCDir_2016 = "/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/ToyMCgluinos2016_21April_unblinded"

mchamp_subDir_prefix_2015 = "mchamp2015"
gluino_subDir_prefix_2015 = "gluino2015"
mchamp_subDir_prefix_2016 = "mchamp2016"
gluino_subDir_prefix_2016 = "gluino2016"

#outputdir = "DelayedMuon2016Single"

'''
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
'''

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

outputdir = "DelayedMuonCombinedMchamp_"
lifetime = "1s"
dataset_name = "DelayedMuonCombineMchamp"
output = open("mchamp_combined.txt", "w")
for i in mchamp_sigEff_2016:
    print i
for i in gluino_sigEff_2016:
    print i
for mass in mass_mchamp:
    limits = {"observed":[], "expected":[],"expected_up1":[],
                        "expected_up2":[], "expected_down1":[], "expected_down2":[]}
    for limit_type in limits.keys():
        signal_name = dataset_name + str(mass) + '_'  + lifetime
        condor_dir = "limits/"+outputdir+str(mass)+"/"+signal_name+"_"+limit_type
        condor_output = condor_dir + "/condor_0.out"
        f = open(condor_output)
        limit = 0
        for line in f:
            if line.startswith("Limit"):
                limit = line.split()[3]
        limits[limit_type].append(float(limit)*13673.9*mchamp_sigEff_2016[mass_mchamp.index(mass)]/1000)
    output.write("%-10d%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f\n"%(mass, limits["observed"][0], limits["expected"][0], limits["expected_down1"][0], limits["expected_up1"][0], limits["expected_down2"][0], limits["expected_up2"][0]))

output.close()

gluino_outputdir = "DelayedMuonCombinedGluino_"
dataset_name = "DelayedMuonCombineGluino"
output = open("gluino_combined.txt", "w")

for mass in mass_gluino:
    limits = {"observed":[], "expected":[],"expected_up1":[],
                        "expected_up2":[], "expected_down1":[], "expected_down2":[]}
    for limit_type in limits.keys():
        signal_name = dataset_name + str(mass) + '_'  + lifetime
        condor_dir = "limits/"+gluino_outputdir+str(mass)+"/"+signal_name+"_"+limit_type
        condor_output = condor_dir + "/condor_0.out"
        f = open(condor_output)
        limit = 0
        for line in f:
            if line.startswith("Limit"):
                limit = line.split()[3]
        limits[limit_type].append(float(limit)*13673.9*gluino_sigEff_2016[mass_gluino.index(mass)]/1000)
    output.write("%-10d%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f\n"%(mass, limits["observed"][0], limits["expected"][0], limits["expected_down1"][0], limits["expected_up1"][0], limits["expected_down2"][0], limits["expected_up2"][0]))

output.close()

############# Parameter Setting #############
#mass_mchamp = [100, 200, 400, 600, 800, 1000, 1800, 2600]
mass_mchamp = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]
mass_gluino = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]

mchamp_stopEff = [0.33, 0.29, 0.28, 0.25, 0.30, 0.32, 0.35, 0.41, 0.48, 0.54]
gluino_stopEff = [0.19, 0.17, 0.17, 0.17, 0.18, 0.20, 0.21, 0.22, 0.23, 0.25, 0.25, 0.26]

mchamp_reco_2015 = [0.0051, 0.044, 0.050, 0.048, 0.041, 0.039, 0.038, 0.031, 0.031, 0.030]
gluino_reco_2015 = [0.0019, 0.0025, 0.0046, 0.0031, 0.0033, 0.0039, 0.0033, 0.0030, 0.0025, 0.0033, 0.0030, 0.0033]
mchamp_reco_2016 = [0.0059, 0.041, 0.045, 0.042, 0.038, 0.035, 0.032, 0.027, 0.026, 0.026]
gluino_reco_2016 = [0.0015, 0.0024, 0.0037, 0.0029, 0.0025, 0.0031, 0.0029, 0.0023, 0.0020, 0.0028, 0.0025, 0.0025]

effLumi_2016 = 13673.9
#outputdir = "DelayedMuon2016Single"

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

outputdir = "DelayedMuonCombinedMchamp_"
lifetime = "1s"
dataset_name = "DelayedMuonCombineMchamp"
output = open("mchamp_combined.txt", "w")

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
        limits[limit_type].append(float(limit)*effLumi_2016*mchamp_sigEff_2016[mass_mchamp.index(mass)]/1000)
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
        limits[limit_type].append(float(limit)*effLumi_2016*gluino_sigEff_2016[mass_gluino.index(mass)]/1000)
    output.write("%-10d%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f\n"%(mass, limits["observed"][0], limits["expected"][0], limits["expected_down1"][0], limits["expected_up1"][0], limits["expected_down2"][0], limits["expected_up2"][0]))

output.close()

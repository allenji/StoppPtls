#!/bin/env python
import os,sys
import re
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--outputDir", dest="outputDir",
                          help="output directory")

parser.add_option("-p", "--localConfig", dest="localConfig",
                          help="parameters file")

(arguments, args) = parser.parse_args()

if arguments.outputDir:
    if not os.path.exists(arguments.outputDir):
        print "Output directory doesn't exist, shame on you"
        sys.exit(0)
    elif not os.path.exists(arguments.outputDir+"/limits"):
        print "No limits subdirectory, aborting"
        sys.exit(0)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

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
output = open("mchamp_combined_at1S.txt", "w")

for mass in mass_mchamp:
    limits = {"observed":[], "expected":[],"expected_up1":[],
                        "expected_up2":[], "expected_down1":[], "expected_down2":[]}
    for limit_type in limits.keys():
        signal_name = dataset_name + str(mass) + '_'  + lifetime
        condor_dir = arguments.outputDir+"/limits/"+outputdir+str(mass)+"/"+signal_name+"_"+limit_type
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
output = open("gluino_combined_at1S.txt", "w")

for mass in mass_gluino:
    limits = {"observed":[], "expected":[],"expected_up1":[],
                        "expected_up2":[], "expected_down1":[], "expected_down2":[]}
    for limit_type in limits.keys():
        signal_name = dataset_name + str(mass) + '_'  + lifetime
        condor_dir = arguments.outputDir+"/limits/"+gluino_outputdir+str(mass)+"/"+signal_name+"_"+limit_type
        condor_output = condor_dir + "/condor_0.out"
        f = open(condor_output)
        limit = 0
        for line in f:
            if line.startswith("Limit"):
                limit = line.split()[3]
        limits[limit_type].append(float(limit)*effLumi_2016*gluino_sigEff_2016[mass_gluino.index(mass)]/1000)
    output.write("%-10d%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f%-10.4f\n"%(mass, limits["observed"][0], limits["expected"][0], limits["expected_down1"][0], limits["expected_up1"][0], limits["expected_down2"][0], limits["expected_up2"][0]))

output.close()

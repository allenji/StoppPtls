import time
import os
import sys
import math
import copy
import re
import subprocess
import shutil
from array import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--outputDir", dest="outputDir",
                                            help="output directory")
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local config file")
(arguments, args) = parser.parse_args()

if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)

if not os.path.exists ("limits/"+arguments.outputDir):
    print "The output directory does not exist, shame on you"
    sys.exit(0)

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

def get_lifetime(toymc_txt):
    lifetimes = []
    f = open(toymc_txt)
    for line in f:
        line_split = line.split()
        lifetime = line_split[0].replace(".", "p")
        lifetimes.append(lifetime+"s")
    return lifetimes

def get_lifetime_combine(toymc_txt1, toymc_txt2):
    lifetimes1 = []
    lifetimes2 = []
    f1 = open(toymc_txt1)
    f2 = open(toymc_txt2)
    for line in f1:
        line_split = line.split()
        lifetime = line_split[0].replace(".", "p")
        lifetimes1.append(lifetime+"s")
    for line in f2:
        line_split = line.split()
        lifetime = line_split[0].replace(".", "p")
        lifetimes2.append(lifetime+"s")
    return set(lifetimes1).intersection(lifetimes2)

toymc2015 = '/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_8_0_12/src/ToyMC_Apr27_2015/toymc/summary.txt'
toymc2016 = '/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_8_0_12/src/ToyMC_Apr27_2016Full/toymc/summary.txt'
limits = {}
limits_type = ["observed", "expected","expected_up1",
            "expected_up2", "expected_down1", "expected_down2"]
lifetimes = get_lifetime_combine(toymc[0], toymc[1])
for lifetime in lifetimes:
    limits[lifetime] = {}
#for lifetime in ["1s", "1000s"]:
    for limit_type in limits_type:
        signal_name = dataset_name + "_" + lifetime
        condor_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_"+limit_type
        condor_output = condor_dir + "/condor_0.out"
        f = open(condor_output)
        for line in f:
            if line.startswith("Limit"):
                limit = line.split()[3]
        limits[lifetime][limit_type] = limit

#toymc_input = open(toymc2016)
toymc_input = open(toymc[1])
toymc_output = open("toymc_combinedMchamp2600", "w")
for line in toymc_input:
    line_split = line.split()
    lifetime = line_split[0].replace('.', 'p') + 's'
    if lifetime in lifetimes:
        output_line = ""
        for i in [0, 1, 2, 3, 4, 7]:
            output_line += line_split[i] + " "
        #signal_efficiency = 0.023
        #signal_efficiency = 0.01436
        #signal_efficiency = 0.00060 # delayed muon 2016 1000GeV gluino
        signal_efficiency = 0.00960 # delayed muon 2016 1000GeV mchamp
        #signal_efficiency = 0.01296 # delayed muon 2016 2600GeV mchamp
        #signal_efficiency = 0.00091 # delayed muon 2016 2600GeV gluino
        obs = float(limits[lifetime]["observed"]) * float(line_split[1]) * signal_efficiency / 1000
        exp = float(limits[lifetime]["expected"]) * float(line_split[1]) * signal_efficiency / 1000
        expu1 = float(limits[lifetime]["expected_up1"]) * float(line_split[1]) * signal_efficiency / 1000
        expu2 = float(limits[lifetime]["expected_up2"]) * float(line_split[1]) * signal_efficiency / 1000
        expd1 = float(limits[lifetime]["expected_down1"]) * float(line_split[1]) * signal_efficiency / 1000
        expd2 = float(limits[lifetime]["expected_down2"]) * float(line_split[1]) * signal_efficiency / 1000
        output_line += "%10.5f%10.5f%10.5f%10.5f%10.5f%10.5f\n"%(obs, exp,expd1, expu1, expd2, expu2)
        #output_line += "%10s%10s%10s%10s%10s%10s\n"%(limits[lifetime]["observed"], limits[lifetime]["expected"],limits[lifetime]["expected_down1"], limits[lifetime]["expected_up1"], limits[lifetime]["expected_down2"], limits[lifetime]["expected_up2"])

        toymc_output.write(output_line)
toymc_output.close()


print limits

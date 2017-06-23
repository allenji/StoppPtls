#!/bin/env python
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
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                  help="run on the condor queue")
parser.add_option("-M", "--method", dest="method", default="Asymptotic",
                                    help="which method of combine to use: currently supported options are Asymptotic (default), MarkovChainMC and HybridNew")
(arguments, args) = parser.parse_args()


if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists ("limits/"+arguments.outputDir):
        os.system("mkdir limits/%s" % (arguments.outputDir))

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

def datacardOnlyGammaBkg(datacard):
    gamma = True
    datacard_file = open(datacard)
    for line in datacard_file:
        split_line = line.split()
        if line.startswith("bkg_err") and (split_line[1] == "lnN"):
            gamma = False
    return gamma

def output_condor(combine_command, datacard, options):
    script = "#!/usr/bin/env bash\n\n"
    script += "./combine "+options+"\n"
    f = open ("condor.sh", "w")
    f.write (script)
    f.close ()
    os.chmod ("condor.sh", 0775)
    command = "condor.sh"

    sub_file = ""
#    if os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/data/condor.sub"):
    sub_file += "Executable              = "+command+"\n"
    sub_file += "Universe                = vanilla\n"
    sub_file += "Getenv                  = True\n"
    sub_file += "\n"
    sub_file += "Output                  = condor_$(Process).out\n"
    sub_file += "Error                   = condor_$(Process).err\n"
    sub_file += "Log                     = condor_$(Process).log\n"
    sub_file += "\n"
    sub_file += "should_transfer_files   = yes\n"
    sub_file += "transfer_input_files    = " + combine_command + "," + datacard + "\n"
    sub_file += "\n"
    sub_file += "request_memory          = 2048MB\n"
    sub_file += "request_cpus            = 1\n"
    sub_file += "\n"
    sub_file += "Queue 1\n"

    f = open ("condor.sub", "w")
    f.write (sub_file)
    f.close ()

# beginning of the main loop
if combine is False:
    if year == 2015:
        lifetimes = get_lifetime(toymc[0])
    if year == 2016:
        lifetimes = get_lifetime(toymc[1])
else:
    lifetimes = get_lifetime_combine(toymc[0], toymc[1])
    #lifetimes = set(get_lifetime("/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_8_0_12/src/ToyMC_Apr27_2016Full/searchLifetimes.txt"))
if onlyOneSec is True:
    lt_itr = ["1s"]
else: 
    lt_itr = lifetimes

for lifetime in lt_itr:
#for lifetime in ["1s"]:
    signal_name = dataset_name + "_" + lifetime
    condor_expected_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_expected"
    condor_observed_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_observed"
    datacard_name = "datacard_" + signal_name + ".txt"
    datacard_src_name = "limits/" + arguments.outputDir +"/"+datacard_name
    datacard_dst_expected_name = condor_expected_dir+"/"+datacard_name
    datacard_dst_observed_name = condor_observed_dir+"/"+datacard_name
    combine_expected_options = combine_observed_options = " -H ProfileLikelihood "

    combine_expected_options += "-M " + arguments.method + " "
    combine_observed_options += "-M " + arguments.method + " "
    originalDatacard = os.getcwd() + '/' + datacard_src_name
    #gammaOnly = datacardOnlyGammaBkg(originalDatacard)
    gammaOnly = False
    #hybridExtraOptions = "--fork 4 --frequentist --testStat LHC --rAbsAcc 0.00001 -T 2000 "
    #hybridExtraOptions = "--fork 4 --frequentist --testStat LHC --rAbsAcc 0.001 -T 2000 "
    #hybridExtraOptions = "--testStat LHC --rAbsAcc 0.00001 -T 2000 "
    #hybridExtraOptions = "--fork 4 --testStat LHC --rAbsAcc 0.001 --rRelAcc 0.001 --fullBToys -T 10000 "
    hybridExtraOptions = "--fork 4 --testStat LHC"
    if gammaOnly is True:
        combine_expected_options = combine_expected_options + hybridExtraOptions + " --expectedFromGrid 0.01 "
    else:
        combine_expected_options = combine_expected_options + hybridExtraOptions + " --expectedFromGrid 0.5 "
    combine_observed_options = combine_observed_options + hybridExtraOptions

    combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
    combine_command = combine_command.rstrip()

    shutil.rmtree(condor_expected_dir, True)
    os.mkdir(condor_expected_dir)
    shutil.copy(datacard_src_name, datacard_dst_expected_name)
    os.chdir(condor_expected_dir)

    print "combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name
    output_condor(combine_command, datacard_name, datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
    os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

    expectedVariations = [("up1", "0.84", "0.68"), ("up2", "0.975", "0.95"), ("down1", "0.16", "0.01"), ("down2", "0.025", "0.01")]
    for vary in expectedVariations:
        os.chdir("../../..")
        condor_expected_dirVary = condor_expected_dir + "_" + vary[0]
        shutil.rmtree(condor_expected_dirVary, True)
        os.mkdir(condor_expected_dirVary)
        shutil.copy(datacard_src_name, condor_expected_dirVary + "/" + datacard_name)
        os.chdir(condor_expected_dirVary)
        if gammaOnly is True:
            combine_expected_optionsVary = combine_expected_options.replace("expectedFromGrid 0.01", "expectedFromGrid " + vary[2])
        else:
            combine_expected_optionsVary = combine_expected_options.replace("expectedFromGrid 0.5", "expectedFromGrid " + vary[1])
        print "combine "+datacard_name+" "+combine_expected_optionsVary+" --name "+signal_name
        output_condor(combine_command, datacard_name, datacard_name+" "+combine_expected_optionsVary+" --name "+signal_name+" | tee /dev/null")
        os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

    os.chdir("../../..")

    shutil.rmtree(condor_observed_dir, True)
    os.mkdir(condor_observed_dir)
    shutil.copy(datacard_src_name, datacard_dst_observed_name)
    os.chdir(condor_observed_dir)

    print "combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name
    output_condor(combine_command, datacard_name, datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null")
    os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

    os.chdir("../../..")

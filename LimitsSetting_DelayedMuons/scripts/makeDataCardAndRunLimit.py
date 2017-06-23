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
    elif os.path.exists(arguments.outputDir+"/limits"):
        print "Output directory already has subdir named 'limits', please remove it before proceeding!"
        sys.exit(0)
    else:
        os.system("mkdir "+arguments.outputDir+"/limits")
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

os.chdir(arguments.outputDir)

for mass in mass_mchamp_runLimits:
    makeDataCardCMD = "makeDataCardsFinal_DM.py -l localConfig_DMMchampCombined_%s'.py' -c DelayedMuonCombinedMchamp_%s"%(str(mass), str(mass))
    runLimitCMS = "runLimits_DM.py -M HybridNew -l localConfig_DMMchampCombined_%s'.py' -c DelayedMuonCombinedMchamp_%s"%(str(mass), str(mass))
    print "Writing datacards for mchamp of mass %d GeV..."%(mass)
    os.system(makeDataCardCMD)
    print "Submitting jobs for mchamp of mass %d GeV..."%(mass)
    os.system(runLimitCMS)

for mass in mass_gluino_runLimits:
    makeDataCardCMD = "makeDataCardsFinal_DM.py -l localConfig_DMGluinoCombined_%s'.py' -c DelayedMuonCombinedGluino_%s"%(str(mass), str(mass))
    runLimitCMS = "runLimits_DM.py -M HybridNew -l localConfig_DMGluinoCombined_%s'.py' -c DelayedMuonCombinedGluino_%s"%(str(mass), str(mass))
    print "Writing datacards for gluino of mass %d GeV..."%mass
    os.system(makeDataCardCMD)
    print "Submitting jobs for gluino of mass %d GeV..."%(mass)
    os.system(runLimitCMS)    



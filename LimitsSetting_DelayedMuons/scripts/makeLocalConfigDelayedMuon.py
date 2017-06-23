#!/bin/env python
import os
import sys
import re
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-o", "--outputDir", dest="outputDir",
                          help="output directory")
parser.add_option("-p", "--localConfig", dest="localConfig",
                          help="parameters file")

(arguments, args) = parser.parse_args()

if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)
elif os.path.exists(arguments.outputDir):
    print "Output directory already exists, aborting...."
    sys.exit(0)
else:
    os.mkdir(arguments.outputDir)

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
    
    os.system("rm -rf "+arguments.outputDir+"/"+"localConfig_DMMchampCombined_"+str(mmchamp)+".py")
    localConfig = open(arguments.outputDir+"/"+"localConfig_DMMchampCombined_"+str(mmchamp)+".py", "w")
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
    os.system("rm -rf "+arguments.outputDir+"/"+"localConfig_DMGluinoCombined_"+str(mgluino)+".py")
    localConfig = open(arguments.outputDir+"/"+"localConfig_DMGluinoCombined_"+str(mgluino)+".py", "w")
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

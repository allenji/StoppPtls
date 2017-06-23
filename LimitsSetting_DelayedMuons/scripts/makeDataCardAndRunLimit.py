gluino_mass = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]

mchamp_mass = [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]

import os,sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--outputDir", dest="outputDir",
                          help="output directory")

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

os.chdir(arguments.outputDir)

for mass in mchamp_mass:
    makeDataCardCMD = "python ../makeDataCardsFinal_DM.py -l localConfig_DMMchampCombined_%s'.py' -c DelayedMuonCombinedMchamp_%s"%(str(mass), str(mass))
    runLimitCMS = "python ../runLimits_DM.py -M HybridNew -l localConfig_DMMchampCombined_%s'.py' -c DelayedMuonCombinedMchamp_%s"%(str(mass), str(mass))
    os.system(makeDataCardCMD)
    os.system(runLimitCMS)

for mass in gluino_mass:
    makeDataCardCMD = "python ../makeDataCardsFinal_DM.py -l localConfig_DMGluinoCombined_%s'.py' -c DelayedMuonCombinedGluino_%s"%(str(mass), str(mass))
    runLimitCMS = "python ../runLimits_DM.py -M HybridNew -l localConfig_DMGluinoCombined_%s'.py' -c DelayedMuonCombinedGluino_%s"%(str(mass), str(mass))
    os.system(makeDataCardCMD)
    os.system(runLimitCMS)    



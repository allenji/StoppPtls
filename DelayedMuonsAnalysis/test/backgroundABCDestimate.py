import time
import os
import sys
import math
import copy
import re
from math import *
from array import *
from optparse import OptionParser
from operator import itemgetter
from ROOT import *

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.histogramUtilities import *

parser = OptionParser()
parser = set_commandline_arguments(parser)
parser.add_option("-B", "--blinded", dest="blinded",default=True,
                  help="if true (default) then blind to observed number in region D")
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    condor_dir = arguments.condorDir
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

blinded = arguments.blinded

pt_threshold = [63, 65, 100, 150, 200]
#pt_threshold = [63, 65, 70, 90, 100]
#pt_threshold = [110, 120, 130, 150] 
#pt_threshold = [160, 170, 190, 200]
#pt_threshold = [230, 240, 260, 290]


for dataset in datasets:
    for pt in pt_threshold:
        regionA = "DelayedMuonsUpperLowerSelectionRegionAUpperP%dCutFlowPlotter"%(int(pt))
        regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP%dCutFlowPlotter"%(int(pt))
        regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP%dCutFlowPlotter"%(int(pt))
        regionD = "DelayedMuonsUpperLowerSelectionRegionDUpperP%dCutFlowPlotter"%(int(pt))
        (numA, errA) = getYield(dataset,condor_dir, regionA)
        (numB, errB) = getYield(dataset,condor_dir, regionB)
        (numC, errC) = getYield(dataset,condor_dir, regionC)
        (numD, errD) = getYield(dataset,condor_dir, regionD)

        errC_plus = errC
        errC_minum = errC

        print "/////////////////////////////////////////////////////////////////////"
        print "for " + dataset + ", "
        print "  \Delta RPC Hit BX Average cut at -0.3, "
        print "   and upper DSA p threshold " + str(pt) + " GeV:"

        if numC==0.:
            numC = 0.000001
            errC_plus = 1.8 #poisson error
            errC_minus = 1.8
            print "numC is 0 +/- 1.8, need to model as gamma function"
        if numC==1.:
            errC_plus = 2.3
            errC_minus = 0.8
            print "numC is 1 +2.3 -0.8"

        if numA!=0.:
            background_estimate = 1.0*numB*numC/numA
        else:
            print "numA is zero!!!"

        print "number of events in region A is: " + str(int(numA)) + " +/- " + str("%.1f" % errA)
        print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.1f" % errB)
        #print "number of events in region C is: " + str(int(numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)
        print "number of events in region C is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)
        if blinded!=True: print "number of events in region D is: " + str(int(numD)) + " +/- " + str("%.1f" % errD)

        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))
        print "background estimate (B*C/A) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
        print "/////////////////////////////////////////////////////////////////////"
print "done"

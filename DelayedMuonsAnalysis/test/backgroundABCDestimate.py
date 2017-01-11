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

#pt_threshold = [65, 70, 90, 100, 110, 120, 130, 150]
#pt_threshold = [160, 170, 190, 200, 230, 240, 260, 290]
pt_threshold = [65, 70, 90, 100, 110, 120, 130, 150, 160, 170, 190, 200, 230, 240, 260, 290]
#pt_threshold = [65, 300]

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

        print "/////////////////////////////////////////////////////////////////////"
        print "for " + dataset + ", "
        print "  \Delta RPC Hit BX Average cut at -1.0, "
        print "   and upper DSA p threshold " + str(pt) + " GeV:"
        print "number of events in region A is: " + str(int(numA)) + " +/- " + str("%.1f" % errA)
        print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.1f" % errB)
        print "number of events in region C is: " + str(int(numC)) + " +/- " + str("%.1f" % errC)
        if blinded!=True: print "number of events in region D is: " + str(int(numD)) + " +/- " + str("%.1f" % errD)

        if numA!=0.:
            background_estimate = 1.0*numB*numC/numA
        else:
            print "numA is zero!!!"
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        print "background estimate (B*C/A) is: " + str("%.1f" % background_estimate) + " +/- " + str("%.1f" % background_error)
        print "/////////////////////////////////////////////////////////////////////"
print "done"


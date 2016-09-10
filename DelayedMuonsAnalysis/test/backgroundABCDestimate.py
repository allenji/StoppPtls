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
parser.add_option("-H", "--hist", dest="hist",default="run",
                  help="which histogram to plot")
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    #condor_dir = set_condor_output_dir(arguments)
    condor_dir = arguments.condorDir
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

pt_threshold = [50, 60, 110, 150, 170, 200, 250, 300, 400]

for dataset in datasets:
    for pt in pt_threshold:
        #outputFile = TFile(condor_dir+"/"+dataset+"_OnlyFilledRuns.root","RECREATE")
        #(numA, errA) = getYield(dataset,condor_dir,"DelayedMuonsUpperLowerSelectionCutFlowPlotter")
        regionA = "DelayedMuonsUpperLowerSelectionRegionAUpperP%dCutFlowPlotter"%(int(pt))
        regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP%dCutFlowPlotter"%(int(pt))
        regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP%dCutFlowPlotter"%(int(pt))
        regionD = "DelayedMuonsUpperLowerSelectionRegionDUpperP%dCutFlowPlotter"%(int(pt))
        #(numA, errA) = getYield(dataset,condor_dir,"DelayedMuonsUpperLowerSelectionRegionAUpperP50CutFlowPlotter")
        (numA, errA) = getYield(dataset,condor_dir, regionA)
        #(numB, errB) = getYield(dataset,condor_dir,"DelayedMuonsUpperLowerSelectionRegionBUpperP50CutFlowPlotter")
        (numB, errB) = getYield(dataset,condor_dir, regionB)
        #(numC, errC) = getYield(dataset,condor_dir,"DelayedMuonsUpperLowerSelectionRegionCUpperP50CutFlowPlotter")
        (numC, errC) = getYield(dataset,condor_dir, regionC)
        #(numD, errD) = getYield(dataset,condor_dir,"DelayedMuonsUpperLowerSelectionRegionDUpperP50CutFlowPlotter")
        (numD, errD) = getYield(dataset,condor_dir, regionD)

        print "///////////////////////////////////////////////////////////"
        print "for " + dataset + " and pt threshold " + str(pt) + " GeV:"
        print "number of events in region A is: " + str(numA) + " +/- " + str(errA)
        print "number of events in region B is: " + str(numB) + " +/- " + str(errB)
        print "number of events in region C is: " + str(numC) + " +/- " + str(errC)
        print "number of events in region D is: " + str(numD) + " +/- " + str(errD)

        if numA!=0.:
            background_estimate = 1.0*numB*numC/numA
        else:
            print "numA is zero!!!"
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        print "background estimate (B*C/A) for " + dataset + " is: " + str(background_estimate) + " +/- " + str(background_error)
        print "///////////////////////////////////////////////////////////"

        #plots = MakeOnlyFilledRunsHist(dataset,channel,arguments.hist)
        #outputFile.Close()
print "done"

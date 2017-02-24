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



for dataset in datasets:
    regionA = "DelayedMuonsUpperLowerSelectionRegionA1UpperP90CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionC1UpperP90CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    print "number of events in region A1 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C1 is: " + str(int(numC)) + " +/- " + str("%.2f" % errC)
    
    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    if numC==0.:
        background_error = 0.0
        print "numC is 0, so background error is 0, need to model as gamma function"
    if numC==1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB) ))
        print "numC is 1, so background error is only error on numA and numB"
    if numC>1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        
    print "background estimate (B*C1/A1) is: " + str("%.2f" % background_estimate) + " +/- " + str("%.2f" % background_error)
    print "/////////////////////////////////////////////////////////////////////"


    regionA = "DelayedMuonsUpperLowerSelectionRegionA2UpperP90CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionC2UpperP90CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    print "number of events in region A2 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C2 is: " + str(int(numC)) + " +/- " + str("%.2f" % errC)
    
    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    if numC==0.:
        background_error = 0.0
        print "numC is 0, so background error is 0, need to model as gamma function"
    if numC==1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB) ))
        print "numC is 1, so background error is only error on numA and numB"
    if numC>1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        
    print "background estimate (B*C2/A2) is: " + str("%.2f" % background_estimate) + " +/- " + str("%.2f" % background_error)
    print "/////////////////////////////////////////////////////////////////////"



    regionA = "DelayedMuonsUpperLowerSelectionRegionA1UpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionB1UpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    print "number of events in region A1 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B1 is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str(int(numC)) + " +/- " + str("%.2f" % errC)
    
    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    if numC==0.:
        background_error = 0.0
        print "numC is 0, so background error is 0, need to model as gamma function"
    if numC==1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB) ))
        print "numC is 1, so background error is only error on numA and numB"
    if numC>1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        
    print "background estimate (B1*C/A1) is: " + str("%.2f" % background_estimate) + " +/- " + str("%.2f" % background_error)
    print "/////////////////////////////////////////////////////////////////////"





    regionA = "DelayedMuonsUpperLowerSelectionRegionA2UpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionB2UpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    print "number of events in region A2 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B2 is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str(int(numC)) + " +/- " + str("%.2f" % errC)
    
    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    if numC==0.:
        background_error = 0.0
        print "numC is 0, so background error is 0, need to model as gamma function"
    if numC==1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB) ))
        print "numC is 1, so background error is only error on numA and numB"
    if numC>1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        
    print "background estimate (B2*C/A2) is: " + str("%.2f" % background_estimate) + " +/- " + str("%.2f" % background_error)
    print "/////////////////////////////////////////////////////////////////////"



    regionA = "DelayedMuonsUpperLowerSelectionRegionAUpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    print "number of events in region A is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str(int(numC)) + " +/- " + str("%.2f" % errC)
    
    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    if numC==0.:
        background_error = 0.0
        print "numC is 0, so background error is 0, need to model as gamma function"
    if numC==1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB) ))
        print "numC is 1, so background error is only error on numA and numB"
    if numC>1.:
        background_error = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC/numC)*(errC/numC) ))
        
    print "NOMINAL background estimate (B*C/A) is: " + str("%.2f" % background_estimate) + " +/- " + str("%.2f" % background_error)
    print "/////////////////////////////////////////////////////////////////////"

    print "done"


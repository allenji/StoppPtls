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
    
    if numC==0.:
        numC = 0.000001
        errC_plus = 1.8 #poisson error                                                                                                                       
        errC_minus = 0
        print "numC is 0 + 1.8, need to model as gamma function"
    if numC==1.:
        errC_plus = 2.3
        errC_minus = 0.8
        print "numC is 1 +2.3 -0.8"

    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    print "number of events in region A1 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C1 is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)

    if numC==0.000001:
        background_error_plus = ROOT.Math.gamma_quantile(.68,1,1.0*numB/numA) #68% confidence, 1+N (N is numC which here is 0), alpha=numB/numA
        background_error_minus = 0.
    else:
        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))

    print "background estimate (B*C1/A1) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
    print "/////////////////////////////////////////////////////////////////////"


    regionA = "DelayedMuonsUpperLowerSelectionRegionA2UpperP90CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionC2UpperP90CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "
    
    if numC==0.:
        numC = 0.000001
        errC_plus = 1.8 #poisson error                                                                                                                       
        errC_minus = 0
        print "numC is 0 + 1.8, need to model as gamma function"
    if numC==1.:
        errC_plus = 2.3
        errC_minus = 0.8
        print "numC is 1 +2.3 -0.8"

    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    print "number of events in region A2 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C2 is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)

    if numC==0.000001:
        background_error_plus = ROOT.Math.gamma_quantile(.68,1,1.0*numB/numA) #68% confidence, 1+N (N is numC which here is 0), alpha=numB/numA
        background_error_minus = 0.
    else:
        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))

    print "background estimate (B*C2/A2) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
    print "/////////////////////////////////////////////////////////////////////"



    regionA = "DelayedMuonsUpperLowerSelectionRegionA1UpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionB1UpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "

    if numC==0.:
        numC = 0.000001
        errC_plus = 1.8 #poisson error                                                                                                                       
        errC_minus = 0
        print "numC is 0 + 1.8, need to model as gamma function"
    if numC==1.:
        errC_plus = 2.3
        errC_minus = 0.8
        print "numC is 1 +2.3 -0.8"

    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    print "number of events in region A1 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B1 is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)

    if numC==0.000001:
        background_error_plus = ROOT.Math.gamma_quantile(.68,1,1.0*numB/numA) #68% confidence, 1+N (N is numC which here is 0), alpha=numB/numA
        background_error_minus = 0.
    else:
        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))

    print "background estimate (B1*C/A1) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
    print "/////////////////////////////////////////////////////////////////////"





    regionA = "DelayedMuonsUpperLowerSelectionRegionA2UpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionB2UpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "

    if numC==0.:
        numC = 0.000001
        errC_plus = 1.8 #poisson error                                                                                                                       
        errC_minus = 0
        print "numC is 0 + 1.8, need to model as gamma function"
    if numC==1.:
        errC_plus = 2.3
        errC_minus = 0.8
        print "numC is 1 +2.3 -0.8"

    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    print "number of events in region A2 is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B2 is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)

    if numC==0.000001:
        background_error_plus = ROOT.Math.gamma_quantile(.68,1,1.0*numB/numA) #68% confidence, 1+N (N is numC which here is 0), alpha=numB/numA
        background_error_minus = 0.
    else:
        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))

    print "background estimate (B2*C/A2) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
    print "/////////////////////////////////////////////////////////////////////"



    regionA = "DelayedMuonsUpperLowerSelectionRegionAUpperP150CutFlowPlotter"
    regionB = "DelayedMuonsUpperLowerSelectionRegionBUpperP150CutFlowPlotter"
    regionC = "DelayedMuonsUpperLowerSelectionRegionCUpperP150CutFlowPlotter"
    (numA, errA) = getYield(dataset,condor_dir, regionA)
    (numB, errB) = getYield(dataset,condor_dir, regionB)
    (numC, errC) = getYield(dataset,condor_dir, regionC)
    
    print "/////////////////////////////////////////////////////////////////////"
    print "for " + dataset + ", "

    if numC==0.:
        numC = 0.000001
        errC_plus = 1.8 #poisson error                                                                                                                       
        errC_minus = 0
        print "numC is 0 + 1.8, need to model as gamma function"
    if numC==1.:
        errC_plus = 2.3
        errC_minus = 0.8
        print "numC is 1 +2.3 -0.8"

    if numA!=0.:
        background_estimate = 1.0*numB*numC/numA
    else:
        print "numA is zero!!!"

    print "number of events in region A is: " + str(int(numA)) + " +/- " + str("%.2f" % errA)
    print "number of events in region B is: " + str(int(numB)) + " +/- " + str("%.2f" % errB)
    print "number of events in region C is: " + str((numC)) + " + " + str("%.1f" % errC_plus) + " - " + str("%.1f" % errC_minus)

    if numC==0.000001:
        background_error_plus = ROOT.Math.gamma_quantile(.68,1,1.0*numB/numA) #68% confidence, 1+N (N is numC which here is 0), alpha=numB/numA
        background_error_minus = 0.
    else:
        background_error_plus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_plus/numC)*(errC_plus/numC) ))
        background_error_minus = background_estimate*(sqrt( (errA/numA)*(errA/numA)+(errB/numB)*(errB/numB)+(errC_minus/numC)*(errC_minus/numC) ))

    print "NOMINAL background estimate (B*C/A) is: " + str("%.2f" % background_estimate) + " + " + str("%.2f" % background_error_plus) + " - " + str("%.2f" % background_error_minus)
    print "/////////////////////////////////////////////////////////////////////"

    print "done"


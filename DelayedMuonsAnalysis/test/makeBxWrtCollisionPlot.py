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

parser = OptionParser()
parser = set_commandline_arguments(parser)
parser.add_option("-H", "--hist", dest="hist",default="bxWrtBunch",
                  help="which histogram to plot")
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    condor_dir = set_condor_output_dir(arguments)
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

def ShiftByOneBin(dataset,channel,hist):
    inputFile = TFile(condor_dir+"/"+dataset+".root")
    HistObj = inputFile.Get(channel+"Plotter/Event Plots/"+hist)
    if not HistObj:
        print "WARNING:  Could not find histogram " + channel+"Plotter/Event Plots/"+hist + " in file " + dataset+".root" + ".  Will skip it and continue."
        return
    
    NewHist = HistObj.Clone()
    NewHist.SetDirectory(0)
    NBins = NewHist.GetNbinsX()
    inputFile.Close()
    binContent = []
    binError = []
    binLabel = []

    for bin in range(1, NBins+1):
        content = NewHist.GetBinContent(bin)
        error = NewHist.GetBinError(bin)
        label = int(NewHist.GetBinLowEdge(bin))
        binContent.append(content)
        binError.append(error)
        binLabel.append(label)

    title = ';BX with respect to collision;Number of Events'
    newNewHist = TH1D(hist,title, NBins, 0, NBins )
    newNewHist.SetLineColor(1)
    newNewHist.SetLineWidth(3)
    #newNewHist.GetXaxis().SetNdivisions(200,kFALSE)
    newNewHist.SetDirectory(0)

    for bin in range(1,NBins+1):
        newNewHist.SetBinContent(bin, binContent[bin-1])
        newNewHist.SetBinError(bin, binError[bin-1])
        if (bin-2) % 5 == 0:
            newNewHist.GetXaxis().SetBinLabel(bin, str(binLabel[bin-2]))

    directory = outputFile.mkdir(channel)
    outputFile.cd()
    directory.cd()
    newNewHist.Write()


channels = ["TriggerSelection","NoBPTXControlTriggerSelection","NoBPTX3BXControlTriggerSelection"]

for dataset in datasets:
    outputFile = TFile(condor_dir+"/"+dataset+"_new.root","RECREATE")
    for channel in channels:
        plots = ShiftByOneBin(dataset,channel,arguments.hist)
    outputFile.Close()

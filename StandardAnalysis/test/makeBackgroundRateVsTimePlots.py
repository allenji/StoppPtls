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
    condor_dir = set_condor_output_dir(arguments)
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

def MakeOnlyFilledRunsHist(dataset,channel,hist):
    inputFile = TFile(condor_dir+"/"+dataset+".root")
    HistObj = inputFile.Get(channel+"Plotter/Event Plots/"+hist)
    if not HistObj:
        print "WARNING:  Could not find histogram " + channel+"Plotter/Event Plots/"+hist + " in file " + dataset+".root" + ".  Will skip it and continue."
        return
    
    RateHist = HistObj.Clone()
    RateHist.SetDirectory(0)
    NBins = RateHist.GetNbinsX()
    inputFile.Close()
    newNBins = 0
    binContent = []
    binError = []
    binLabel = []

    for bin in range(1, NBins+1):
        content = RateHist.GetBinContent(bin)
        error = RateHist.GetBinError(bin)
        label = int(RateHist.GetBinLowEdge(bin))
        if content > 0.:
            newNBins+=1
            binContent.append(content)
            binError.append(error)
            binLabel.append(label)

    title = ';'+hist+';Rate [Hz]'
    newRateHist = TH1D(hist,title, newNBins, 0, newNBins )
    newRateHist.SetDirectory(0)

    for bin in range(1,newNBins+1):
        newRateHist.SetBinContent(bin, binContent[bin-1])
        newRateHist.SetBinError(bin, binError[bin-1])
        newRateHist.GetXaxis().SetBinLabel(bin, str(binLabel[bin-1]))

    directory = outputFile.mkdir(channel)
    outputFile.cd()
    directory.cd()
    newRateHist.Write()


channels = ["TriggerSelection","BeamHaloControlSelection","CosmicMuonControlSelection","HcalNoiseControlSelection"]

for dataset in datasets:
    outputFile = TFile(condor_dir+"/"+dataset+"_OnlyFilledRuns.root","RECREATE")
    for channel in channels:
        plots = MakeOnlyFilledRunsHist(dataset,channel,arguments.hist)
    outputFile.Close()

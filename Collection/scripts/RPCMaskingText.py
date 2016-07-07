# This python script is used to produce a textfile showing the RPC masking region, the output should be

import ROOT as rt
import os

from optparse import OptionParser

input_file = "/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_8_0_12/src/StoppPtls/StandardAnalysis/test/condor/070216_RPCHits_0/Data2016_readinlocal/hist_0.root"
input_TFile = rt.TFile(input_file, "READ")

hist_neighbourRPChits = input_TFile.Get("rpchitsPlotting/RPCHitsInCone")
#hist_neighbourRPChits_count = input_TFile.Get()

density_threshold = 400

Nbins_X = hist_neighbourRPChits.GetNbinsX()
Nbins_Y = hist_neighbourRPChits.GetNbinsY()
Nbins_Z = hist_neighbourRPChits.GetNbinsZ()

print Nbins_X
print Nbins_Y
print Nbins_Z

x_Min = hist_neighbourRPChits.GetXaxis().GetXmin()
x_Max = hist_neighbourRPChits.GetXaxis().GetXmax()
y_Min = hist_neighbourRPChits.GetYaxis().GetXmin()
y_Max = hist_neighbourRPChits.GetYaxis().GetXmax()
z_Min = hist_neighbourRPChits.GetZaxis().GetXmin()
z_Max = hist_neighbourRPChits.GetZaxis().GetXmax()

print x_Min
print x_Max
print y_Min
print y_Max
print z_Min
print z_Max

x_binSize = (x_Max - x_Min)/Nbins_X
y_binSize = (y_Max - y_Min)/Nbins_Y
z_binSize = (z_Max - z_Min)/Nbins_Z

print x_binSize

f = open("RPCMasking.txt", 'w')

count = 0
for i in range(1, Nbins_X + 1):
    for j in range(1, Nbins_Y + 1):
        for k in range(1, Nbins_Z + 1):
            count += 1
            print count
            if (hist_neighbourRPChits.GetBinContent(i,j,k) > density_threshold):
                output_x_Min = x_Min + (i - 1) * x_binSize
                output_x_Max = output_x_Min + x_binSize
                output_y_Min = y_Min + (j - 1) * y_binSize
                output_y_Max = output_y_Min + y_binSize
                output_z_Min = z_Min + (k - 1) * z_binSize
                output_z_Max = output_z_Min + z_binSize
                f.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(output_x_Min, output_x_Max, output_y_Min, output_y_Max, output_z_Min, output_z_Max))

                
f.close()


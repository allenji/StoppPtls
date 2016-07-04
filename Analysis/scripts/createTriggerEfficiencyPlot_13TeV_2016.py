# Weifeng Ji, Jul 2016
#
#

import sys, os, time
from array import array
from ROOT import *
from math import *

# Run in batch mode
#ROOT.gROOT.SetBatch()

output = TFile('2016_stoppingEff.root', 'RECREATE')

# 2016 stop and gluino points
gluinox2016 = array('d',
                [400.,600.,800.,1000.,1200.,1400.,1600.,1800.,2000.,2200.,2400.,2600.])
gluinoyNum2016 = array('d',
                [3630.,3500.,3290.,3560.,3440.,3710.,3790.,4010.,4210.,4400.,4680.,4820.])
gluinoyDen2016 = array('d',
                [5541.,5390.,5112.,5432.,5317.,5702.,5822.,6247.,6499.,6792.,7138.,7323.])
gluinoxErr2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoyErr2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoy2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

stopx2016 = array('d',
                  [400.,600.,800.,1000.,1200.,1400.,1600.,1800.,2000.,2200.,2400.,2600.])
stopyNum2016 = array('d',
                     [3120., 2850., 2690., 2650., 2630., 2640., 2690., 2680., 2560., 2650., 2720., 2470.])
stopyDen2016 = array('d',
                     [4800., 4450., 4220., 4210., 4080., 3990., 4160., 4100., 3900., 4050., 4090., 3750.])

stopy2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
stopxErr2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
stopyErr2016 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

for i in xrange(0, len(gluinox2016)):
    gluinoy2016[i] = gluinoyNum2016[i]/gluinoyDen2016[i]
    gluinoyErr2016[i] = gluinoy2016[i]*sqrt(1.0/gluinoyNum2016[i] + 1.0/gluinoyDen2016[i])

for i in xrange(0, len(stopx2016)):
    stopy2016[i] = stopyNum2016[i]/stopyDen2016[i]
    stopyErr2016[i] = stopy2016[i]*sqrt(1.0/stopyNum2016[i] + 1.0/stopyDen2016[i])

# TGraphs
geff_gluino2016 = TGraphErrors(len(gluinox2016), gluinox2016, gluinoy2016, gluinoxErr2016, gluinoyErr2016)
geff_stop2016   = TGraphErrors(len(stopx2016), stopx2016, stopy2016, stopxErr2016, stopyErr2016)

geff_gluino2016.SetTitle(';M [GeV/c^{2}];#varepsilon_{trigger}')
geff_gluino2016.SetMarkerStyle(8)
geff_gluino2016.SetMarkerSize(2)
geff_gluino2016.SetMarkerColor(kRed)
geff_gluino2016.SetLineColor(kRed)
geff_gluino2016.SetLineWidth(4)

geff_stop2016.SetTitle(';m [GeV];#varepsilon_{trigger}')
geff_stop2016.SetMarkerStyle(8)
geff_stop2016.SetMarkerSize(2)
geff_stop2016.SetMarkerColor(kBlue)
geff_stop2016.SetLineColor(kBlue)
geff_stop2016.SetLineWidth(4)
#geff_stop2016.SetLineStyle(7)

c1 = TCanvas('c1', '', 1400,1000)
c1.SetGrid()

#blank.Draw()
#geff_gluino.Draw('ALPE1 same')
#geff_stop.Draw('ALPE1 same')

mg = TMultiGraph()
mg.Add(geff_gluino2016)
mg.Add(geff_stop2016)
mg.SetMaximum(1.0)
mg.SetMinimum(0.0)
mg.SetTitle(';M [GeV/c^{2}];#varepsilon_{trigger}')
mg.Draw('aple')

gPad.Modified()
mg.GetXaxis().SetLimits(400,2600)

leg = TLegend(0.50, 0.25 ,0.89, 0.49)
leg.SetTextFont(42)
leg.AddEntry(geff_gluino2016, '2016 gluinos, #tilde{g} #tilde{g}, E_{gluon} = 100 GeV', 'l')
leg.AddEntry(geff_stop2016, '2016 stops, #tilde{t} #tilde{t}, E_{top} = 180 GeV', 'l')
leg.SetHeader("CMS Simulation, #sqrt{s} = 13 TeV")
leg.SetFillColor(kWhite)
leg.SetBorderSize(0)
leg.Draw()

output.Write()
geff_gluino2016.Write()
geff_stop2016.Write()
mg.Write()
c1.RedrawAxis()

c1.RedrawAxis()

#time.sleep(10)
c1.Print('2016_triggerEff_requireHBEB.pdf')

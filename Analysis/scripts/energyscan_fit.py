import ROOT as rt
import array
from math import *
#Run2 signal simulation
x_G600 = [50.,75.,85.,95.,105.,150.,195.,220]
count_G600 = [18, 703, 1180, 1540, 1940, 2410, 2550, 2550]
total_G600 = [5390.,5390.,5390.,5390.,5390.,5390.,5390.,5390.]

x_G1200 = [50.,75.,85.,95.,105.,145.,185.,220.,260.,300]
count_G1200 = [25, 654, 1180, 1620, 1920, 2410, 2510, 2550, 2550, 2540]
total_G1200 = [5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.]

x_G1800 = [250.,300.,350.,400.,450.,500.,550.,595.]
count_G1800 = [3040, 2970, 1960, 1980, 1010, 897, 125, 951]
total_G1800 = [6247., 6247., 4187., 4187., 2208., 1946., 262., 2208.]

allx_Gluino = x_G600 + x_G1200 + x_G1800
allcount_Gluino = count_G600 + count_G1200 + count_G1800
alltotal_Gluino = total_G600 + total_G1200 + total_G1800
allzip_Gluino = zip(allx_Gluino, allcount_Gluino, alltotal_Gluino)
allzip_Gluino.sort()
allx_Gluino = [x for x, y, z in allzip_Gluino]
allcount_Gluino = [y for x, y, z in allzip_Gluino]
alltotal_Gluino = [z for x, y, z in allzip_Gluino]

ally_Gluino, allerr_Gluino, ally_Gplus1, ally_Gminus1 = [], [], [], [] 
for i in range(len(allx_Gluino)):
    ally_Gluino.append(allcount_Gluino[i]/alltotal_Gluino[i])
    allerr_Gluino.append(ally_Gluino[i] * rt.TMath.Sqrt(1./allcount_Gluino[i] + 1./alltotal_Gluino[i]))
    ally_Gplus1.append(ally_Gluino[i] + allerr_Gluino[i])
    ally_Gminus1.append(ally_Gluino[i] - allerr_Gluino[i])

y_G600, err_G600, y_G1200, err_G1200, y_G1800, err_G1800 = [], [], [], [], [], []
for i in range(len(x_G600)):
    y_G600.append(count_G600[i]/total_G600[i])
    err_G600.append(y_G600[i] * rt.TMath.Sqrt(1./count_G600[i] + 1./total_G600[i]))

for i in range(len(x_G1200)):
    y_G1200.append(count_G1200[i]/total_G1200[i])
    err_G1200.append(y_G1200[i] * rt.TMath.Sqrt(1./count_G1200[i] + 1./total_G1200[i]))

for i in range(len(x_G1800)):
    y_G1800.append(count_G1800[i]/total_G1800[i])
    err_G1800.append(y_G1800[i] * rt.TMath.Sqrt(1./count_G1800[i] + 1./total_G1800[i]))

def convert_to_array(input_list):
    return array.array('f', input_list)

graph_G600 = rt.TGraphErrors(len(x_G600), convert_to_array(x_G600), convert_to_array(y_G600), 
                             convert_to_array(len(x_G600)*[0]), convert_to_array(err_G600))
graph_G1200 = rt.TGraphErrors(len(x_G1200), convert_to_array(x_G1200), convert_to_array(y_G1200),
                              convert_to_array(len(x_G1200)*[0]), convert_to_array(err_G1200))
graph_G1800 = rt.TGraphErrors(len(x_G1800), convert_to_array(x_G1800), convert_to_array(y_G1800),
                              convert_to_array(len(x_G1800)*[0]), convert_to_array(err_G1800))
graph_Gluino = rt.TGraphErrors(len(allx_Gluino), convert_to_array(allx_Gluino), convert_to_array(ally_Gluino),
                               convert_to_array(len(allx_Gluino)*[0]), convert_to_array(len(allx_Gluino)*[0]))
graph_GluinoPlus = rt.TGraphErrors(len(allx_Gluino), convert_to_array(allx_Gluino), convert_to_array(ally_Gplus1),
                                   convert_to_array(len(allx_Gluino)*[0]), convert_to_array(len(allx_Gluino)*[0]))
graph_GluinoMinus = rt.TGraphErrors(len(allx_Gluino), convert_to_array(allx_Gluino), convert_to_array(ally_Gminus1),
                                    convert_to_array(len(allx_Gluino)*[0]), convert_to_array(len(allx_Gluino)*[0]))
#graph_GluinoPlus = rt.TGraphErrors(len(allx_Gluino), allx_Gluino, ally_Gplus1, 0, 0)
#graph_GluinoMinus = rt.TGraphErrors(len(allx_Gluino), allx_Gluino, ally_Gminus1, 0, 0)

canvas = rt.TCanvas("reco_eff", "reco_eff", 50, 50, 800, 600)
outputfile = rt.TFile("energyscan_fit_13TeV.root","RECREATE")
canvas.cd()

graph_Gluino.SetTitle(";E_{gluon}(E_{top}) [GeV];#varepsilon_{RECO}")
graph_Gluino.SetMarkerSize(0.1)
graph_Gluino.SetMarkerColor(rt.kWhite)
graph_Gluino.SetMaximum(0.53)
graph_Gluino.GetXaxis().SetLimits(40, 390)
graph_Gluino.Draw("AP")
graph_GluinoPlus.Draw("P same")
graph_GluinoMinus.Draw("P same")

graph_G600.SetLineColor(rt.kRed)
graph_G600.SetMarkerColor(rt.kRed)
graph_G600.SetMarkerStyle(24)
graph_G600.SetMarkerSize(1.15)
graph_G600.SetLineWidth(2)

graph_G1200.SetLineColor(rt.kRed + 2)
graph_G1200.SetMarkerColor(rt.kRed + 2)
graph_G1200.SetMarkerStyle(26)
graph_G1200.SetMarkerSize(1.15)
graph_G1200.SetLineWidth(2)

graph_G1800.SetLineColor(rt.kRed + 3)
graph_G1800.SetMarkerColor(rt.kRed + 3)
graph_G1800.SetMarkerStyle(25)
graph_G1800.SetMarkerSize(1.15)
graph_G1800.SetLineWidth(2)

fit_Gluino = rt.TF1("gfit", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 500)
fit_Gluino.SetParameters(0.25,0.034,2.33,0.25)
fit_GluinoPlus = rt.TF1("gfitp", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 500)
fit_GluinoPlus.SetParameters(0.25,0.034,2.33,0.25)
fit_GluinoPlus.SetFillStyle(1001)
fit_GluinoPlus.SetFillColor(rt.kRed -10)
fit_GluinoPlus.SetLineColor(rt.kRed -10)
fit_GluinoPlus.SetLineWidth(7)
fit_GluinoPlus.Draw("FC same")

fit_GluinoMinus = rt.TF1("gfitm", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 500)
fit_GluinoMinus.SetParameters(0.25,0.034,2.33,0.25)
fit_GluinoMinus.SetFillStyle(1001)
fit_GluinoMinus.SetFillColor(10)
fit_GluinoMinus.SetLineColor(rt.kRed - 10)
fit_GluinoMinus.SetLineWidth(7)
fit_GluinoMinus.Draw("FC same")

graph_G600.Draw("P same")
graph_G1200.Draw("P same")
graph_G1800.Draw("P same")

graph_Gluino.Fit(fit_Gluino)
graph_GluinoPlus.Fit(fit_GluinoPlus)
graph_GluinoMinus.Fit(fit_GluinoMinus)

gluino_max = fit_Gluino.GetMaximum()
print "============== gluino max : " + str(gluino_max) + "=================="
gluino_avg = 0
gluino_syst = 0
for i in range (10, len(allx_Gluino)):
    print str(ally_Gluino[i]) + " - " + str(gluino_max) + " = " + str(fabs(ally_Gluino[i]-gluino_max))
    gluino_avg = gluino_avg + fabs(ally_Gluino[i]-gluino_max)
    if fabs(ally_Gluino[i]-gluino_max) > gluino_syst:
        gluino_syst = fabs(ally_Gluino[i]-gluino_max)
gluino_avg = gluino_avg/(len(allx_Gluino)-10)
print "Systematic error on reco eff: " + str(gluino_syst/gluino_max)


legend = rt.TLegend(0.55,0.15,0.9,0.45,"","brNDC")
legend.SetTextFont(42)
legend.SetHeader("CMS Simulation,  #sqrt{s} = 13 TeV")
legend.AddEntry(graph_G600, "m_{#tilde{g}} = 600 GeV","ep")
legend.AddEntry(graph_G1200, "m_{#tilde{g}} = 1200 GeV","ep")
legend.AddEntry(graph_G1800, "m_{#tilde{g}} = 1800 GeV","ep")
legend.SetFillColor(rt.kWhite)
legend.SetBorderSize(0)
legend.Draw()

outputfile.cd()
canvas.RedrawAxis()
canvas.Write()
canvas.Print("energyscan_fit_13TeV.pdf")
outputfile.Close()


def test():
    print allx_Gluino
#    print allcount_Gluino
#    print alltotal_Gluino
#    print ally_Gluino
#    print allerr_Gluino
#    print ally_Gplus1
#    print ally_Gminus1
 
test()

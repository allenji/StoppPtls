import ROOT as rt
import array
from math import *
from CMS_lumi import *
#Run2 signal simulation
#Gluino counting
x_G600 = [50.,75.,85.,95.,105.,150.,195.,220]
count_G600 = [24, 815, 1396, 1745, 2111, 2773, 2937, 2906]
total_G600 = [5390.,5390.,5390.,5390.,5390.,5390.,5390.,5390.]

x_G1200 = [50.,75.,85.,95.,105.,145.,185.,220.,260.,300]
count_G1200 = [23, 792, 1330, 1833, 2132, 2784, 2910, 2921, 2904, 2912]
total_G1200 = [5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.,5317.]

x_G1800 = [250.,300.,350.,400.,450.,500.,550.,595.]
count_G1800 = [3489, 2249, 3310, 3309, 3333, 2191, 3146, 3079]
total_G1800 = [6247., 4187., 6247., 6247., 6247., 4187., 6247., 6247.]

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
#Stop counting
x_S400 = [98., 111., 141., 189., 210., 231.]
count_S400 = [941, 1239, 1569, 1848, 1879, 1951]
total_S400 = [4797., 4797., 4797., 4797., 4797., 4797.]

x_S600 = [99., 192., 251., 299.]
count_S600 = [904, 1723, 1821, 1763]
total_S600 = [4449., 4449., 4449., 4449.]

#x_S1000 = [250., 300., 351., 400., 450., 500., 510.]
x_S1000 = [250., 300., 351., 400., 450., 500.]
#count_S1000 = [1716, 1342, 1692, 1686, 1594, 1657, 1590]
count_S1000 = [1716, 1342, 1692, 1686, 1594, 1657]
#total_S1000 = [4205., 3295., 4205., 4205., 4205., 4205., 4205.]
total_S1000 = [4205., 3295., 4205., 4205., 4205., 4205.]

allx_Stop = x_S400 + x_S600 + x_S1000
allcount_Stop = count_S400 + count_S600 + count_S1000
alltotal_Stop = total_S400 + total_S600 + total_S1000
allzip_Stop = zip(allx_Stop, allcount_Stop, alltotal_Stop)
allzip_Stop.sort()
allx_Stop = [x for x, y, z in allzip_Stop]
allcount_Stop = [y for x, y, z in allzip_Stop]
alltotal_Stop = [z for x, y, z in allzip_Stop]

ally_Stop, allerr_Stop, ally_Splus1, ally_Sminus1 = [], [], [], []
for i in range(len(allx_Stop)):
    ally_Stop.append(allcount_Stop[i]/alltotal_Stop[i])
    allerr_Stop.append(ally_Stop[i] * rt.TMath.Sqrt(1./allcount_Stop[i] + 1./alltotal_Stop[i]))
    ally_Splus1.append(ally_Stop[i] + allerr_Stop[i])
    ally_Sminus1.append(ally_Stop[i] - allerr_Stop[i])

y_S400, err_S400, y_S600, err_S600, y_S1000, err_S1000 = [], [], [], [], [], []
for i in range(len(x_S400)):
    y_S400.append(count_S400[i]/total_S400[i])
    err_S400.append(y_S400[i] * rt.TMath.Sqrt(1./count_S400[i] + 1./total_S400[i]))

for i in range(len(x_S600)):
    y_S600.append(count_S600[i]/total_S600[i])
    err_S600.append(y_S600[i] * rt.TMath.Sqrt(1./count_S600[i] + 1./total_S600[i]))

for i in range(len(x_S1000)):
    y_S1000.append(count_S1000[i]/total_S1000[i])
    err_S1000.append(y_S1000[i] * rt.TMath.Sqrt(1./count_S1000[i] + 1./total_S1000[i]))

graph_S400 = rt.TGraphErrors(len(x_S400), convert_to_array(x_S400), convert_to_array(y_S400),
                             convert_to_array(len(x_S400)*[0]), convert_to_array(err_S400))
graph_S600 = rt.TGraphErrors(len(x_S600), convert_to_array(x_S600), convert_to_array(y_S600),
                              convert_to_array(len(x_S600)*[0]), convert_to_array(err_S600))
graph_S1000 = rt.TGraphErrors(len(x_S1000), convert_to_array(x_S1000), convert_to_array(y_S1000),
                              convert_to_array(len(x_S1000)*[0]), convert_to_array(err_S1000))
graph_Stop = rt.TGraphErrors(len(allx_Stop), convert_to_array(allx_Stop), convert_to_array(ally_Stop),
                               convert_to_array(len(allx_Stop)*[0]), convert_to_array(len(allx_Stop)*[0]))
graph_StopPlus = rt.TGraphErrors(len(allx_Stop), convert_to_array(allx_Stop), convert_to_array(ally_Splus1),
                                   convert_to_array(len(allx_Stop)*[0]), convert_to_array(len(allx_Stop)*[0]))
graph_StopMinus = rt.TGraphErrors(len(allx_Stop), convert_to_array(allx_Stop), convert_to_array(ally_Sminus1),
                                    convert_to_array(len(allx_Stop)*[0]), convert_to_array(len(allx_Stop)*[0]))

#making plot
#Gluino
canvas = rt.TCanvas("reco_eff", "reco_eff", 50, 50, 800, 600)
canvas.SetRightMargin(0.8*canvas.GetRightMargin())
canvas.SetLeftMargin(1.3*canvas.GetLeftMargin())
canvas.SetTopMargin(0.7*canvas.GetTopMargin())
canvas.SetBottomMargin(1.5*canvas.GetBottomMargin())
#canvas.SetTicks(canvas.GetTickx(),0)
outputfile = rt.TFile("energyscan_fit_13TeV_2016Simulation_CWR.root","RECREATE")
canvas.cd()
rt.gPad.SetTicks()

graph_Gluino.SetTitle(";E_{g}(E_{t}) [GeV];#varepsilon_{reco}")
ax = rt.TAttAxis(graph_Gluino.GetXaxis())
#ax.SetTitleSize(0.1)
graph_Gluino.GetXaxis().SetTitleSize(0.055)
graph_Gluino.GetXaxis().SetLabelSize(0.055)
graph_Gluino.GetXaxis().SetTitleOffset(1.3)
graph_Gluino.GetYaxis().SetTitleSize(0.065)
graph_Gluino.GetYaxis().SetLabelSize(0.055)
graph_Gluino.SetMarkerSize(0.1)
graph_Gluino.SetMarkerColor(rt.kWhite)
graph_Gluino.SetMaximum(0.75)
graph_Gluino.GetXaxis().SetLimits(40, 510)
graph_Gluino.Draw("AP")
#graph_Gluino.Draw("")
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

fit_Gluino = rt.TF1("gfit", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
fit_Gluino.SetParameters(0.25,0.034,2.33,0.25)
fit_GluinoPlus = rt.TF1("gfitp", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
fit_GluinoPlus.SetParameters(0.25,0.034,2.33,0.25)
fit_GluinoPlus.SetFillStyle(1001)
fit_GluinoPlus.SetFillColor(rt.kRed -10)
fit_GluinoPlus.SetLineColor(rt.kRed -10)
fit_GluinoPlus.SetLineWidth(7)
fit_GluinoPlus.Draw("FC same")

fit_GluinoMinus = rt.TF1("gfitm", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
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

#Stop
graph_S400.SetLineColor(rt.kBlue + 1)
graph_S400.SetMarkerColor(rt.kBlue + 1)
graph_S400.SetMarkerStyle(22)
graph_S400.SetMarkerSize(1.15)
graph_S400.SetLineWidth(2)

graph_S600.SetLineColor(rt.kBlue + 3)
graph_S600.SetMarkerColor(rt.kBlue + 3)
graph_S600.SetMarkerStyle(21)
graph_S600.SetMarkerSize(1.15)
graph_S600.SetLineWidth(2)

graph_S1000.SetLineColor(rt.kCyan + 3)
graph_S1000.SetMarkerColor(rt.kCyan + 3)
graph_S1000.SetMarkerStyle(34)
graph_S1000.SetMarkerSize(1.15)
graph_S1000.SetLineWidth(2)

fit_Stop = rt.TF1("sfit", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
fit_Stop.SetParameters(20, 0.001, -1, -22)
fit_Stop.SetLineColor(rt.kBlue - 9)
fit_Stop.SetRange(50, 510)
fit_StopPlus = rt.TF1("sfitp", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
fit_StopPlus.SetParameters(20, 0.001, -1, -22)
fit_StopPlus.SetRange(50, 510)
fit_StopPlus.SetFillStyle(1001)
fit_StopPlus.SetFillColor(rt.kBlue -10)
fit_StopPlus.SetLineColor(rt.kBlue -10)
fit_StopPlus.SetLineWidth(7)
fit_StopPlus.Draw("FC same")

fit_StopMinus = rt.TF1("sfitm", "[0]*TMath::Erf([1]*x-[2])+[3]", 0, 510)
fit_StopMinus.SetParameters(20, 0.001, -1, -22)
fit_StopMinus.SetFillStyle(1001)
fit_StopMinus.SetFillColor(10)
fit_StopMinus.SetLineColor(rt.kBlue - 10)
fit_StopMinus.SetRange(50, 510)
fit_StopMinus.SetLineWidth(7)
fit_StopMinus.Draw("FC same")

graph_S400.Draw("P same")
graph_S600.Draw("P same")
graph_S1000.Draw("P same")

graph_Stop.Fit(fit_Stop)
graph_StopPlus.Fit(fit_StopPlus)
graph_StopMinus.Fit(fit_StopMinus)

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
print "\n"
stop_max = fit_Stop.GetMaximum()
print "============== stop max : " + str(stop_max) + "=================="
stop_avg = 0
stop_syst = 0
for i in range (4, len(allx_Stop)):
    print str(ally_Stop[i]) + " - " + str(stop_max) + " = " + str(fabs(ally_Stop[i]-stop_max))
    stop_avg = stop_avg + fabs(ally_Stop[i]-stop_max)
    if fabs(ally_Stop[i]-stop_max) > stop_syst:
        stop_syst = fabs(ally_Stop[i]-stop_max)
stop_avg = stop_avg/(len(allx_Stop)-4)
print "Systematic error on reco eff: " + str(stop_syst/stop_max)


legend = rt.TLegend(0.40,0.20,0.9,0.50,"","brNDC")
legend.SetTextFont(42)
legend.SetTextSize(0.045)
#legend.SetHeader("CMS Simulation 2016,  #sqrt{s} = 13 TeV")
legend.AddEntry(graph_G600, "m_{#tilde{g}} = 600 GeV","ep")
legend.AddEntry(graph_G1200, "m_{#tilde{g}} = 1200 GeV","ep")
legend.AddEntry(graph_G1800, "m_{#tilde{g}} = 1800 GeV","ep")
legend.AddEntry(graph_S400, "m_{#tilde{t}} = 400 GeV","ep")
legend.AddEntry(graph_S600, "m_{#tilde{t}} = 600 GeV","ep")
legend.AddEntry(graph_S1000, "m_{#tilde{t}} = 1000 GeV","ep")
legend.SetFillColor(rt.kWhite)
legend.SetBorderSize(0)
legend.Draw()

outputfile.cd()
canvas.RedrawAxis()

pd = rt.gPad
pd.Update()
line = rt.TLine(pd.GetUxmax(), pd.GetUymin(), pd.GetUxmax(), pd.GetUymax())
print pd.GetUxmax()
print pd.GetUymin()
print pd.GetUymax()
line.Draw()
iPeriod = 1
iPos = 11
CMS_lumi(canvas, iPeriod, iPos)
canvas.Write()
canvas.Print("energyscan_fit_13TeV_2016Simulation_CWR_test.pdf")
outputfile.Close()

import ROOT as rt
import copy
import os
import math

def halo_background(IncomingOnlyBeam1_hist,
                    OutgoingOnlyBeam1_hist,
                    BothBeam1_hist,
                    AllBeam1_hist,
                    HaloControlBeam1_hist,
                    IncomingOnlyBeam2_hist,
                    OutgoingOnlyBeam2_hist,
                    BothBeam2_hist,
                    AllBeam2_hist,
                    HaloControlBeam2_hist):

    IneffNumBeam1_hist = IncomingOnlyBeam1_hist.Clone()
    IneffNumBeam1_hist.SetDirectory(0)
    IneffNumBeam1_hist.Multiply(OutgoingOnlyBeam1_hist)
    IneffDenBeam1_hist = BothBeam1_hist.Clone()
    IneffDenBeam1_hist.SetDirectory(0)
    IneffDenBeam1_hist.Multiply(AllBeam1_hist)
    IneffFractionBeam1_hist = IneffNumBeam1_hist.Clone()
    IneffFractionBeam1_hist.SetDirectory(0)
    IneffFractionBeam1_hist.Divide(IneffDenBeam1_hist)
    BackgroundBeam1_hist = IneffFractionBeam1_hist.Clone()
    BackgroundBeam1_hist.SetDirectory(0)
    BackgroundBeam1_hist.Multiply(HaloControlBeam1_hist)

    nIncomingOnlyBeam1 = IncomingOnlyBeam1_hist.GetEntries()
    nOutgoingOnlyBeam1 = OutgoingOnlyBeam1_hist.GetEntries()
    nBothBeam1 = BothBeam1_hist.GetEntries()
    nAllBeam1 = AllBeam1_hist.GetEntries()
    epsBeam1 = nIncomingOnlyBeam1*nOutgoingOnlyBeam1/(nBothBeam1*nAllBeam1)
    eps_errBeam1 = epsBeam1*math.sqrt(1./nIncomingOnlyBeam1 + 1./nOutgoingOnlyBeam1 + 4./nBothBeam1)
    print "Beam1: \n"
    print  "       N_incoming * N_outgoing      " + str(nIncomingOnlyBeam1) + " * " + str(nOutgoingOnlyBeam1) + "\n"
    print  " eps = -----------------------  =  ----------------------- " + "\n"
    print  "           N_both * N_all           " + str(nBothBeam1) +  " * " + str(nAllBeam1)  + "\n"
    print  "" + "\n"
    print  " eps = " + "%.3f" %epsBeam1 + " +/- " + "%.3f" %eps_errBeam1 + "\n"
    print  " N_haloEvents = " + str(HaloControlBeam1_hist.Integral()) + "\n"
    print  "" + "\n"
    errorBeam1 = rt.Double(0)
    integralBeam1 = BackgroundBeam1_hist.IntegralAndError(1,BackgroundBeam1_hist.GetNbinsX(),
                                                          1,BackgroundBeam1_hist.GetNbinsY(),
                                                          errorBeam1)
    print " background = " + "%.3f" %integralBeam1 + " +/- " + "%.3f" %errorBeam1 + "\n"
    print "----------------------------------------------------------------\n"


    IneffNumBeam2_hist = IncomingOnlyBeam2_hist.Clone()
    IneffNumBeam2_hist.SetDirectory(0)
    IneffNumBeam2_hist.Multiply(OutgoingOnlyBeam2_hist)
    IneffDenBeam2_hist = BothBeam2_hist.Clone()
    IneffDenBeam2_hist.SetDirectory(0)
    IneffDenBeam2_hist.Multiply(AllBeam2_hist)
    IneffFractionBeam2_hist = IneffNumBeam2_hist.Clone()
    IneffFractionBeam2_hist.SetDirectory(0)
    IneffFractionBeam2_hist.Divide(IneffDenBeam2_hist)
    BackgroundBeam2_hist = IneffFractionBeam2_hist.Clone()
    BackgroundBeam2_hist.SetDirectory(0)
    BackgroundBeam2_hist.Multiply(HaloControlBeam2_hist)

    nIncomingOnlyBeam2 = IncomingOnlyBeam2_hist.GetEntries()
    nOutgoingOnlyBeam2 = OutgoingOnlyBeam2_hist.GetEntries()
    nBothBeam2 = BothBeam2_hist.GetEntries()
    nAllBeam2 = AllBeam2_hist.GetEntries()
    epsBeam2 = nIncomingOnlyBeam2*nOutgoingOnlyBeam2/(nBothBeam2*nAllBeam2)
    eps_errBeam2 = epsBeam2*math.sqrt(1./nIncomingOnlyBeam2 + 1./nOutgoingOnlyBeam2 + 4./nBothBeam2)
    print "Beam2: \n"
    print  "       N_incoming * N_outgoing      " + str(nIncomingOnlyBeam2) + " * " + str(nOutgoingOnlyBeam2) + "\n"
    print  " eps = -----------------------  =  ----------------------- " + "\n"
    print  "           N_both * N_all           " + str(nBothBeam2) +  " * " + str(nAllBeam2) + "\n"
    print  "" + "\n"
    print  " eps = " + "%.3f" %epsBeam2 + " +/- " + "%.3f" %eps_errBeam2 + "\n"
    print  " N_haloEvents = " + str(HaloControlBeam2_hist.Integral()) + "\n"
    print  "" + "\n"
    errorBeam2 = rt.Double(0)
    integralBeam2 = BackgroundBeam2_hist.IntegralAndError(1,BackgroundBeam2_hist.GetNbinsX(),
                                                          1,BackgroundBeam2_hist.GetNbinsY(),
                                                          errorBeam2)
    print " background = " + "%.3f" %integralBeam2 + " +/- " + "%.3f" %errorBeam2 + "\n"
    print "----------------------------------------------------------------\n"
    print "----------------------------------------------------------------\n"
    
    return [IneffFractionBeam1_hist,HaloControlBeam1_hist,BackgroundBeam1_hist,
            IneffFractionBeam2_hist,HaloControlBeam2_hist,BackgroundBeam2_hist,
            integralBeam1,integralBeam2,errorBeam1,errorBeam2]

if __name__ == "__main__":

    #read in input files and histograms
    inputfile = rt.TFile("/data/users/jalimena/condor/HaloBackground/NoBPTX_2015D.root","READ")

    xyIntegralBeam1 = -1
    xyIntegralBeam2 = -1
    rPhiIntegralBeam1 = -1
    rPhiIntegralBeam2 = -1
    xyErrorBeam1 = -1
    xyErrorBeam2 = -1
    

    for a in range(1,3):
        if a==1:
            print "doing halo background\n"
            outputfile = rt.TFile("/data/users/jalimena/condor/HaloBackground/halo_background.root", "RECREATE")

            IncomingOnlyBeam1_hist = inputfile.Get("IncomingOnlyBeam1Plotter/Eventvariable Plots/meanCscX_meanCscY")
            OutgoingOnlyBeam1_hist = inputfile.Get("OutgoingOnlyBeam1Plotter/Eventvariable Plots/meanCscX_meanCscY")
            BothBeam1_hist = inputfile.Get("BothBeam1Plotter/Eventvariable Plots/meanCscX_meanCscY")
            AllBeam1_hist = inputfile.Get("AllBeam1Plotter/Eventvariable Plots/meanCscX_meanCscY")
            HaloControlBeam1_hist = inputfile.Get("HaloControlBeam1Plotter/Eventvariable Plots/meanCscX_meanCscY")

            IncomingOnlyBeam2_hist = inputfile.Get("IncomingOnlyBeam2Plotter/Eventvariable Plots/meanCscX_meanCscY")
            OutgoingOnlyBeam2_hist = inputfile.Get("OutgoingOnlyBeam2Plotter/Eventvariable Plots/meanCscX_meanCscY")
            BothBeam2_hist = inputfile.Get("BothBeam2Plotter/Eventvariable Plots/meanCscX_meanCscY")
            AllBeam2_hist = inputfile.Get("AllBeam2Plotter/Eventvariable Plots/meanCscX_meanCscY")
            HaloControlBeam2_hist = inputfile.Get("HaloControlBeam2Plotter/Eventvariable Plots/meanCscX_meanCscY")

        if a==2:
            print "doing halo background systematic\n"
            outputfile = rt.TFile("/data/users/jalimena/condor/HaloBackground/halo_background_systematic.root", "RECREATE")

            IncomingOnlyBeam1_hist = inputfile.Get("IncomingOnlyBeam1Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            OutgoingOnlyBeam1_hist = inputfile.Get("OutgoingOnlyBeam1Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            BothBeam1_hist = inputfile.Get("BothBeam1Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            AllBeam1_hist = inputfile.Get("AllBeam1Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            HaloControlBeam1_hist = inputfile.Get("HaloControlBeam1Plotter/Eventvariable Plots/meanCscR_meanCscPhi")

            IncomingOnlyBeam2_hist = inputfile.Get("IncomingOnlyBeam2Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            OutgoingOnlyBeam2_hist = inputfile.Get("OutgoingOnlyBeam2Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            BothBeam2_hist = inputfile.Get("BothBeam2Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            AllBeam2_hist = inputfile.Get("AllBeam2Plotter/Eventvariable Plots/meanCscR_meanCscPhi")
            HaloControlBeam2_hist = inputfile.Get("HaloControlBeam2Plotter/Eventvariable Plots/meanCscR_meanCscPhi")

        IncomingOnlyBeam1_hist.RebinX(10)
        OutgoingOnlyBeam1_hist.RebinX(10)
        BothBeam1_hist.RebinX(10)
        AllBeam1_hist.RebinX(10)
        HaloControlBeam1_hist.RebinX(10)
        IncomingOnlyBeam2_hist.RebinX(10)
        OutgoingOnlyBeam2_hist.RebinX(10)
        BothBeam2_hist.RebinX(10)
        AllBeam2_hist.RebinX(10)
        HaloControlBeam2_hist.RebinX(10)

        IncomingOnlyBeam1_hist.RebinY(10)
        OutgoingOnlyBeam1_hist.RebinY(10)
        BothBeam1_hist.RebinY(10)
        AllBeam1_hist.RebinY(10)
        HaloControlBeam1_hist.RebinY(10)
        IncomingOnlyBeam2_hist.RebinY(10)
        OutgoingOnlyBeam2_hist.RebinY(10)
        BothBeam2_hist.RebinY(10)
        AllBeam2_hist.RebinY(10)
        HaloControlBeam2_hist.RebinY(10)

        #calculate background estimate
        result_background = halo_background(IncomingOnlyBeam1_hist,
                                            OutgoingOnlyBeam1_hist,
                                            BothBeam1_hist,
                                            AllBeam1_hist,
                                            HaloControlBeam1_hist,
                                            IncomingOnlyBeam2_hist,
                                            OutgoingOnlyBeam2_hist,
                                            BothBeam2_hist,
                                            AllBeam2_hist,
                                            HaloControlBeam2_hist)

        #write output plots 
        outputfile.cd()
        result_background[0].SetTitle("Beam 1 Inefficiency")
        result_background[0].Write("IneffFractionBeam1_hist")
        result_background[1].SetTitle("Beam 1 Halo Events")
        result_background[1].Write("HaloControlBeam1_hist")
        result_background[2].SetTitle("Beam 1 Halo Background Estimate")
        result_background[2].Write("BackgroundBeam1_hist")
        result_background[3].SetTitle("Beam 2 Inefficiency")
        result_background[3].Write("IneffFractionBeam2_hist")
        result_background[4].SetTitle("Beam 2 Halo Events")
        result_background[4].Write("HaloControlBeam2_hist")
        result_background[5].SetTitle("Beam 2 Halo Background Estimate")
        result_background[5].Write("BackgroundBeam2_hist")
        outputfile.Close()

        if a==1:
                xyIntegralBeam1 = result_background[6]
                xyIntegralBeam2 = result_background[7]
                xyErrorBeam1 = result_background[8]
                xyErrorBeam2 = result_background[9]
        if a==2:
                rPhiIntegralBeam1 = result_background[6]
                rPhiIntegralBeam2 = result_background[7]
        
    print "TOTAL background = " + "%.3f" %(xyIntegralBeam1+xyIntegralBeam2) + " +/- " + "%.3f" %(math.sqrt(xyErrorBeam1*xyErrorBeam1+xyErrorBeam2*xyErrorBeam2))+" (stat) +/- " + "%.3f" %(math.fabs(xyIntegralBeam1+xyIntegralBeam2-rPhiIntegralBeam1+rPhiIntegralBeam2)) +" (syst.)\n"        

    #outputtext = open(outputdir + "/halo_background.txt", "w")
    #outputtext.write("DT by barrel RPC background: ")
    #outputtext.write(str(result_background[3])+" +/- "+str(result_background[6])+"\n")
    #outputtext.write("Smeared background: ")
    #outputtext.write(str(result_background[4])+" +/- "+str(result_background[7])+"\n")
    #outputtext.write("Uncertainty background: ")
    #outputtext.write(str(result_background[5])+" +/- "+str(result_background[8]))
    #outputtext.close()
    


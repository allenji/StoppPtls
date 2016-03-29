import ROOT as rt
import copy

def cosmic_inefficiency(hist_untagged, hist_all):
    # both input histos should be made from cosmic MC samples
    hist_untagged_uncert = copy.copy(hist_untagged)
    # adding systematic uncertainty
    for i in range(1, hist_untagged_uncert.GetNbinsX()+1):
        for j in range(1, hist_untagged_uncert.GetNbinsY()+1):
            if hist_untagged_uncert.GetBinContent(i,j) == 0:
                hist_untagged_uncert.SetBinContent(i,j,0.01)

    hist_all.Sumw2()
    hist_ineff = copy.copy(hist_untagged)
    hist_ineff.Sumw2()
    hist_ineff.Divide(hist_all)
    hist_ineff_uncert = copy.copy(hist_untagged_uncert)
    hist_ineff_uncert.Sumw2()
    hist_ineff_uncert.Divide(hist_all)

    error_binned = rt.Double(0)
    error_binned_uncert = rt.Double(0)
    ineff_binned = hist_ineff.IntegralAndError(1,hist_ineff.GetNbinsX(),
                                               1,hist_ineff.GetNbinsY(),
                                               error_binned)
    ineff_binned_uncert = hist_ineff_uncert.IntegralAndError(1,hist_ineff_uncert.GetNbinsX(),
                                                              1,hist_ineff_uncert.GetNbinsY(),
                                                              error_binned_uncert)
    # return histograms(with and without uncert) , as well as their integrals and errors
    return [hist_ineff, hist_ineff_uncert, ineff_binned, ineff_binned_uncert,
            error_binned, error_binned_uncert]

def cosmic_background(hist_ineff, hist_ineff_uncert, hist_NMinusOne):
    hist_NMinusOne_smeared = copy.copy(hist_NMinusOne)
    # do smearing to N-1 histogram
    nx = hist_NMinusOne_smeared.GetNbinsX()
    ny = hist_NMinusOne_smeared.GetNbinsY()
    for i in reversed(range(1, nx+1)):
        for j in range(1, ny+1):
            if (hist_NMinusOne_smeared.GetBinContent(x, y) == 0.):
                if x == 1: z = hist_NMinusOne_smeared.GetBinContent(x+1, y)/2.
                elif x == nx: z = hist_NMinusOne_smeared.GetBinContent(x-1, y)/2.
                else: z = (hist_NMinusOne_smeared.GetBinContent(x-1, y) + 
                          hist_NMinusOne_smeared.GetBinContent(x+1, y))/2.
                hist_NMinusOne_smeared.SetBinContent(x, y, z)

    hist_background = copy.copy(hist_NMinusOne)
    hist_background_smeared = copy.copy(hist_NMinusOne_smeared)
    hist_background_uncert = copy.copy(hist_NMinusOne_smeared)
    hist_background.Multiply(hist_ineff)
    hist_background_smeared.Multiply(hist_ineff)
    hist_background_uncert.Multiply(hist_ineff_uncert)

    error = rt.Double(0)
    error_smeared = rt.Double(0)
    error_uncert = rt.Double(0)

    background = hist_background.IntegralAndError(1, hist_background.GetNbinsX(),
                                                  1, hist_background.GetNbinsY(),
                                                  error)
    background_smeared = hist_background_smeared.IntegralAndError(1, hist_background_smeared.GetNbinsX(),
                                                                  1, hist_background_smeared.GetNbinsY(),
                                                                  error_smeared)
    background_uncert = hist_background_uncert.IntegralAndError(1, hist_background_uncert.GetNbinsX(),
                                                                1, hist_background_uncert.GetNbinsY(),
                                                                error_uncert)
    
    return [hist_background, hist_background_smeared, hist_background_uncert,
            background, background_smeared, background_uncert,
            error, error_smeared, error_uncert]

if __name__ == "__main__":
    file_test = rt.TFile("/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_7_4_5_ROOT5/src/StoppPtls/StandardAnalysis/test/condor/rpcstudy_94_CosmicControlSampleFromCtrlDatasets/NoBPTX_2015Dv4_controlSample.root", "READ")
    h1 = file_test.Get("CosmicMuonControlSelectionPlotter/Rpchit Plots/rpcHitXVsY")
    output_file = rt.TFile("output.root", "RECREATE")
    result = cosmic_inefficiency(h1, h1)
    h2 = rt.TH1D("a","a",10,0,10)
    print "the number of bins is"
    print h2.GetNbinsX() 
    print h2.GetBinContent(111)
    h3 = copy.copy(h2)
    h2.Fill(5)
    h2.Fill(5)
    h2.Fill(5)
    h3.Fill(5)
    h3.Fill(5)
    h2.Fill(-1)
    h2.Fill(-2)
    h2.Fill(10)
    h2.Fill(11)
    h2.SetBinContent(6,100)
    print h2.GetBinContent(6)
    print h2.GetBinContent(0)
    print h2.GetBinContent(11)
    h3.Fill(8)

    print "Seems like it passed"
    for i in range(2, 6):
        print result[i]
    output_file.cd()
    result[0].Write("dummy1")
    result[1].Write("dummy2")
    h2.Multiply(h3)
    h2.Write("dummy3")
    h3.Write("dummy4")
    output_file.Close()
    #from here starts the serious stuff
    """inputfile_untagged = rt.TFile("","READ")
    inputfile_all = rt.TFile("","READ")
    inputfile_NMinusOne = rt.TFile("","READ")
    outputfile = rt.TFile("cosmic_background.root", "RECREATE")

    histogram_untagged = inputfile_untagged.Get("")
    histogram_all = inputfile_all.Get("")
    histogram_NMinusOne = inputfile_NMinusOne.Get("")

    result_inefficiency = cosmic_inefficiency(histogram_untagged, histogram_all)
    result_background = cosmic_background(result_inefficiency[0], result_inefficiency[1],
                                          histogram_NMinusOne)

    #write output plots 
    output_file.cd()
    result_inefficiency[0].Write("cosmic_inefficiency")
    result_inefficiency[1].Write("cosmic_inefficiency_uncert")
    result_background[0].Write("cosmic_background")
    result_background[1].Write("cosmic_background_smeared")
    result_background[2].Write("cosmic_background_smeared_uncert")
    output_file.Close()"""

    output_text = open("cosmic_background.txt", "w")
    output_text.write("cosmic crap")
    output_text.close()
    


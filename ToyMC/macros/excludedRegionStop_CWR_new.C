#include <sstream>

#include "TGraph.h"
#include "TGaxis.h"
#include "TF1.h"
#include "TGraphAsymmErrors.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TH1.h"
#include "TH1F.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TPaveText.h"

#include "ExtraLimitPlots.h"
#include "CMS_lumi.C" 

void excludedRegionStop_CWR_new() {
  double stopNum[] = {5494.,4797.,4449.,4215.,4205.,4076.,3993.};
  double stopDenom[] = {95902.,96352.,99608.,100000.,100000.,100000.,100000};
  double stopStopEff[7] = {0};
  for (int i = 0; i!= 7; ++i) {
    stopStopEff[i] = stopNum[i]/stopDenom[i];
  }

  double stopMass = 173.0; // used for limit plots

  //double data[32]  = { 70.,     470,    450,     30,   21,  60,   42,
  double data[32]  = { 70.,     744,    450,     30,   21,  60,   42,
		       100.,	530.,   480.,    38,   23,  70,   46,
		       150.,	550,    500.,    45,   25,  90,   50,
		       200.,	550,    510.,    36,   25,  72,   50};
	
  double e[4]           = { data[0], data[7], data[14], data[21] };
  double obs[4]         = { data[1], data[8], data[15], data[22]  };
  double exp[4]         = { data[2], data[9], data[16], data[23]  };
  double exp_1sig_hi[4] = { data[3], data[10], data[17], data[24]  };
  double exp_1sig_lo[4] = { data[4], data[11], data[18], data[25]  };
  double exp_2sig_hi[4] = { data[5], data[12], data[19], data[26]  };
  double exp_2sig_lo[4] = { data[6], data[13], data[20], data[27]  };
  
  double e_g[4]       = {175., 200., 300., 360. };
  
  cout << "Energy thresholds : " << e[0] << ", " << e[1] << ", " << e[2] << ", " << e[3] << std::endl;
  cout << "Obs limit         : " << obs[0] << ", " << obs[1] << ", " << obs[2] << ", " << obs[3] << std::endl;
  cout << "Exp limit         : " << exp[0] << ", " << exp[1] << ", " << exp[2] << ", " << exp[3] << std::endl;
  
  // plot as fn of E_cut
  TGraphAsymmErrors g_exp_1sig(4, &e[0], &exp[0], 0, 0, &exp_1sig_lo[0], &exp_1sig_hi[0]);
  TGraphAsymmErrors g_exp_2sig(4, &e[0], &exp[0], 0, 0, &exp_2sig_lo[0], &exp_2sig_hi[0]);
  TGraph g_exp(4, &e[0], &exp[0]); 
  TGraph g_obs(4, &e[0], &obs[0]); 

  // exclusion in m_stop, m_neutralino plane	
  TFile f("excludedRegionStop_CWR_new.root","RECREATE");

  double m_chi0[1000];
  double m_chi0sq[1000];
  for (int i=0; i<1000; i++) {
    m_chi0[i] = i;
    m_chi0sq[i] = (i)*(i);
  }
  
  
  // observed exclusion
  double obsExcl70[1000];
  double obsExcl100[100];
  double obsExcl150[100];
  double obsExcl200[100];
  double obsExclFull[100];
  int npoints70=0;
  int npoints100=0;
  int npoints150=0;
  int npoints200=0;
  int npointsFull=0;

  int start70 = 0;
  int start70exp = 0;
  int start70expp1 = 0;
  int start70expm1 = 0;
  int start100 = 0;
  int start150 = 0;
  int start200 = 0;
  int startFull = 0;

  double expExcl70[1000];
  double expExcl70p1[1000];
  double expExcl70m1[1000];


  int expExcl70v = 701;
  int expExcl70p1v = 755;
  int expExcl70m1v = 638;

  int npoints_expExcl70 = 0;
  int npoints_expExcl70p1 = 0;
  int npoints_expExcl70m1 = 0;

  for (int i=0; i<1000; ++i) {
    expExcl70[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (expExcl70[i]>expExcl70v) break;
    npoints_expExcl70++;
  }

  for (int i=0; i<1000; ++i) {
    expExcl70p1[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (expExcl70p1[i]>expExcl70p1v) break;
    npoints_expExcl70p1++;
  }

  for (int i=0; i<1000; ++i) {
    expExcl70m1[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (expExcl70m1[i]>expExcl70m1v) break;
    npoints_expExcl70m1++;
  }

  for (int i=0; i<1000; ++i) {
    obsExcl70[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (obsExcl70[i]>obs[0]) break;
    npoints70++;
  }

  for (int i=0; i<100; ++i) {
    obsExcl100[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (obsExcl100[i]>obs[1]) break;
    npoints100++;
  }

  
  // For small values of m_chi0, on-shell top mass is fine. 
  // But as m_chi0 increases, we need to decrease the top mass (take it off-shell)
  // Starting off-shell means that the calculated stop mass is larger than the limit
  /*
  for (int i=0; i<100; ++i) {
    double tmp = e_g[2] + sqrt(e_g[2]*e_g[2] + m_chi0sq[i]-stopMass*stopMass);
    if (isnan(tmp)) {
      start150 = i + 1;
      continue;
    }
    obsExcl150[i] = tmp;
    if (obsExcl150[i]>obs[2]) break;
    npoints150++;
  }
  
  for (int i=0; i<100; ++i) {
    double tmp = e_g[3] + sqrt(e_g[3]*e_g[3] + m_chi0sq[i]-stopMass*stopMass);
    if (isnan(tmp)) {
      start200 = i + 1;
      continue;
    }
    obsExcl200[i] = tmp;
    if (obsExcl200[i]>obs[2]) break;	
    npoints200++;	
  }

  for (int i=0; i<100; ++i) {
    double tmp = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0sq[i]-stopMass*stopMass);
    if (isnan(tmp)) {
      startFull = i + 1;
      continue;
    }
    obsExclFull[i] = tmp;
    if (obsExclFull[i]>obs[1]) break;	
    npointsFull++;	
  }
  */
	
	
  TGraph g_obsExcl70(npoints70+1,&obsExcl70[start70], &m_chi0[start70]);
  cout << start70 << endl;
  cout << "a" << obsExcl70[start70] << m_chi0[start70] << endl;
  //TGraph g_obsExcl70(npoints70+1, &m_chi0[start70], &obsExcl70[start70]);
  g_obsExcl70.SetPoint(npoints70, obs[0], 0.);
  //g_obsExcl70.SetPoint(npoints70, 0., obs[0]);
  TGraph g_obsExcl70exp(npoints_expExcl70+1,&expExcl70[start70exp], &m_chi0[start70exp]);
  g_obsExcl70exp.SetPoint(npoints_expExcl70, expExcl70v, 0.);

  TGraph g_obsExcl70expp1(npoints_expExcl70p1+1,&expExcl70p1[start70expp1], &m_chi0[start70expp1]);
  g_obsExcl70expp1.SetPoint(npoints_expExcl70p1, expExcl70p1v, 0.);

  TGraph g_obsExcl70expm1(npoints_expExcl70m1+1,&expExcl70m1[start70expm1], &m_chi0[start70expm1]);
  g_obsExcl70expm1.SetPoint(npoints_expExcl70m1, expExcl70m1v, 0.);

  TGraph g_obsExcl100(npoints100+1, &m_chi0[start100], &obsExcl100[start100]);
  g_obsExcl100.SetPoint(npoints100, 0., obs[1]);
  TGraph g_obsExcl150(npoints150+1, &m_chi0[start150], &obsExcl150[start150]);
  g_obsExcl150.SetPoint(npoints150, 0., obs[2]);
  TGraph g_obsExcl200(npoints200+1, &m_chi0[start200], &obsExcl200[start200]);
  g_obsExcl200.SetPoint(npoints200, 0., obs[3]);
  TGraph g_obsExclFull(npointsFull+1, &m_chi0[startFull], &obsExclFull[startFull]);
  g_obsExclFull.SetPoint(npointsFull, 0., obs[1]);


  TCanvas canvas3("excludedRegionStop", "");
  //canvas3 = new TCanvas("excludedRegionStop", "");
  canvas3.SetBottomMargin(1.1*canvas3.GetBottomMargin());
  canvas3.SetLeftMargin(0.9*canvas3.GetLeftMargin());
  //canvas3.SetRightMargin(0.2);
  cout << "nimei" << canvas3.GetRightMargin() << endl;


  //-------------------------
  // MAKE ALL THE TEXT BLURBS
  //-------------------------
  //TH1F h3("h3", "", 1, 0., 650.);
	TH2F h3("stopxsec", "",400, 0, 800, 400, 0, 650);
  h3.SetStats (0);

  h3.SetMinimum (30);
  //h3.SetMaximum (55);
  h3.GetYaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  h3.GetXaxis()->SetTitleSize(0.058);
  h3.GetXaxis()->SetTitleOffset(1.1);
  h3.GetXaxis()->SetLabelSize(0.05);
  h3.GetYaxis()->SetTitleOffset(1.1);
  h3.GetXaxis()->SetTitle("m_{#tilde{t}} [GeV]");
  h3.GetYaxis()->SetTitleSize(0.058);
  h3.GetYaxis()->SetLabelSize(0.05);
  h3.Draw();

  canvas3.SetRightMargin(0.15);
  canvas3.SetLeftMargin(0.8*canvas3.GetLeftMargin());

  gStyle->SetPalette(kRainBow);
  //TFile  F("rehi.root","RECREATE");
  //TH2F h3("stopxsec","",275, 0, 550, 350, 100, 800);
  //h3.GetXaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  //h3.GetYaxis()->SetTitle("m_{#tilde{t}}   [GeV]  ");
  h3.SetStats (0);
  //h4.GetZaxis()->SetRange(0.001, 1000);
  //h4.SetMinimum(0.01);
  for (int i = 1; i <= 400; i++){
    for (int j = 1; j <= 400; j++) {
      double superTopMass = i * 800.0 / 400;
      double chi0Mass = j * 650./ 400;
      double lowLimit = e_g[0] + sqrt(e_g[0]*e_g[0] + chi0Mass * chi0Mass -stopMass*stopMass);
      int massPoint = superTopMass / 200;
      double superTopMassRef = 744;
      int massPointRef = superTopMassRef / 200;
      double eff = stopStopEff[massPoint - 1] + (stopStopEff[massPoint] - stopStopEff[massPoint - 1]) * (superTopMass - 200*massPoint) / 200;
      double effRef = stopStopEff[massPointRef - 1] + (stopStopEff[massPointRef] - stopStopEff[massPointRef - 1]) * (superTopMassRef - 200*massPointRef) / 200;
      if (superTopMass < 400){
      //cout << eff << endl;
      }
      //double xsec = stop_xs.mass2xsec(100+ 2*j);
      //cout << xsec << endl;
      if (superTopMass > lowLimit) {
      h3.SetBinContent(i, j, (0.045)*1000*effRef/(eff));
      }
    }
  }

  //h3.GetZaxis()->SetTitle("95% CL upper limit on #sigma#bf{#it{#Beta}} [pb]");
  //h3.GetZaxis()->SetMaxDigits(2);
  h3.GetZaxis()->SetTitle("95% CL upper limit on #sigma(pp #rightarrow #tilde{t}#tilde{t}) #bf{#it{#Beta}}(#tilde{t} #rightarrow t#tilde{#chi}^{0}) [fb]");
  h3.Draw("COLZ");
  h3.SetContour(1000);
  h3.GetZaxis()->SetTitleOffset(1);

  TGraph disallowed(4);
  disallowed.SetPoint(0, 0., 0.);
  disallowed.SetPoint(1, 30000., 30000.);
  disallowed.SetPoint(2, 0., 30000);
  //disallowed.SetPoint(3, 0., 0.);
  disallowed.SetFillColor(kGray);
  //disallowed.SetFillStyle(3001);
  disallowed.Draw("FL");

  TText dislabel(0.46, 0.6, "Kinematically forbidden");
  dislabel.SetNDC(true);
  dislabel.SetTextFont(42);
  dislabel.SetTextSize(0.045);
  dislabel.SetTextAngle(42); //638 by 372
  dislabel.Draw();

  //	TPaveText blurb3(0.48, 0.15, 0.6, 0.37, "NDC");
  TPaveText blurb3(0.14, 0.40, 0.72, 0.65, "NDC");
  //blurb3.AddText("CMS preliminary 2015+2016");
  //blurb3.AddText("#int L dt = 2.7 + 35.9 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb3.AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
 //blurb3.AddText("#sqrt{s} = 13 TeV");
  blurb3.AddText("10 #mus < #tau < 1000 s");
  blurb3.AddText("#tilde{t} #rightarrow t#tilde{#chi}^{0}");
  blurb3.AddText("E_{t} > 170 GeV"); 
  //blurb3.AddText("95% CL Exclusion contours");
  blurb3.SetTextFont(42);
  blurb3.SetBorderSize(0);
  blurb3.SetFillColor(kGray);
  blurb3.SetFillStyle(4001);
  blurb3.SetShadowColor(0);
  blurb3.SetTextAlign(12);
  blurb3.SetTextSize(0.045);
  blurb3.Draw();	
	
  TLegend leg3(0.15, 0.65, 0.45, 0.82,"","NDC");
  leg3.SetTextSize(0.05);
  leg3.SetBorderSize(0);
  leg3.SetTextFont(42);
  leg3.SetFillColor(kGray);
  leg3.SetFillStyle(4001);
  //leg3.AddEntry(&g_obsExcl100, "E_{thresh} > 100 GeV", "lf");
  //leg3.AddEntry(&g_obsExcl150, "E_{thresh} > 150 GeV", "lf");
  //leg3.AddEntry(&g_obsExcl200, "E_{thresh} > 200 GeV", "lf");

  //----------------------
  //FORMAT AND DRAW GRAPHS
  //----------------------
  g_obsExclFull.SetLineWidth(302);
  g_obsExclFull.SetFillColor(kYellow);
  g_obsExclFull.SetLineColor(kYellow);
  //g_obsExclFull.Draw("f");

  TGraph* g_obs70y = (TGraph*)g_obsExcl70.Clone("70y");
  //g_obs70y->SetFillColor(kOrange);
  g_obs70y->SetLineWidth(3);
  g_obs70y->SetLineColor(kBlack);
  g_obs70y->Draw("L");

  //g_obs70y->Draw("f");
  leg3.AddEntry(g_obs70y, "Observed", "l");
  leg3.AddEntry(&g_obsExcl70exp, "Median expected", "l");
  leg3.AddEntry(&g_obsExcl70expp1, "68% expected", "l");
  leg3.Draw();
  TGraph* g_obs100y = (TGraph*)g_obsExcl100.Clone("100y");
  g_obs100y->SetFillColor(kYellow);
  //g_obs100y->Draw("f");
  
  g_obsExcl70.SetLineWidth(3);
  g_obsExcl70.SetFillStyle(0);
  g_obsExcl70.SetFillColor(kBlack);
  g_obsExcl70.SetLineColor(kBlack);
  //g_obsExcl70.Draw("L");

  g_obsExcl70exp.SetLineWidth(2);
  g_obsExcl70exp.SetLineStyle(7);
  g_obsExcl70exp.SetLineColor(kBlack);
  g_obsExcl70exp.Draw("L");

  g_obsExcl70expp1.SetLineWidth(2);
  g_obsExcl70expp1.SetLineStyle(3);
  g_obsExcl70expp1.SetLineColor(kBlack);
  g_obsExcl70expp1.Draw("L");

  g_obsExcl70expm1.SetLineWidth(2);
  g_obsExcl70expm1.SetLineStyle(3);
  g_obsExcl70expm1.SetLineColor(kBlack);
  g_obsExcl70expm1.Draw("L");
	
  g_obsExcl100.SetLineWidth(302);
  g_obsExcl100.SetFillStyle(3004);
  g_obsExcl100.SetFillColor(kBlue);
  g_obsExcl100.SetLineColor(kBlue);
 // g_obsExcl100.Draw();
	
  g_obsExcl150.SetLineWidth(302);
  g_obsExcl150.SetFillStyle(3004);
  g_obsExcl150.SetFillColor(kBlack);
  g_obsExcl150.SetLineColor(kBlack);
  //g_obsExcl150.Draw();
	
  g_obsExcl200.SetLineWidth(302);
  g_obsExcl200.SetFillStyle(3005);
  g_obsExcl200.SetFillColor(kRed);
  g_obsExcl200.SetLineColor(kRed);
  //g_obsExcl200.Draw();
	
  TLatex t1(0.50, 0.44, "E_{thresh} > 70 GeV");
  t1.SetNDC(true);
  t1.SetTextFont(42);
  t1.SetTextSize(0.04);
  t1.SetTextAngle(25);
  t1.SetTextColor(kGreen+2);
  //t1.Draw();
	
  TLatex t2(0.36, 0.45, "E_{thresh} > 100 GeV");
  t2.SetNDC(true);
  t2.SetTextFont(42);
  t2.SetTextSize(0.03);
  t2.SetTextAngle(22);
  t2.SetTextColor(kBlue);
  //t2.Draw();
	
	
  TLatex t3(0.29, 0.55, "E_{thresh} > 150 GeV");
  t3.SetNDC(true);
  t3.SetTextFont(42);
  t3.SetTextSize(0.03);
  t3.SetTextAngle(14);
  t3.SetTextColor(kBlack);
  //t3.Draw();

  TLatex t4(0.2, 0.69, "E_{thresh} > 200 GeV");
  t4.SetNDC(true);
  t4.SetTextFont(42);
  t4.SetTextSize(0.03);
  t4.SetTextAngle(5);
  t4.SetTextColor(kRed);
  //t4.Draw();
			
  h3.Draw("sameaxis");
	
  int iPeriod = 4;
  int iPos=11;
  CMS_lumi(&canvas3, iPeriod, iPos);

  g_obs70y->Write();
  g_obsExcl70exp.Write("expExcl70");
  g_obsExcl70expp1.Write("expExcl70p1");
  g_obsExcl70expm1.Write("expExcl70m1");
  f.Write();

  canvas3.Print("excludedRegionStop_awesome.pdf");
  canvas3.Print("excludedRegionStop.eps");
  /*

   double g_mass [26] = {
    200 ,     250 ,     300 ,     350 ,     400 ,
    450 ,     500 ,     550 ,     600 ,     650 ,
    700 ,     750 ,     800 ,     850 ,     900 ,
    950 ,    1000 ,    1050 ,    1100 ,    1150 ,
    1200 , 1250, 1300, 1350, 1400, 1450};
  double g_xsec [26] = {
    3574,      1190,     462,     202,     98.0,
    50.4,      27.4,    15.6,     9.20,    5.60,
    3.53,      2.27,     1.49,   0.996,   0.677,
    0.466,     0.325,  0.229,   0.163,  0.118,
    0.0856, 0.0627, 0.046, 0.035, 0.025, 0.0189
  };
  double g_xsecdcpl [26] = {
    3574,      1190,     462,     202,     98.0,
    50.4,      27.4,    15.6,     9.20,    5.60,
    3.53,      2.27,     1.49,   0.996,   0.677,
    0.466,     0.325,  0.229,   0.163,  0.118,
    0.0856, 0.0627, 0.046, 0.035, 0.025, 0.0189
  };
  double s_mass [21] = {
    100 ,     150 ,     200 ,     250 ,     300 ,
    350 ,     400 ,     450 ,     500 ,     550 ,
    600 ,     650 ,     700 ,     750 ,     800 ,
    850 ,     900 ,     950 ,    1000 ,    1050 ,
    1100 };
  double s_xsec [21] = {
    1521,       249.4,     64.5,     21.6,     8.51,
    3.79,        1.84,    0.948,   0.518,   0.296,
    0.175,      0.107,  0.067,  0.0431,  0.0283,
    0.0190,    0.0129, 0.00883, 0.00615, 0.00432,
    0.00307
  }; 

class Xsection {
  vector<double> masses;
  vector<double> logXsecs;
public:
  Xsection (const vector<double>& m, const double* xs) {
    masses = m;
    for (size_t i = 0; i < masses.size(); ++i) logXsecs.push_back (xs[i]);
  }
  double mass2xsec (double mass) {
    double logXsec = 0;
    if (mass < masses.front() || mass > masses.back()) {
      cerr << "gluinoXsection::mass2xsec-> mass is beyond the range: " << mass << endl;
      return 0;
    }
    int index = 0;
    while (mass > masses[index]) ++index;
    if (index == 0) logXsec = logXsecs[0];
    else logXsec = logXsecs[index-1] + (mass-masses[index-1])*(logXsecs[index]-logXsecs[index-1])/(masses[index]-masses[index-1]);
    return 1.e-3*pow(10, logXsec/20.);
  }
};
vector<double> masses;
  for (int i = 0; i < 19; ++i)  {
    masses.push_back(s_mass[i]);
    s_xsec [i] = log10 (s_xsec [i]*1e3) * 20.;
  }
Xsection stop_xs (masses, s_xsec);

  TCanvas canvas4("stopLimitVsMChiXSec", "");
  //canvas4.SetLogz();
  canvas4.SetRightMargin(0.15);

  gStyle->SetPalette(87);
  TFile  F("rehi.root","RECREATE");
  TH2F h4("stopxsec","",275, 0, 550, 350, 100, 800);
  h4.GetXaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  h4.GetYaxis()->SetTitle("m_{#tilde{t}}   [GeV]  ");
  h4.SetStats (0);
  //h4.GetZaxis()->SetRange(0.001, 1000);
  //h4.SetMinimum(0.01);
  for (int i = 1; i <= 275; i++){
    for (int j = 1; j <= 350; j++) {
      double superTopMass = 100 + 2*j;
      double chi0Mass = 2*i;
      double lowLimit = e_g[0] + sqrt(e_g[0]*e_g[0] + chi0Mass * chi0Mass -stopMass*stopMass);
      int massPoint = superTopMass / 200;
      double eff = stopStopEff[massPoint - 1] + (stopStopEff[massPoint] - stopStopEff[massPoint - 1]) * (superTopMass - 200*massPoint) / 200;
      if (superTopMass < 400){
      //cout << eff << endl;
      }
      double xsec = stop_xs.mass2xsec(100+ 2*j);
      //cout << xsec << endl;
      if (superTopMass > lowLimit) {
      h4.SetBinContent(i, j, (10.65/6200)/(eff*0.374));
      }
    }
  }

  h4.GetZaxis()->SetTitle("95% CL upper limit on #sigma [pb]");
  h4.Draw("COLZ");
  h4.SetContour(1000);
  TGraph disallowed1(4);
  disallowed1.SetPoint(0, 100., 100.);
  disallowed1.SetPoint(1, 550., 550.);
  disallowed1.SetPoint(2, 550., 100.);
  //disallowed.SetPoint(3, 0., 0.);
  disallowed1.SetFillColor(19);
  //disallowed1.SetFillStyle(4001);
  disallowed1.Draw("FL");

  g_obsExcl70.SetLineColor(kBlack);
  g_obsExcl70.SetLineWidth(2);

  g_obsExcl70.SetFillStyle(0);
  g_obsExcl70.SetFillColor(0);
  g_obsExcl70.Draw("L");

  TText dislabel1(0.65, 0.42, "Kinematically forbidden");
  dislabel1.SetNDC(true);
  dislabel1.SetTextFont(42);
  dislabel1.SetTextSize(0.030);
  dislabel1.SetTextAngle(30);
  dislabel1.Draw();

TPaveText blurb4(0.50, 0.13, 0.68, 0.35, "NDC");
  blurb4.AddText("CMS preliminary 2015+2016");
  blurb4.AddText("#int L dt = 2.5+12.8 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");

  blurb4.AddText("#sqrt{s} = 13 TeV");
  blurb4.AddText("10 #mus < #tau < 1000 s");
  //blurb3.AddText("95% CL Exclusion contours");
  blurb4.SetTextFont(42);
  blurb4.SetBorderSize(0);
  blurb4.SetFillColor(kGray);
  blurb4.SetFillStyle(4001);
  blurb4.SetShadowColor(0);
  blurb4.SetTextAlign(12);
  blurb4.SetTextSize(0.030);
  blurb4.Draw();

  TLegend leg4(0.69, 0.15, 0.92, 0.37,"95% CL Excluded","NDC");
  leg4.SetTextSize(0.030);
  leg4.SetBorderSize(0);
  leg4.SetTextFont(42);
  leg4.SetFillColor(kGray);
  leg4.SetFillStyle(4001);
  leg4.AddEntry(&g_obsExcl70, "Obs. Limit", "lf");
  leg4.Draw();
  h4.Write("",TObject::kOverwrite);
  h4.Draw("sameaxis");
  canvas4.Print("excludedRegionStopXsec.pdf");
  */
}



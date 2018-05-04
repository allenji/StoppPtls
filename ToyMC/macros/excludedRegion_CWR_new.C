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
#include "TStyle.h"

#include "ExtraLimitPlots.h"
#include "CMS_lumi.C"
//#include "gluinostopMassLifetime.C"

void excludedRegion() {
  gStyle->SetPalette(57);
  double gluinoNum[] = {6781.,5541.,5390.,5112.,5432.,5317., 5822., 6247.};
  double gluinoDenom[] = {98893., 99405., 99410., 98459., 99306., 99013., 99411., 98800.};
  double gluinoStopEff[8] = {0};
  for (int i=0; i != 8; ++i) {
     gluinoStopEff[i] = gluinoNum[i]/gluinoDenom[i];
  }

  double data[32]  = { 70.,     1385,     857,     46.2,    32.0,    92.4,   64.0,
  //double data[32]  = { 70.,     890,     857,     46.2,    32.0,    92.4,   64.0,
		       100.,	990.,   981.,    89.2,    50.2,   178.4,  100.4,
		       150.,	1010,     927.,    62.7,    39.6,   125.4,   79.2,
		       200.,	1020.,    944.,    48.5,    37.4,    97.0,   74.8};
	
  double e[4]           = { data[0], data[7], data[14], data[21] };
  double obs[4]         = { data[1], data[8], data[15], data[22]  };
  double exp[4]         = { data[2], data[9], data[16], data[23]  };
  double exp_1sig_hi[4] = { data[3], data[10], data[17], data[24]  };
  double exp_1sig_lo[4] = { data[4], data[11], data[18], data[25]  };
  double exp_2sig_hi[4] = { data[5], data[12], data[19], data[26]  };
  double exp_2sig_lo[4] = { data[6], data[13], data[20], data[27]  };
  
  double e_g[4]       = {130., 150., 220., 320. };
  
  cout << "Energy thresholds : " << e[0] << ", " << e[1] << ", " << e[2] << ", " << e[3] << std::endl;
  cout << "Obs limit         : " << obs[0] << ", " << obs[1] << ", " << obs[2] << ", " << obs[3] << std::endl;
  cout << "Exp limit         : " << exp[0] << ", " << exp[1] << ", " << exp[2] << ", " << exp[3] << std::endl;
  
  // plot as fn of E_cut
  TGraphAsymmErrors g_exp_1sig(4, &e[0], &exp[0], 0, 0, &exp_1sig_lo[0], &exp_1sig_hi[0]);
  TGraphAsymmErrors g_exp_2sig(4, &e[0], &exp[0], 0, 0, &exp_2sig_lo[0], &exp_2sig_hi[0]);
  TGraph g_exp(4, &e[0], &exp[0]); 
  TGraph g_obs(4, &e[0], &obs[0]); 
  
  TCanvas canvas("gluinoLimitVsE", "", 1200, 1000);
  
  TH1F* h = new TH1F ("h", "", 1,  70., 200.);
  h->SetStats (0);
  h->SetMinimum (500);
  h->SetMaximum (1000);
  h->GetXaxis()->SetTitle("E_{cut} [GeV]");
  h->GetYaxis()->SetTitle("m_{#tilde{g}}   [GeV]  ");
  h->Draw();
  
  TPaveText* blurb = new TPaveText(0.25, 0.67, 0.50, 0.87, "NDC");
  blurb->AddText("#int L dt = 18.6 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb->AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
  blurb->AddText("#sqrt{s} = 8 TeV");
  blurb->SetTextFont(42);
  blurb->SetBorderSize(0);
  blurb->SetFillColor(0);
  blurb->SetShadowColor(0);
  blurb->SetTextAlign(12);
  blurb->SetTextSize(0.04);
  blurb->Draw();
  
  
  g_exp_2sig.SetLineColor(0);
  g_exp_2sig.SetLineStyle(0);
  g_exp_2sig.SetLineWidth(0);
  g_exp_2sig.SetFillColor(kYellow);
  g_exp_2sig.SetFillStyle(1001);
  g_exp_2sig.Draw("3");
  
  g_exp_1sig.SetLineColor(0);
  g_exp_1sig.SetLineStyle(0);
  g_exp_1sig.SetLineWidth(0);
  g_exp_1sig.SetFillColor(kGreen);
  g_exp_1sig.SetFillStyle(1001);
  g_exp_1sig.Draw("3");
  
  g_exp.SetLineStyle(2);
  g_exp.SetLineWidth(2);
  g_exp.Draw("L3");
  
  g_obs.SetLineStyle(1);
  g_obs.SetLineWidth(2);
  g_obs.SetLineColor(kBlack);
  g_obs.Draw("L");
  
  TLegend leg(0.70, 0.65, 0.82, 0.90,"95% CL Limits:","NDC");
  leg.SetTextSize(0.04);
  leg.SetBorderSize(0);
  leg.SetTextFont(42);
  leg.SetFillColor(0);
  leg.AddEntry(&g_obs, "Observed", "l");
  TGraph expectedStyle1(g_exp);
  expectedStyle1.SetFillColor(g_exp_1sig.GetFillColor());
  TGraph expectedStyle2(g_exp);
  expectedStyle2.SetFillColor(g_exp_2sig.GetFillColor());
  leg.AddEntry(&expectedStyle1, "Expected #pm1#sigma", "lf");
  leg.AddEntry(&expectedStyle2, "Expected #pm2#sigma", "lf");
  leg.Draw();
	
  canvas.Print("gluinoLimitVsECut.pdf");


  // plot as fn of E_gluon
	
  TGraphAsymmErrors g2_exp_1sig(4, &e_g[0], &exp[0], 0, 0, &exp_1sig_lo[0], &exp_1sig_hi[0]);
  TGraphAsymmErrors g2_exp_2sig(4, &e_g[0], &exp[0], 0, 0, &exp_2sig_lo[0], &exp_2sig_hi[0]);
  TGraph g2_exp(4, &e_g[0], &exp[0]); 
  TGraph g2_obs(4, &e_g[0], &obs[0]); 
  
  TCanvas canvas2("gluinoLimitVsEVis", "", 1200, 1000);
  
  TH1F h2("h2", "", 1,  100., 300.);
  h2.SetStats (0);
  h2.SetMinimum (500);
  h2.SetMaximum (1000);
  h2.GetXaxis()->SetTitle("E_{gluon} [GeV]");
  h2.GetYaxis()->SetTitle("m_{#tilde{g}}   [GeV]  ");
  h2.Draw();
  
  TPaveText blurb2(0.25, 0.67, 0.50, 0.87, "NDC");
  blurb2.AddText("#int L dt = 18.6 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb2.AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
  blurb2.AddText("#sqrt{s} = 8 TeV");
  blurb2.SetTextFont(42);
  blurb2.SetBorderSize(0);
  blurb2.SetFillColor(0);
  blurb2.SetShadowColor(0);
  blurb2.SetTextAlign(12);
  blurb2.SetTextSize(0.04);
  blurb2.Draw();
  
  
  g2_exp_2sig.SetLineColor(0);
  g2_exp_2sig.SetLineStyle(0);
  g2_exp_2sig.SetLineWidth(0);
  g2_exp_2sig.SetFillColor(kYellow);
  g2_exp_2sig.SetFillStyle(1001);
  g2_exp_2sig.Draw("3");
  
  g2_exp_1sig.SetLineColor(0);
  g2_exp_1sig.SetLineStyle(0);
  g2_exp_1sig.SetLineWidth(0);
  g2_exp_1sig.SetFillColor(kGreen);
  g2_exp_1sig.SetFillStyle(1001);
  g2_exp_1sig.Draw("3");
  
  g2_exp.SetLineStyle(2);
  g2_exp.SetLineWidth(2);
  g2_exp.Draw("L3");
  
  g2_obs.SetLineStyle(1);
  g2_obs.SetLineWidth(2);
  g2_obs.SetLineColor(kBlack);
  g2_obs.Draw("L");
  
  TLegend leg2(0.67, 0.65, 0.82, 0.87,"95% CL Limits:","NDC");
  leg2.SetTextSize(0.04);
  leg2.SetBorderSize(0);
  leg2.SetTextFont(42);
  leg2.SetFillColor(0);
  leg2.AddEntry(&g2_obs, "Observed", "l");
  leg2.AddEntry(&expectedStyle1, "Expected #pm1#sigma", "lf");
  leg2.AddEntry(&expectedStyle2, "Expected #pm2#sigma", "lf");
  leg2.Draw();
  
  canvas2.Print("gluinoLimitVsEGluon.pdf");
  
  

  // exclusion in m_gluino m_neutralino plane
	
  double m_chi0[1400];
  for (int i=0; i<1400; ++i) {
    m_chi0[i] = i;
  }
  
  // observed exclusion
  double obsExcl70[1400];
  double obsExcl100[100];
  double obsExcl150[100];
  double obsExcl200[100];
  double obsExclFull[100];
  int npoints70=0;
  int npoints100=0;
  int npoints150=0;
  int npoints200=0;	
  int npointsFull=0;

  double expExcl70[1400];
  double expExcl70p1[1400];
  double expExcl70m1[1400];


  int expExcl70v = 1314;
  int expExcl70p1v = 1397;
  int expExcl70m1v = 1219;

  int npoints_expExcl70 = 0;
  int npoints_expExcl70p1 = 0;
  int npoints_expExcl70m1 = 0;

  for (int i=0; i<1400; ++i) {
    expExcl70[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);
    if (expExcl70[i]>expExcl70v) break;
    npoints_expExcl70++;
  }

  for (int i=0; i<1400; ++i) {
    expExcl70p1[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);
    if (expExcl70p1[i]>expExcl70p1v) break;
    npoints_expExcl70p1++;
  }

  for (int i=0; i<1400; ++i) {
    expExcl70m1[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);
    if (expExcl70m1[i]>expExcl70m1v) break;
    npoints_expExcl70m1++;
  }

  for (int i=0; i<1400; ++i) {
    obsExcl70[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);
    if (obsExcl70[i]>obs[0]) break;	
    npoints70++;
  }
	
  for (int i=0; i<100; ++i) {
    obsExcl100[i] = e_g[1] + sqrt(e_g[1]*e_g[1] + m_chi0[i]*m_chi0[i]);
    if (obsExcl100[i]>obs[1]) break;	
    npoints100++;
  }	
	
  int mchi_ind = 0;
  for (int i=0; i<100; ++i) {
    obsExcl150[i] = e_g[2] + sqrt(e_g[2]*e_g[2] + m_chi0[i]*m_chi0[i]);
    if (obsExcl150[i]>obs[3]) break;	
    npoints150++;
    mchi_ind = i;
  }
	
  for (int i=0; i<100; ++i) {
    obsExcl200[i] = e_g[3] + sqrt(e_g[3]*e_g[3] + m_chi0[i]*m_chi0[i]);		
    if (obsExcl200[i]>obs[3]) break;	
    npoints200++;	
  }	

  // Full exclusion plot
  for (int i=0; i<100; ++i) {
    obsExclFull[i] = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);		
    if (obsExclFull[i]>obs[3]) break;	
    //if (i > mchi_ind) break;	
    npointsFull++;	
  }	
	
  //exp limits
	TGraph g_expExcl70(npoints_expExcl70+1, &expExcl70[0], &m_chi0[0]);
	g_expExcl70.SetPoint(npoints_expExcl70+1, expExcl70v, m_chi0[0]);
	TGraph g_expExcl70p1(npoints_expExcl70p1+1, &expExcl70p1[0], &m_chi0[0]);
	g_expExcl70p1.SetPoint(npoints_expExcl70p1+1, expExcl70p1v, m_chi0[0]);
	TGraph g_expExcl70m1(npoints_expExcl70m1+1, &expExcl70m1[0], &m_chi0[0]);
	g_expExcl70m1.SetPoint(npoints_expExcl70m1+1, expExcl70m1v, m_chi0[0]);
  //TGraph g_obsExcl70(npoints70+1, &m_chi0[0], &obsExcl70[0]);
  TGraph g_obsExcl70(npoints70+1, &obsExcl70[0],&m_chi0[0]);
  //g_obsExcl70.SetPoint(npoints70, 0., obs[0]);
  g_obsExcl70.SetPoint(npoints70, obs[0], 0.);
  TGraph g_obsExcl100(npoints100+1, &m_chi0[0], &obsExcl100[0]);
  g_obsExcl100.SetPoint(npoints100, 0., obs[1]);
  TGraph g_obsExcl150(npoints150+1, &m_chi0[0], &obsExcl150[0]);
  g_obsExcl150.SetPoint(npoints150, 0., obs[2]);
  TGraph g_obsExcl200(npoints200+1, &m_chi0[0], &obsExcl200[0]);
  g_obsExcl200.SetPoint(npoints200, 0., obs[3]);
  TGraph g_obsExclFull(npointsFull+1, &m_chi0[0], &obsExclFull[0]);
  g_obsExclFull.SetPoint(npointsFull, 0., obs[3]);
  //g_obsExclFull.SetPoint(npointsFull, m_chi0[mchi_ind], obs[3]);

  /**
  // expected exclusion
  double expExcl70[100];
  double expExcl100[100];
  double expExcl150[100];
  double expExcl200[100];
  npoints70=0;
  npoints100=0;
  npoints150=0;
  npoints200=0;	

  for (int i=0; i<100; ++i) {
    expExcl70[i]  = e_g[0] + sqrt(e_g[0]*e_g[0] + m_chi0[i]*m_chi0[i]);
    if (expExcl70[i]>exp[0]) break;	
    npoints70++;
  }

  for (int i=0; i<100; ++i) {
    expExcl100[i] = e_g[1] + sqrt(e_g[1]*e_g[1] + m_chi0[i]*m_chi0[i]);
    if (expExcl100[i]>exp[1]) break;	
    npoints100++;
  }	
	
  for (int i=0; i<100; ++i) {
    expExcl150[i] = e_g[2] + sqrt(e_g[2]*e_g[2] + m_chi0[i]*m_chi0[i]);
    if (expExcl150[i]>exp[2]) break;	
    npoints150++;
  }
	
  for (int i=0; i<100; ++i) {
    expExcl200[i] = e_g[3] + sqrt(e_g[3]*e_g[3] + m_chi0[i]*m_chi0[i]);		
    if (expExcl200[i]>exp[3]) break;	
    npoints200++;	
  }	
  
  TGraph g_expExcl70(npoints70+1, &m_chi0[0], &expExcl70[0]);
  g_expExcl70.SetPoint(npoints70, 0., exp[0]);
  TGraph g_expExcl100(npoints100+1, &m_chi0[0], &expExcl100[0]);
  g_expExcl100.SetPoint(npoints100, 0., exp[1]);
  TGraph g_expExcl150(npoints150+1, &m_chi0[0], &expExcl150[0]);
  g_expExcl150.SetPoint(npoints150, 0., exp[2]);
  TGraph g_expExcl200(npoints200+1, &m_chi0[0], &expExcl200[0]);
  g_expExcl200.SetPoint(npoints200, 0., exp[3]);
  */	
  TCanvas canvas3("gluinoLimitVsMChi", "");
  //canvas3 = new TCanvas("gluinoLimitVsMChi", "");
  canvas3.SetLeftMargin(0.9*canvas3.GetLeftMargin());
  canvas3.SetBottomMargin(1.1*canvas3.GetBottomMargin());
  canvas3.SetRightMargin(3*canvas3.GetRightMargin());

  //TH1F h3("h3", "", 1,  0., 1600.);
  TH2F h3("gluinoxsec","",400, 0, 1600, 400, 0, 1400);
  h3.SetStats (0);
  //h3.SetMinimum (0);
  //h3.SetMaximum (1400);
  //h3.GetXaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  h3.GetYaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  h3.GetXaxis()->SetTitleSize(0.058);
  h3.GetXaxis()->SetLabelSize(0.05);
  //h3.GetYaxis()->SetTitle("m_{#tilde{g}}   [GeV]  ");
  h3.GetXaxis()->SetTitle("m_{#tilde{g}} [GeV]");
  h3.GetYaxis()->SetTitleSize(0.058);
  h3.GetYaxis()->SetTitleOffset(1.2);
  h3.GetXaxis()->SetTitleOffset(1.1);
  h3.GetYaxis()->SetLabelSize(0.05);
  //h3.Draw();
  h3.SetContour(1000);
  //h4.GetXaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  //h4.GetYaxis()->SetTitle("m_{#tilde{g}}   [GeV]  ");
  h3.SetStats (0);
  //h4.GetZaxis()->SetRange(0.001, 1000);
  //h4.SetMinimum(0.1);


  for (int i = 1; i <= 400; i++){
    for (int j = 1; j <= 400; j++) {
      double gluinoMass = 4*i;
      double chi0Mass = 3.5*j;
      double lowLimit = e_g[0] + sqrt(e_g[0]*e_g[0] + chi0Mass*chi0Mass);
      //double xsec = gluino_xs.mass2xsec(200+ 6*j);
      //cout << xsec << endl;

      int massPoint = gluinoMass / 200;
      double gluinoMassRef = 1385;
      int massPointRef = gluinoMassRef / 200;
      double eff = gluinoStopEff[massPoint - 1] + (gluinoStopEff[massPoint] - gluinoStopEff[massPoint - 1]) * (gluinoMass - 200*massPoint)/ 200;
      double effRef = gluinoStopEff[massPointRef - 1] + (gluinoStopEff[massPointRef] - gluinoStopEff[massPointRef - 1]) * (gluinoMassRef - 200*massPointRef)/ 200;
      if (gluinoMass > lowLimit) {
      h3.SetBinContent(i, j, 0.0278*1000*effRef/eff);
          //(10.66/6200)/(eff*0.50));
      }
    }
  }
  h3.GetZaxis()->SetTitle("95% CL upper limit on #sigma(pp #rightarrow #tilde{g}#tilde{g}) #bf{#it{#Beta}}(#tilde{g} #rightarrow g#tilde{#chi}^{0}) [fb]");
  h3.GetZaxis()->SetLimits(0.01,0.03);
  //h3.GetZaxis()->SetLimits(0.01,0.03);
  //h3.SetMaximum(40);
  h3.SetMinimum(22);
  h3.GetZaxis()->SetTitleOffset(1);
  h3.Draw("COLZ");
  

  TGraph disallowed(4);
  disallowed.SetPoint(0, 0., 0.);
  disallowed.SetPoint(1, 1400., 1400.);
  disallowed.SetPoint(2, 0., 1400.);
  //disallowed.SetPoint(3, 0., 0.);
  disallowed.SetFillColor(kGray);
  //disallowed.SetFillStyle(3001);
  disallowed.Draw("FL");
  

  TText dislabel(0.50, 0.60, "Kinematically forbidden");
  dislabel.SetNDC(true);
  dislabel.SetTextFont(42);
  dislabel.SetTextSize(0.045);
  dislabel.SetTextAngle(41);
  dislabel.Draw();
  

  //	TPaveText blurb3(0.48, 0.15, 0.6, 0.37, "NDC");
  TPaveText blurb3(0.16, 0.40, 0.72, 0.65, "NDC");
  //blurb3.AddText("CMS preliminary 2015+2016");
  //blurb3.AddText("#int L dt = 2.7 + 35.9 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb3.AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
  //blurb3.AddText("#sqrt{s} = 13 TeV");
  blurb3.AddText("10 #mus < #tau < 1000 s");
  blurb3.AddText("#tilde{g} #rightarrow g#tilde{#chi}^{0}");//,  #int L_{eff} dt = 935 pb^{-1}");
  blurb3.AddText("E_{g} > 130 GeV");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb3.AddText("95% CL Exclusion contours");
  blurb3.SetTextFont(42);
  blurb3.SetBorderSize(0);
  blurb3.SetFillColor(kGray);
  blurb3.SetFillStyle(4001);
  blurb3.SetShadowColor(0);
  blurb3.SetTextAlign(12);
  blurb3.SetTextSize(0.05);
  blurb3.Draw();	
	
  TLegend leg3(0.18, 0.65, 0.50, 0.82,"","NDC");
  leg3.SetTextSize(0.050);
  leg3.SetBorderSize(0);
  leg3.SetTextFont(42);
  leg3.SetFillColor(kGray);
  leg3.SetFillStyle(4001);
  
  //leg3.AddEntry(&g_obsExcl70, "E_{jet} > 70 GeV", "lf");
  //leg3.AddEntry(&g_obsExcl100, "E_{thresh} > 100 GeV", "lf");
  //leg3.AddEntry(&g_obsExcl150, "E_{thresh} > 150 GeV", "lf");
  //leg3.AddEntry(&g_obsExcl200, "E_{thresh} > 200 GeV", "lf");

	g_expExcl70.SetLineColor(kBlack);
	g_expExcl70.SetLineWidth(2);
  g_expExcl70.SetLineStyle(7);
	g_expExcl70.Draw("L");

	g_expExcl70p1.SetLineColor(kBlack);
	g_expExcl70p1.SetLineWidth(2);
  g_expExcl70p1.SetLineStyle(3);
	g_expExcl70p1.Draw("L");

	g_expExcl70m1.SetLineColor(kBlack);
	g_expExcl70m1.SetLineWidth(2);
  g_expExcl70m1.SetLineStyle(3);
	g_expExcl70m1.Draw("L");
  

  g_obsExclFull.SetLineWidth(302);
  //g_obsExclFull.SetFillStyle(3004);
  g_obsExclFull.SetFillColor(kOrange);
  g_obsExclFull.SetLineColor(6);
  //g_obsExclFull.Draw("f");

  TGraph* g_obs70y = (TGraph*)g_obsExcl70.Clone("70y");
  //g_obs70y->SetFillColor(kOrange);
  g_obs70y->SetLineColor(kBlack);
  g_obs70y->SetLineWidth(3);
  g_obs70y->Draw("L");
  //g_obs70y->Draw();
  TGraph* g_obs100y = (TGraph*)g_obsExcl100.Clone("100y");
  g_obs100y->SetFillColor(kYellow);
  //g_obs100y->Draw("f");
  TGraph* g_obs150y = (TGraph*)g_obsExcl150.Clone("150y");
  g_obs150y->SetFillColor(kYellow);
  //g_obs150y->Draw("f");
  TGraph* g_obs200y = (TGraph*)g_obsExcl200.Clone("200y");
  g_obs200y->SetFillColor(kYellow);
  //g_obs200y->Draw("f");
  
  
  leg3.AddEntry(g_obs70y, "Observed", "l");
  leg3.AddEntry(&g_expExcl70, "Median expected", "l");
  leg3.AddEntry(&g_expExcl70p1, "68% expected", "l");
  //leg3.AddEntry(&g_expExcl70m1, "median expected", "lf");
  leg3.Draw();
  g_obsExcl70.SetLineWidth(302);
  g_obsExcl70.SetFillStyle(0);
  g_obsExcl70.SetFillColor(kBlack);
  g_obsExcl70.SetLineColor(kBlack);
  //g_obsExcl70.SetLineStyle(9);
  //g_obsExcl70.Draw("L");
  /*

  //g_expExcl70.SetLineStyle(3);
  //g_expExcl70.SetLineColor(kGreen+2);	
  //g_expExcl70.Draw();
	
  g_obsExcl100.SetLineWidth(302);
  g_obsExcl100.SetFillStyle(3004);
  g_obsExcl100.SetFillColor(kBlue);
  g_obsExcl100.SetLineColor(kBlue);
  //g_obsExcl100.SetLineStyle(9);
  g_obsExcl100.Draw();

  //g_expExcl100.SetLineStyle(3);
  //g_expExcl100.SetLineColor(kBlue);
  //g_expExcl100.Draw();
	
  g_obsExcl150.SetLineWidth(302);
  g_obsExcl150.SetFillStyle(3004);
  g_obsExcl150.SetFillColor(kBlack);
  g_obsExcl150.SetLineColor(kBlack);
  //g_obsExcl150.SetLineStyle(9);
  g_obsExcl150.Draw();

  //g_expExcl150.SetLineStyle(3);
  //g_expExcl150.SetLineColor(kBlack);
  //g_expExcl150.Draw();
	
  g_obsExcl200.SetLineWidth(302);
  g_obsExcl200.SetFillStyle(3005);
  g_obsExcl200.SetFillColor(kRed);
  g_obsExcl200.SetLineColor(kRed);
  //g_obsExcl200.SetLineStyle(9);
  g_obsExcl200.Draw();
	
  //g_expExcl200.SetLineStyle(3);
  //g_expExcl200.SetLineColor(kRed);
  //g_expExcl200.Draw();
	
  TLatex t1(0.50, 0.44, "E_{thresh} > 70 GeV");
  t1.SetNDC(true);
  t1.SetTextFont(42);
  t1.SetTextSize(0.03);
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
  */
/*
			
  h3.Draw("sameaxis");
  int iPeriod = 4;
  int iPos=11;
  cout << "nimei" << endl;

  CMS_lumi(&canvas3, iPeriod, iPos);	
  canvas3.Print("excludedRegion_awesome.pdf");
  canvas3.Print("excludedRegion_awesome.eps");
  */

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

  vector<double> masses;
  for (int i = 0; i < 26; ++i)  {
    masses.push_back(g_mass[i]);
    g_xsec [i] = log10 (g_xsec [i]*1e3) * 20.;
    g_xsecdcpl [i] = log10 (g_xsecdcpl [i]*1e3) * 20.;
  }

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
  //  Xsection gluino_xs (masses, g_xsec);
  Xsection gluino_xs (masses, g_xsecdcpl);

  //TCanvas canvas4("gluinoLimitVsMChiXSec", "");
  //canvas4.SetLogz();
  //canvas4.SetRightMargin(0.15);
  
  gStyle->SetPalette(kRainBow);
  TFile  F("rehi.root","RECREATE");
  //TH2F h4("gluinoxsec","",200, 0, 1200, 200, 200, 1400);
  //TF2 h4("gluinoxsec", "x+y", 0, 1200, 200, 1400);
  /*
  h3.SetContour(1000);
  //h4.GetXaxis()->SetTitle("m_{#tilde{#chi}^{0}} [GeV]");
  //h4.GetYaxis()->SetTitle("m_{#tilde{g}}   [GeV]  ");
  h3.SetStats (0);
  //h4.GetZaxis()->SetRange(0.001, 1000);
  //h4.SetMinimum(0.1);

  
  for (int i = 1; i <= 200; i++){
    for (int j = 1; j <= 200; j++) {
      double gluinoMass = 8*i;
      double chi0Mass = 7*j;
      double lowLimit = e_g[0] + sqrt(e_g[0]*e_g[0] + chi0Mass*chi0Mass);
      double xsec = gluino_xs.mass2xsec(200+ 6*j);
      //cout << xsec << endl;
      
      int massPoint = gluinoMass / 200;
      double eff = gluinoStopEff[massPoint - 1] + (gluinoStopEff[massPoint] - gluinoStopEff[massPoint - 1]) * (gluinoMass - 200*massPoint)/ 200;
      if (gluinoMass > lowLimit) {
      h3.SetBinContent(i, j, (10.66/6200)/(eff*0.50));
      }
    }
  }
  h3.GetZaxis()->SetTitle("95% CL upper limit on #sigma [pb]");
  h3.Draw("COLZ");
  */

  
  int iPeriod = 4;
  int iPos=11;
  cout << "nimei" << endl;

  CMS_lumi(&canvas3, iPeriod, iPos);
  gPad->RedrawAxis();
  canvas3.Print("excludedRegion_awesome.pdf");
  canvas3.Print("excludedRegion_awesome.eps"); 
  
	/*
  h4.GetZaxis()->SetTitle("95% CL upper limit on #sigma [pb]");
  h4.Draw("COLZ");
  //h4.Draw("surflz");
  TGraph disallowed1(4);
  disallowed1.SetPoint(0, 0., 0.);
  disallowed1.SetPoint(1, 1200., 1200.);
  disallowed1.SetPoint(2, 1200., 0.);
  disallowed.SetPoint(3, 0., 0.);
  disallowed1.SetFillColor(19);
  //disallowed1.SetFillStyle(4001);
  //disallowed1.Draw("FL");
  
  g_obsExcl70.SetLineColor(kBlack);
  g_obsExcl70.SetLineWidth(2);
  
  g_obsExcl70.SetFillStyle(0);
  g_obsExcl70.SetFillColor(0);
  g_obsExcl70.Draw("L");
 
  TText dislabel1(0.65, 0.45, "Kinematically forbidden");
  dislabel1.SetNDC(true);
  dislabel1.SetTextFont(42);
  dislabel1.SetTextSize(0.04);
  dislabel1.SetTextAngle(35);
  dislabel1.Draw();

TPaveText blurb4(0.47, 0.15, 0.72, 0.37, "NDC");
  blurb4.AddText("CMS 2015+2016");
  blurb4.AddText("#int L dt = 2.5+12.8 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb3.AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
  blurb4.AddText("#sqrt{s} = 13 TeV");
  blurb4.AddText("10 #mus < #tau < 1000 s");
  //blurb3.AddText("95% CL Exclusion contours");
  blurb4.SetTextFont(42);
  blurb4.SetBorderSize(0);
  blurb4.SetFillColor(kGray);
  blurb4.SetFillStyle(4001);
  blurb4.SetShadowColor(0);
  blurb4.SetTextAlign(12);
  blurb4.SetTextSize(0.04);
  blurb4.Draw();

  TLegend leg4(0.65, 0.15, 0.90, 0.37,"95% CL Excluded","NDC");
  leg4.SetTextSize(0.040);
  leg4.SetBorderSize(0);
  leg4.SetTextFont(42);
  leg4.SetFillColor(kGray);
  leg4.SetFillStyle(4001);
  leg4.AddEntry(&g_obsExcl70, "Obs. Limit", "lf");
  leg4.Draw();
  h4.Write("",TObject::kOverwrite);
  canvas4.Print("excludedRegionGluinoXsec.pdf");
*/
}

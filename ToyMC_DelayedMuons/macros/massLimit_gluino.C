//#include "CMS_lumi.C"
void massLimit()
{
//=========Macro generated from canvas: canvas/
//=========  (Wed Jan 18 12:17:28 2017) by ROOT version6.06/06
   TCanvas *canvas = new TCanvas("canvas", "",37,45,575,500);
   canvas->Range(-12.50001,-6,1112.5,4);
   canvas->SetFillColor(0);
   canvas->SetBorderMode(0);
   canvas->SetBorderSize(2);
   canvas->SetLogy();
   canvas->SetFrameBorderMode(0);
   canvas->SetFrameBorderMode(0);
   
   TH1F *hframe__1 = new TH1F("hframe__1","",2200,400,2600);
   hframe__1->SetMinimum(5e-8);
   hframe__1->SetMaximum(1000);
   hframe__1->SetDirectory(0);
   hframe__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hframe__1->SetLineColor(ci);
   hframe__1->GetXaxis()->SetTitle("m_{mchamp} [GeV]");
   hframe__1->GetXaxis()->SetLabelFont(42);
   hframe__1->GetXaxis()->SetLabelSize(0.035);
   hframe__1->GetXaxis()->SetTitleSize(0.035);
   hframe__1->GetXaxis()->SetTitleFont(42);
   hframe__1->GetYaxis()->SetTitle("#sigma(pp #rightarrow mchamp mchamp) [pb]");
   hframe__1->GetYaxis()->SetLabelFont(42);
   hframe__1->GetYaxis()->SetLabelSize(0.035);
   hframe__1->GetYaxis()->SetTitleSize(0.035);
   hframe__1->GetYaxis()->SetTitleFont(42);
   hframe__1->GetZaxis()->SetLabelFont(42);
   hframe__1->GetZaxis()->SetLabelSize(0.035);
   hframe__1->GetZaxis()->SetTitleSize(0.035);
   hframe__1->GetZaxis()->SetTitleFont(42);
   hframe__1->Draw(" ");
   int iPeriod = 4; // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV
   int iPos = 11;
   CMS_lumi(canvas, iPeriod, iPos);
       //int iPos=0;
       //  int iPos=11;
   
   TLegend *leg = new TLegend(0.45,0.7,0.7,0.92,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.033);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","95% CL Limits:","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   //entry=leg->AddEntry("Graph","Observed, 10 #mus - 1000 s","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected, 10 #mus - 1000 s","l");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected #pm1#sigma, 10 #mus - 1000 s","lf");

   ci = TColor::GetColor("#00ff00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected #pm2#sigma, 10 #mus - 1000 s","lf");

   ci = TColor::GetColor("#ffff00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","LO Prediction","l");

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();

  TPaveText* blurb = new TPaveText(0.25, 0.57, 0.50, 0.87, "NDC");

  blurb->AddText("CMS Preliminary 2016");
  // std::stringstream label;
  // label<<"#int L dt = "<<lumi<<" pb^{-1}";
  // blurb->AddText(label.str().c_str());
  // double peakInstLumi=maxInstLumi;
  // int exponent=30;
  // while (peakInstLumi>10) {
  //   peakInstLumi/=10;
  //   ++exponent;
  // }
  // std::stringstream label2;
  // label2<<"L^{max}_{inst} = "<<peakInstLumi<<" x 10^{"<<exponent<<"} cm^{-2}s^{-1}";
  // blurb->AddText(label2.str().c_str());

  //blurb->AddText("CMS 2011");
  blurb->AddText("#int L dt = 37.2 fb^{-1}");//,  #int L_{eff} dt = 935 pb^{-1}");
  //blurb->AddText("L^{max}_{inst} = 3.5 #times 10^{33} cm^{-2}s^{-1}");
  blurb->AddText("#sqrt{s} = 13 TeV");
  //blurb->AddText("m_{#tilde{g}} = 300 GeV/c^{2}");
  //blurb->AddText("m_{#tilde{#chi}^{0}} = 200 GeV/c^{2}");
  blurb->SetTextFont(42);
  blurb->SetBorderSize(0);
  blurb->SetFillColor(0);
  blurb->SetShadowColor(0);
  blurb->SetTextAlign(12);
  blurb->SetTextSize(0.033);
  //blurb->Draw();
   
   Double_t Graph0_fx3001[10] = {
   100,
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph0_fy3001[10] = {
   4.79816,
   0.3004293,
   0.1434955,
   0.125013,
   0.09565251,
   0.07811414,
   0.07388136,
   0.06386079,
   0.05909341,
   0.05222133};
   Double_t Graph0_felx3001[10] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fely3001[10] = {
   3.974109,
   0.2488326,
   0.1086795,
   0.08804158,
   0.06973013,
   0.04945645,
   0.04677654,
   0.04142024,
   0.0383281,
   0.03354075};
   Double_t Graph0_fehx3001[10] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fehy3001[10] = {
   5.520429,
   0.345653,
   0.156186,
   0.1284641,
   0.108257,
   0.08195586,
   0.0775149,
   0.06831471,
   0.06321483,
   0.05600936};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(10,Graph0_fx3001,Graph0_fy3001,Graph0_felx3001,Graph0_fehx3001,Graph0_fely3001,Graph0_fehy3001);
   grae->SetName("Graph0");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffff00");
   grae->SetFillColor(ci);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   
   TH1F *Graph_Graph3001 = new TH1F("Graph_Graph3001","Graph",100,0,2850);
   Graph_Graph3001->SetMinimum(0.01681252);
   Graph_Graph3001->SetMaximum(11.34858);
   Graph_Graph3001->SetDirectory(0);
   Graph_Graph3001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3001->SetLineColor(ci);
   Graph_Graph3001->GetXaxis()->SetLabelFont(42);
   Graph_Graph3001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetXaxis()->SetTitleFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetYaxis()->SetTitleFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3001->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3001);
   
   grae->Draw("3");
   
   Double_t Graph1_fx3002[10] = {
   100,
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph1_fy3002[10] = {
   4.79816,
   0.3004293,
   0.1434955,
   0.125013,
   0.09565251,
   0.07811414,
   0.07388136,
   0.06386079,
   0.05909341,
   0.05222133};
   Double_t Graph1_felx3002[10] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph1_fely3002[10] = {
   2.405556,
   0.1506201,
   0.06557318,
   0.05245336,
   0.04429642,
   0.03226295,
   0.03051472,
   0.02692336,
   0.02491345,
   0.02201574};
   Double_t Graph1_fehx3002[10] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph1_fehy3002[10] = {
   2.400161,
   0.1502823,
   0.06601285,
   0.05318161,
   0.04445661,
   0.03270677,
   0.03093449,
   0.02720367,
   0.02517284,
   0.02211896};
   grae = new TGraphAsymmErrors(10,Graph1_fx3002,Graph1_fy3002,Graph1_felx3002,Graph1_fehx3002,Graph1_fely3002,Graph1_fehy3002);
   grae->SetName("Graph1");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00ff00");
   grae->SetFillColor(ci);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   
   TH1F *Graph_Graph3002 = new TH1F("Graph_Graph3002","Graph",100,0,2850);
   Graph_Graph3002->SetMinimum(0.02718503);
   Graph_Graph3002->SetMaximum(7.915133);
   Graph_Graph3002->SetDirectory(0);
   Graph_Graph3002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3002->SetLineColor(ci);
   Graph_Graph3002->GetXaxis()->SetLabelFont(42);
   Graph_Graph3002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3002->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3002->GetXaxis()->SetTitleFont(42);
   Graph_Graph3002->GetYaxis()->SetLabelFont(42);
   Graph_Graph3002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3002->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3002->GetYaxis()->SetTitleFont(42);
   Graph_Graph3002->GetZaxis()->SetLabelFont(42);
   Graph_Graph3002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3002);
   
   grae->Draw("3");
   
   Double_t Graph2_fx1[10] = {
   100,
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph2_fy1[10] = {
   4.79816,
   0.3004293,
   0.1434955,
   0.125013,
   0.09565251,
   0.07811414,
   0.07388136,
   0.06386079,
   0.05909341,
   0.05222133};
   TGraph *graph = new TGraph(10,Graph2_fx1,Graph2_fy1);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Graph",100,0,2850);
   Graph_Graph1->SetMinimum(0.0469992);
   Graph_Graph1->SetMaximum(5.272754);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1->SetLineColor(ci);
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   graph->Draw("l");
   
   Double_t Graph3_fx2[10] = {
   100,
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph3_fy2[10] = {
   3.777944,
   0.2986527,
   0.02309972,
   0.003465116,
   0.0007969627,
   0.000240319,
   2.663338e-05,
   3.934695e-06,
   5.58633e-07,
   7.397318e-08};
   graph = new TGraph(10,Graph3_fx2,Graph3_fy2);
   graph->SetName("Graph3");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#ff3333");
   graph->SetFillColor(ci);
   graph->SetFillStyle(3001);

   ci = TColor::GetColor("#ff0000");
   graph->SetLineColor(ci);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","Graph",100,0,2850);
   Graph_Graph2->SetMinimum(6.657586e-08);
   Graph_Graph2->SetMaximum(4.155738);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph2->SetLineColor(ci);
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph2);
   
   graph->Draw("l3");
   
   TH1F *hframe_copy__2 = new TH1F("hframe_copy__2","",1000,100,1000);
   hframe_copy__2->SetMinimum(1e-05);
   hframe_copy__2->SetMaximum(1000);
   hframe_copy__2->SetDirectory(0);
   hframe_copy__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hframe_copy__2->SetLineColor(ci);
   hframe_copy__2->GetXaxis()->SetTitle("m_{mchamp} [GeV]");
   hframe_copy__2->GetXaxis()->SetLabelFont(42);
   hframe_copy__2->GetXaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetXaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetXaxis()->SetTitleFont(42);
   hframe_copy__2->GetYaxis()->SetTitle("#sigma(pp #rightarrow mchamp mchamp) [pb]");
   hframe_copy__2->GetYaxis()->SetLabelFont(42);
   hframe_copy__2->GetYaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetYaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetYaxis()->SetTitleFont(42);
   hframe_copy__2->GetZaxis()->SetLabelFont(42);
   hframe_copy__2->GetZaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetZaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetZaxis()->SetTitleFont(42);
   hframe_copy__2->Draw("sameaxis");
   canvas->Modified();
   canvas->cd();
   canvas->SetSelected(canvas);
}

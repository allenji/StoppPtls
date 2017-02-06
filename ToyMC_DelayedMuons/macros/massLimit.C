void massLimit()
{
//=========Macro generated from canvas: canvas/
//=========  (Mon Feb  6 11:31:30 2017) by ROOT version6.06/06
   TCanvas *canvas = new TCanvas("canvas", "",43,45,575,500);
   gStyle->SetOptFit(1);
   gStyle->SetOptTitle(0);
   canvas->Range(-110.3896,-6.316456,1058.442,3.810127);
   canvas->SetFillColor(0);
   canvas->SetBorderMode(0);
   canvas->SetBorderSize(0);
   canvas->SetLogy();
   canvas->SetTickx(1);
   canvas->SetTicky(1);
   canvas->SetLeftMargin(0.18);
   canvas->SetRightMargin(0.05);
   canvas->SetTopMargin(0.08);
   canvas->SetBottomMargin(0.13);
   canvas->SetFrameFillStyle(0);
   canvas->SetFrameLineStyle(0);
   canvas->SetFrameLineWidth(2);
   canvas->SetFrameBorderMode(0);
   canvas->SetFrameBorderSize(0);
   canvas->SetFrameFillStyle(0);
   canvas->SetFrameLineStyle(0);
   canvas->SetFrameLineWidth(2);
   canvas->SetFrameBorderMode(0);
   canvas->SetFrameBorderSize(0);
   
   TH1F *hframe__1 = new TH1F("hframe__1","",1000,100,1000);
   hframe__1->SetMinimum(1e-05);
   hframe__1->SetMaximum(1000);
   hframe__1->SetDirectory(0);
   hframe__1->SetStats(0);
   hframe__1->SetLineStyle(0);
   hframe__1->SetMarkerStyle(8);
   hframe__1->GetXaxis()->SetTitle("m_{mchamp} [GeV]");
   hframe__1->GetXaxis()->SetLabelFont(42);
   hframe__1->GetXaxis()->SetLabelOffset(0.012);
   hframe__1->GetXaxis()->SetTitleSize(0.05);
   hframe__1->GetXaxis()->SetTickLength(0.015);
   hframe__1->GetXaxis()->SetTitleOffset(1.2);
   hframe__1->GetXaxis()->SetTitleFont(42);
   hframe__1->GetYaxis()->SetTitle("#sigma(pp #rightarrow mchamp mchamp) [pb]");
   hframe__1->GetYaxis()->SetLabelFont(42);
   hframe__1->GetYaxis()->SetLabelOffset(0.012);
   hframe__1->GetYaxis()->SetTitleSize(0.05);
   hframe__1->GetYaxis()->SetTickLength(0.015);
   hframe__1->GetYaxis()->SetTitleOffset(1.2);
   hframe__1->GetYaxis()->SetTitleFont(42);
   hframe__1->GetZaxis()->SetLabelFont(42);
   hframe__1->GetZaxis()->SetTitleFont(42);
   hframe__1->Draw(" ");
   
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
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","Observed, 10 #mus - 1000 s","lp");
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

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
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
   
   Double_t Graph0_fx3001[12] = {
   400,
   600,
   800,
   1000,
   1200,
   1400,
   1600,
   1800,
   2000,
   2200,
   2400,
   2600};
   Double_t Graph0_fy3001[12] = {
   21.34656,
   12.83532,
   8.63572,
   7.667863,
   6.564798,
   4.547411,
   3.2094,
   3.640835,
   2.476628,
   1.894906,
   1.805959,
   1.572868};
   Double_t Graph0_felx3001[12] = {
   0,
   0,
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
   Double_t Graph0_fely3001[12] = {
   16.61032,
   9.987503,
   6.719682,
   5.946265,
   4.662559,
   3.229737,
   2.225968,
   2.515924,
   1.679107,
   1.284711,
   1.261076,
   1.098312};
   Double_t Graph0_fehx3001[12] = {
   0,
   0,
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
   Double_t Graph0_fehy3001[12] = {
   21.63034,
   13.00595,
   8.750523,
   7.752315,
   6.448914,
   4.467138,
   3.134721,
   3.570081,
   2.489731,
   1.904932,
   1.898125,
   1.653139};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(12,Graph0_fx3001,Graph0_fy3001,Graph0_felx3001,Graph0_fehx3001,Graph0_fely3001,Graph0_fehy3001);
   grae->SetName("Graph0");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffff00");
   grae->SetFillColor(ci);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   grae->SetMarkerStyle(8);
   
   TH1F *Graph_Graph3001 = new TH1F("Graph_Graph3001","Graph",100,180,2820);
   Graph_Graph3001->SetMinimum(0.4271006);
   Graph_Graph3001->SetMaximum(47.22714);
   Graph_Graph3001->SetDirectory(0);
   Graph_Graph3001->SetStats(0);
   Graph_Graph3001->SetLineStyle(0);
   Graph_Graph3001->SetMarkerStyle(8);
   Graph_Graph3001->GetXaxis()->SetLabelFont(42);
   Graph_Graph3001->GetXaxis()->SetLabelOffset(0.012);
   Graph_Graph3001->GetXaxis()->SetTitleSize(0.05);
   Graph_Graph3001->GetXaxis()->SetTickLength(0.015);
   Graph_Graph3001->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph3001->GetXaxis()->SetTitleFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelOffset(0.012);
   Graph_Graph3001->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph3001->GetYaxis()->SetTickLength(0.015);
   Graph_Graph3001->GetYaxis()->SetTitleOffset(1.2);
   Graph_Graph3001->GetYaxis()->SetTitleFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelFont(42);
   Graph_Graph3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3001);
   
   grae->Draw("3");
   
   Double_t Graph1_fx3002[12] = {
   400,
   600,
   800,
   1000,
   1200,
   1400,
   1600,
   1800,
   2000,
   2200,
   2400,
   2600};
   Double_t Graph1_fy3002[12] = {
   21.34656,
   12.83532,
   8.63572,
   7.667863,
   6.564798,
   4.547411,
   3.2094,
   3.640835,
   2.476628,
   1.894906,
   1.805959,
   1.572868};
   Double_t Graph1_felx3002[12] = {
   0,
   0,
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
   Double_t Graph1_fely3002[12] = {
   9.142774,
   5.497393,
   3.698696,
   3.258857,
   2.579149,
   1.786567,
   1.239344,
   1.409919,
   0.9760899,
   0.7468214,
   0.7521136,
   0.6550403};
   Double_t Graph1_fehx3002[12] = {
   0,
   0,
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
   Double_t Graph1_fehy3002[12] = {
   9.319036,
   5.603377,
   3.770002,
   3.312856,
   2.655054,
   1.839146,
   1.277094,
   1.451482,
   0.9998438,
   0.7649959,
   0.7663009,
   0.6673964};
   grae = new TGraphAsymmErrors(12,Graph1_fx3002,Graph1_fy3002,Graph1_felx3002,Graph1_fehx3002,Graph1_fely3002,Graph1_fehy3002);
   grae->SetName("Graph1");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00ff00");
   grae->SetFillColor(ci);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   grae->SetMarkerStyle(8);
   
   TH1F *Graph_Graph3002 = new TH1F("Graph_Graph3002","Graph",100,180,2820);
   Graph_Graph3002->SetMinimum(0.8260453);
   Graph_Graph3002->SetMaximum(33.64037);
   Graph_Graph3002->SetDirectory(0);
   Graph_Graph3002->SetStats(0);
   Graph_Graph3002->SetLineStyle(0);
   Graph_Graph3002->SetMarkerStyle(8);
   Graph_Graph3002->GetXaxis()->SetLabelFont(42);
   Graph_Graph3002->GetXaxis()->SetLabelOffset(0.012);
   Graph_Graph3002->GetXaxis()->SetTitleSize(0.05);
   Graph_Graph3002->GetXaxis()->SetTickLength(0.015);
   Graph_Graph3002->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph3002->GetXaxis()->SetTitleFont(42);
   Graph_Graph3002->GetYaxis()->SetLabelFont(42);
   Graph_Graph3002->GetYaxis()->SetLabelOffset(0.012);
   Graph_Graph3002->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph3002->GetYaxis()->SetTickLength(0.015);
   Graph_Graph3002->GetYaxis()->SetTitleOffset(1.2);
   Graph_Graph3002->GetYaxis()->SetTitleFont(42);
   Graph_Graph3002->GetZaxis()->SetLabelFont(42);
   Graph_Graph3002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3002);
   
   grae->Draw("3");
   
   Double_t Graph2_fx1[12] = {
   400,
   600,
   800,
   1000,
   1200,
   1400,
   1600,
   1800,
   2000,
   2200,
   2400,
   2600};
   Double_t Graph2_fy1[12] = {
   21.34656,
   12.83532,
   8.63572,
   7.667863,
   6.564798,
   4.547411,
   3.2094,
   3.640835,
   2.476628,
   1.894906,
   1.805959,
   1.572868};
   TGraph *graph = new TGraph(12,Graph2_fx1,Graph2_fy1);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Graph",100,180,2820);
   Graph_Graph1->SetMinimum(1.415582);
   Graph_Graph1->SetMaximum(23.32393);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetMarkerStyle(8);
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.012);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.05);
   Graph_Graph1->GetXaxis()->SetTickLength(0.015);
   Graph_Graph1->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.012);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph1->GetYaxis()->SetTickLength(0.015);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.2);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   graph->Draw("l");
   
   Double_t Graph3_fx2[12] = {
   400,
   600,
   800,
   1000,
   1200,
   1400,
   1600,
   1800,
   2000,
   2200,
   2400,
   2600};
   Double_t Graph3_fy2[12] = {
   94.8,
   9.07,
   1.47,
   0.32,
   0.0836,
   0.0247,
   0.00796,
   0.00273,
   0.000974,
   0.000358,
   0.000134,
   5.03e-05};
   graph = new TGraph(12,Graph3_fx2,Graph3_fy2);
   graph->SetName("Graph3");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#ff3333");
   graph->SetFillColor(ci);
   graph->SetFillStyle(3001);

   ci = TColor::GetColor("#ff0000");
   graph->SetLineColor(ci);
   graph->SetLineWidth(2);
   graph->SetMarkerStyle(8);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","Graph",100,180,2820);
   Graph_Graph2->SetMinimum(4.527e-05);
   Graph_Graph2->SetMaximum(104.28);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);
   Graph_Graph2->SetLineStyle(0);
   Graph_Graph2->SetMarkerStyle(8);
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelOffset(0.012);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.05);
   Graph_Graph2->GetXaxis()->SetTickLength(0.015);
   Graph_Graph2->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelOffset(0.012);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph2->GetYaxis()->SetTickLength(0.015);
   Graph_Graph2->GetYaxis()->SetTitleOffset(1.2);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph2);
   
   graph->Draw("l3");
   
   TH1F *hframe_copy__2 = new TH1F("hframe_copy__2","",1000,100,1000);
   hframe_copy__2->SetMinimum(1e-05);
   hframe_copy__2->SetMaximum(1000);
   hframe_copy__2->SetDirectory(0);
   hframe_copy__2->SetStats(0);
   hframe_copy__2->SetLineStyle(0);
   hframe_copy__2->SetMarkerStyle(8);
   hframe_copy__2->GetXaxis()->SetTitle("m_{mchamp} [GeV]");
   hframe_copy__2->GetXaxis()->SetLabelFont(42);
   hframe_copy__2->GetXaxis()->SetLabelOffset(0.012);
   hframe_copy__2->GetXaxis()->SetTitleSize(0.05);
   hframe_copy__2->GetXaxis()->SetTickLength(0.015);
   hframe_copy__2->GetXaxis()->SetTitleOffset(1.2);
   hframe_copy__2->GetXaxis()->SetTitleFont(42);
   hframe_copy__2->GetYaxis()->SetTitle("#sigma(pp #rightarrow mchamp mchamp) [pb]");
   hframe_copy__2->GetYaxis()->SetLabelFont(42);
   hframe_copy__2->GetYaxis()->SetLabelOffset(0.012);
   hframe_copy__2->GetYaxis()->SetTitleSize(0.05);
   hframe_copy__2->GetYaxis()->SetTickLength(0.015);
   hframe_copy__2->GetYaxis()->SetTitleOffset(1.2);
   hframe_copy__2->GetYaxis()->SetTitleFont(42);
   hframe_copy__2->GetZaxis()->SetLabelFont(42);
   hframe_copy__2->GetZaxis()->SetTitleFont(42);
   hframe_copy__2->Draw("sameaxis");
   canvas->Modified();
   canvas->cd();
   canvas->SetSelected(canvas);
}

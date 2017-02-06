void mchampMassLimit()
{
//=========Macro generated from canvas: canvas/
//=========  (Wed Jan 18 11:22:56 2017) by ROOT version6.06/06
   TCanvas *canvas = new TCanvas("canvas", "",39,45,700,500);
   canvas->Range(212.5,-2.161341,1087.5,2.462371);
   canvas->SetFillColor(0);
   canvas->SetBorderMode(0);
   canvas->SetBorderSize(2);
   canvas->SetLogy();
   canvas->SetFrameBorderMode(0);
   canvas->SetFrameBorderMode(0);
   
   TH1F *hframe__1 = new TH1F("hframe__1","Beamgap Expt",1000,300,1000);
   hframe__1->SetMinimum(0.02);
   hframe__1->SetMaximum(100);
   hframe__1->SetDirectory(0);
   hframe__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hframe__1->SetLineColor(ci);
   hframe__1->GetXaxis()->SetTitle("m_{#tilde{g}} [GeV/c^{2}]");
   hframe__1->GetXaxis()->SetLabelFont(42);
   hframe__1->GetXaxis()->SetLabelSize(0.035);
   hframe__1->GetXaxis()->SetTitleSize(0.035);
   hframe__1->GetXaxis()->SetTitleFont(42);
   hframe__1->GetYaxis()->SetTitle(" #sigma(pp #rightarrow #tilde{g}#tilde{g}) #times BR(#tilde{g} #rightarrow g#tilde{#chi}^{0}) [pb]");
   hframe__1->GetYaxis()->SetLabelFont(42);
   hframe__1->GetYaxis()->SetLabelSize(0.035);
   hframe__1->GetYaxis()->SetTitleSize(0.035);
   hframe__1->GetYaxis()->SetTitleFont(42);
   hframe__1->GetZaxis()->SetLabelFont(42);
   hframe__1->GetZaxis()->SetLabelSize(0.035);
   hframe__1->GetZaxis()->SetTitleSize(0.035);
   hframe__1->GetZaxis()->SetTitleFont(42);
   hframe__1->Draw(" ");
   TBox *box = new TBox(600,2,900,100);
   box->SetFillColor(19);
   box->Draw();
   
   TLegend *leg = new TLegend(0.4428571,0.5325528,0.7857143,0.9,NULL,"");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.028);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","95% C.L. Limits","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected: 10 #mus - 1000 s Counting Exp. ","l");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected #pm1#sigma: 10 #mus - 1000 s Counting Exp. ","f");
   entry->SetFillColor(3);
   entry->SetFillStyle(1001);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Expected #pm2#sigma: 10 #mus - 1000 s Counting Exp. ","f");
   entry->SetFillColor(5);
   entry->SetFillStyle(1001);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Obs.: 10 #mus - 1000 s Counting Exp. ","l");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","Obs.: 10 #mus Timing Profile ","l");

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   Double_t Graph0_fx3001[9] = {
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph0_fy3001[9] = {
   0.3004293,
   0.2815247,
   0.3395621,
   0.3153077,
   0.3448678,
   0.3261804,
   0.3105751,
   0.2873898,
   0.2665645};
   Double_t Graph0_felx3001[9] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fely3001[9] = {
   0.2488326,
   0.2331747,
   0.2812446,
   0.2611557,
   0.2856391,
   0.2701611,
   0.2572359,
   0.2380326,
   0.2207838};
   Double_t Graph0_fehx3001[9] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph0_fehy3001[9] = {
   0.345653,
   0.3239027,
   0.3906765,
   0.3627711,
   0.3967809,
   0.3752804,
   0.3573261,
   0.3306507,
   0.3066905};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(9,Graph0_fx3001,Graph0_fy3001,Graph0_felx3001,Graph0_fehx3001,Graph0_fely3001,Graph0_fehy3001);
   grae->SetName("Graph0");
   grae->SetTitle("Graph");
   grae->SetFillColor(5);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   
   TH1F *Graph_Graph3001 = new TH1F("Graph_Graph3001","Graph",100,0,2840);
   Graph_Graph3001->SetMinimum(0.04120258);
   Graph_Graph3001->SetMaximum(0.8112354);
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
   
   Double_t Graph1_fx3002[9] = {
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph1_fy3002[9] = {
   0.3004293,
   0.2815247,
   0.3395621,
   0.3153077,
   0.3448678,
   0.3261804,
   0.3105751,
   0.2873898,
   0.2665645};
   Double_t Graph1_felx3002[9] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph1_fely3002[9] = {
   0.1506201,
   0.1411423,
   0.1702394,
   0.1580794,
   0.1728993,
   0.1635304,
   0.1557067,
   0.1440828,
   0.133642};
   Double_t Graph1_fehx3002[9] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph1_fehy3002[9] = {
   0.1502823,
   0.1408258,
   0.1698576,
   0.1577249,
   0.1725116,
   0.1631637,
   0.1553575,
   0.1437597,
   0.1333423};
   grae = new TGraphAsymmErrors(9,Graph1_fx3002,Graph1_fy3002,Graph1_felx3002,Graph1_fehx3002,Graph1_fely3002,Graph1_fehy3002);
   grae->SetName("Graph1");
   grae->SetTitle("Graph");
   grae->SetFillColor(3);
   grae->SetLineColor(0);
   grae->SetLineStyle(0);
   grae->SetLineWidth(0);
   
   TH1F *Graph_Graph3002 = new TH1F("Graph_Graph3002","Graph",100,0,2840);
   Graph_Graph3002->SetMinimum(0.09447677);
   Graph_Graph3002->SetMaximum(0.5558251);
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
   
   Double_t Graph2_fx1[9] = {
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph2_fy1[9] = {
   0.3004293,
   0.2815247,
   0.3395621,
   0.3153077,
   0.3448678,
   0.3261804,
   0.3105751,
   0.2873898,
   0.2665645};
   TGraph *graph = new TGraph(9,Graph2_fx1,Graph2_fy1);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetLineStyle(2);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Graph",100,0,2840);
   Graph_Graph1->SetMinimum(0.2587341);
   Graph_Graph1->SetMaximum(0.3526981);
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
   
   Double_t Graph3_fx2[9] = {
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph3_fy2[9] = {
   0.02117995,
   0.0198472,
   0.02393877,
   0.02222886,
   0.02431282,
   0.02299537,
   0.02189522,
   0.02026068,
   0.01879252};
   graph = new TGraph(9,Graph3_fx2,Graph3_fy2);
   graph->SetName("Graph3");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","Graph",100,0,2840);
   Graph_Graph2->SetMinimum(0.01824049);
   Graph_Graph2->SetMaximum(0.02486485);
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
   
   graph->Draw("l");
   
   graph = new TGraph();
   graph->SetName("Graph4");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);

   ci = TColor::GetColor("#ff0000");
   graph->SetLineColor(ci);
   graph->SetLineWidth(2);
   graph->Draw("l");
   
   Double_t Graph5_fx4[9] = {
   200,
   400,
   600,
   800,
   1000,
   1400,
   1800,
   2200,
   2600};
   Double_t Graph5_fy4[9] = {
   0.2986527,
   0.02309972,
   0.003465116,
   0.0007969627,
   0.000240319,
   2.663338e-05,
   3.934695e-06,
   5.58633e-07,
   7.397318e-08};
   graph = new TGraph(9,Graph5_fx4,Graph5_fy4);
   graph->SetName("Graph5");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#3333ff");
   graph->SetFillColor(ci);
   graph->SetFillStyle(3001);

   ci = TColor::GetColor("#0000ff");
   graph->SetLineColor(ci);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","Graph",100,0,2840);
   Graph_Graph4->SetMinimum(6.657586e-08);
   Graph_Graph4->SetMaximum(0.328518);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph4->SetLineColor(ci);
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph4);
   
   graph->Draw("l3");
   TLatex *   tex = new TLatex(600,0.3,"NLO+NLL #tilde{g}");

   ci = TColor::GetColor("#0000ff");
   tex->SetTextColor(ci);
   tex->SetTextFont(42);
   tex->SetTextSize(0.035);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TPaveText *pt = new TPaveText(300,2,550,100,"br");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetTextAlign(12);
   pt->SetTextFont(42);
   pt->SetTextSize(0.032);
   AText = pt->AddText("CMS Preliminary 2012");
   AText = pt->AddText("#int L dt = 877 fb^{-1}");
   AText = pt->AddText("L^{max}_{inst} = 1.3 x 10^{33} cm^{-2}s^{-1}");
   AText = pt->AddText("#sqrt{s} = 8 TeV");
   AText = pt->AddText("m_{#tilde{g}} - m_{#tilde{#chi}^{0}} = 100 GeV/c^{2}");
   pt->Draw();
   
   TH1F *hframe_copy__2 = new TH1F("hframe_copy__2","Beamgap Expt",1000,300,1000);
   hframe_copy__2->SetMinimum(0.02);
   hframe_copy__2->SetMaximum(100);
   hframe_copy__2->SetDirectory(0);
   hframe_copy__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hframe_copy__2->SetLineColor(ci);
   hframe_copy__2->GetXaxis()->SetTitle("m_{#tilde{g}} [GeV/c^{2}]");
   hframe_copy__2->GetXaxis()->SetLabelFont(42);
   hframe_copy__2->GetXaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetXaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetXaxis()->SetTitleFont(42);
   hframe_copy__2->GetYaxis()->SetTitle(" #sigma(pp #rightarrow #tilde{g}#tilde{g}) #times BR(#tilde{g} #rightarrow g#tilde{#chi}^{0}) [pb]");
   hframe_copy__2->GetYaxis()->SetLabelFont(42);
   hframe_copy__2->GetYaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetYaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetYaxis()->SetTitleFont(42);
   hframe_copy__2->GetZaxis()->SetLabelFont(42);
   hframe_copy__2->GetZaxis()->SetLabelSize(0.035);
   hframe_copy__2->GetZaxis()->SetTitleSize(0.035);
   hframe_copy__2->GetZaxis()->SetTitleFont(42);
   hframe_copy__2->Draw("sameaxis");
   
   pt = new TPaveText(0.3710888,0.9368947,0.6289112,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   AText = pt->AddText("Beamgap Expt");
   pt->Draw();
   canvas->Modified();
   canvas->cd();
   canvas->SetSelected(canvas);
}

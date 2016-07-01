//analyzer to get the total livetime by run and by fill
#include <memory>
#include <iostream>
#include <fstream>

#include "TFile.h"
#include "TH1.h"

#include "StoppPtls/Livetime/interface/GetLivetime.h"

using namespace std;

GetLivetime::GetLivetime(const edm::ParameterSet& iConfig) :
  lhcFills_(),
  livetime_(&lhcFills_),
  nEvents_(0),
  runMin_(iConfig.getParameter<unsigned>("RunMin")),
  runMax_(iConfig.getParameter<unsigned>("RunMax")),
  fillMin_(iConfig.getParameter<unsigned>("FillMin")),
  fillMax_(iConfig.getParameter<unsigned>("FillMax"))
{
};

GetLivetime::~GetLivetime(){

  unsigned run_livetime_hist_low = runMin_;
  unsigned  run_livetime_hist_up = runMax_ + 1;
  unsigned run_livetime_hist_Nbins = run_livetime_hist_up - run_livetime_hist_low;
  run_livetime_hist = fs_->make<TH1D>("run_livetime_hist","Run vs Livetime",run_livetime_hist_Nbins , run_livetime_hist_low, run_livetime_hist_up);

  unsigned fill_livetime_hist_low = fillMin_;
  unsigned fill_livetime_hist_up = fillMax_;
  unsigned fill_livetime_hist_Nbins = fill_livetime_hist_up - fill_livetime_hist_low;
  fill_livetime_hist = fs_->make<TH1D>("fill_livetime_hist","Fill vs Livetime",fill_livetime_hist_Nbins, fill_livetime_hist_low, fill_livetime_hist_up);

  vector<unsigned long> runList = livetime_.runList();
  for (unsigned i=0; i!=runList.size(); ++i) {
    run_livetime_hist->Fill(runList.at(i),livetime_.getLivetimeByRun(runList.at(i)));
  }

  vector<unsigned long> fillList = livetime_.fillList();
  for (unsigned i=0; i!=fillList.size(); ++i) {
    fill_livetime_hist->Fill(fillList.at(i),livetime_.getLivetimeByFill(fillList.at(i)));
  }

  //print total livetime and rate to log file
  double totalLivetime = livetime_.getTotalLivetime();
  clog << "Total livetime : " << totalLivetime << endl;
  clog << "Final rate : " << nEvents_/totalLivetime << " +/- " << sqrt(nEvents_)/totalLivetime << endl;
  clog << "Fills analyzed: " << endl;
  for (unsigned i=0; i!=fillList.size(); ++i) {
    clog << fillList.at(i) << ", ";
  }
  clog << endl;
  
  clog << "Runs analyzed: " << endl;
  for (unsigned i=0; i!=runList.size(); ++i) {
    clog << runList.at(i) << ", ";
  }

}//end of destructor


void GetLivetime::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){

  //unsigned long event = iEvent.id().event();
  //unsigned long bx = iEvent.bunchCrossing();
  //unsigned long orbit = iEvent.orbitNumber();
  unsigned long lb = iEvent.luminosityBlock();
  unsigned long run = iEvent.id().run();
  unsigned long fill = lhcFills_.getFillFromRun(run);

  livetime_.newEvent(fill, run, lb);
  nEvents_++;

}//end of analyze

void GetLivetime::endJob(){
}//end of endJob()


void GetLivetime::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(GetLivetime);


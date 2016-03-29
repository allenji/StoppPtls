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
  nEvents_(0)
{
}

GetLivetime::~GetLivetime(){

  run_livetime_hist = fs_->make<TH1D>("run_livetime_hist","Run vs Livetime",30000,235000,265000);
  fill_livetime_hist = fs_->make<TH1D>("fill_livetime_hist","Fill vs Livetime",2000,3000,5000);

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


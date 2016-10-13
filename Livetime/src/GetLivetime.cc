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
  fillMax_(iConfig.getParameter<unsigned>("FillMax")),
  instLumiMin_(iConfig.getParameter<int>("InstLumiMin")),
  instLumiMax_(iConfig.getParameter<int>("InstLumiMax")),
  eventsTag_     (iConfig.getParameter<edm::InputTag>("events")),
  eventsToken_   (consumes<std::vector<CandidateEvent> >(eventsTag_))
{

  instLumis.resize(instLumiNBins_);
  for(unsigned int i=0; i<instLumis.size(); i++) instLumis.at(i) = instLumiMin_ + i;

  livetimeForInstLumi.resize(instLumiNBins_);
  for(unsigned int i=0; i<livetimeForInstLumi.size(); i++) livetimeForInstLumi.at(i) = 0.;

};

GetLivetime::~GetLivetime(){

  unsigned run_livetime_hist_low = runMin_;
  unsigned run_livetime_hist_up = runMax_ + 1;
  unsigned run_livetime_hist_Nbins = run_livetime_hist_up - run_livetime_hist_low;
  run_livetime_hist = fs_->make<TH1D>("run_livetime_hist","Run vs Livetime",run_livetime_hist_Nbins , run_livetime_hist_low, run_livetime_hist_up);

  unsigned fill_livetime_hist_low = fillMin_;
  unsigned fill_livetime_hist_up = fillMax_;
  unsigned fill_livetime_hist_Nbins = fill_livetime_hist_up - fill_livetime_hist_low;
  fill_livetime_hist = fs_->make<TH1D>("fill_livetime_hist","Fill vs Livetime",fill_livetime_hist_Nbins, fill_livetime_hist_low, fill_livetime_hist_up);

  instLumi_livetime_hist = fs_->make<TH1D>("instLumi_livetime_hist","Instantaneous Luminosity vs Livetime",instLumiNBins_, instLumiMin_, instLumiMax_);

  vector<unsigned long> runList = livetime_.runList();
  for (unsigned i=0; i!=runList.size(); ++i) {
    run_livetime_hist->Fill(runList.at(i),livetime_.getLivetimeByRun(runList.at(i)));
  }

  vector<unsigned long> fillList = livetime_.fillList();
  for (unsigned i=0; i!=fillList.size(); ++i) {
    fill_livetime_hist->Fill(fillList.at(i),livetime_.getLivetimeByFill(fillList.at(i)));
  }

  for(unsigned int i=0; i<instLumis.size(); i++){
    instLumi_livetime_hist->Fill(instLumis.at(i),livetimeForInstLumi.at(i));
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
  clog << endl;

  for(unsigned int i=0; i<instLumis.size(); i++){
    if(livetimeForInstLumi.at(i)!=0.) clog<<"For instantaneous luminosity of "<<instLumis.at(i)<<" E30 cm^-2 s^-1, livetime is: "<<livetimeForInstLumi.at(i)<<" sec"<<endl;
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


  edm::Handle<std::vector<CandidateEvent> > events;
  iEvent.getByToken (eventsToken_, events);
  int instLumi = (int)events->begin()->instLumi();
  //clog<<"instLumi is: "<<instLumi<<endl;

  for(unsigned int i=0; i<instLumis.size(); i++){
    if(instLumi==instLumis.at(i)){
      livetimeForInstLumi.at(i) += livetime_.getLivetimeByLS(run,lb);
      //clog<<"livetimeForInstLumi.at("<<i<<") is: "<<livetimeForInstLumi.at(i)<<endl;
    }
  }



}//end of analyze

void GetLivetime::endJob(){
}//end of endJob()


void GetLivetime::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(GetLivetime);


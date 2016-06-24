#include <iostream>
#include <fstream>
#include <TVector3.h>
#include "TFile.h"
#include "TH1.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/DelayedMuonsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

DelayedMuonsEventVariableProducer::DelayedMuonsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tracksToken_ = consumes<vector<TYPE(tracks)> >(collections_.getParameter<edm::InputTag>("tracks"));
  secondaryTracksToken_ = consumes<vector<TYPE(secondaryTracks)> >(collections_.getParameter<edm::InputTag>("secondaryTracks"));
}

DelayedMuonsEventVariableProducer::~DelayedMuonsEventVariableProducer()
{
}

void DelayedMuonsEventVariableProducer::AddVariables(const edm::Event & event) {
  
  edm::Handle<std::vector<CandidateDelayedMuonsTrack> > tracks;
  event.getByToken(tracksToken_, tracks);

  edm::Handle<std::vector<CandidateDelayedMuonsTrack> > secondaryTracks;
  event.getByToken(secondaryTracksToken_, secondaryTracks);
  
  (*eventvariables)["nTracks"] = tracks->size();
  (*eventvariables)["nSecondaryTracks"] = secondaryTracks->size();
  //std::cout<<"nTracks is: "<<tracks->size()<<std::endl;

  //for(decltype(tracks->size()) i = 0; i != tracks->size(); ++i) {
  //std::cout<<"track number "<<i<<": phi is: "<<tracks->at(i).phi()<<std::endl;
  //std::cout<<"track number "<<i<<": pt is: "<<tracks->at(i).pt()<<std::endl;
  //if(tracks->at(i).phi()>0.){
  //}
  //}
  
}//end of AddVariables()
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DelayedMuonsEventVariableProducer);

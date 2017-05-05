#include <iostream>
#include <fstream>
#include <TVector3.h>
#include "TFile.h"
#include "TH1.h"
#include "TRandom2.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/DelayedMuonsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

DelayedMuonsEventVariableProducer::DelayedMuonsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tracksToken_ = consumes<vector<TYPE(tracks)> >(collections_.getParameter<edm::InputTag>("tracks"));
  secondaryTracksToken_ = consumes<vector<TYPE(secondaryTracks)> >(collections_.getParameter<edm::InputTag>("secondaryTracks"));
  rndm = new TRandom2();
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

  //for pt resolution signal systematic:
  //get random number from a Gaussian with mean 0 and sigma 0.09
  //multiply this random number by the track's pt and add to original pt, to smear by 9% of the pt
  //then observe change in signal yield with smeared pt
  double ptSmearedUpper = 0.;
  double ptSmearedLower = 0.;
  double pSmearedUpper = 0.;
  double pSmearedLower = 0.;

  for(decltype(tracks->size()) i = 0; i != tracks->size(); ++i) {
    //std::cout<<"track number "<<i<<": phi is: "<<tracks->at(i).phi()<<std::endl;
    //std::cout<<"track number "<<i<<": pt is: "<<tracks->at(i).pt()<<std::endl;
    double randomNum = rndm->Gaus(0, 0.09);
    //std::cout<<"randomNum is: "<<randomNum<<std::endl;
    if(ptSmearedUpper==0. && tracks->at(i).phi()>0.){
      ptSmearedUpper = tracks->at(i).pt()*(1 + randomNum);
      pSmearedUpper = tracks->at(i).p()*(1 + randomNum);
    }
    if(ptSmearedLower==0. && tracks->at(i).phi()<=0.){
      ptSmearedLower = tracks->at(i).pt()*(1 + randomNum);
      pSmearedLower = tracks->at(i).p()*(1 + randomNum);
    } 
  }
  
  //std::cout<<"ptSmearedUpper is: "<<ptSmearedUpper<<std::endl;
  //std::cout<<"ptSmearedLower is: "<<ptSmearedLower<<std::endl;

  (*eventvariables)["ptSmearedUpper"] = ptSmearedUpper;
  (*eventvariables)["ptSmearedLower"] = ptSmearedLower;
  (*eventvariables)["pSmearedUpper"] = pSmearedUpper;
  (*eventvariables)["pSmearedLower"] = pSmearedLower;

}//end of AddVariables()
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DelayedMuonsEventVariableProducer);

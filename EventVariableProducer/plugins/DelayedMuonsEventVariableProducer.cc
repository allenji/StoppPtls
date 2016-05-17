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
}

DelayedMuonsEventVariableProducer::~DelayedMuonsEventVariableProducer()
{
}

void DelayedMuonsEventVariableProducer::AddVariables(const edm::Event & event) {
  
  edm::Handle<std::vector<CandidateDelayedMuonsTrack> > tracks;
  event.getByToken(tracksToken_, tracks);
  
  (*eventvariables)["nTracks"] = tracks->size();
  std::cout<<"nTracks is: "<<tracks->size()<<std::endl;

  int upper0_index = 999;
  int upper1_index = 999;
  int upper2_index = 999;
  int lower0_index = 999;
  int lower1_index = 999;
  int lower2_index = 999;
  for(decltype(tracks->size()) i = 0; i != tracks->size(); ++i) {
    std::cout<<"track phi is: "<<(tracks->at(i)).phi()<<std::endl;

    if((tracks->at(i)).phi()>0.){
      if(i==0) upper0_index = i;
      if(i==1) upper1_index = i;
      if(i==2) upper2_index = i;
    }//end of if upper
    else{
      if(i==0) lower0_index = i;
      if(i==1) lower1_index = i;
      if(i==2) lower2_index = i;
    }//end of if lower

  }//end of loop over DSA tracks
  std::cout<<std::endl;

  if(upper0_index!=999){
    (*eventvariables)["pt_upper0"] = (tracks->at(upper0_index)).pt();
  }
  else{
    (*eventvariables)["pt_upper0"] = -999;
  }
  if(upper1_index!=999){
    (*eventvariables)["pt_upper1"] = (tracks->at(upper1_index)).pt();
  }
  else{
    (*eventvariables)["pt_upper1"] = -999;
  }
  if(upper2_index!=999){
    (*eventvariables)["pt_upper2"] = (tracks->at(upper2_index)).pt();
  }
  else{
    (*eventvariables)["pt_upper2"] = -999;
  }


  if(lower0_index!=999){
    (*eventvariables)["pt_lower0"] = (tracks->at(lower0_index)).pt();
  }
  else{
    (*eventvariables)["pt_lower0"] = -999;
  }
  if(lower1_index!=999){
    (*eventvariables)["pt_lower1"] = (tracks->at(lower1_index)).pt();
  }
  else{
    (*eventvariables)["pt_lower1"] = -999;
  }
  if(lower2_index!=999){
    (*eventvariables)["pt_lower2"] = (tracks->at(lower2_index)).pt();
  }
  else{
    (*eventvariables)["pt_lower2"] = -999;
  }

}//end of AddVariables()
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DelayedMuonsEventVariableProducer);

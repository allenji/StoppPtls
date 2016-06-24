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
  /*
    long unsigned int nRpcHits = tracks->at(upper0_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_upper0"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_upper0"] =            Rpc_Bx_Pattern(tracks,upper0_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_upper0"] =            Rpc_Bx_Average(tracks,upper0_index,nRpcHits);
  */
}//end of AddVariables()

int DelayedMuonsEventVariableProducer::Rpc_Bx_Pattern(edm::Handle<std::vector<CandidateDelayedMuonsTrack> > &tracks, long unsigned int& i, long unsigned int& nRpcHits) {

  bool all_bx_0 = true;
  bool all_bx_positive = true;
  bool all_bx_negative = true;
  bool all_bx_positiveOr0 = true;
  bool all_bx_negativeOr0 = true;
  bool all_bx_constant = true;
  bool all_bx_increasing = true;
  bool all_bx_decreasing = true;

  if(nRpcHits==0){
    all_bx_0 = false;
    all_bx_positive = false;
    all_bx_negative = false;
    all_bx_positiveOr0 = false;
    all_bx_negativeOr0 = false;
    all_bx_constant = false;
    all_bx_increasing = false;
    all_bx_decreasing = false;
  }

  //loop over Rpc hits
  for(unsigned int j = 0; j != nRpcHits; ++j) {
    //std::cout<<"  for rpc hit "<<j<<", BX is: "<<tracks->at(i).rpcHitBx().at(j)<<", Z is: "<<tracks->at(i).rpcHitZ().at(j)<<", Rho is: "<<tracks->at(i).rpcHitRho().at(j)<<", phi is: "<<tracks->at(i).rpcHitPhi().at(j)<<", region is: "<<tracks->at(i).rpcHitRegion().at(j)<<std::endl;
    if(tracks->at(i).rpcHitBx().at(j) != 0) all_bx_0 = false;
    if(tracks->at(i).rpcHitBx().at(j) <= 0) all_bx_positive = false;
    if(tracks->at(i).rpcHitBx().at(j) >= 0) all_bx_negative = false;
    if(tracks->at(i).rpcHitBx().at(j) < 0) all_bx_positiveOr0 = false;
    if(tracks->at(i).rpcHitBx().at(j) > 0) all_bx_negativeOr0 = false;
    unsigned int k=j+1;
    if(k<nRpcHits){
      if(tracks->at(i).rpcHitBx().at(k) != tracks->at(i).rpcHitBx().at(j)) all_bx_constant = false;
      if(tracks->at(i).rpcHitBx().at(k) < tracks->at(i).rpcHitBx().at(j)) all_bx_increasing = false;
      if(tracks->at(i).rpcHitBx().at(k) > tracks->at(i).rpcHitBx().at(j)) all_bx_decreasing = false;
    }
  }
  if(all_bx_constant) {
    all_bx_increasing = false;
    all_bx_decreasing = false;
  }

  if(nRpcHits<=0) return(-1);
  if(all_bx_0 && all_bx_constant){
    return(0);
    //cout<<"0BX"<<endl;
  }
  if(all_bx_positive && all_bx_constant){
    return(1);
    //cout<<"positiveConstantBX"<<endl;
  }
  if(all_bx_positiveOr0 && all_bx_increasing){
    return(2);
    //cout<<"positiveOr0IncreasingBX"<<endl;
  }
  if(all_bx_positiveOr0 && all_bx_decreasing){
    return(3);
    //cout<<"positiveOr0DecreasingBX"<<endl;
  }
  if(all_bx_positiveOr0 && !all_bx_decreasing && !all_bx_increasing && !all_bx_constant){
    return(4);
    //cout<<"positiveOr0StrangeBX"<<endl;
  }
  if(all_bx_negative && all_bx_constant){
    return(5);
    //cout<<"negativeConstantBX"<<endl;
  }
  if(all_bx_negativeOr0 && all_bx_increasing){
    return(6);
    //cout<<"negativeOr0IncreasingBX"<<endl;
  }
  if(all_bx_negativeOr0 && all_bx_decreasing){
    return(7);
    //cout<<"negativeOr0DecreasingBX"<<endl;
  }
  if(all_bx_negativeOr0 && !all_bx_decreasing && !all_bx_increasing && !all_bx_constant){
    return(8);
    //cout<<"negativeOr0StrangeBX"<<endl;
  }
  return(-1);
}//end of Rpc_Bx_Pattern

double DelayedMuonsEventVariableProducer::Rpc_Bx_Average(edm::Handle<std::vector<CandidateDelayedMuonsTrack> > &tracks, long unsigned int& i, long unsigned int& nRpcHits) {
  double rpc_bx_average = 0.;

  //loop over Rpc hits
  for(unsigned int j = 0; j != nRpcHits; ++j) {
    rpc_bx_average += tracks->at(i).rpcHitBx().at(j);
  }

  if(nRpcHits!=0) rpc_bx_average = 1.0*rpc_bx_average/nRpcHits;
  else rpc_bx_average = -999;

  return rpc_bx_average;
}//end of Rpc_Bx_Average
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DelayedMuonsEventVariableProducer);

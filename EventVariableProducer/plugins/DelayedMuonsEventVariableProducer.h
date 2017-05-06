#ifndef DELAYEDMUONSEVENTVARIABLEPRODUCER_H
#define DELAYEDMUONSEVENTVARIABLEPRODUCER_H

#include "TFile.h"
#include "TH1.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

#include "StoppPtls/Collection/interface/CandidateDelayedMuonsTrack.h"

using namespace std;

class DelayedMuonsEventVariableProducer : public EventVariableProducer
{
 public:
  DelayedMuonsEventVariableProducer (const edm::ParameterSet &);
  ~DelayedMuonsEventVariableProducer ();
  
 private:
  void AddVariables(const edm::Event &);

  edm::EDGetTokenT<vector<TYPE(tracks)> > tracksToken_;
  edm::EDGetTokenT<vector<TYPE(secondaryTracks)> > secondaryTracksToken_;
  TRandom2* rndm;
  double ptResolutionWidth_;
};


#endif

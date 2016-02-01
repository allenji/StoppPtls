#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/StoppPtlsEventVariableProducer.h"

StoppPtlsEventVariableProducer::StoppPtlsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
}

StoppPtlsEventVariableProducer::~StoppPtlsEventVariableProducer()
{
}

void 
StoppPtlsEventVariableProducer::AddVariables(const edm::Event & event) {
  edm::Handle<std::vector<CandidateJet> > jets;
  edm::Handle<std::vector<CandidateDTSeg> > dtsegs;
  edm::Handle<std::vector<CandidateCscSeg> > cscsegs;
  edm::Handle<std::vector<CandidateRpcHit> > rpchits;

  anatools::getCollection (collections_.getParameter<edm::InputTag> ("jets"), jets, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("dtsegs"), dtsegs, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("cscsegs"), cscsegs, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("rpchits"), rpchits, event);

  (*eventvariables)["cscSegN"] = cscsegs->size();

  double maxDeltaPhi = -1.;
  double testPhi = -1.;

  for (decltype(dtsegs->size()) i = 0; i != dtsegs->size(); ++i) {
    if (i == 0)
      testPhi = (dtsegs->at(i)).phi();
    else {
      double deltaphi = acos(cos((dtsegs->at(i)).phi()-testPhi));
      if (deltaphi > maxDeltaPhi) maxDeltaPhi = deltaphi;
    }
  }
  (*eventvariables)["maxDeltaPhi"] = maxDeltaPhi;

  double maxRPCDeltaPhi = -1.;
  unsigned closeRPCPairs = 0;
  for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
    if (i == 0)
      testPhi = (rpchits->at(i)).phi();
    else {
      double deltaphi = acos(cos((rpchits->at(i)).phi()-testPhi));
      if (deltaphi > maxRPCDeltaPhi) maxRPCDeltaPhi = deltaphi;
    }
    for (decltype(i) j = i+1; j < rpchits->size(); ++j){
      double deltaPhi = acos(cos((rpchits->at(i)).phi()-(rpchits->at(j)).phi()));
      if (deltaPhi > 1.57) {
        closeRPCPairs++;
      }
    }
  }
  (*eventvariables)["maxRPCDeltaPhi"] = maxRPCDeltaPhi;
  (*eventvariables)["nCloseRPCPairs"] = closeRPCPairs;
  
  if (jets->size() == 0){
    (*eventvariables)["leadingJetEta"] = 999.0;
    (*eventvariables)["leadingJetN90"] = -1;
  }
  else {
    (*eventvariables)["leadingJetEta"] = fabs(jets->begin()->eta());
    (*eventvariables)["leadingJetN90"] = jets->begin()->n90();
  }

  if (jets->size() == 0 && dtsegs->size() ==0){
    (*eventvariables)["maxDeltaJetPhi"] = -1.0;
  }
  else {
    double maxDeltaJetPhi = -1.;
    for ( auto itjet = jets->begin(); itjet != jets->end(); ++itjet){
      for (auto itdt = dtsegs->begin(); itdt != dtsegs->end(); ++itdt){
        double deltajetphi = acos(cos(itdt->phi() - itjet->phi()));
        if (deltajetphi > maxDeltaJetPhi)
          maxDeltaJetPhi = deltajetphi;
      }
    }
    (*eventvariables)["maxDeltaJetPhi"] = maxDeltaJetPhi;
  }
  (*eventvariables)["jetnumber"] = jets->size();
  if (jets->size() > 1) {
    (*eventvariables)["secondJetEnergy"] = (jets->at(1)).energy();
  }
  else {
    (*eventvariables)["secondJetEnergy"] = -1.0;
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsEventVariableProducer);

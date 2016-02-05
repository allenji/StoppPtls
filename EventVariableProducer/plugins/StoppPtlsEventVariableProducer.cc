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

  (*eventvariables)["jetN"] = jets->size();
  (*eventvariables)["dtSegN"] = dtsegs->size();
  (*eventvariables)["cscSegN"] = cscsegs->size();
  (*eventvariables)["rpcHitN"] = rpchits->size();
  (*eventvariables)["nima"] = 1.0;

  double maxDeltaPhi = -1.;
  double testPhi = -1.;
  double outerDT = 0.00000001; // avoid divide by zero
  int innerDT = 0;

  for (decltype(dtsegs->size()) i = 0; i != dtsegs->size(); ++i) {
    if (i == 0)
      testPhi = (dtsegs->at(i)).phi();
    else {
      double deltaphi = acos(cos((dtsegs->at(i)).phi()-testPhi));
      if (deltaphi > maxDeltaPhi) maxDeltaPhi = deltaphi;
    }

    if(dtsegs->at(i).r()>560) outerDT++;
    else innerDT++;
  }
  (*eventvariables)["maxDeltaPhi"] = maxDeltaPhi;
  (*eventvariables)["outerDT"] = outerDT;
  (*eventvariables)["innerDT"] = innerDT;

  double maxRPCDeltaPhi = -1.;
  unsigned closeRPCPairs = 0;
  double outerRPC = 0.00000001;
  double innerRPC = 0;

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
    if(rpchits->at(i).r()>560) outerRPC++;
    else innerRPC++;
  }
  (*eventvariables)["maxRPCDeltaPhi"] = maxRPCDeltaPhi;
  (*eventvariables)["nCloseRPCPairs"] = closeRPCPairs;
  (*eventvariables)["outerRPC"] = outerRPC;
  (*eventvariables)["innerRPC"] = innerRPC;
  
  if (jets->size() > 0){
    (*eventvariables)["leadingJetEnergy"] = jets->begin()->energy();
    (*eventvariables)["leadingJetEt"] = jets->begin()->et();
    (*eventvariables)["leadingJetEta"] = fabs(jets->begin()->eta());
    (*eventvariables)["leadingJetPhi"] = jets->begin()->phi();
    (*eventvariables)["leadingJetN60"] = jets->begin()->n60();
    (*eventvariables)["leadingJetN90"] = jets->begin()->n90();
  }
  else {
    (*eventvariables)["leadingJetEnergy"] = -1;
    (*eventvariables)["leadingJetEt"] = -1;
    (*eventvariables)["leadingJetEta"] = 999.0;
    (*eventvariables)["leadingJetPhi"] = 999.0;
    (*eventvariables)["leadingJetN60"] = -1;
    (*eventvariables)["leadingJetN90"] = -1;
  }

  if (jets->size() > 1){
    (*eventvariables)["secondJetEnergy"] = (jets->at(1)).energy();
    (*eventvariables)["secondJetEt"] = (jets->at(1)).et();
    (*eventvariables)["secondJetEta"] = fabs((jets->at(1)).eta());
    (*eventvariables)["secondJetPhi"] = (jets->at(1)).phi();
    (*eventvariables)["secondJetN60"] = (jets->at(1)).n60();
    (*eventvariables)["secondJetN90"] = (jets->at(1)).n90();
  }
  else {
    (*eventvariables)["secondJetEnergy"] = -1;
    (*eventvariables)["secondJetEt"] = -1;
    (*eventvariables)["secondJetEta"] = 999.0;
    (*eventvariables)["secondJetPhi"] = 999.0;
    (*eventvariables)["secondJetN60"] = -1;
    (*eventvariables)["secondJetN90"] = -1;
  }

  int nJetsEMin10  = 0;
  int nJetsEMin20  = 0;
  int nJetsEMin50  = 0;
  int nJetsEMin100 = 0;
  int nJetsEMin200 = 0;

  if (jets->size() == 0 && dtsegs->size() ==0){
    (*eventvariables)["maxDeltaJetPhi"] = -1.0;
  }
  else {
    double maxDeltaJetPhi = -1.;
    for ( auto itjet = jets->begin(); itjet != jets->end(); ++itjet){

      if (itjet->energy() > 10)  nJetsEMin10++; 
      if (itjet->energy() > 20)  nJetsEMin20++; 
      if (itjet->energy() > 50)  nJetsEMin50++; 
      if (itjet->energy() > 100) nJetsEMin100++; 
      if (itjet->energy() > 200) nJetsEMin200++; 

      for (auto itdt = dtsegs->begin(); itdt != dtsegs->end(); ++itdt){
        double deltajetphi = acos(cos(itdt->phi() - itjet->phi()));
        if (deltajetphi > maxDeltaJetPhi)
          maxDeltaJetPhi = deltajetphi;
      }
    }
    (*eventvariables)["maxDeltaJetPhi"] = maxDeltaJetPhi;
  }

  (*eventvariables)["nJetsEMin10"]  = nJetsEMin10; // Should be identical to NJets.  
  (*eventvariables)["nJetsEMin20"]  = nJetsEMin20; 
  (*eventvariables)["nJetsEMin50"]  = nJetsEMin50; 
  (*eventvariables)["nJetsEMin100"] = nJetsEMin100; 
  (*eventvariables)["nJetsEMin200"] = nJetsEMin200; 
  
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsEventVariableProducer);

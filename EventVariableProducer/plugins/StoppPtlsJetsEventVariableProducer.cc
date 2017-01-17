#include <iostream>
#include <fstream>
#include <TVector3.h>
#include "TFile.h"
#include "TH1.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/StoppPtlsJetsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

StoppPtlsJetsEventVariableProducer::StoppPtlsJetsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  jetsToken_ = consumes<vector<TYPE(jets)> >(collections_.getParameter<edm::InputTag>("jets"));
  dtsegsToken_ = consumes<vector<TYPE(dtsegs)> >(collections_.getParameter<edm::InputTag>("dtsegs"));
  cscsegsToken_ = consumes<vector<TYPE(cscsegs)> >(collections_.getParameter<edm::InputTag>("cscsegs"));
  rpchitsToken_ = consumes<vector<TYPE(rpchits)> >(collections_.getParameter<edm::InputTag>("rpchits"));
}

StoppPtlsJetsEventVariableProducer::~StoppPtlsJetsEventVariableProducer()
{
}

void StoppPtlsJetsEventVariableProducer::AddVariables(const edm::Event & event) {
     
  edm::Handle<std::vector<CandidateJet> > jets;
  edm::Handle<std::vector<CandidateDTSeg> > dtsegs;
  edm::Handle<std::vector<CandidateCscSeg> > cscsegs;
  edm::Handle<std::vector<CandidateRpcHit> > rpchits;
  
  event.getByToken (jetsToken_, jets);
  event.getByToken (dtsegsToken_, dtsegs);
  event.getByToken (cscsegsToken_, cscsegs);
  event.getByToken (rpchitsToken_, rpchits);

  (*eventvariables)["jetN"] = jets->size();
  (*eventvariables)["dtSegN"] = dtsegs->size();
  (*eventvariables)["cscSegN"] = cscsegs->size();
  (*eventvariables)["rpcHitN"] = rpchits->size();
  (*eventvariables)["nima"] = 1.0;

  double maxDeltaPhi = -1.;
  double outerDT = 0.00000001; // avoid divide by zero
  double  innerDT = 0;

  //loop over DT segments
  for (decltype(dtsegs->size()) i = 0; i != dtsegs->size(); ++i) {
    for (decltype(i) j = 0; j < i; ++j){
      double deltaphi = acos(cos((dtsegs->at(i)).phi()-(dtsegs->at(j)).phi()));
      if (deltaphi > maxDeltaPhi) maxDeltaPhi = deltaphi;
    }
    if(dtsegs->at(i).r()>560) outerDT++;
    else innerDT++;
  }

  (*eventvariables)["maxDeltaPhi"] = maxDeltaPhi;
  (*eventvariables)["outerDT"] = outerDT;
  (*eventvariables)["innerDT"] = innerDT;

  double maxRPCDeltaPhi = -1.;
  double maxRPCDeltaPhi_outer = -1.;
  unsigned closeRPCPairs = 0;
  unsigned oppositeRPCPairs = 0;
  unsigned totalRPCPairs = 0;
  double outerRPC = 0.00000001;
  double innerRPC = 0;

  int outerRPCbarrel = 0;
  int innerRPCbarrel = 0;
  int RPCbarrel = 0;
  int outerRPCendcap = 0;
  int innerRPCendcap = 0;
  int RPCendcap = 0;

  int NOuterCsc = 0;
  int NInnerCsc = 0;
  bool havingCsc = 0;
  bool havingCscSegNHit56 = 0;
  for (decltype(cscsegs->size()) i = 0; i != cscsegs->size(); ++i)  {
    if ((cscsegs->at(i)).endcap() == 1 && (cscsegs->at(i)).station() == 1) {
      havingCsc = 1;
      break;
    }
  }

  for (decltype(cscsegs->size()) i = 0; i != cscsegs->size(); ++i)  {
    if ((cscsegs->at(i)).r() > 340) {
      havingCscSegNHit56 = 1;
    }
    if ((cscsegs->at(i)).r() <= 340 && (cscsegs->at(i)).nHits() > 4) {
      havingCscSegNHit56 = 1;
    }
    if ((cscsegs->at(i)).r() > 340) {
      NOuterCsc++;
    }
    else {
      NInnerCsc++;
    }
}
  (*eventvariables)["NOuterCsc"] = NOuterCsc;
  (*eventvariables)["NInnerCsc"] = NInnerCsc;


  (*eventvariables)["havingSpecificCsc"] = havingCsc;
  (*eventvariables)["havingCscSegNHit56"] = havingCscSegNHit56;
  //loop over RPC hits
  for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
    for (decltype(i) j = 0; j < i; ++j){
      totalRPCPairs++;
      double deltaPhi = acos(cos((rpchits->at(i)).phi()-(rpchits->at(j)).phi()));
      if (deltaPhi > maxRPCDeltaPhi) maxRPCDeltaPhi = deltaPhi;
      if (deltaPhi > 1.57) closeRPCPairs++;
      if (deltaPhi > 3.0) oppositeRPCPairs++;      

      if(rpchits->at(i).r()>560 && rpchits->at(j).r()>560){
        double deltaPhi_outer = acos(cos((rpchits->at(i)).phi()-(rpchits->at(j)).phi()));
        if (deltaPhi_outer > maxRPCDeltaPhi_outer) maxRPCDeltaPhi_outer = deltaPhi_outer;
      }
    }
    if(rpchits->at(i).r()>560) outerRPC++;
    else innerRPC++;
    if(rpchits->at(i).region()==0){ //barrel
      RPCbarrel++;
      if(rpchits->at(i).r()>560) outerRPCbarrel++;
      else innerRPCbarrel++;
    }
    else{ //endcap
      RPCendcap++;
      if(rpchits->at(i).r()>560) outerRPCendcap++;
      else innerRPCendcap++;
    }
  }

  (*eventvariables)["maxRPCDeltaPhi"] = maxRPCDeltaPhi;
  (*eventvariables)["maxRPCDeltaPhi_outer"] = maxRPCDeltaPhi_outer;
  (*eventvariables)["nCloseRPCPairs"] = closeRPCPairs;
  (*eventvariables)["nOppositeRPCPairs"] = oppositeRPCPairs;
  (*eventvariables)["outerRPC"] = outerRPC;
  (*eventvariables)["innerRPC"] = innerRPC;

  (*eventvariables)["outerRPCbarrel"] = outerRPCbarrel;
  (*eventvariables)["innerRPCbarrel"] = innerRPCbarrel;
  (*eventvariables)["RPCbarrel"] = RPCbarrel;
  (*eventvariables)["outerRPCendcap"] = outerRPCendcap;
  (*eventvariables)["innerRPCendcap"] = innerRPCendcap;
  (*eventvariables)["RPCendcap"] = RPCendcap;

  unsigned nCloseAllAllRpcPairDeltaR0p2 = 0; //rpchit-rpchit pairs, selected from all available rpc hits
  unsigned nCloseAllAllRpcPairDeltaR0p4 = 0;
  unsigned nCloseAllAllRpcPairDeltaR0p6 = 0;
  unsigned nCloseAllAllRpcPairDeltaR0p8 = 0;
  unsigned nCloseOuterAllRpcPairDeltaR0p2 = 0; //rpchit-rpchit pairs, the first rpchit is in outer barrel, no such restriction on the second rpchit
  unsigned nCloseOuterAllRpcPairDeltaR0p4 = 0;
  unsigned nCloseOuterAllRpcPairDeltaR0p6 = 0;
  unsigned nCloseOuterAllRpcPairDeltaR0p8 = 0;
  unsigned nCloseOuterAllBarrelRPCPairDeltaR0p2 = 0;

  if (rpchits->size() > 1) {
    for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
      if ((rpchits->at(i)).r() < 560) {
        for (decltype(i) j = 0; j != i; ++j) {
          TVector3 tveci((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z());
          TVector3 tvecj((rpchits->at(j)).x(), (rpchits->at(j)).y(), (rpchits->at(j)).z());
          double rpc_eta_i = tveci.Eta();
          double rpc_eta_j = tvecj.Eta();
          double deltaR = reco::deltaR(rpc_eta_i, (rpchits->at(i)).phi(), rpc_eta_j, (rpchits->at(j)).phi());
          if (deltaR < 0.2) nCloseAllAllRpcPairDeltaR0p2++;
          if (deltaR < 0.4) nCloseAllAllRpcPairDeltaR0p4++;
          if (deltaR < 0.6) nCloseAllAllRpcPairDeltaR0p6++;
          if (deltaR < 0.8) nCloseAllAllRpcPairDeltaR0p8++;
        }
          
      }
      else {
        for (decltype(i) j = 0; j != i; ++j) {
          TVector3 tveci((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z());
          TVector3 tvecj((rpchits->at(j)).x(), (rpchits->at(j)).y(), (rpchits->at(j)).z());
          double rpc_eta_i = tveci.Eta();
          double rpc_eta_j = tvecj.Eta();
          double deltaR = reco::deltaR(rpc_eta_i, (rpchits->at(i)).phi(), rpc_eta_j, (rpchits->at(j)).phi());
          if (deltaR < 0.2) {
            nCloseAllAllRpcPairDeltaR0p2++;
            nCloseOuterAllRpcPairDeltaR0p2++;
            if ((rpchits->at(i)).region() == 0 && (rpchits->at(j)).region() == 0)
              nCloseOuterAllBarrelRPCPairDeltaR0p2++;
          }
          if (deltaR < 0.4) {
            nCloseAllAllRpcPairDeltaR0p4++;
            nCloseOuterAllRpcPairDeltaR0p4++;
          }
          if (deltaR < 0.6) {
            nCloseAllAllRpcPairDeltaR0p6++;
            nCloseOuterAllRpcPairDeltaR0p6++;
          }
          if (deltaR < 0.8) {
            nCloseAllAllRpcPairDeltaR0p8++;
            nCloseOuterAllRpcPairDeltaR0p8++;
          }
        }
      }
    }
  }
  (*eventvariables)["nCloseAllAllRpcPairDeltaR0p2"] = nCloseAllAllRpcPairDeltaR0p2;
  (*eventvariables)["nCloseAllAllRpcPairDeltaR0p4"] = nCloseAllAllRpcPairDeltaR0p4;
  (*eventvariables)["nCloseAllAllRpcPairDeltaR0p6"] = nCloseAllAllRpcPairDeltaR0p6;
  (*eventvariables)["nCloseAllAllRpcPairDeltaR0p8"] = nCloseAllAllRpcPairDeltaR0p8;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p2"] = nCloseOuterAllRpcPairDeltaR0p2;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p4"] = nCloseOuterAllRpcPairDeltaR0p4;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p6"] = nCloseOuterAllRpcPairDeltaR0p6;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p8"] = nCloseOuterAllRpcPairDeltaR0p8;
  (*eventvariables)["nCloseOuterAllBarrelRPCPairDeltaR0p2"] = nCloseOuterAllBarrelRPCPairDeltaR0p2;

  unsigned ljetRPCPairsST1 = 0;
  unsigned ljetRPCPairsGT1 = 0;
  unsigned ljetRPCPairsGT1p5 = 0;
  unsigned ljetRPCPairsGT0p5 = 0;

  unsigned ljetRPCPairsDeltaR0p6 = 0; // deltaR<jet, rpchit> <= 0.6
  unsigned ljetRPCPairsDeltaR0p8 = 0;
  unsigned ljetRPCPairsDeltaR1p0 = 0;
  unsigned ljetRPCPairsDeltaR1p2 = 0;
  unsigned ljetRPCPairsDeltaR1p4 = 0;
  unsigned ljetRPCPairsDeltaR1p6 = 0;
  unsigned ljetRPCPairsDeltaR1p8 = 0;

  unsigned ljetOuterRPCPairsDeltaR0p6 = 0;
  unsigned ljetOuterRPCPairsDeltaR0p8 = 0;
  unsigned ljetOuterRPCPairsDeltaR1p0 = 0;
  unsigned ljetOuterRPCPairsDeltaR1p2 = 0;
  unsigned ljetOuterRPCPairsDeltaR1p4 = 0;
  unsigned ljetOuterRPCPairsDeltaR1p6 = 0;
  unsigned ljetOuterRPCPairsDeltaR1p8 = 0;

  if (jets->size() > 0 && rpchits->size() > 0) {
    double jetphi = jets->begin()->phi();
    for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
      double deltajetRPCphi = acos(cos((rpchits->at(i)).phi()-jetphi));
      if (deltajetRPCphi < 1) {
        ljetRPCPairsST1++;
      }
      if (deltajetRPCphi > 1) {
        ljetRPCPairsGT1++;
      }
      if (deltajetRPCphi > 1.5) {
        ljetRPCPairsGT1p5++;
      }
      if (deltajetRPCphi > 0.5) {
        ljetRPCPairsGT0p5++;
      }

      TVector3 tvec((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z());
      double rpc_eta = tvec.Eta();
      double deltaR = reco::deltaR (jets->begin()->eta(), jets->begin()->phi(), rpc_eta, (rpchits->at(i)).phi());
      if (deltaR < 0.6) {
        ljetRPCPairsDeltaR0p6++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR0p6++;
      }
      if (deltaR < 0.8) {
        ljetRPCPairsDeltaR0p8++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR0p8++;
      }
      if (deltaR < 1.0) {
        ljetRPCPairsDeltaR1p0++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR1p0++;
      }
      if (deltaR < 1.2) {
        ljetRPCPairsDeltaR1p2++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR1p2++;
      }
      if (deltaR < 1.4) {
        ljetRPCPairsDeltaR1p4++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR1p4++;
      }
      if (deltaR < 1.6) {
        ljetRPCPairsDeltaR1p6++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR1p6++;
      }
      if (deltaR < 1.8) {
        ljetRPCPairsDeltaR1p8++;
        if ((rpchits->at(i)).r() > 560)
          ljetOuterRPCPairsDeltaR1p8++;
      }
    }
  }
  (*eventvariables)["nLJetRPCPairsDeltaPhiST1"] = ljetRPCPairsST1;
  (*eventvariables)["nLJetRPCPairsDeltaPhiGT1"] = ljetRPCPairsGT1;
  (*eventvariables)["nLJetRPCPairsDeltaPhiGT1p5"] = ljetRPCPairsGT1p5;
  (*eventvariables)["nLJetRPCPairsDeltaPhiGT0p5"] = ljetRPCPairsGT0p5;
  
  (*eventvariables)["nLJetRPCPairsDeltaR0p6"] = ljetRPCPairsDeltaR0p6;
  (*eventvariables)["nLJetRPCPairsDeltaR0p8"] = ljetRPCPairsDeltaR0p8;
  (*eventvariables)["nLJetRPCPairsDeltaR1p0"] = ljetRPCPairsDeltaR1p0;
  (*eventvariables)["nLJetRPCPairsDeltaR1p2"] = ljetRPCPairsDeltaR1p2;
  (*eventvariables)["nLJetRPCPairsDeltaR1p4"] = ljetRPCPairsDeltaR1p4;
  (*eventvariables)["nLJetRPCPairsDeltaR1p6"] = ljetRPCPairsDeltaR1p6;
  (*eventvariables)["nLJetRPCPairsDeltaR1p8"] = ljetRPCPairsDeltaR1p8;

  (*eventvariables)["nLJetOuterRPCPairsDeltaR0p6"] = ljetOuterRPCPairsDeltaR0p6;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR0p8"] = ljetOuterRPCPairsDeltaR0p8;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR1p0"] = ljetOuterRPCPairsDeltaR1p0;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR1p2"] = ljetOuterRPCPairsDeltaR1p2;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR1p4"] = ljetOuterRPCPairsDeltaR1p4;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR1p6"] = ljetOuterRPCPairsDeltaR1p6;
  (*eventvariables)["nLJetOuterRPCPairsDeltaR1p8"] = ljetOuterRPCPairsDeltaR1p8;


  if (jets->size() > 0){
    (*eventvariables)["leadingJetEnergy"] = jets->begin()->energy();
    (*eventvariables)["leadingJetEt"] = jets->begin()->et();
    (*eventvariables)["leadingJetEta"] = fabs(jets->begin()->eta());
    (*eventvariables)["leadingJetEtaPM"] = jets->begin()->eta();
    (*eventvariables)["leadingJetPhi"] = jets->begin()->phi();
    (*eventvariables)["leadingJetN60"] = jets->begin()->n60();
    (*eventvariables)["leadingJetN90"] = jets->begin()->n90();
    (*eventvariables)["leadingJetEMFraction"] = jets->begin()->emJetEnergyFraction();
  }
  else {
    (*eventvariables)["leadingJetEnergy"] = -1;
    (*eventvariables)["leadingJetEt"] = -1;
    (*eventvariables)["leadingJetEta"] = 999.0;
    (*eventvariables)["leadingJetEtaPM"] = 999.0;
    (*eventvariables)["leadingJetPhi"] = 999.0;
    (*eventvariables)["leadingJetN60"] = -1;
    (*eventvariables)["leadingJetN90"] = -1;
    (*eventvariables)["leadingJetEMFraction"] = -1;
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
  //CSC DT angles
  double maxDeltaPhiCscPair = -1;
  double maxDeltaPhiCscDT = -1;
  double minDeltaPhiCscPair = 999;
  double minDeltaPhiCscDT = 999;
  if (cscsegs->size() >= 2) {
    int csc_size = cscsegs->size();
    double deltaPhiCscPair = 999;
    for (int i = 0; i != csc_size; ++ i) {
      if ((jets->size() > 0 && acos(cos((cscsegs->at(i)).phi() - (jets->at(0)).phi()))) < 0.4 && (cscsegs->at(i)).r() < 340)
        continue;
      for (int j = i+1; j!= csc_size; ++j) {
        if ((jets->size() > 0 && acos(cos((cscsegs->at(j)).phi() - (jets->at(0)).phi()))) < 0.4 && (cscsegs->at(j)).r() < 340)
          continue;
        deltaPhiCscPair = acos(cos((cscsegs->at(i)).phi() - (cscsegs->at(j)).phi()));
        if (deltaPhiCscPair < minDeltaPhiCscPair) {
          minDeltaPhiCscPair = deltaPhiCscPair;
        }
        if (deltaPhiCscPair > maxDeltaPhiCscPair) {
          maxDeltaPhiCscPair = deltaPhiCscPair;
        }
          
      }
    }
  }

  if (cscsegs->size() > 0 && dtsegs->size() > 0) {
    int csc_size = cscsegs->size();
    int dt_size = dtsegs->size();
    double deltaPhiCscDtPair = 999;
    for (int i = 0; i < csc_size; i++) {
      for (int j = 0; j < dt_size; j++) {
        deltaPhiCscDtPair = acos(cos((cscsegs->at(i)).phi() - (dtsegs->at(j)).phi()));
        if (deltaPhiCscDtPair < minDeltaPhiCscDT) {
          minDeltaPhiCscDT = deltaPhiCscDtPair;
        }
        if (deltaPhiCscDtPair > maxDeltaPhiCscDT) {
          maxDeltaPhiCscDT = deltaPhiCscDtPair;
        }
      }
    }
  }

  (*eventvariables)["minDeltaPhiCscPair"] = minDeltaPhiCscPair;
  (*eventvariables)["maxDeltaPhiCscPair"] = maxDeltaPhiCscPair;
  (*eventvariables)["minDeltaPhiCscDT"] = minDeltaPhiCscDT;
  (*eventvariables)["maxDeltaPhiCscDT"] = maxDeltaPhiCscDT;



  int nCscNearJetDeltaPhi0p2 = 0;
  int nCscNearJetDeltaPhi0p2EndcapPosZ = 0; 
  int nCscNearJetDeltaPhi0p2EndcapMinZ = 0;
  int nIncomingCscSegsNearJetDeltaPhi0p2 = 0;
  int nOutgoingCscSegsNearJetDeltaPhi0p2 = 0;
  double meanCscXNearJetDeltaPhi0p2 = 0.;
  double meanCscYNearJetDeltaPhi0p2 = 0.;
  double meanCscRNearJetDeltaPhi0p2 = 0.;
  double meanCscDirectionNearJetDeltaPhi0p2 = 0.;
  double meanCscPhiNearJetDeltaPhi0p2 = 0;
  
  set<int>nLayersNearJetDeltaPhi0p2;
  
  int nIncomingCscSegs = 0;
  int nOutgoingCscSegs = 0;
  double meanCscX = 0.;
  double meanCscY = 0.;
  double meanCscR = 0.;
  double meanCscPhi = 0.;
  double meanCscDirection = 0.;
  set<int> nLayers;
  double minDeltaPhiCscJet = 999.;

  double minDeltaPhiOuterCscJet = 999;
  double maxDeltaPhiOuterCscJet = -1;

  //loop over csc segments
  for (auto itcsc = cscsegs->begin(); itcsc != cscsegs->end(); ++itcsc){
    
    double cscSegX = itcsc->r()*cos(itcsc->phi());
    double cscSegY = itcsc->r()*sin(itcsc->phi());

    //incoming = time < -10; outgoing = time > -10
    //find direction of each csc segment and then average direction of the "halo" in the event
    //direction -1 means traveling in the +z direction (beam 2) and direction +1 means travel in the -z direction (beam 1)
    double cscSegDir = 0.;
    if (itcsc->time() < -15.){
      nIncomingCscSegs++;
      if (jets->size() > 0 && acos(cos(itcsc->phi() - jets->begin()->phi())) < 0.4 && itcsc->r() < 340 && itcsc->nHits() > 4) {
        nIncomingCscSegsNearJetDeltaPhi0p2++;
      }
      if(itcsc->z() < 0) cscSegDir = -1.0;  // +Z direction
      else cscSegDir = 1.0; //-Z direction
    }
    else{
      if (jets->size() > 0 && acos(cos(itcsc->phi() - jets->begin()->phi())) < 0.4 && itcsc->r() < 340 && itcsc->nHits() > 4) {
        nOutgoingCscSegsNearJetDeltaPhi0p2++; 
      }
      nOutgoingCscSegs++;
      if(itcsc->z() < 0) cscSegDir = 1.0;  // -Z direction
      else cscSegDir = -1.0; //+Z direction
    }

    meanCscX += cscSegX;
    meanCscY += cscSegY;
    meanCscR += itcsc->r();
    meanCscPhi += itcsc->phi();
    meanCscDirection += cscSegDir;

    int chamber = chamberType(itcsc->station(), itcsc->ring());
    int endcap = (itcsc->z() > 0) ? 1 : -1;
    int layer = chamber * endcap;
    nLayers.insert(layer);
    if (jets->size() > 0 && acos(cos(itcsc->phi() - jets->begin()->phi())) < 0.4 && itcsc->r() < 340 && itcsc->nHits() > 4) {
      nCscNearJetDeltaPhi0p2++;
      meanCscXNearJetDeltaPhi0p2 += cscSegX;
      meanCscYNearJetDeltaPhi0p2 += cscSegY;
      meanCscRNearJetDeltaPhi0p2 += itcsc->r();
      meanCscPhiNearJetDeltaPhi0p2 += itcsc->phi();
      meanCscDirectionNearJetDeltaPhi0p2 += cscSegDir;
      nLayersNearJetDeltaPhi0p2.insert(layer);
      if (endcap == 1) {
        nCscNearJetDeltaPhi0p2EndcapPosZ++;
      }
      else {
        nCscNearJetDeltaPhi0p2EndcapMinZ++;
      }
      
    }

    if (jets->size() > 0){
      double deltaphicscjet = acos(cos(itcsc->phi() - jets->begin()->phi()));
      if(deltaphicscjet < minDeltaPhiCscJet) 
	minDeltaPhiCscJet = deltaphicscjet;
      if (itcsc->r() > 340) {
        if (deltaphicscjet < minDeltaPhiOuterCscJet) {
          minDeltaPhiOuterCscJet = deltaphicscjet;
        }
        if (deltaphicscjet > maxDeltaPhiOuterCscJet) {
         maxDeltaPhiOuterCscJet = deltaphicscjet; 
        }
      }
    }//end of if at least 1 jet
  }//end of loop over csc segments

  meanCscDirection = meanCscDirection/cscsegs->size();
  meanCscX = meanCscX/cscsegs->size();
  meanCscY = meanCscY/cscsegs->size();
  meanCscR = meanCscR/cscsegs->size();
  meanCscPhi = meanCscPhi/cscsegs->size();

  if(nCscNearJetDeltaPhi0p2 > 0){
    meanCscDirectionNearJetDeltaPhi0p2 = meanCscDirectionNearJetDeltaPhi0p2/nCscNearJetDeltaPhi0p2;
    meanCscXNearJetDeltaPhi0p2 = meanCscXNearJetDeltaPhi0p2/nCscNearJetDeltaPhi0p2;
    meanCscYNearJetDeltaPhi0p2 = meanCscYNearJetDeltaPhi0p2/nCscNearJetDeltaPhi0p2;
    meanCscRNearJetDeltaPhi0p2 = meanCscRNearJetDeltaPhi0p2/nCscNearJetDeltaPhi0p2;
    meanCscPhiNearJetDeltaPhi0p2 = meanCscPhiNearJetDeltaPhi0p2/nCscNearJetDeltaPhi0p2;
  }

  (*eventvariables)["meanCscDirection"] = meanCscDirection;
  (*eventvariables)["meanCscX"] = meanCscX;
  (*eventvariables)["meanCscY"] = meanCscY;
  (*eventvariables)["meanCscR"] = meanCscR;
  (*eventvariables)["meanCscPhi"] = meanCscPhi;

  (*eventvariables) ["nIncomingCscSegs"] = nIncomingCscSegs;
  (*eventvariables) ["nOutgoingCscSegs"] = nOutgoingCscSegs;

  (*eventvariables)["nCscLayers"] = nLayers.size();
  (*eventvariables)["minDeltaPhiCscJet"] = minDeltaPhiCscJet;

  (*eventvariables)["minDeltaPhiOuterCscJet"] = minDeltaPhiOuterCscJet;
  (*eventvariables)["maxDeltaPhiOuterCscJet"] = maxDeltaPhiOuterCscJet;

  (*eventvariables)["meanCscDirectionNearJetDeltaPhi0p2"] = meanCscDirectionNearJetDeltaPhi0p2;
  (*eventvariables)["meanCscXNearJetDeltaPhi0p2"] = meanCscXNearJetDeltaPhi0p2;
  (*eventvariables)["meanCscYNearJetDeltaPhi0p2"] = meanCscYNearJetDeltaPhi0p2;
  (*eventvariables)["meanCscRNearJetDeltaPhi0p2"] = meanCscRNearJetDeltaPhi0p2;
  (*eventvariables)["meanCscPhiNearJetDeltaPhi0p2"] = meanCscPhiNearJetDeltaPhi0p2;
  (*eventvariables)["nCscNearJetDeltaPhi0p2"] = nCscNearJetDeltaPhi0p2;
  (*eventvariables)["nCscNearJetDeltaPhi0p2EndcapPosZ"] = nCscNearJetDeltaPhi0p2EndcapPosZ;
  (*eventvariables)["nCscNearJetDeltaPhi0p2EndcapMinZ"] = nCscNearJetDeltaPhi0p2EndcapMinZ;
  (*eventvariables)["nIncomingCscSegsNearJetDeltaPhi0p2"] = nIncomingCscSegsNearJetDeltaPhi0p2;
  (*eventvariables)["nOutgoingCscSegsNearJetDeltaPhi0p2"] = nOutgoingCscSegsNearJetDeltaPhi0p2;
  (*eventvariables)["nLayersNearJetDeltaPhi0p2"] = nLayersNearJetDeltaPhi0p2.size();

  bool havingCscDeltaJet0p4R3p4 = 0;
  if (jets->size() > 0) {
    double lJetPhi = jets->begin()->phi();
    for (auto itcsc = cscsegs->begin(); itcsc != cscsegs->end(); ++itcsc) {
      //double delta_R_pre = fabs(itcsc->phi() - lJetPhi);
//double delta_R = delta_R_pre < M_PI ? delta_R_pre : 2*M_PI - delta_R_pre;
      double delta_R = acos(cos(itcsc->phi()-lJetPhi));
      if (itcsc->r() < 340 && delta_R < 0.4 && itcsc->nHits() > 4) {
        havingCscDeltaJet0p4R3p4 = 1;
      }
    }
  }
  (*eventvariables)["havingCscDeltaJet0p4R3p4"] = havingCscDeltaJet0p4R3p4;

  

}//end of AddVariables()
  
// Shamelessly stolen from DataFormats/MuonDetId/src/CSCDetId.cc#100
int StoppPtlsJetsEventVariableProducer::chamberType(int iStation, int iRing) {
  int i = 2*iStation + iRing;
  if (iStation == 1) {
    i = i - 1;
    if (i>4) i = 1;
  }
  return i;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsJetsEventVariableProducer);

#include <TVector3.h>
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/StoppPtlsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

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
  /*
  edm::Handle<std::vector<CandidateEvent> > events;
  edm::Handle<std::vector<reco::GenParticle> > mcparticles;
  */
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("jets"), jets, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("dtsegs"), dtsegs, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("cscsegs"), cscsegs, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("rpchits"), rpchits, event);
  /*
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("events"), events, event);
  anatools::getCollection (collections_.getParameter<edm::InputTag> ("mcparticles"), mcparticles, event);
  */

  (*eventvariables)["jetN"] = jets->size();
  (*eventvariables)["dtSegN"] = dtsegs->size();
  (*eventvariables)["cscSegN"] = cscsegs->size();
  (*eventvariables)["rpcHitN"] = rpchits->size();
  (*eventvariables)["nima"] = 1.0;

  double maxDeltaPhi = -1.;
  double outerDT = 0.00000001; // avoid divide by zero
  int innerDT = 0;

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

  unsigned nCloseOuterAllRpcPairDeltaR0p4 = 0;
  unsigned nCloseOuterAllRpcPairDeltaR0p6 = 0;
  unsigned nCloseOuterAllRpcPairDeltaR0p8 = 0;

  if (rpchits->size() > 1) {
    for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
      if ((rpchits->at(i)).r() < 560) continue;
      else {
        for (decltype(i) j = 0; j != i; ++j) {
           TVector3 tveci((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z());
           TVector3 tvecj((rpchits->at(j)).x(), (rpchits->at(j)).y(), (rpchits->at(j)).z());
           double rpc_eta_i = tveci.Eta();
           double rpc_eta_j = tvecj.Eta();
           double deltaR = reco::deltaR(rpc_eta_i, (rpchits->at(i)).phi(), rpc_eta_j, (rpchits->at(j)).phi());
           if (deltaR < 0.4) nCloseOuterAllRpcPairDeltaR0p4++;
           if (deltaR < 0.6) nCloseOuterAllRpcPairDeltaR0p6++;
           if (deltaR < 0.8) nCloseOuterAllRpcPairDeltaR0p8++;
        }
      }
    }
  }
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p4"] = nCloseOuterAllRpcPairDeltaR0p4;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p6"] = nCloseOuterAllRpcPairDeltaR0p6;
  (*eventvariables)["nCloseOuterAllRpcPairDeltaR0p8"] = nCloseOuterAllRpcPairDeltaR0p8;

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

  set<int> nLayers;
  double minDeltaPhiCscJet = 999.;

  //loop over csc segments
  for (auto itcsc = cscsegs->begin(); itcsc != cscsegs->end(); ++itcsc){
    int chamber = chamberType(itcsc->station(), itcsc->ring());
    int endcap = (itcsc->z() > 0) ? 1 : -1;
    int layer = chamber * endcap;
    nLayers.insert(layer);

    if (jets->size() > 0){
      double deltaphicscjet = acos(cos(itcsc->phi() - jets->begin()->phi()));
      if(deltaphicscjet < minDeltaPhiCscJet) 
	minDeltaPhiCscJet = deltaphicscjet;
    }//end of if at least 1 jet
  }//end of loop over csc segments
  (*eventvariables)["nCscLayers"] = nLayers.size();
  (*eventvariables)["minDeltaPhiCscJet"] = minDeltaPhiCscJet;

  /*
  //gen particles
  double neutralinoMass = -999;
  double neutralinoPx = -999;
  double neutralinoPy = -999;
  double neutralinoPz = -999;
  double neutralinoPt = -999;
  double neutralinoP = -999;
  double neutralinoEta = -999;
  double neutralinoPhi = -999;

  double gluonMass = -999;
  double gluonPx = -999;
  double gluonPy = -999;
  double gluonPz = -999;
  double gluonPt = -999;
  double gluonP = -999;
  double gluonEta = -999;
  double gluonPhi = -999;

  double uMass = -999;
  double uPx = -999;
  double uPy = -999;
  double uPz = -999;
  double uPt = -999;
  double uP = -999;
  double uEta = -999;
  double uPhi = -999;

  double ubarMass = -999;
  double ubarPx = -999;
  double ubarPy = -999;
  double ubarPz = -999;
  double ubarPt = -999;
  double ubarP = -999;
  double ubarEta = -999;
  double ubarPhi = -999;

  bool matched = false;
  auto stopped_genParticle = mcparticles->begin();
  
  for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
    //if mcparticle matched to correct stopped particle ID
    if(itmcpart->pdgId()==events->begin()->stoppedParticleId()){
      matched = true;
      stopped_genParticle = itmcpart;
      //std::cout<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
      break;
    }
    //sometimes only another R-hadron, not the exact stopped particle r-hadron, is in the mcparticles list
    else if(fabs(itmcpart->pdgId())>1000900 && fabs(itmcpart->pdgId())<2000000){
      matched = true;
      stopped_genParticle = itmcpart;
      //std::cout<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
      break;
    }
  }//end of loop over mcparticles

  if(matched){
    //loop over rhadron daughters
    for(size_t j=0; j<stopped_genParticle->numberOfDaughters(); j++){
      const reco::Candidate* daughter = stopped_genParticle->daughter(j);
      int partId = daughter->pdgId();
      //std::cout<<"  daughter pdgid is: "<<partId<<std::endl;
      
      //look for sparticle (gluino, stop - left and right handed, stau) 
      if (fabs(partId) == 1000021 || fabs(partId) == 1000006 || fabs(partId) == 2000006 || fabs(partId) == 1000015 || fabs(partId) == 2000015){
	const reco::Candidate* sparticle = daughter;
	
	//loop over sparticle's daughters
	for(size_t k=0; k<sparticle->numberOfDaughters(); k++){	    
	  const reco::Candidate* daughter2 = sparticle->daughter(k);
	  //std::cout<<"  daughter2 pdgid is: "<<daughter2->pdgId()<<", mass is: "<<daughter2->mass()<<", px is: "<<daughter2->px()<<", py: "<<daughter2->py()<<", pz: "<<daughter2->pz()<<std::endl;  
	  
	  //look for neutralino
	  if(fabs(daughter2->pdgId())==1000022){
	    const reco::Candidate* neutralino = daughter2;
	    //std::cout<<"  neutralino mass is: "<<neutralino->mass()<<", px is: "<<neutralino->px()<<", py: "<<neutralino->py()<<", pz: "<<neutralino->pz()<<std::endl;
	    neutralinoMass = neutralino->mass();
	    neutralinoPx = neutralino->px();
	    neutralinoPy = neutralino->py();
	    neutralinoPz = neutralino->pz();
	    neutralinoPt = neutralino->pt();
	    neutralinoP = neutralino->p();
	    neutralinoEta = neutralino->eta();
	    neutralinoPhi = neutralino->phi();
	  }//end of if neutralino
	  
	  //look for gluon
	  if(fabs(daughter2->pdgId())==21){
	    const reco::Candidate* gluon = daughter2;
	    //std::cout<<"  gluon mass is: "<<gluon->mass()<<", px is: "<<gluon->px()<<", py: "<<gluon->py()<<", pz: "<<gluon->pz()<<std::endl;
	    gluonMass = gluon->mass();
	    gluonPx = gluon->px();
	    gluonPy = gluon->py();
	    gluonPz = gluon->pz();
	    gluonPt = gluon->pt();
	    gluonP = gluon->p();
	    gluonEta = gluon->eta();
	    gluonPhi = gluon->phi();
	  }//end of if gluon
	  
	  //look for up quark
	  if(daughter2->pdgId()==2){
	    const reco::Candidate* u = daughter2;
	    //std::cout<<"  u mass is: "<<u->mass()<<", px is: "<<u->px()<<", py: "<<u->py()<<", pz: "<<u->pz()<<std::endl;
	    uMass = u->mass();
	    uPx = u->px();
	    uPy = u->py();
	    uPz = u->pz();
	    uPt = u->pt();
	    uP = u->p();
	    uEta = u->eta();
	    uPhi = u->phi();
	  }//end of if u
	  
	  //look for ubar quark
	  if(daughter2->pdgId()==-2){
	    const reco::Candidate* ubar = daughter2;
	    //std::cout<<"  ubar mass is: "<<ubar->mass()<<", px is: "<<ubar->px()<<", py: "<<ubar->py()<<", pz: "<<ubar->pz()<<std::endl;
	    ubarMass = ubar->mass();
	    ubarPx = ubar->px();
	    ubarPy = ubar->py();
	    ubarPz = ubar->pz();
	    ubarPt = ubar->pt();
	    ubarP = ubar->p();
	    ubarEta = ubar->eta();
	    ubarPhi = ubar->phi();
	  }//end of if ubar
	}//end of loop over sparticle's daughters
      }//end of if gluino, stop - left and right handed, stau
    }//end of loop over daughters of stopped particle
  }//end of if matched
  
  else{
    std::cout<<"stopped particle id "<<events->begin()->stoppedParticleId()<<" is NOT MATCHED TO A GEN PARTICLE!!"<<std::endl;
    std::cout<<"mcparticles are: "<<endl;
    for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
      std::cout<<"  "<<itmcpart->pdgId()<<std::endl;
    }
  }//end of if not matched

  (*eventvariables)["neutralinoMass"] = neutralinoMass;
  (*eventvariables)["neutralinoPx"] = neutralinoPx;
  (*eventvariables)["neutralinoPy"] = neutralinoPy;
  (*eventvariables)["neutralinoPz"] = neutralinoPz;
  (*eventvariables)["neutralinoPt"] = neutralinoPt;
  (*eventvariables)["neutralinoP"] = neutralinoP;
  (*eventvariables)["neutralinoEta"] = neutralinoEta;
  (*eventvariables)["neutralinoPhi"] = neutralinoPhi;

  (*eventvariables)["gluonMass"] = gluonMass;
  (*eventvariables)["gluonPx"] = gluonPx;
  (*eventvariables)["gluonPy"] = gluonPy;
  (*eventvariables)["gluonPz"] = gluonPz;
  (*eventvariables)["gluonPt"] = gluonPt;
  (*eventvariables)["gluonP"] = gluonP;
  (*eventvariables)["gluonEta"] = gluonEta;
  (*eventvariables)["gluonPhi"] = gluonPhi;

  (*eventvariables)["uMass"] = uMass;
  (*eventvariables)["uPx"] = uPx;
  (*eventvariables)["uPy"] = uPy;
  (*eventvariables)["uPz"] = uPz;
  (*eventvariables)["uPt"] = uPt;
  (*eventvariables)["uP"] = uP;
  (*eventvariables)["uEta"] = uEta;
  (*eventvariables)["uPhi"] = uPhi;

  (*eventvariables)["ubarMass"] = ubarMass;
  (*eventvariables)["ubarPx"] = ubarPx;
  (*eventvariables)["ubarPy"] = ubarPy;
  (*eventvariables)["ubarPz"] = ubarPz;
  (*eventvariables)["ubarPt"] = ubarPt;
  (*eventvariables)["ubarP"] = ubarP;
  (*eventvariables)["ubarEta"] = ubarEta;
  (*eventvariables)["ubarPhi"] = ubarPhi;
  */  
}//end of AddVariables()
  
  // Shamelessly stolen from DataFormats/MuonDetId/src/CSCDetId.cc#100
int StoppPtlsEventVariableProducer::chamberType(int iStation, int iRing) {
  int i = 2*iStation + iRing;
  if (iStation == 1) {
    i = i - 1;
    if (i>4) i = 1;
  }
  return i;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsEventVariableProducer);

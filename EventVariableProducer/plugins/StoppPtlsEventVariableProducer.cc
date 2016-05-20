#include <iostream>
#include <fstream>
#include <TVector3.h>
#include "TFile.h"
#include "TH1.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/StoppPtlsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

StoppPtlsEventVariableProducer::StoppPtlsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  livetimeRootFile_(cfg.getParameter<string>("livetimeRootFile")),
  stoppedParticlesNameTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesName")),
  stoppedParticlesNameToken_    (consumes<std::vector<std::string> >(stoppedParticlesNameTag_)),
  stoppedParticlesXTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesX")),
  stoppedParticlesXToken_    (consumes<std::vector<float> >(stoppedParticlesXTag_)),
  stoppedParticlesYTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesY")),
  stoppedParticlesYToken_    (consumes<std::vector<float> >(stoppedParticlesYTag_)),
  stoppedParticlesZTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesZ")),
  stoppedParticlesZToken_    (consumes<std::vector<float> >(stoppedParticlesZTag_)),
  stoppedParticlesTimeTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesTime")),
  stoppedParticlesTimeToken_    (consumes<std::vector<float> >(stoppedParticlesTimeTag_)),
  stoppedParticlesPdgIdTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesPdgId")),
  stoppedParticlesPdgIdToken_    (consumes<std::vector<int> >(stoppedParticlesPdgIdTag_)),
  stoppedParticlesMassTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesMass")),
  stoppedParticlesMassToken_    (consumes<std::vector<float> >(stoppedParticlesMassTag_)),
  stoppedParticlesChargeTag_ (cfg.getParameter<edm::InputTag>("stoppedParticlesCharge")),
  stoppedParticlesChargeToken_    (consumes<std::vector<float> >(stoppedParticlesChargeTag_))
{
  file = TFile::Open(livetimeRootFile_.c_str());
  file->cd("TriggerResults");
  run_livetime_hist = (TH1D*)gDirectory->Get("run_livetime_hist");
  fill_livetime_hist = (TH1D*)gDirectory->Get("fill_livetime_hist");

  clog<<"Total livetime is: "<<run_livetime_hist->GetSumOfWeights()<<" seconds"<<endl;

  eventsToken_ = consumes<vector<TYPE(events)> >(collections_.getParameter<edm::InputTag>("events"));
  mcparticlesToken_ = consumes<vector<TYPE(mcparticles)> >(collections_.getParameter<edm::InputTag>("mcparticles"));
}

StoppPtlsEventVariableProducer::~StoppPtlsEventVariableProducer()
{
}

void StoppPtlsEventVariableProducer::AddVariables(const edm::Event & event) {
     
  edm::Handle<std::vector<CandidateEvent> > events;
  edm::Handle<std::vector<reco::GenParticle> > mcparticles;
  
  event.getByToken (eventsToken_, events);
  event.getByToken (mcparticlesToken_, mcparticles);
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
  */
  bool matched = false;
  auto stopped_genParticle = mcparticles->begin();

  // Fill variables based on the StoppedParticles vectors made by RHStopTracer module                                                                              
  edm::Handle<std::vector<std::string> > names;
  event.getByToken(stoppedParticlesNameToken_,names);
  edm::Handle<std::vector<float> > xs;
  event.getByToken(stoppedParticlesXToken_, xs);
  edm::Handle<std::vector<float> > ys;
  event.getByToken(stoppedParticlesYToken_, ys);
  edm::Handle<std::vector<float> > zs;
  event.getByToken(stoppedParticlesZToken_, zs);
  edm::Handle<std::vector<float> > times;
  event.getByToken(stoppedParticlesTimeToken_, times);
  edm::Handle<std::vector<int> > ids;
  event.getByToken(stoppedParticlesPdgIdToken_, ids);
  edm::Handle<std::vector<float> > masses;
  event.getByToken(stoppedParticlesMassToken_, masses);
  edm::Handle<std::vector<float> > charges;
  event.getByToken(stoppedParticlesChargeToken_, charges);

  if (!names.isValid() || !xs.isValid() || !ys.isValid() || !zs.isValid() || !times.isValid()
      || !ids.isValid() || !masses.isValid() || !charges.isValid() ){
    edm::LogError ("MissingProduct") << "StoppedParticles* vectors not available. Branch "
                                     << "will not be filled." << std::endl;
  }
  else if (names->size() != xs->size() || xs->size() != ys->size() || ys->size() != zs->size() || ids->size()!= names->size()) {
    edm::LogError ("StoppPtsCandProducer") << "mismatch array sizes name/x/y/z:"
                                           << names->size() << '/' << xs->size() << '/'
                                           << ys->size() << '/' << zs->size() << '/' << ids->size() << std::endl;
  }
  else {
    for (size_t i = 0; i < names->size(); ++i) {
      //float phi = ((*ys)[i]==0 && (*xs)[i]==0) ? 0 : atan2((*ys)[i],(*xs)[i]);
      //float r = sqrt((*xs)[i]*(*xs)[i] + (*ys)[i]*(*ys)[i]);
      
      std::cout<<"stopped particles name is: "<<names->at(i)<<std::endl;
  
      for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
	//if mcparticle matched to correct stopped particle ID
	if(itmcpart->pdgId()==ids->at(i)){
	  matched = true;
	  stopped_genParticle = itmcpart;
	  std::clog<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
	  break;
	}
	//sometimes only another R-hadron, not the exact stopped particle r-hadron, is in the mcparticles list
	else if(fabs(itmcpart->pdgId())>1000900 && fabs(itmcpart->pdgId())<2000000){
	  matched = true;
	  stopped_genParticle = itmcpart;
	  std::clog<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
	  break;
	}
      }//end of loop over mcparticles
    }//end of loop over stopped particles
  }//end of if stopped particles is valid

  if(matched){
    std::cout<<"matched!"<<std::endl;
  /*
    //loop over rhadron daughters
    for(size_t j=0; j<stopped_genParticle->numberOfDaughters(); j++){
      const reco::Candidate* daughter = stopped_genParticle->daughter(j);
      int partId = daughter->pdgId();
      //std::clog<<"  daughter pdgid is: "<<partId<<std::endl;
      
      //look for sparticle (gluino, stop - left and right handed, stau) 
      if (fabs(partId) == 1000021 || fabs(partId) == 1000006 || fabs(partId) == 2000006 || fabs(partId) == 1000015 || fabs(partId) == 2000015){
	const reco::Candidate* sparticle = daughter;
	
	//loop over sparticle's daughters
	for(size_t k=0; k<sparticle->numberOfDaughters(); k++){	    
	  const reco::Candidate* daughter2 = sparticle->daughter(k);
	  //std::clog<<"  daughter2 pdgid is: "<<daughter2->pdgId()<<", mass is: "<<daughter2->mass()<<", px is: "<<daughter2->px()<<", py: "<<daughter2->py()<<", pz: "<<daughter2->pz()<<std::endl;  
	  
	  //look for neutralino
	  if(fabs(daughter2->pdgId())==1000022){
	    const reco::Candidate* neutralino = daughter2;
	    //std::clog<<"  neutralino mass is: "<<neutralino->mass()<<", px is: "<<neutralino->px()<<", py: "<<neutralino->py()<<", pz: "<<neutralino->pz()<<std::endl;
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
	    //std::clog<<"  gluon mass is: "<<gluon->mass()<<", px is: "<<gluon->px()<<", py: "<<gluon->py()<<", pz: "<<gluon->pz()<<std::endl;
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
	    //std::clog<<"  u mass is: "<<u->mass()<<", px is: "<<u->px()<<", py: "<<u->py()<<", pz: "<<u->pz()<<std::endl;
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
	    //std::clog<<"  ubar mass is: "<<ubar->mass()<<", px is: "<<ubar->px()<<", py: "<<ubar->py()<<", pz: "<<ubar->pz()<<std::endl;
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
  */
  }//end of if matched
  
  else{
    std::clog<<"stopped particle id "<<events->begin()->stoppedParticleId()<<" is NOT MATCHED TO A GEN PARTICLE!!"<<std::endl;
    std::clog<<"mcparticles are: "<<endl;
    for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
      std::clog<<"  "<<itmcpart->pdgId()<<std::endl;
    }
  }//end of if not matched
  /*
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


  int nRuns = run_livetime_hist->GetNbinsX();
  double livetimeByRun = 9999; //default value should be large so if something is wrong, the event contributes very little to the 1/livetime weighted distribution
  for(int i=1; i<=nRuns; i++){
    if(events->begin()->run()==(unsigned int)run_livetime_hist->GetBinLowEdge(i)){
      if(run_livetime_hist->GetBinContent(i)>0.){ //if livetime is 0, the livetime should be the default 9999
	livetimeByRun = run_livetime_hist->GetBinContent(i);
      }
    }
  }
  clog<<"livetimeByRun is: "<<livetimeByRun<<endl;
  (*eventvariables)["livetimeByRun"] = livetimeByRun;

  int nFills = fill_livetime_hist->GetNbinsX();
  double livetimeByFill = 9999;
  for(int i=1; i<=nFills; i++){
    if(events->begin()->fill()==(unsigned int)fill_livetime_hist->GetBinLowEdge(i)){
      if(fill_livetime_hist->GetBinContent(i)>0.){
	livetimeByFill = fill_livetime_hist->GetBinContent(i);
      }
    }
  }
  clog<<"livetimeByFill is: "<<livetimeByFill<<endl;
  (*eventvariables)["livetimeByFill"] = livetimeByFill;

}//end of AddVariables()
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsEventVariableProducer);

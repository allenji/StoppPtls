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
  //livetimeRootFile_(cfg.getParameter<string>("livetimeRootFile")),
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
  /*
  file = TFile::Open(livetimeRootFile_.c_str());
  file->cd("TriggerResults");
  run_livetime_hist = (TH1D*)gDirectory->Get("run_livetime_hist");
  fill_livetime_hist = (TH1D*)gDirectory->Get("fill_livetime_hist");
  instLumi_livetime_hist = (TH1D*)gDirectory->Get("instLumi_livetime_hist");

  clog<<"Total livetime is: "<<run_livetime_hist->GetSumOfWeights()<<" seconds"<<endl;
  */
  eventsToken_ = consumes<vector<TYPE(events)> >(collections_.getParameter<edm::InputTag>("events"));
  mcparticlesToken_ = consumes<vector<TYPE(mcparticles)> >(collections_.getParameter<edm::InputTag>("mcparticles"));
}

StoppPtlsEventVariableProducer::~StoppPtlsEventVariableProducer()
{
}

void StoppPtlsEventVariableProducer::AddVariables(const edm::Event & event) {

  //stopped particles and gen particles
  edm::Handle<std::vector<CandidateEvent> > events;
  edm::Handle<std::vector<reco::GenParticle> > mcparticles;
  
  event.getByToken (eventsToken_, events);
  event.getByToken (mcparticlesToken_, mcparticles);
  //
  std::vector<std::vector<double> > caloTowerHadEtLargestRbx = (events->at(0)).caloTowerHadEtLargestRbx();
  for (int i = 0; i < 4; i++) {
    std::cout << "ieta" << i << std::endl;
    for (int j = 0; j < 16; j++) {
      std::cout << caloTowerHadEtLargestRbx[i][j] << ", " << std::endl;
    }
  }

  //////////////////////////////stage2////////////////////////////////////////
  ////////////////////////////////////////////////////////////////////////////

  int nStoppedParticles = -1;
  int stoppedParticle_index = -999;
  //string stoppedParticleName  = "";
  int stoppedParticleId       = -999;
  float stoppedParticleMass   = -999;
  float stoppedParticleCharge = -999;
  float stoppedParticleX      = -999;
  float stoppedParticleY      = -999;
  float stoppedParticleZ      = -999;
  float stoppedParticleR      = -999;
  float stoppedParticleEta    = -999;
  float stoppedParticlePhi    = -999;
  float stoppedParticleTime   = -999;
  int stoppedParticleRegion = -1;
  bool stoppedInCavern = true;

  //gen particles
  double neutralinoNLSPMass = -999;
  double neutralinoNLSPPx = -999;
  double neutralinoNLSPPy = -999;
  double neutralinoNLSPPz = -999;
  double neutralinoNLSPPt = -999;
  double neutralinoNLSPP = -999;
  double neutralinoNLSPEta = -999;
  double neutralinoNLSPPhi = -999;

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

  double muon0Mass = -999;
  double muon0Charge = -999;
  double muon0Px = -999;
  double muon0Py = -999;
  double muon0Pz = -999;
  double muon0Pt = -999;
  double muon0P = -999;
  double muon0Eta = -999;
  double muon0Phi = -999;

  double muon1Mass = -999;
  double muon1Charge = -999;
  double muon1Px = -999;
  double muon1Py = -999;
  double muon1Pz = -999;
  double muon1Pt = -999;
  double muon1P = -999;
  double muon1Eta = -999;
  double muon1Phi = -999;

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
    nStoppedParticles = names->size();
    for (int i = 0; i < nStoppedParticles; ++i) {
      std::cout<<"stopped particles name is: "<<names->at(i)<<std::endl;
      
      for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
	//if mcparticle matched to correct stopped particle ID
	if(itmcpart->pdgId()==ids->at(i)){
	  matched = true;
	  stopped_genParticle = itmcpart;
	  stoppedParticle_index = i;
	  std::clog<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
	  break;
	}
	//sometimes only another R-hadron, not the exact stopped particle r-hadron, is in the mcparticles list
	else if(fabs(itmcpart->pdgId())>1000000 && fabs(itmcpart->pdgId())<2000000){
	  matched = true;
	  stopped_genParticle = itmcpart;
	  stoppedParticle_index = i;
	  std::clog<<"stopped particle id (Rhadron) is: "<<itmcpart->pdgId()<<std::endl;
	  break;
	}
      }//end of loop over mcparticles
    }//end of loop over stopped particles
  }//end of if stopped particles is valid

  if(matched){
    //std::cout<<"matched!"<<std::endl;
    float r = sqrt(xs->at(stoppedParticle_index)*xs->at(stoppedParticle_index) + ys->at(stoppedParticle_index)*ys->at(stoppedParticle_index));
    float eta = Eta(xs->at(stoppedParticle_index),ys->at(stoppedParticle_index),
		    zs->at(stoppedParticle_index),times->at(stoppedParticle_index));
    float phi = ((*ys)[stoppedParticle_index]==0 && (*xs)[stoppedParticle_index]==0) ? 0 : atan2((*ys)[stoppedParticle_index],(*xs)[stoppedParticle_index]);
    
    //stoppedParticleName = names->at(stoppedParticle_index);
    stoppedParticleId = ids->at(stoppedParticle_index);	   
    stoppedParticleMass = masses->at(stoppedParticle_index);
    stoppedParticleCharge = charges->at(stoppedParticle_index);
    stoppedParticleX = 1.0*xs->at(stoppedParticle_index)/10; //divide by 10 to convert to cm
    stoppedParticleY = 1.0*ys->at(stoppedParticle_index)/10;   
    stoppedParticleZ = 1.0*zs->at(stoppedParticle_index)/10;
    stoppedParticleR = 1.0*r/10;
    stoppedParticleEta = eta;				   
    stoppedParticlePhi = phi;
    stoppedParticleTime = times->at(stoppedParticle_index);

    if (stoppedParticleR < 131.0 && fabs(stoppedParticleEta) <= 2.5 && fabs(stoppedParticleZ) < 300.0) stoppedParticleRegion = 0; //tracker
    else if (stoppedParticleR>=131.0 && stoppedParticleR<184.0 && fabs(stoppedParticleZ)<376.0 && fabs(stoppedParticleEta)<1.479) stoppedParticleRegion = 1; //EB
    else if (fabs(stoppedParticleZ)<376.0 && fabs(stoppedParticleZ) >= 300.0 && fabs(stoppedParticleEta)>=1.479 && fabs(stoppedParticleEta)<3.0) stoppedParticleRegion = 2; //EE
    else if (stoppedParticleR>=184.0 && stoppedParticleR<295.0 && fabs(stoppedParticleEta)<1.3 && fabs(stoppedParticleZ)<500.0) stoppedParticleRegion = 3; //HB
    else if (fabs(stoppedParticleZ)<560.0 && fabs(stoppedParticleZ)>=376.0 && fabs(stoppedParticleEta)>=1.3 && fabs(stoppedParticleEta)<3.0) stoppedParticleRegion = 4; //HE
    else if (stoppedParticleR>=295.0 && stoppedParticleR<728.5 && fabs(stoppedParticleZ)<675.0) stoppedParticleRegion = 5; //MB
    else if (stoppedParticleR>=517.3 && stoppedParticleR<728.5 && fabs(stoppedParticleZ)>=675.0 && fabs(stoppedParticleZ)<1080.0) stoppedParticleRegion = 6; // ME-top
    else if (stoppedParticleR<517.3 && fabs(stoppedParticleEta)<3.0 && fabs(stoppedParticleZ)>=560.0 && fabs(stoppedParticleZ)<1080.0) stoppedParticleRegion = 6; // ME-bottom
    else if (stoppedParticleR<728.5 && fabs(stoppedParticleZ)<1080.0) stoppedParticleRegion = 7; // other regions? 
    
    if (stoppedParticleR >= 728.5 || fabs(stoppedParticleZ) > 1080) stoppedInCavern = true;
    else stoppedInCavern = false;


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
	  
	  //look for NLSP neutralino
	  if(fabs(daughter2->pdgId())==1000023){
	    const reco::Candidate* neutralinoNLSP = daughter2;
	    //std::clog<<"  neutralinoNLSP mass is: "<<neutralinoNLSP->mass()<<", px is: "<<neutralinoNLSP->px()<<", py: "<<neutralinoNLSP->py()<<", pz: "<<neutralinoNLSP->pz()<<std::endl;
	    neutralinoNLSPMass = neutralinoNLSP->mass();
	    neutralinoNLSPPx = neutralinoNLSP->px();
	    neutralinoNLSPPy = neutralinoNLSP->py();
	    neutralinoNLSPPz = neutralinoNLSP->pz();
	    neutralinoNLSPPt = neutralinoNLSP->pt();
	    neutralinoNLSPP = neutralinoNLSP->p();
	    neutralinoNLSPEta = neutralinoNLSP->eta();
	    neutralinoNLSPPhi = neutralinoNLSP->phi();

	    //loop over NLSP neutralino's daughters
	    for(size_t l=0; l<neutralinoNLSP->numberOfDaughters(); l++){	    
	      const reco::Candidate* daughter3 = neutralinoNLSP->daughter(l);
	      //std::clog<<"     daughter3 pdgid is: "<<daughter3->pdgId()<<", mass is: "<<daughter3->mass()<<", px is: "<<daughter3->px()<<", py: "<<daughter3->py()<<", pz: "<<daughter3->pz()<<std::endl;  
	      
	      //loop over CM shower's daughters
	      for(size_t m=0; m<daughter3->numberOfDaughters(); m++){	    
		const reco::Candidate* daughter4 = daughter3->daughter(m);
		//std::clog<<"     daughter4 pdgid is: "<<daughter4->pdgId()<<", mass is: "<<daughter4->mass()<<", px is: "<<daughter4->px()<<", py: "<<daughter4->py()<<", pz: "<<daughter4->pz()<<std::endl;

		if(fabs(daughter4->pdgId())==1000023){
		  const reco::Candidate* neutralinoNLSP_take2 = daughter4;

		  int numberOfMuons = 0;
		  for(size_t n=0; n<neutralinoNLSP_take2->numberOfDaughters(); n++){
		    const reco::Candidate* daughter5 = neutralinoNLSP_take2->daughter(n);
		    //std::clog<<"     daughter5 pdgid is: "<<daughter5->pdgId()<<", mass is: "<<daughter5->mass()<<", px is: "<<daughter5->px()<<", py: "<<daughter5->py()<<", pz: "<<daughter5->pz()<<std::endl;

		    //look for LSP neutralino
		    if(fabs(daughter5->pdgId())==1000022){
		      const reco::Candidate* neutralino = daughter5;
		      //std::clog<<"  neutralino mass is: "<<neutralino->mass()<<", px is: "<<neutralino->px()<<", py: "<<neutralino->py()<<", pz: "<<neutralino->pz()<<std::endl;
		      neutralinoMass = neutralino->mass();
		      neutralinoPx = neutralino->px();
		      neutralinoPy = neutralino->py();
		      neutralinoPz = neutralino->pz();
		      neutralinoPt = neutralino->pt();
		      neutralinoP = neutralino->p();
		      neutralinoEta = neutralino->eta();
		      neutralinoPhi = neutralino->phi();
		    }//end of if LSP neutralino

		    if (fabs(daughter5->pdgId()) == 13) {
		      const reco::Candidate* muon = daughter5;
		      numberOfMuons++;
		      if(numberOfMuons==1){
			muon0Mass = muon->mass();
			muon0Charge = muon->charge();
			muon0Px = muon->px();
			muon0Py = muon->py();
			muon0Pz = muon->pz();
			muon0Pt = muon->pt();
			muon0P = muon->p();
			muon0Eta = muon->eta();
			muon0Phi = muon->phi();
		      }
		      else if(numberOfMuons==2){
			muon1Mass = muon->mass();
			muon1Charge = muon->charge();
			muon1Px = muon->px();
			muon1Py = muon->py();
			muon1Pz = muon->pz();
			muon1Pt = muon->pt();
			muon1P = muon->p();
			muon1Eta = muon->eta();
			muon1Phi = muon->phi();
		      }
		      else std::cout<<"daughter number "<<n<<" !!!!!!"<<std::endl;
		    }//end of if daughter is muon

		  }
		}
	      }// end of loop over CM shower's daughters
	      
	    }//end of loop over NLSP neutralino's daughters

	  }//end of if NLSP neutralino

	  //look for LSP neutralino
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
	  }//end of if LSP neutralino
	  
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

      //look for sparticle (gluino, stop - left and right handed, stau) 
      if (fabs(stopped_genParticle->pdgId()) == 17 && fabs(partId) == 13) {
	const reco::Candidate* muon = daughter;

	if(j==0){
	  muon0Mass = muon->mass();
	  muon0Charge = muon->charge();
	  muon0Px = muon->px();
	  muon0Py = muon->py();
	  muon0Pz = muon->pz();
	  muon0Pt = muon->pt();
	  muon0P = muon->p();
	  muon0Eta = muon->eta();
	  muon0Phi = muon->phi();
	}
	else if(j==1){
	  muon1Mass = muon->mass();
	  muon1Charge = muon->charge();
	  muon1Px = muon->px();
	  muon1Py = muon->py();
	  muon1Pz = muon->pz();
	  muon1Pt = muon->pt();
	  muon1P = muon->p();
	  muon1Eta = muon->eta();
	  muon1Phi = muon->phi();
	}
	else std::cout<<"daughter number "<<j<<" !!!!!!"<<std::endl;
      }//end of if daughter is muon
    }//end of loop over daughters of stopped particle
  }//end of if matched
  
  else{
    if(ids->size()>0){
      std::clog<<"stopped particle id "<<ids->at(0)<<" is NOT MATCHED TO A GEN PARTICLE!!"<<std::endl;
      std::clog<<"mcparticles are: "<<endl;
      for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
	std::clog<<"  "<<itmcpart->pdgId()<<std::endl;
      }
    }
  }//end of if not matched

  (*eventvariables)["nStoppedParticles"] = nStoppedParticles;
  //(*eventvariables)["stoppedParticleName"]   = stoppedParticleName;
  (*eventvariables)["stoppedParticleId"]     = stoppedParticleId;
  (*eventvariables)["stoppedParticleMass"]   = stoppedParticleMass;
  (*eventvariables)["stoppedParticleCharge"] = stoppedParticleCharge;
  (*eventvariables)["stoppedParticleX"]      = stoppedParticleX;
  (*eventvariables)["stoppedParticleY"]      = stoppedParticleY;
  (*eventvariables)["stoppedParticleZ"]      = stoppedParticleZ;
  (*eventvariables)["stoppedParticleR"]      = stoppedParticleR;
  (*eventvariables)["stoppedParticleEta"]    = stoppedParticleEta;
  (*eventvariables)["stoppedParticlePhi"]    = stoppedParticlePhi;
  (*eventvariables)["stoppedParticleTime"]   = stoppedParticleTime;
  (*eventvariables)["stoppedParticleRegion"]   = stoppedParticleRegion;
  (*eventvariables)["stoppedInCavern"]   = stoppedInCavern;

  (*eventvariables)["neutralinoNLSPMass"] = neutralinoNLSPMass;
  (*eventvariables)["neutralinoNLSPPx"] = neutralinoNLSPPx;
  (*eventvariables)["neutralinoNLSPPy"] = neutralinoNLSPPy;
  (*eventvariables)["neutralinoNLSPPz"] = neutralinoNLSPPz;
  (*eventvariables)["neutralinoNLSPPt"] = neutralinoNLSPPt;
  (*eventvariables)["neutralinoNLSPP"] = neutralinoNLSPP;
  (*eventvariables)["neutralinoNLSPEta"] = neutralinoNLSPEta;
  (*eventvariables)["neutralinoNLSPPhi"] = neutralinoNLSPPhi;

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

  (*eventvariables)["muon0Mass"] = muon0Mass;
  (*eventvariables)["muon0Charge"] = muon0Charge;
  (*eventvariables)["muon0Px"] = muon0Px;
  (*eventvariables)["muon0Py"] = muon0Py;
  (*eventvariables)["muon0Pz"] = muon0Pz;
  (*eventvariables)["muon0Pt"] = muon0Pt;
  (*eventvariables)["muon0P"] = muon0P;
  (*eventvariables)["muon0Eta"] = muon0Eta;
  (*eventvariables)["muon0Phi"] = muon0Phi;

  (*eventvariables)["muon1Mass"] = muon1Mass;
  (*eventvariables)["muon1Charge"] = muon1Charge;
  (*eventvariables)["muon1Px"] = muon1Px;
  (*eventvariables)["muon1Py"] = muon1Py;
  (*eventvariables)["muon1Pz"] = muon1Pz;
  (*eventvariables)["muon1Pt"] = muon1Pt;
  (*eventvariables)["muon1P"] = muon1P;
  (*eventvariables)["muon1Eta"] = muon1Eta;
  (*eventvariables)["muon1Phi"] = muon1Phi;


  //////////////////////////////stage1////////////////////////////////////////
  ////////////////////////////////////////////////////////////////////////////
  int gluinoIndex=0;

  double gluino0Mass = -999;
  double gluino0Charge = -999;
  double gluino0Px = -999;
  double gluino0Py = -999;
  double gluino0Pz = -999;
  double gluino0Pt = -999;
  double gluino0P = -999;
  double gluino0Eta = -999;
  double gluino0Phi = -999;
  double gluino0Beta = -999;

  double gluino1Mass = -999;
  double gluino1Charge = -999;
  double gluino1Px = -999;
  double gluino1Py = -999;
  double gluino1Pz = -999;
  double gluino1Pt = -999;
  double gluino1P = -999;
  double gluino1Eta = -999;
  double gluino1Phi = -999;
  double gluino1Beta = -999;

  double stoppedGluino0Mass = -999;
  double stoppedGluino0Charge = -999;
  double stoppedGluino0Px = -999;
  double stoppedGluino0Py = -999;
  double stoppedGluino0Pz = -999;
  double stoppedGluino0Pt = -999;
  double stoppedGluino0P = -999;
  double stoppedGluino0Eta = -999;
  double stoppedGluino0Phi = -999;
  double stoppedGluino0Beta = -999;

  double stoppedGluino1Mass = -999;
  double stoppedGluino1Charge = -999;
  double stoppedGluino1Px = -999;
  double stoppedGluino1Py = -999;
  double stoppedGluino1Pz = -999;
  double stoppedGluino1Pt = -999;
  double stoppedGluino1P = -999;
  double stoppedGluino1Eta = -999;
  double stoppedGluino1Phi = -999;
  double stoppedGluino1Beta = -999;

  int stopIndex=0;

  double stop0Mass = -999;
  double stop0Charge = -999;
  double stop0Px = -999;
  double stop0Py = -999;
  double stop0Pz = -999;
  double stop0Pt = -999;
  double stop0P = -999;
  double stop0Eta = -999;
  double stop0Phi = -999;
  double stop0Beta = -999;

  double stop1Mass = -999;
  double stop1Charge = -999;
  double stop1Px = -999;
  double stop1Py = -999;
  double stop1Pz = -999;
  double stop1Pt = -999;
  double stop1P = -999;
  double stop1Eta = -999;
  double stop1Phi = -999;
  double stop1Beta = -999;

  double stoppedStop0Mass = -999;
  double stoppedStop0Charge = -999;
  double stoppedStop0Px = -999;
  double stoppedStop0Py = -999;
  double stoppedStop0Pz = -999;
  double stoppedStop0Pt = -999;
  double stoppedStop0P = -999;
  double stoppedStop0Eta = -999;
  double stoppedStop0Phi = -999;
  double stoppedStop0Beta = -999;

  double stoppedStop1Mass = -999;
  double stoppedStop1Charge = -999;
  double stoppedStop1Px = -999;
  double stoppedStop1Py = -999;
  double stoppedStop1Pz = -999;
  double stoppedStop1Pt = -999;
  double stoppedStop1P = -999;
  double stoppedStop1Eta = -999;
  double stoppedStop1Phi = -999;
  double stoppedStop1Beta = -999;

  int mchampIndex=0;

  double mchamp0Mass = -999;
  double mchamp0Charge = -999;
  double mchamp0Px = -999;
  double mchamp0Py = -999;
  double mchamp0Pz = -999;
  double mchamp0Pt = -999;
  double mchamp0P = -999;
  double mchamp0Eta = -999;
  double mchamp0Phi = -999;
  double mchamp0Beta = -999;

  double mchamp1Mass = -999;
  double mchamp1Charge = -999;
  double mchamp1Px = -999;
  double mchamp1Py = -999;
  double mchamp1Pz = -999;
  double mchamp1Pt = -999;
  double mchamp1P = -999;
  double mchamp1Eta = -999;
  double mchamp1Phi = -999;
  double mchamp1Beta = -999;

  double stoppedMchamp0Mass = -999;
  double stoppedMchamp0Charge = -999;
  double stoppedMchamp0Px = -999;
  double stoppedMchamp0Py = -999;
  double stoppedMchamp0Pz = -999;
  double stoppedMchamp0Pt = -999;
  double stoppedMchamp0P = -999;
  double stoppedMchamp0Eta = -999;
  double stoppedMchamp0Phi = -999;
  double stoppedMchamp0Beta = -999;

  double stoppedMchamp1Mass = -999;
  double stoppedMchamp1Charge = -999;
  double stoppedMchamp1Px = -999;
  double stoppedMchamp1Py = -999;
  double stoppedMchamp1Pz = -999;
  double stoppedMchamp1Pt = -999;
  double stoppedMchamp1P = -999;
  double stoppedMchamp1Eta = -999;
  double stoppedMchamp1Phi = -999;
  double stoppedMchamp1Beta = -999;

  double minDeltaR0 = 999;
  double minDeltaR1 = 999;
  auto gluino0MatchedToStoppedParticle = mcparticles->begin();
  auto gluino1MatchedToStoppedParticle = mcparticles->begin();
  auto stop0MatchedToStoppedParticle = mcparticles->begin();
  auto stop1MatchedToStoppedParticle = mcparticles->begin();
  auto mchamp0MatchedToStoppedParticle = mcparticles->begin();
  auto mchamp1MatchedToStoppedParticle = mcparticles->begin();

  for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
    //gluinos before hadronization
    if(fabs(itmcpart->pdgId())==1000021 && itmcpart->status()==23){
      auto gluino = itmcpart;

      if(gluinoIndex==0){
	gluino0Mass = gluino->mass();
	gluino0Charge = gluino->charge();
	gluino0Px = gluino->px();
	gluino0Py = gluino->py();
	gluino0Pz = gluino->pz();
	gluino0Pt = gluino->pt();
	gluino0P = gluino->p();
	gluino0Eta = gluino->eta();
	gluino0Phi = gluino->phi();
	gluino0Beta = Beta(*gluino);
	if(dRmatchedToStoppedParticle(*gluino,nStoppedParticles,xs,ys,zs,times)<minDeltaR0){
	  minDeltaR0 = dRmatchedToStoppedParticle(*gluino,nStoppedParticles,xs,ys,zs,times);
	  gluino0MatchedToStoppedParticle = gluino;
	}
      }
      else if(gluinoIndex==1){
	gluino1Mass = gluino->mass();
	gluino1Charge = gluino->charge();
	gluino1Px = gluino->px();
	gluino1Py = gluino->py();
	gluino1Pz = gluino->pz();
	gluino1Pt = gluino->pt();
	gluino1P = gluino->p();
	gluino1Eta = gluino->eta();
	gluino1Phi = gluino->phi();
	gluino1Beta = Beta(*gluino);
	if(dRmatchedToStoppedParticle(*gluino,nStoppedParticles,xs,ys,zs,times)<minDeltaR1){
	  minDeltaR1 = dRmatchedToStoppedParticle(*gluino,nStoppedParticles,xs,ys,zs,times);
	  gluino1MatchedToStoppedParticle = gluino;
	}
      }
      else std::cout<<"gluino number "<<gluinoIndex<<" !!!!!!"<<std::endl;
      gluinoIndex++;
    }//end of if gluino with status 23

    //stops before hadronization
    if((fabs(itmcpart->pdgId())==1000006 || fabs(itmcpart->pdgId())==2000006) && itmcpart->status()==23){
      auto stop = itmcpart;

      if(stopIndex==0){
	stop0Mass = stop->mass();
	stop0Charge = stop->charge();
	stop0Px = stop->px();
	stop0Py = stop->py();
	stop0Pz = stop->pz();
	stop0Pt = stop->pt();
	stop0P = stop->p();
	stop0Eta = stop->eta();
	stop0Phi = stop->phi();
	stop0Beta = Beta(*stop);
	if(dRmatchedToStoppedParticle(*stop,nStoppedParticles,xs,ys,zs,times)<minDeltaR0){
	  minDeltaR0 = dRmatchedToStoppedParticle(*stop,nStoppedParticles,xs,ys,zs,times);
	  stop0MatchedToStoppedParticle = stop;
	}
      }
      else if(stopIndex==1){
	stop1Mass = stop->mass();
	stop1Charge = stop->charge();
	stop1Px = stop->px();
	stop1Py = stop->py();
	stop1Pz = stop->pz();
	stop1Pt = stop->pt();
	stop1P = stop->p();
	stop1Eta = stop->eta();
	stop1Phi = stop->phi();
	stop1Beta = Beta(*stop);
	if(dRmatchedToStoppedParticle(*stop,nStoppedParticles,xs,ys,zs,times)<minDeltaR1){
	  minDeltaR1 = dRmatchedToStoppedParticle(*stop,nStoppedParticles,xs,ys,zs,times);
	  stop1MatchedToStoppedParticle = stop;
	}
      }
      else std::cout<<"stop number "<<stopIndex<<" !!!!!!"<<std::endl;
      stopIndex++;
    }//end of if stop with status 23

    //mchamps
    if(fabs(itmcpart->pdgId())==17){
      auto mchamp = itmcpart;
      
      if(mchampIndex==0){
	mchamp0Mass = mchamp->mass();
	mchamp0Charge = mchamp->charge();
	mchamp0Px = mchamp->px();
	mchamp0Py = mchamp->py();
	mchamp0Pz = mchamp->pz();
	mchamp0Pt = mchamp->pt();
	mchamp0P = mchamp->p();
	mchamp0Eta = mchamp->eta();
	mchamp0Phi = mchamp->phi();
	mchamp0Beta = Beta(*mchamp);
	if(dRmatchedToStoppedParticle(*mchamp,nStoppedParticles,xs,ys,zs,times)<minDeltaR0){
	  minDeltaR0 = dRmatchedToStoppedParticle(*mchamp,nStoppedParticles,xs,ys,zs,times);
	  mchamp0MatchedToStoppedParticle = mchamp;
	}
      }
      else if(mchampIndex==1){
	mchamp1Mass = mchamp->mass();
	mchamp1Charge = mchamp->charge();
	mchamp1Px = mchamp->px();
	mchamp1Py = mchamp->py();
	mchamp1Pz = mchamp->pz();
	mchamp1Pt = mchamp->pt();
	mchamp1P = mchamp->p();
	mchamp1Eta = mchamp->eta();
	mchamp1Phi = mchamp->phi();
	mchamp1Beta = Beta(*mchamp);
	if(dRmatchedToStoppedParticle(*mchamp,nStoppedParticles,xs,ys,zs,times)<minDeltaR1){
	  minDeltaR1 = dRmatchedToStoppedParticle(*mchamp,nStoppedParticles,xs,ys,zs,times);
	  mchamp1MatchedToStoppedParticle = mchamp;
	}
      }
      else std::cout<<"mchamp number "<<mchampIndex<<" !!!!!!"<<std::endl;
      mchampIndex++;
    }//end of if mchamp
  }//end of loop over mcparticles

  (*eventvariables)["gluino0Mass"] = gluino0Mass;
  (*eventvariables)["gluino0Charge"] = gluino0Charge;
  (*eventvariables)["gluino0Px"] = gluino0Px;
  (*eventvariables)["gluino0Py"] = gluino0Py;
  (*eventvariables)["gluino0Pz"] = gluino0Pz;
  (*eventvariables)["gluino0Pt"] = gluino0Pt;
  (*eventvariables)["gluino0P"] = gluino0P;
  (*eventvariables)["gluino0Eta"] = gluino0Eta;
  (*eventvariables)["gluino0Phi"] = gluino0Phi;
  (*eventvariables)["gluino0Beta"] = gluino0Beta;

  (*eventvariables)["gluino1Mass"] = gluino1Mass;
  (*eventvariables)["gluino1Charge"] = gluino1Charge;
  (*eventvariables)["gluino1Px"] = gluino1Px;
  (*eventvariables)["gluino1Py"] = gluino1Py;
  (*eventvariables)["gluino1Pz"] = gluino1Pz;
  (*eventvariables)["gluino1Pt"] = gluino1Pt;
  (*eventvariables)["gluino1P"] = gluino1P;
  (*eventvariables)["gluino1Eta"] = gluino1Eta;
  (*eventvariables)["gluino1Phi"] = gluino1Phi;
  (*eventvariables)["gluino1Beta"] = gluino1Beta;

  (*eventvariables)["stop0Mass"] = stop0Mass;
  (*eventvariables)["stop0Charge"] = stop0Charge;
  (*eventvariables)["stop0Px"] = stop0Px;
  (*eventvariables)["stop0Py"] = stop0Py;
  (*eventvariables)["stop0Pz"] = stop0Pz;
  (*eventvariables)["stop0Pt"] = stop0Pt;
  (*eventvariables)["stop0P"] = stop0P;
  (*eventvariables)["stop0Eta"] = stop0Eta;
  (*eventvariables)["stop0Phi"] = stop0Phi;
  (*eventvariables)["stop0Beta"] = stop0Beta;

  (*eventvariables)["stop1Mass"] = stop1Mass;
  (*eventvariables)["stop1Charge"] = stop1Charge;
  (*eventvariables)["stop1Px"] = stop1Px;
  (*eventvariables)["stop1Py"] = stop1Py;
  (*eventvariables)["stop1Pz"] = stop1Pz;
  (*eventvariables)["stop1Pt"] = stop1Pt;
  (*eventvariables)["stop1P"] = stop1P;
  (*eventvariables)["stop1Eta"] = stop1Eta;
  (*eventvariables)["stop1Phi"] = stop1Phi;
  (*eventvariables)["stop1Beta"] = stop1Beta;

  (*eventvariables)["mchamp0Mass"] = mchamp0Mass;
  (*eventvariables)["mchamp0Charge"] = mchamp0Charge;
  (*eventvariables)["mchamp0Px"] = mchamp0Px;
  (*eventvariables)["mchamp0Py"] = mchamp0Py;
  (*eventvariables)["mchamp0Pz"] = mchamp0Pz;
  (*eventvariables)["mchamp0Pt"] = mchamp0Pt;
  (*eventvariables)["mchamp0P"] = mchamp0P;
  (*eventvariables)["mchamp0Eta"] = mchamp0Eta;
  (*eventvariables)["mchamp0Phi"] = mchamp0Phi;
  (*eventvariables)["mchamp0Beta"] = mchamp0Beta;

  (*eventvariables)["mchamp1Mass"] = mchamp1Mass;
  (*eventvariables)["mchamp1Charge"] = mchamp1Charge;
  (*eventvariables)["mchamp1Px"] = mchamp1Px;
  (*eventvariables)["mchamp1Py"] = mchamp1Py;
  (*eventvariables)["mchamp1Pz"] = mchamp1Pz;
  (*eventvariables)["mchamp1Pt"] = mchamp1Pt;
  (*eventvariables)["mchamp1P"] = mchamp1P;
  (*eventvariables)["mchamp1Eta"] = mchamp1Eta;
  (*eventvariables)["mchamp1Phi"] = mchamp1Phi;
  (*eventvariables)["mchamp1Beta"] = mchamp1Beta;

  
  if(nStoppedParticles==2 ||(nStoppedParticles==1 && minDeltaR0<minDeltaR1)){
    stoppedGluino0Mass = gluino0MatchedToStoppedParticle->mass();
    stoppedGluino0Charge = gluino0MatchedToStoppedParticle->charge();
    stoppedGluino0Px = gluino0MatchedToStoppedParticle->px();
    stoppedGluino0Py = gluino0MatchedToStoppedParticle->py();
    stoppedGluino0Pz = gluino0MatchedToStoppedParticle->pz();
    stoppedGluino0Pt = gluino0MatchedToStoppedParticle->pt();
    stoppedGluino0P = gluino0MatchedToStoppedParticle->p();
    stoppedGluino0Eta = gluino0MatchedToStoppedParticle->eta();
    stoppedGluino0Phi = gluino0MatchedToStoppedParticle->phi();
    stoppedGluino0Beta = Beta(*gluino0MatchedToStoppedParticle);

    stoppedStop0Mass = stop0MatchedToStoppedParticle->mass();
    stoppedStop0Charge = stop0MatchedToStoppedParticle->charge();
    stoppedStop0Px = stop0MatchedToStoppedParticle->px();
    stoppedStop0Py = stop0MatchedToStoppedParticle->py();
    stoppedStop0Pz = stop0MatchedToStoppedParticle->pz();
    stoppedStop0Pt = stop0MatchedToStoppedParticle->pt();
    stoppedStop0P = stop0MatchedToStoppedParticle->p();
    stoppedStop0Eta = stop0MatchedToStoppedParticle->eta();
    stoppedStop0Phi = stop0MatchedToStoppedParticle->phi();
    stoppedStop0Beta = Beta(*stop0MatchedToStoppedParticle);

    stoppedMchamp0Mass = mchamp0MatchedToStoppedParticle->mass();
    stoppedMchamp0Charge = mchamp0MatchedToStoppedParticle->charge();
    stoppedMchamp0Px = mchamp0MatchedToStoppedParticle->px();
    stoppedMchamp0Py = mchamp0MatchedToStoppedParticle->py();
    stoppedMchamp0Pz = mchamp0MatchedToStoppedParticle->pz();
    stoppedMchamp0Pt = mchamp0MatchedToStoppedParticle->pt();
    stoppedMchamp0P = mchamp0MatchedToStoppedParticle->p();
    stoppedMchamp0Eta = mchamp0MatchedToStoppedParticle->eta();
    stoppedMchamp0Phi = mchamp0MatchedToStoppedParticle->phi();
    stoppedMchamp0Beta = Beta(*mchamp0MatchedToStoppedParticle);
  }
  if(nStoppedParticles==2 ||(nStoppedParticles==1 && minDeltaR1<minDeltaR0)){
    stoppedGluino1Mass = gluino1MatchedToStoppedParticle->mass();
    stoppedGluino1Charge = gluino1MatchedToStoppedParticle->charge();
    stoppedGluino1Px = gluino1MatchedToStoppedParticle->px();
    stoppedGluino1Py = gluino1MatchedToStoppedParticle->py();
    stoppedGluino1Pz = gluino1MatchedToStoppedParticle->pz();
    stoppedGluino1Pt = gluino1MatchedToStoppedParticle->pt();
    stoppedGluino1P = gluino1MatchedToStoppedParticle->p();
    stoppedGluino1Eta = gluino1MatchedToStoppedParticle->eta();
    stoppedGluino1Phi = gluino1MatchedToStoppedParticle->phi();
    stoppedGluino1Beta = Beta(*gluino1MatchedToStoppedParticle);

    stoppedStop1Mass = stop1MatchedToStoppedParticle->mass();
    stoppedStop1Charge = stop1MatchedToStoppedParticle->charge();
    stoppedStop1Px = stop1MatchedToStoppedParticle->px();
    stoppedStop1Py = stop1MatchedToStoppedParticle->py();
    stoppedStop1Pz = stop1MatchedToStoppedParticle->pz();
    stoppedStop1Pt = stop1MatchedToStoppedParticle->pt();
    stoppedStop1P = stop1MatchedToStoppedParticle->p();
    stoppedStop1Eta = stop1MatchedToStoppedParticle->eta();
    stoppedStop1Phi = stop1MatchedToStoppedParticle->phi();
    stoppedStop1Beta = Beta(*stop1MatchedToStoppedParticle);

    stoppedMchamp1Mass = mchamp1MatchedToStoppedParticle->mass();
    stoppedMchamp1Charge = mchamp1MatchedToStoppedParticle->charge();
    stoppedMchamp1Px = mchamp1MatchedToStoppedParticle->px();
    stoppedMchamp1Py = mchamp1MatchedToStoppedParticle->py();
    stoppedMchamp1Pz = mchamp1MatchedToStoppedParticle->pz();
    stoppedMchamp1Pt = mchamp1MatchedToStoppedParticle->pt();
    stoppedMchamp1P = mchamp1MatchedToStoppedParticle->p();
    stoppedMchamp1Eta = mchamp1MatchedToStoppedParticle->eta();
    stoppedMchamp1Phi = mchamp1MatchedToStoppedParticle->phi();
    stoppedMchamp1Beta = Beta(*mchamp1MatchedToStoppedParticle);
  }

  std::cout<<"stop0Beta is: "<<stop0Beta<<std::endl;
  std::cout<<"stop1Beta is: "<<stop1Beta<<std::endl;
  std::cout<<"stoppedStop0Beta is: "<<stoppedStop0Beta<<std::endl;
  std::cout<<"stoppedStop1Beta is: "<<stoppedStop1Beta<<std::endl;

  (*eventvariables)["stoppedGluino0Mass"] = stoppedGluino0Mass;
  (*eventvariables)["stoppedGluino0Charge"] = stoppedGluino0Charge;
  (*eventvariables)["stoppedGluino0Px"] = stoppedGluino0Px;
  (*eventvariables)["stoppedGluino0Py"] = stoppedGluino0Py;
  (*eventvariables)["stoppedGluino0Pz"] = stoppedGluino0Pz;
  (*eventvariables)["stoppedGluino0Pt"] = stoppedGluino0Pt;
  (*eventvariables)["stoppedGluino0P"] = stoppedGluino0P;
  (*eventvariables)["stoppedGluino0Eta"] = stoppedGluino0Eta;
  (*eventvariables)["stoppedGluino0Phi"] = stoppedGluino0Phi;
  (*eventvariables)["stoppedGluino0Beta"] = stoppedGluino0Beta;

  (*eventvariables)["stoppedGluino1Mass"] = stoppedGluino1Mass;
  (*eventvariables)["stoppedGluino1Charge"] = stoppedGluino1Charge;
  (*eventvariables)["stoppedGluino1Px"] = stoppedGluino1Px;
  (*eventvariables)["stoppedGluino1Py"] = stoppedGluino1Py;
  (*eventvariables)["stoppedGluino1Pz"] = stoppedGluino1Pz;
  (*eventvariables)["stoppedGluino1Pt"] = stoppedGluino1Pt;
  (*eventvariables)["stoppedGluino1P"] = stoppedGluino1P;
  (*eventvariables)["stoppedGluino1Eta"] = stoppedGluino1Eta;
  (*eventvariables)["stoppedGluino1Phi"] = stoppedGluino1Phi;
  (*eventvariables)["stoppedGluino1Beta"] = stoppedGluino1Beta;

  (*eventvariables)["stoppedStop0Mass"] = stoppedStop0Mass;
  (*eventvariables)["stoppedStop0Charge"] = stoppedStop0Charge;
  (*eventvariables)["stoppedStop0Px"] = stoppedStop0Px;
  (*eventvariables)["stoppedStop0Py"] = stoppedStop0Py;
  (*eventvariables)["stoppedStop0Pz"] = stoppedStop0Pz;
  (*eventvariables)["stoppedStop0Pt"] = stoppedStop0Pt;
  (*eventvariables)["stoppedStop0P"] = stoppedStop0P;
  (*eventvariables)["stoppedStop0Eta"] = stoppedStop0Eta;
  (*eventvariables)["stoppedStop0Phi"] = stoppedStop0Phi;
  (*eventvariables)["stoppedStop0Beta"] = stoppedStop0Beta;

  (*eventvariables)["stoppedStop1Mass"] = stoppedStop1Mass;
  (*eventvariables)["stoppedStop1Charge"] = stoppedStop1Charge;
  (*eventvariables)["stoppedStop1Px"] = stoppedStop1Px;
  (*eventvariables)["stoppedStop1Py"] = stoppedStop1Py;
  (*eventvariables)["stoppedStop1Pz"] = stoppedStop1Pz;
  (*eventvariables)["stoppedStop1Pt"] = stoppedStop1Pt;
  (*eventvariables)["stoppedStop1P"] = stoppedStop1P;
  (*eventvariables)["stoppedStop1Eta"] = stoppedStop1Eta;
  (*eventvariables)["stoppedStop1Phi"] = stoppedStop1Phi;
  (*eventvariables)["stoppedStop1Beta"] = stoppedStop1Beta;

  (*eventvariables)["stoppedMchamp0Mass"] = stoppedMchamp0Mass;
  (*eventvariables)["stoppedMchamp0Charge"] = stoppedMchamp0Charge;
  (*eventvariables)["stoppedMchamp0Px"] = stoppedMchamp0Px;
  (*eventvariables)["stoppedMchamp0Py"] = stoppedMchamp0Py;
  (*eventvariables)["stoppedMchamp0Pz"] = stoppedMchamp0Pz;
  (*eventvariables)["stoppedMchamp0Pt"] = stoppedMchamp0Pt;
  (*eventvariables)["stoppedMchamp0P"] = stoppedMchamp0P;
  (*eventvariables)["stoppedMchamp0Eta"] = stoppedMchamp0Eta;
  (*eventvariables)["stoppedMchamp0Phi"] = stoppedMchamp0Phi;
  (*eventvariables)["stoppedMchamp0Beta"] = stoppedMchamp0Beta;

  (*eventvariables)["stoppedMchamp1Mass"] = stoppedMchamp1Mass;
  (*eventvariables)["stoppedMchamp1Charge"] = stoppedMchamp1Charge;
  (*eventvariables)["stoppedMchamp1Px"] = stoppedMchamp1Px;
  (*eventvariables)["stoppedMchamp1Py"] = stoppedMchamp1Py;
  (*eventvariables)["stoppedMchamp1Pz"] = stoppedMchamp1Pz;
  (*eventvariables)["stoppedMchamp1Pt"] = stoppedMchamp1Pt;
  (*eventvariables)["stoppedMchamp1P"] = stoppedMchamp1P;
  (*eventvariables)["stoppedMchamp1Eta"] = stoppedMchamp1Eta;
  (*eventvariables)["stoppedMchamp1Phi"] = stoppedMchamp1Phi;
  (*eventvariables)["stoppedMchamp1Beta"] = stoppedMchamp1Beta;


  //for stage1 (stopped and not stopped)
  int rhadronCharge = -999;
  for (auto itmcpart = mcparticles->begin(); itmcpart != mcparticles->end(); ++itmcpart){
    if(fabs(itmcpart->pdgId())>1000000 && fabs(itmcpart->pdgId())<2000000) rhadronCharge = itmcpart->charge();
  }
  (*eventvariables)["rhadronCharge"] = rhadronCharge;
  
  /*
  //////////////////////////////////livetime//////////////////////////////////
  ////////////////////////////////////////////////////////////////////////////
  int nRuns = run_livetime_hist->GetNbinsX();
  double livetimeByRun = 9999; //default value should be large so if something is wrong, the event contributes very little to the 1/livetime weighted distribution
  for(int i=1; i<=nRuns; i++){
    if(events->begin()->run()==(unsigned int)run_livetime_hist->GetBinLowEdge(i)){
      if(run_livetime_hist->GetBinContent(i)>0.){ //if livetime is 0, the livetime should be the default 9999
	livetimeByRun = run_livetime_hist->GetBinContent(i);
      }
    }
  }
  //clog<<"livetimeByRun is: "<<livetimeByRun<<endl;
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
  //clog<<"livetimeByFill is: "<<livetimeByFill<<endl;
  (*eventvariables)["livetimeByFill"] = livetimeByFill;

  int nInstLumis = instLumi_livetime_hist->GetNbinsX();
  double livetimeByInstLumi = 9999;
  for(int i=1; i<=nInstLumis; i++){
    if((unsigned int)events->begin()->instLumi()==(unsigned int)instLumi_livetime_hist->GetBinLowEdge(i)){
      if(instLumi_livetime_hist->GetBinContent(i)>0.){
	livetimeByInstLumi = instLumi_livetime_hist->GetBinContent(i);
      }
    }
  }
  clog<<"livetimeByInstLumi is: "<<livetimeByInstLumi<<endl;
  (*eventvariables)["livetimeByInstLumi"] = livetimeByInstLumi;
  */
}//end of AddVariables()

double StoppPtlsEventVariableProducer::Eta(double x, double y, double z, double time) {
  TLorentzVector v = TLorentzVector(x, y, z, time);
  return v.PseudoRapidity();
}

double StoppPtlsEventVariableProducer::Beta(const reco::GenParticle& mcpart){
  double beta = -999;
  if(mcpart.p()!=0.) beta = 1.0/(TMath::Sqrt((mcpart.mass()/mcpart.p())*(mcpart.mass()/mcpart.p())+1));
  return beta;
}

double StoppPtlsEventVariableProducer::dRmatchedToStoppedParticle(const reco::GenParticle& mcpart, int nStoppedParticles,edm::Handle< std::vector<float> > xs, edm::Handle< std::vector<float> > ys, edm::Handle< std::vector<float> > zs, edm::Handle< std::vector<float> > times) {
  double minDeltaR=999;

  for (int i = 0; i < nStoppedParticles; ++i) {
    float stoppedParticle_eta = Eta(xs->at(i),ys->at(i),zs->at(i),times->at(i));
    float stoppedParticle_phi = ((*ys)[i]==0 && (*xs)[i]==0) ? 0 : atan2((*ys)[i],(*xs)[i]);

    double dR=deltaR(mcpart.eta(),mcpart.phi(),stoppedParticle_eta,stoppedParticle_phi);

    //std::cout<<"for stopped particle "<<i<<", dR is: "<<dR<<std::endl;
    if (dR<minDeltaR) {
      minDeltaR = dR;
      //std::cout<<"new min dR is: "<<minDeltaR<<std::endl;
    }
  }

  return minDeltaR;
}
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StoppPtlsEventVariableProducer);

// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      StoppPtlsCandProducer
// 
/**\class StoppPtlsCandProducer StoppPtlsCandProducer.cc StoppPtls/Collection/plugins/StoppPtlsCandProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Weifeng Ji
//         Created:  Mon, 23 Nov 2015 15:02:33 GMT
//
//
#include "StoppPtlsCandProducer.h"
using namespace reco;
using namespace std;
using namespace edm;

StoppPtlsCandProducer::StoppPtlsCandProducer(const edm::ParameterSet& iConfig) :
  isMC_             (iConfig.getUntrackedParameter<bool>("isMC",false)),
  caloTowerTag_     (iConfig.getUntrackedParameter<edm::InputTag> ("EventTag",edm::InputTag("towerMaker"))),
  caloTowerToken_   (consumes<CaloTowerCollection>(caloTowerTag_)),
  hcalNoiseFilterResultTag_ (iConfig.getUntrackedParameter<edm::InputTag> ("hcalNoiseFilterResultTag",edm::InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"))),
  hcalNoiseFilterResultToken_   (consumes<bool>(hcalNoiseFilterResultTag_)),
  jetTag_           (iConfig.getUntrackedParameter<edm::InputTag> ("jetTag",edm::InputTag("ak4CaloJets"))),
  jetToken_         (consumes<reco::CaloJetCollection>(jetTag_)),
  rbxTag_           (iConfig.getUntrackedParameter<edm::InputTag> ("rbxTag", edm::InputTag("hcalnoise"))),
  rbxToken_         (consumes<reco::HcalNoiseRBXCollection>(rbxTag_)),
  verticesTag_      (iConfig.getUntrackedParameter<edm::InputTag> ("verticesTag", edm::InputTag("offlinePrimaryVertices"))),
  verticesToken_    (consumes<reco::VertexCollection>(verticesTag_)),
  //genParticlesTag_  (iConfig.getUntrackedParameter<edm::InputTag> ("genParticlesTag", edm::InputTag("genParticles"))),
  mcProducerTag_    (iConfig.getUntrackedParameter<std::string>("producer", "g4SimHits")),

  jetMinEnergy_(iConfig.getUntrackedParameter<double>("jetMinEnergy", 1.)),
  jetMaxEta_(iConfig.getUntrackedParameter<double>("jetMaxEta", 3.)),
  towerMinEnergy_(iConfig.getUntrackedParameter<double>("towerMinEnergy", 1.)),
  towerMaxEta_(iConfig.getUntrackedParameter<double>("towerMaxEta", 1.3))
{
  produces<std::vector<CandidateJet> > ();
  produces<std::vector<CandidateEvent> > ();
}


StoppPtlsCandProducer::~StoppPtlsCandProducer()
{ 
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
StoppPtlsCandProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  doEvents(iEvent, iSetup);

  //if (isMC_){
  //iSetup.getData(fPDGTable);
    //doMC(iEvent, iSetup);
  //}  

}



void StoppPtlsCandProducer::doEvents(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  auto_ptr<vector<CandidateEvent> > events(new vector<CandidateEvent> ());
  
  CandidateEvent event;
  //cout<<iEvent.id().run()<<":" << iEvent.luminosityBlock() << ":" << iEvent.id().event() << endl;
  if(isMC_) doMC(event, iEvent, iSetup);

  event.set_bx(iEvent.bunchCrossing());
  event.set_run(iEvent.id().run());
  event.set_fill(lhcfills_.getFillFromRun(event.run()));
  event.set_bxWrtBunch(static_cast<int>(abs(lhcfills_.getBxWrtBunch(event.fill(), event.bx()))));
  /*******************begin doGlobalCalo***************************************/
  edm::Handle<CaloTowerCollection> caloTowers;
  iEvent.getByLabel(caloTowerTag_,caloTowers);

  if (caloTowers.isValid()) {
    
    std::vector<CaloTower> caloTowersTmp;
    caloTowersTmp.insert(caloTowersTmp.end(), caloTowers->begin(), caloTowers->end());
    sort(caloTowersTmp.begin(), caloTowersTmp.end(), calotower_gt());
    if(caloTowersTmp.begin() != caloTowersTmp.end()){
      int iphiFirst=caloTowersTmp.begin()->iphi();
      bool keepgoing=true;
      for(std::vector<CaloTower>::const_iterator twr = caloTowersTmp.begin();
      twr!=caloTowersTmp.end() && keepgoing;
    ++twr) {
        
        if (fabs(twr->eta()) < 1.3) {  

    // tower same iphi as leading tower
          if (twr->iphi()==iphiFirst) {
            /*event_->nTowerSameiPhi++;
            event_->nTowerLeadingIPhi++;
            event_->eHadLeadingIPhi += twr->hadEnergy();*/
            event.increment_nTowerSameiPhi();
          }
          else {
            keepgoing=false;
          }
        }  
      } // loop on caloTowers
    }
    //event_->leadingIPhiFractionValue=event_->leadingIPhiFraction();
  }
  else {
    edm::LogWarning("MissingProduct") << "CaloTowers not found.  Branches will not be filled";
  }
  edm::Handle<CaloJetCollection> calojets;
  iEvent.getByLabel(jetTag_, calojets);
  if (calojets.isValid()) {
    vector<CaloJet> jets;
    jets.insert(jets.end(), calojets->begin(), calojets->end());
    sort(jets.begin(), jets.end(), jete_gt());

    auto_ptr<vector<CandidateJet> > candjets(new vector<CandidateJet> ());

    vector<double> tmp(75, 0);
    int tower_N = 0;
    vector<CaloJet> bjets;
    for (auto it = jets.begin(); it !=jets.end(); ++it) {
      if (it->energy() > jetMinEnergy_){
        if(fabs(it->eta()) < jetMaxEta_){
          bjets.push_back(*it);
          CandidateJet candjet;
          candjet.set_energy(it->energy());
          candjet.set_et(it->et());
          candjet.set_eta(it->eta());
          candjet.set_phi(it->phi());
          candjet.set_n60(it->n60());
          candjet.set_n90(it->n90());
          candjets->push_back(candjet);
        }
        for (int i = 0; i< it->nConstituents(); ++i){
          CaloTowerPtr tower = it->getCaloConstituent(i);
          if(tower->energy() > towerMinEnergy_ && fabs(tower->eta()) < towerMaxEta_) {
            if (tower_N < 100) {
              tmp.at(tower->iphi()) += tower->energy();
            }
          }
        }//loop over towers
      }
    }//loop over jets
    iEvent.put(candjets);
    if (!bjets.size())
      event.set_leadingIPhiFractionValue(0.);
    else {
      auto max = max_element(tmp.begin(), tmp.end());
      double leadingIPhiFractionValue = (*max)/bjets[0].energy();
      event.set_leadingIPhiFractionValue(leadingIPhiFractionValue);
    }
  }
  else {
    edm::LogWarning("MissingProduct") << "CaloJets not found";
  }
  /***************************end doGlobalCalo*********************************/
  edm::Handle<reco::VertexCollection> recoVertices;
  iEvent.getByLabel(verticesTag_, recoVertices);

  unsigned nvtx = 0;
  if (recoVertices.isValid()) {
    for (auto it = recoVertices->begin(); it != recoVertices->end(); ++it) {
      if (! it->isFake())
        ++nvtx;
    }
    event.set_nVtx(nvtx);
  }
  else {
    edm::LogWarning("MissingProduct") << "Vertices not found";
  }

  edm::Handle<bool> flag;
  iEvent.getByLabel(hcalNoiseFilterResultTag_, flag);

  event.set_noiseFilterResult(1);
  if (flag.isValid()){
    event.set_noiseFilterResult(*flag.product());
  }
  else {
    edm::LogWarning("MissingProduct") << "No noise result filter flag in the event";
  }

  /**************************begin adding pulse shape**************************/
  edm::Handle<HcalNoiseRBXCollection> rbxs;
  iEvent.getByLabel(rbxTag_, rbxs);
  if (rbxs.isValid())
  {
    double maxCharge = 0;
    HcalNoiseHPD maxHPD;
    
    for (auto it = rbxs->begin(); it!= rbxs->end(); ++it) {
      vector<HcalNoiseHPD> hpds = it->HPDs();
      for (auto hpd = hpds.begin(); hpd!=hpds.end(); ++hpd) {
        double totalCharge = 0;
        for (int i = 0; i !=10; ++i) {
          totalCharge += hpd -> big5Charge().at(i);
        }
        if (totalCharge > maxCharge) {
          maxCharge = totalCharge;
          maxHPD = *hpd;
        }
      }//loop on HPDs
    }//loop on RBXs
    vector<double> tphpd5TimeSamples;
    for (int i = 0; i != 10; ++i) {
      tphpd5TimeSamples.push_back(std::max(0., static_cast<double>(maxHPD.big5Charge().at(i))));
    }
    unsigned tphpd5PeakSample;
    double tphpd5Total;
    double tphpd5R1;
    double tphpd5R2;
    double tphpd5RPeak;
    double tphpd5ROuter;

    pulseShapeVariables(tphpd5TimeSamples, tphpd5PeakSample, tphpd5Total, tphpd5R1, tphpd5R2, tphpd5RPeak, tphpd5ROuter);

    event.set_topHPD5PeakSample(tphpd5PeakSample);
    event.set_topHPD5Total(tphpd5Total);
    event.set_topHPD5R1(tphpd5R1);
    event.set_topHPD5R2(tphpd5R2);
    event.set_topHPD5RPeak(tphpd5RPeak);
    event.set_topHPD5ROuter(tphpd5ROuter);
  }
  /**************************end adding pulse shape**************************/
  
  events->push_back(event);
  iEvent.put(events);
  
 
}

void StoppPtlsCandProducer::pulseShapeVariables(const vector<double> &samples, unsigned &ipeak, double &total, double &r1, double &r2, double &rpeak, double &\
						    router){

  ipeak = 3;
  total = 0.;
  r1 = 0.;
  r2 = 0.;
  rpeak = 0.;
  router = 0.;

  for (int i=0; i<HBHEDataFrame::MAXSAMPLES; ++i) {
    if (samples.at(i) > samples.at(ipeak)) {
      ipeak = i;
    }
    total += samples.at(i);
  }

  if (total==0.) return;

  // R1                                                                                                                                                            
  if (ipeak < HBHEDataFrame::MAXSAMPLES-1) {
    if (samples.at(ipeak) > 0.) {
      r1 = samples.at(ipeak+1) / samples.at(ipeak);
    }
    else r1 = 1.;
  }

  // R2                                                                                                                                                            
  if (ipeak < HBHEDataFrame::MAXSAMPLES-2) {
    if (samples.at(ipeak+1) > 0. &&
	samples.at(ipeak+1) > samples.at(ipeak+2)) {
      r2 = samples.at(ipeak+2) / samples.at(ipeak+1);
    }
    else r2 = 1.;
  }

  // Rpeak - leading digi                                                                                                                                          
  rpeak = samples.at(ipeak) / total;

  // Router - leading digi                                                                                                                                         
  double foursample=0.;
  for (int i=-1; i<3; ++i) {
    if (ipeak+i > 0 && ipeak+i<(int)HBHEDataFrame::MAXSAMPLES) { //JIM:  why is this condition "> 0" and not "> = 0"??                                             
      foursample += samples.at(ipeak+i);
    }
  }
  router = 1. - (foursample / total);
}//end of pulseShapeVariables

void StoppPtlsCandProducer::doMC(CandidateEvent& event, edm::Event& iEvent, const edm::EventSetup& iSetup){

  // Fill variables based on the StoppedParticles vectors made by RHStopTracer module
  edm::Handle<std::vector<std::string> > names;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesName", names);
  edm::Handle<std::vector<float> > xs;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesX", xs);
  edm::Handle<std::vector<float> > ys;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesY", ys);
  edm::Handle<std::vector<float> > zs;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesZ", zs);
  edm::Handle<std::vector<float> > times;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesTime", times);
  edm::Handle<std::vector<int> > ids;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesPdgId", ids);
  edm::Handle<std::vector<float> > masses;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesMass", masses);
  edm::Handle<std::vector<float> > charges;
  iEvent.getByLabel (mcProducerTag_, "StoppedParticlesCharge", charges);

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
      float phi = ((*ys)[i]==0 && (*xs)[i]==0) ? 0 : atan2((*ys)[i],(*xs)[i]);
      
      event.set_stoppedParticleName(names->at(i));
      event.set_stoppedParticleId(ids->at(i));
      event.set_stoppedParticleMass(masses->at(i));
      event.set_stoppedParticleCharge(charges->at(i));
      event.set_stoppedParticleX(xs->at(i));
      event.set_stoppedParticleY(ys->at(i));
      event.set_stoppedParticleZ(zs->at(i));
      event.set_stoppedParticleR(sqrt(xs->at(i)*xs->at(i) + ys->at(i)*ys->at(i)));
      event.set_stoppedParticlePhi(phi);
      event.set_stoppedParticleTime(times->at(i));
    }//end of loop over stopped particles
  }//end of if stopped particles are valid

}//end of doMC()

//define this as a plug-in
DEFINE_FWK_MODULE(StoppPtlsCandProducer);

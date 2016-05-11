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


// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ESHandle.h"

// towers
#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
#include "DataFormats/CaloTowers/interface/CaloTowerDetId.h"

// vertices
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

//hcalnoise
#include "DataFormats/METReco/interface/HcalNoiseHPD.h"
#include "DataFormats/METReco/interface/HcalNoiseRBX.h"
#include "DataFormats/METReco/interface/HcalNoiseSummary.h"

//jets
#include "DataFormats/JetReco/interface/CaloJetCollection.h"

//helper class
#include "StoppPtls/Livetime/interface/LhcFills.h"

#include "StoppPtls/Collection/interface/CandidateEvent.h"
#include "StoppPtls/Collection/interface/CandidateJet.h"
//
// class declaration
//

class StoppPtlsCandProducer : public edm::EDProducer {
public:
  explicit StoppPtlsCandProducer(const edm::ParameterSet&);
  ~StoppPtlsCandProducer();
  
private:
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  
  void doEvents(edm::Event&, const edm::EventSetup&);
  void doMC(CandidateEvent&, edm::Event&, const edm::EventSetup&);
  void pulseShapeVariables(const std::vector<double> &samples, unsigned &ipeak, double &total, double &r1, double &r2, double &rpeak, double &router);
  
public:
  struct calotower_gt : public std::binary_function<CaloTower, CaloTower, bool> {
    bool operator()(const CaloTower& x, const CaloTower& y) {
      return ( x.hadEnergy() > y.hadEnergy() );
    }
  };
  
  struct jete_gt : public std::binary_function<reco::CaloJet, reco::CaloJet, bool> {
    bool operator()(const reco::CaloJet& x, const reco::CaloJet& y) {
      return ( x.energy() > y.energy() );
    }
  };
  
  //struct genParticle_pt : public std::binary_function<reco::GenParticle, reco::GenParticle, bool> {
  //bool operator()(const reco::GenParticle& x, const reco::GenParticle& y) {
  //return ( x.pt() > y.pt() ) ;
  //}
  //};
  
private:
  // ----------member data ---------------------------
  bool isMC_;

  edm::InputTag caloTowerTag_;
  edm::EDGetTokenT<CaloTowerCollection> caloTowerToken_;

  edm::InputTag hcalNoiseFilterResultTag_;
  edm::EDGetTokenT<bool> hcalNoiseFilterResultToken_;

  edm::InputTag jetTag_;
  edm::EDGetTokenT<reco::CaloJetCollection> jetToken_;

  edm::InputTag rbxTag_;
  edm::EDGetTokenT<reco::HcalNoiseRBXCollection> rbxToken_;

  edm::InputTag verticesTag_;
  edm::EDGetTokenT<reco::VertexCollection> verticesToken_;

  //edm::InputTag genParticlesTag_;
  std::string mcProducerTag_;


  LhcFills lhcfills_;
  // cuts
  double jetMinEnergy_;
  double jetMaxEta_;
  double towerMinEnergy_;
  double towerMaxEta_;

  //edm::ESHandle<HepPDT::ParticleDataTable> fPDGTable;  
  
};

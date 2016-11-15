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

//halofilter
#include "DataFormats/METReco/interface/BeamHaloSummary.h"
//jets
#include "DataFormats/JetReco/interface/CaloJetCollection.h"

//lumi
#include "DataFormats/Scalers/interface/LumiScalers.h"

//mc product
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

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
  struct calotower_hadEtGt : public std::binary_function<CaloTower, CaloTower, bool> {
    bool operator()(const CaloTower& x, const CaloTower& y) {
      return ( x.hadEt() > y.hadEt() );
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

  edm::InputTag lumiscalersTag_;
  edm::EDGetTokenT<LumiScalersCollection> lumiscalersToken_;

  edm::InputTag caloTowerTag_;
  edm::EDGetTokenT<CaloTowerCollection> caloTowerToken_;

  edm::InputTag hcalNoiseFilterResultTag_;
  edm::EDGetTokenT<bool> hcalNoiseFilterResultToken_;

  edm::EDGetTokenT<reco::BeamHaloSummary> beamHaloSummaryToken_;

  edm::InputTag jetTag_;
  edm::EDGetTokenT<reco::CaloJetCollection> jetToken_;

  edm::InputTag rbxTag_;
  edm::EDGetTokenT<reco::HcalNoiseRBXCollection> rbxToken_;

  edm::InputTag verticesTag_;
  edm::EDGetTokenT<reco::VertexCollection> verticesToken_;

  //edm::InputTag genParticlesTag_;
  //std::string mcProducerTag_;
  //edm::EDGetTokenT<edm::HepMCProduct> mcProducerToken_;

  edm::InputTag stoppedParticlesNameTag_;
  edm::EDGetTokenT<std::vector<std::string> > stoppedParticlesNameToken_;
  edm::InputTag stoppedParticlesXTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesXToken_;
  edm::InputTag stoppedParticlesYTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesYToken_;
  edm::InputTag stoppedParticlesZTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesZToken_;
  edm::InputTag stoppedParticlesTimeTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesTimeToken_;
  edm::InputTag stoppedParticlesPdgIdTag_;
  edm::EDGetTokenT<std::vector<int> > stoppedParticlesPdgIdToken_;
  edm::InputTag stoppedParticlesMassTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesMassToken_;
  edm::InputTag stoppedParticlesChargeTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesChargeToken_;

  LhcFills lhcfills_;
  // cuts
  double jetMinEnergy_;
  double jetMaxEta_;
  double towerMinEnergy_;
  double towerMaxEta_;

  //edm::ESHandle<HepPDT::ParticleDataTable> fPDGTable;  
  
};

template <typename T>
class has_CSCTightHaloId2015
{ 
  typedef char one;
  typedef long two;

  template <typename C> static one test( decltype(&C::CSCTightHaloId2015) ) ;
  template <typename C> static two test(...);
public:
  enum { value = sizeof(test<T>(0)) == sizeof(char) };
};

template <typename T>
class has_GlobalTightHaloId2016
{
  typedef char one;
  typedef long two;

  template <typename C> static one test( decltype(&C::GlobalTightHaloId2016) ) ;
  template <typename C> static two test(...);
public:
  enum { value = sizeof(test<T>(0)) == sizeof(char) };
};

template <typename T>
class has_GlobalSuperTightHaloId2016
{
  typedef char one;
  typedef long two;

  template <typename C> static one test( decltype(&C::GlobalSuperTightHaloId2016) ) ;
  template <typename C> static two test(...);
public:
  enum { value = sizeof(test<T>(0)) == sizeof(char) };
};

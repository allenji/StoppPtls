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

//include Cscs
#include "DataFormats/CSCRecHit/interface/CSCSegment.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/CSCGeometry/interface/CSCChamber.h"
#include "Geometry/CSCGeometry/interface/CSCLayer.h"
#include "Geometry/CSCGeometry/interface/CSCLayerGeometry.h"
//include Dts
#include "DataFormats/DTRecHit/interface/DTRecHit1D.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4D.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment2D.h"
#include "DataFormats/DTRecHit/interface/DTRecHitCollection.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment2DCollection.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "Geometry/DTGeometry/interface/DTChamber.h"
#include "Geometry/DTGeometry/interface/DTLayer.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "DataFormats/MuonDetId/interface/DTLayerId.h"
#include "DataFormats/MuonDetId/interface/DTWireId.h"
//jets
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
// RPC hits
#include "DataFormats/RPCRecHit/interface/RPCRecHit.h"
#include "DataFormats/RPCRecHit/interface/RPCRecHitCollection.h"
#include "Geometry/RPCGeometry/interface/RPCGeometry.h"
#include "Geometry/RPCGeometry/interface/RPCChamber.h"

//helper class
#include "StoppedHSCP/Ntuples/interface/LhcFills.h"


//generator
//#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
//#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"


#include "StoppPtls/Collection/interface/CandidateCscHit.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateEvent.h"
//#include "StoppPtls/Collection/interface/CandidateGenParticle.h"
#include "StoppPtls/Collection/interface/CandidateJet.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"
//
// class declaration
//

class StoppPtlsCandProducer : public edm::EDProducer {
public:
  explicit StoppPtlsCandProducer(const edm::ParameterSet&);
  ~StoppPtlsCandProducer();
  
private:
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  
  void doCscHits(edm::Event&, const edm::EventSetup&);
  void doCscSegments(edm::Event&, const edm::EventSetup&);
  void doEvents(edm::Event&, const edm::EventSetup&);
  void doMuonDTs(edm::Event&, const edm::EventSetup&);      
  void doMuonRPCs(edm::Event&, const edm::EventSetup&);
  void pulseShapeVariables(const std::vector<double> &samples, unsigned &ipeak, double &total, double &r1, double &r2, double &rpeak, double &router);
  void doMC(CandidateEvent&, edm::Event&, const edm::EventSetup&);
  
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

  edm::InputTag cscRecHitsTag_;
  edm::InputTag cscSegmentsTag_;
  edm::InputTag caloTowerTag_;
  edm::InputTag DTRecHitsTag_;
  edm::InputTag DT4DSegmentsTag_;
  edm::InputTag hcalNoiseFilterResultTag_;
  edm::InputTag jetTag_;
  edm::InputTag rpcRecHitsTag_;
  edm::InputTag rbxTag_;
  edm::InputTag verticesTag_;
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

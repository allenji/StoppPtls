// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      StoppPtlsJetsCandProducer
// 
/**\class StoppPtlsJetsCandProducer StoppPtlsJetsCandProducer.cc StoppPtls/Collection/plugins/StoppPtlsJetsCandProducer.cc

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

// RPC hits
#include "DataFormats/RPCRecHit/interface/RPCRecHit.h"
#include "DataFormats/RPCRecHit/interface/RPCRecHitCollection.h"
#include "Geometry/RPCGeometry/interface/RPCGeometry.h"
#include "Geometry/RPCGeometry/interface/RPCChamber.h"


#include "StoppPtls/Collection/interface/CandidateCscHit.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"
//
// class declaration
//

class StoppPtlsJetsCandProducer : public edm::EDProducer {
public:
  explicit StoppPtlsJetsCandProducer(const edm::ParameterSet&);
  ~StoppPtlsJetsCandProducer();
  
private:
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  
  void doCscHits(edm::Event&, const edm::EventSetup&);
  void doCscSegments(edm::Event&, const edm::EventSetup&);
  void doMuonDTs(edm::Event&, const edm::EventSetup&);      
  void doMuonRPCs(edm::Event&, const edm::EventSetup&);
  void pulseShapeVariables(const std::vector<double> &samples, unsigned &ipeak, double &total, double &r1, double &r2, double &rpeak, double &router);
  
public:
  
private:
  // ----------member data ---------------------------
  edm::InputTag cscRecHitsTag_;
  edm::EDGetTokenT<CSCRecHit2DCollection> cscRecHitsToken_;

  edm::InputTag cscSegmentsTag_;
  edm::EDGetTokenT<CSCSegmentCollection> cscSegmentsToken_;

  edm::InputTag DTRecHitsTag_;
  edm::EDGetTokenT<DTRecHitCollection> DTRecHitsToken_;

  edm::InputTag DT4DSegmentsTag_;
  edm::EDGetTokenT<DTRecSegment4DCollection> DT4DSegmentsToken_;

  edm::InputTag rpcRecHitsTag_;
  edm::EDGetTokenT<RPCRecHitCollection> rpcRecHitsToken_;
  
};

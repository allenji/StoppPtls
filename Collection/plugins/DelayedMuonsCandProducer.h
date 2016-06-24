// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      DelayedMuonsCandProducer
// 
/**\class DelayedMuonsCandProducer DelayedMuonsCandProducer.cc StoppPtls/Collection/plugins/DelayedMuonsCandProducer.cc

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

// muons
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonShower.h"
#include "RecoMuon/TrackingTools/interface/MuonServiceProxy.h"
#include "RecoMuon/TrackingTools/interface/MuonSegmentMatcher.h"
#include "RecoMuon/MuonIdentification/interface/TimeMeasurementSequence.h"

#include "DataFormats/Candidate/interface/LeafCandidate.h"
//#include "DataFormats/Candidate/interface/iterator_imp_specific.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/Candidate/interface/CompositeCandidateFwd.h"

#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"

// MuonTimeExtra
#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

// tracks
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"

// CSC segments
#include "DataFormats/CSCRecHit/interface/CSCSegment.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/CSCGeometry/interface/CSCChamber.h"
#include "Geometry/CSCGeometry/interface/CSCLayer.h"
#include "Geometry/CSCGeometry/interface/CSCLayerGeometry.h"

// DT segments
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

#include "StoppPtls/Collection/interface/CandidateDelayedMuonsTrack.h"
//
// class declaration
//

class DelayedMuonsCandProducer : public edm::EDProducer {
public:
  explicit DelayedMuonsCandProducer(const edm::ParameterSet&);
  ~DelayedMuonsCandProducer();
  
private:
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  
  void doDisplacedStandAloneMuons(edm::Event&, const edm::EventSetup&);
  
public:

  struct track_pt : public std::binary_function<reco::Track, reco::Track, bool> {
    bool operator()(const reco::Track& x, const reco::Track& y) {
      return ( x.pt() > y.pt() ) ;
    }
  };
  
private:
  // ----------member data ---------------------------
  edm::InputTag displacedStandAloneMuonTag_;
  edm::EDGetTokenT<reco::TrackCollection> displacedStandAloneMuonToken_;

  edm::InputTag muonTag_;
  edm::EDGetTokenT<reco::MuonCollection> muonToken_;

  edm::InputTag timeTag_;
  edm::EDGetTokenT<reco::MuonTimeExtraMap> timeToken_;

  edm::InputTag rpcRecHitsTag_;
  edm::EDGetTokenT<RPCRecHitCollection> rpcRecHitsToken_;  

  int Rpc_Bx_Pattern(std::vector<int> &);
  double Rpc_Bx_Average(std::vector<int> &);
};

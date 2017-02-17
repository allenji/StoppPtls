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
#include "StoppPtlsJetsCandProducer.h"
//using namespace reco;
using namespace std;
using namespace edm;

StoppPtlsJetsCandProducer::StoppPtlsJetsCandProducer(const edm::ParameterSet& iConfig) :
  cscRecHitsTag_    (iConfig.getParameter<edm::InputTag> ("cscRecHitsTag")),
  cscRecHitsToken_  (consumes<CSCRecHit2DCollection>(cscRecHitsTag_)),
  cscSegmentsTag_   (iConfig.getParameter<edm::InputTag> ("cscSegmentsTag")),
  cscSegmentsToken_ (consumes<CSCSegmentCollection>(cscSegmentsTag_)),
  DTRecHitsTag_     (iConfig.getParameter<edm::InputTag> ("DTRecHitsTag")),
  DTRecHitsToken_   (consumes<DTRecHitCollection>(DTRecHitsTag_)),
  DT4DSegmentsTag_  (iConfig.getParameter<edm::InputTag> ("DT4DSegmentsTag")),
  DT4DSegmentsToken_(consumes<DTRecSegment4DCollection>(DT4DSegmentsTag_)),
  rpcRecHitsTag_    (iConfig.getParameter<edm::InputTag> ("rpcRecHitsTag")),
  rpcRecHitsToken_  (consumes<RPCRecHitCollection>(rpcRecHitsTag_))
{
    //produces<std::vector<CandidateCscHit> > ();
    produces<std::vector<CandidateCscSeg> > ();
    produces<std::vector<CandidateDTSeg> > ();
    produces<std::vector<CandidateRpcHit> > ();
}


StoppPtlsJetsCandProducer::~StoppPtlsJetsCandProducer()
{ 
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
StoppPtlsJetsCandProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //doCscHits(iEvent, iSetup);
  doCscSegments(iEvent, iSetup);
  doMuonDTs(iEvent, iSetup);
  doMuonRPCs(iEvent, iSetup);
}


void StoppPtlsJetsCandProducer::doCscHits(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<CSCRecHit2DCollection> hits;
  iEvent.getByToken(cscRecHitsToken_, hits);
  edm::ESHandle<CSCGeometry> cscGeom;
  iSetup.get<MuonGeometryRecord>().get(cscGeom);
   
  auto_ptr<vector<CandidateCscHit> > candCscHits(new vector<CandidateCscHit> ());
  int iHit = 0;
  CSCRecHit2DCollection::const_iterator dRHIter;
  for (dRHIter = hits->begin(); dRHIter != hits->end(); dRHIter++) {
    iHit++;
    CSCDetId idrec = (CSCDetId)(*dRHIter).cscDetId();
    const CSCLayer* csclayer = cscGeom->layer( idrec );
    LocalPoint rhitlocal = (*dRHIter).localPosition();
    GlobalPoint rhitglobal= csclayer->toGlobal(rhitlocal);
    CandidateCscHit h;
    h.set_z(rhitglobal.z());
    h.set_rho(rhitglobal.perp());
    h.set_phi(rhitglobal.phi());
    h.set_time(dRHIter->tpeak());
    candCscHits->push_back(h);
  }
  iEvent.put (candCscHits);
}


void StoppPtlsJetsCandProducer::doCscSegments(edm::Event& iEvent, const edm::EventSetup& iSetup){
  // get the segments
  edm::Handle<CSCSegmentCollection> segments;
  iEvent.getByToken(cscSegmentsToken_, segments);

  // Get the geometry :
  edm::ESHandle<CSCGeometry> cscGeom;
  iSetup.get<MuonGeometryRecord>().get(cscGeom);

    auto_ptr<vector<CandidateCscSeg> > candCscSegs(new vector<CandidateCscSeg>());
    // write segment info to ntuple
    if(segments.isValid()) {
      unsigned i=0;
      for (CSCSegmentCollection::const_iterator seg=segments->begin();
     seg!=segments->end() && i<1000;
     ++seg, ++i) {
        /// code taken from RecoLocalMuon/CSCValidation/src/CSCValidation.cc
        //  CSCDetId id  = (CSCDetId)seg->cscDetId();
        LocalPoint localPos = seg->localPosition();
        LocalVector segDir = seg->localDirection();
        CSCDetId id  = seg->cscDetId();
        GlobalPoint globalPos = cscGeom->chamber(id)->toGlobal(localPos);
        GlobalVector globalVec = cscGeom->chamber(id)->toGlobal(segDir);
        //float chisq    = seg->chi2();
        //int nDOF       = 2*nhits-4;
        //double chisqProb = ChiSquaredProbability( (double)chisq, nDOF );
        //float segX     = localPos.x();
        //float segY     = localPos.y();
        //double theta   = segDir.theta();
        CandidateCscSeg candCscSeg;
        
        candCscSeg.set_endcap(id.endcap());
        candCscSeg.set_ring(id.ring());
        candCscSeg.set_station(id.station());
        candCscSeg.set_chamber(id.chamber());
        candCscSeg.set_nHits(seg->nRecHits());
        candCscSeg.set_phi(globalPos.phi());
        candCscSeg.set_x(globalPos.x());
        candCscSeg.set_y(globalPos.y());
        candCscSeg.set_z(globalPos.z());
        candCscSeg.set_r(sqrt((globalPos.x()*globalPos.x()) + (globalPos.y()*globalPos.y())));
        candCscSeg.set_dirTheta(globalVec.theta());
        candCscSeg.set_dirPhi(globalVec.phi());
        candCscSeg.set_time(seg->time());
        
        candCscSegs->push_back(candCscSeg);
      }
    
      
    }
    /*else {
      if (!cscSegsMissing_) edm::LogWarning("MissingProduct") << "CSC Segments not found.  Branches will not be filled";
      cscSegsMissing_ = true;
    }*/
    iEvent.put(candCscSegs);
}

void StoppPtlsJetsCandProducer::doMuonDTs(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::ESHandle<DTGeometry> dtGeom;
  iSetup.get<MuonGeometryRecord>().get(dtGeom);

  edm::Handle<DTRecSegment4DCollection> all4DSegments;
  iEvent.getByToken(DT4DSegmentsToken_, all4DSegments);
  edm::Handle<DTRecHitCollection> dtRecHits;
  iEvent.getByToken(DTRecHitsToken_, dtRecHits);

  // create vector we are gonna save
  auto_ptr<vector<CandidateDTSeg> > candDTs (new vector<CandidateDTSeg>());

  //loop over each DT chamber
  DTRecSegment4DCollection::id_iterator chamberId;
  for (chamberId = all4DSegments->id_begin();
       chamberId != all4DSegments->id_end();
       ++chamberId){
    const DTChamber* chamber = dtGeom->chamber(*chamberId);
    DTRecSegment4DCollection::range range = all4DSegments->get(*chamberId);

    //loop over all segments in chamber
    for (DTRecSegment4DCollection::const_iterator segment4D = range.first;
        segment4D!=range.second;
        ++segment4D){
      //skip invalid values
      //if((*chamberId).station() != 4 &&
          //(*segment4D).dimension() != 4) continue;
      //if((*chamberId).station() == 4 &&
          //(*segment4D).dimension() != 2) continue;

      const GeomDet* gdet=dtGeom->idToDet(segment4D->geographicalId());
      const BoundPlane& DTSurface = gdet->surface();
      LocalPoint segmentLocal = (*segment4D).localPosition();
      GlobalPoint segmentGlobal = DTSurface.toGlobal(segmentLocal);

      LocalVector segmentLocalDir = (*segment4D).localDirection();
      GlobalVector segmentGlobalDir = DTSurface.toGlobal(segmentLocalDir);

      int nPhiHits=0;
      if((*segment4D).hasPhi())
        nPhiHits = (((*segment4D).phiSegment())->specificRecHits()).size();

      int nZHits=0;
      if((*segment4D).hasZed())
        nZHits = (((*segment4D).zSegment())->specificRecHits()).size();

      CandidateDTSeg candDTSeg;
      
      candDTSeg.set_wheel((chamber->id()).wheel());
      candDTSeg.set_station((chamber->id()).station());
      candDTSeg.set_sector((chamber->id()).sector());
      candDTSeg.set_localX(segmentLocal.x());
      candDTSeg.set_localY(segmentLocal.y());
      candDTSeg.set_x(segmentGlobal.x());
      candDTSeg.set_y(segmentGlobal.y());
      candDTSeg.set_r(sqrt(segmentGlobal.x()*segmentGlobal.x() + segmentGlobal.y()*segmentGlobal.y()));
      candDTSeg.set_z(segmentGlobal.z());
      candDTSeg.set_rho(segmentGlobal.perp());
      candDTSeg.set_phi(segmentGlobal.phi());
      candDTSeg.set_xdir(segmentGlobalDir.x());
      candDTSeg.set_ydir(segmentGlobalDir.y());
      candDTSeg.set_phidir(segmentGlobalDir.phi());
      candDTSeg.set_zdir(segmentGlobalDir.z());
      candDTSeg.set_nPhiHits(nPhiHits);
      candDTSeg.set_nZHits(nZHits);
      candDTSeg.set_nHits(nPhiHits + nZHits);
      candDTs->push_back(candDTSeg);
    }//finish loop over all segments in chamber
  }//finish loop over all chambers
  // save the vector
  iEvent.put(candDTs);
}

void StoppPtlsJetsCandProducer::doMuonRPCs(edm::Event& iEvent, const edm::EventSetup& iSetup){
  edm::Handle<RPCRecHitCollection> hits;
  iEvent.getByToken(rpcRecHitsToken_, hits);
  edm::ESHandle<RPCGeometry> rpcGeom;
  iSetup.get<MuonGeometryRecord>().get(rpcGeom);
  
  //int nRecHits = hits->size();
  int iHit = 0;
  RPCRecHitCollection::const_iterator rpcIter;
  //create object we are gonna put back to the event
  auto_ptr<vector<CandidateRpcHit> > candRpcHits(new vector<CandidateRpcHit> ());
  for (rpcIter = hits->begin(); rpcIter != hits->end(); ++rpcIter) {
    ++iHit;
    const RPCDetId detId = static_cast<const RPCDetId>(rpcIter->rpcId());
    const RPCRoll* roll = dynamic_cast<const RPCRoll*>(rpcGeom->roll(detId));
    const GlobalPoint rhitglobal = roll->toGlobal(rpcIter->localPosition());
    CandidateRpcHit candRpcHit;
    candRpcHit.set_x(rhitglobal.x());
    candRpcHit.set_y(rhitglobal.y());
    candRpcHit.set_r(sqrt(rhitglobal.x()*rhitglobal.x() + rhitglobal.y()*rhitglobal.y()));
    candRpcHit.set_z(rhitglobal.z());
    candRpcHit.set_rho(rhitglobal.perp());
    candRpcHit.set_phi(rhitglobal.phi());
    candRpcHit.set_region(detId.region());
    candRpcHit.set_bx((*rpcIter).BunchX());
    
    candRpcHits->push_back(candRpcHit); 
  }//loop on rpc hits
  iEvent.put(candRpcHits);
}



//define this as a plug-in
DEFINE_FWK_MODULE(StoppPtlsJetsCandProducer);

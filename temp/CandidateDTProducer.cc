// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      CandidateDTProducer
// 
/**\class CandidateDTProducer CandidateDTProducer.cc StoppPtls/Collection/plugins/CandidateDTProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Weifeng Ji
//         Created:  Fri, 20 Nov 2015 19:50:22 GMT
//
//


// user include files
#include "StoppPtls/Collection/interface/CandidateDT.h"
#include "StoppPtls/Collection/plugins/CandidateDTProducer.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"

// constructors and destructor
CandidateDTProducer::CandidateDTProducer(const edm::ParameterSet& iConfig):
  DTRecHitsTag_   (iConfig.getParameter<edm::InputTag> ("DTRecHit")),
  DT4DSegmentsTag_(iConfig.getParameter<edm::InputTag> ("DTSegment"))
{
  produces<std::vector<CandidateDT> > ();  
}


CandidateDTProducer::~CandidateDTProducer()
{
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
CandidateDTProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;

  edm::ESHandle<DTGeometry> dtGeom;
  iSetup.get<MuonGeometryRecord>().get(dtGeom);

  edm::Handle<DTRecSegment4DCollection> all4DSegments;
  iEvent.getByLabel(DT4DSegmentsTag_, all4DSegments);
  edm::Handle<DTRecHitCollection> dtRecHits;
  iEvent.getByLabel(DTRecHitsTag_, dtRecHits);

  // create vector we are gonna save
  auto_ptr<vector<CandidateDT> > candDTs (new vector<CandidateDT>());

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
      if((*chamberId).station() != 4 &&
          (*segment4D).dimension() != 4) continue;
      if((*chamberId).station() == 4 && 
          (*segment4D).dimension() != 2) continue;

      const GeomDet* gdet=dtGeom->idToDet(segment4D->geographicalId());
      const BoundPlane& DTSurface = gdet->surface();
      LocalPoint segmentLocal = (*segment4D).localPosition();
      GlobalPoint segmentGlobal = DTSurface.toGlobal(segmentLocal);

      LocalVector segmentLocalDir = (*segment4D).localDirection();
      GlobalVector segmentGlobalDir = DTSurface.toGlobal(segmentLocalDir);

      CandidateDT candDT(chamber, segmentLocal, segmentGlobal, segmentGlobalDir);
      candDTs->push_back(candDT);
    }//finish loop over all segments in chamber
  }//finish loop over all chambers
  // save the vector
  iEvent.put(candDTs);
}
//define this as a plug-in
DEFINE_FWK_MODULE(CandidateDTProducer);

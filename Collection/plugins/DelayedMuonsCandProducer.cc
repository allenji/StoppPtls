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
// Original Author:  Juliette Alimena
//         Created:  Mon, 23 Nov 2015 15:02:33 GMT
//
//
#include "DelayedMuonsCandProducer.h"

using namespace reco;
using namespace std;
using namespace edm;

DelayedMuonsCandProducer::DelayedMuonsCandProducer(const edm::ParameterSet& iConfig) :
  displacedStandAloneMuonTag_(iConfig.getParameter<edm::InputTag>("displacedStandAloneMuonTag")),
  displacedStandAloneMuonToken_(consumes<reco::TrackCollection>(displacedStandAloneMuonTag_)),
  muonTag_(iConfig.getParameter<edm::InputTag>("muonTag")),
  muonToken_(consumes<reco::MuonCollection>(muonTag_)),
  timeTag_(iConfig.getParameter<edm::InputTag>("timeTag")),
  timeToken_(consumes<reco::MuonTimeExtraMap>(timeTag_)),
  rpcRecHitsTag_(iConfig.getParameter<edm::InputTag>("rpcRecHitsTag")),
  rpcRecHitsToken_(consumes<RPCRecHitCollection>(rpcRecHitsTag_))
{
  produces<std::vector<CandidateDelayedMuonsTrack> > ();
}


DelayedMuonsCandProducer::~DelayedMuonsCandProducer()
{ 
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
DelayedMuonsCandProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //std::cout<<"starting produce of DelayedMuonsCandProducer"<<std::endl;
  doDisplacedStandAloneMuons(iEvent, iSetup);
}


void DelayedMuonsCandProducer::doDisplacedStandAloneMuons(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //std::cout<<"starting doDisplacedStandAloneMuons"<<std::endl;  
  // loop over displaced standalone muons
  edm::Handle<TrackCollection> displacedStandAloneMuons;
  iEvent.getByLabel(displacedStandAloneMuonTag_,displacedStandAloneMuons);

  edm::Handle<MuonCollection> muons;
  iEvent.getByLabel(muonTag_,muons);

  edm::Handle<MuonTimeExtraMap> timeMap2;
  //iEvent.getByLabel(timeTag_.label(),"dt",timeMap2);
  iEvent.getByLabel(timeTag_,timeMap2);
  const MuonTimeExtraMap & timeMapDT = *timeMap2;

  edm::Handle<RPCRecHitCollection> rpcHits;
  iEvent.getByLabel(rpcRecHitsTag_, rpcHits);

  edm::ESHandle<RPCGeometry> rpcGeom;
  iSetup.get<MuonGeometryRecord>().get(rpcGeom);

  edm::ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  auto_ptr<vector<CandidateDelayedMuonsTrack> > candDelayedMuonsTracks(new vector<CandidateDelayedMuonsTrack> ());                                          //std::cout<<"got all collections"<<std::endl;  
  
  if (displacedStandAloneMuons.isValid()) {
    //std::cout<<"displacedStandAloneMuons is valid"<<std::endl;  
    // sort muon tracks by pt
    std::vector<Track> displacedStandAloneMuons_;
    displacedStandAloneMuons_.insert(displacedStandAloneMuons_.end(), displacedStandAloneMuons->begin(), displacedStandAloneMuons->end());
    std::sort(displacedStandAloneMuons_.begin(), displacedStandAloneMuons_.end(), track_pt() );

    //for(reco::TrackCollection::const_iterator it =displacedStandAloneMuons_.begin();
    //it!=displacedStandAloneMuons_.end();
    //it++) {
    for(const auto &it : *displacedStandAloneMuons){
      //for(const auto &it : displacedStandAloneMuons_){
      //std::cout<<"in displacedStandAloneMuons loop"<<std::endl;  
    
      CandidateDelayedMuonsTrack track(it);
      //std::cout<<"declared CandidateDelayedMuonsTrack"<<std::endl;  

      //int muonStations (int subdet, int hitType) const
      //subdet = 0(all), 1(DT), 2(CSC), 3(RPC); hitType=-1(all), 0=valid, 3=bad 
      //track.nHitsMuonStations = it.hitPattern().muonStations(0,0);
      track.set_nStationsWithAnyHits(it.hitPattern().muonStationsWithAnyHits()); //muon stations in track fit; same varaible as hitPattern().muonStations(0,0)
      track.set_nCscChambersWithAnyHits(it.hitPattern().cscStationsWithAnyHits()); //csc chambers in track fit
      track.set_nDtChambersWithAnyHits(it.hitPattern().dtStationsWithAnyHits()); //dt chambers in track fit
      track.set_nRpcChambersWithAnyHits(it.hitPattern().rpcStationsWithAnyHits()); //rpc chambers in track fit
      track.set_innermostStationWithAnyHits(it.hitPattern().innermostMuonStationWithAnyHits());
      track.set_outermostStationWithAnyHits(it.hitPattern().outermostMuonStationWithAnyHits());

      track.set_nStationsWithValidHits(it.hitPattern().muonStationsWithValidHits()); //muon stations anywhere near track; same varaible as hitPattern().muonStations(0,0)
      track.set_nCscChambersWithValidHits(it.hitPattern().cscStationsWithValidHits()); //csc chambers anywhere near track
      track.set_nDtChambersWithValidHits(it.hitPattern().dtStationsWithValidHits()); //dt chambers anywhere near track
      track.set_nRpcChambersWithValidHits(it.hitPattern().rpcStationsWithValidHits()); //rpc chambers anywhere near track
      track.set_nValidMuonHits(it.hitPattern().numberOfValidMuonHits()); //muon hits anywhere near track
      track.set_nValidCscHits(it.hitPattern().numberOfValidMuonCSCHits()); //CSC hits anywhere near track
      track.set_nValidDtHits(it.hitPattern().numberOfValidMuonDTHits()); //DT hits anywhere near track
      track.set_nValidRpcHits(it.hitPattern().numberOfValidMuonRPCHits()); //RPC hits anywhere near track
      track.set_innermostStationWithValidHits(it.hitPattern().innermostMuonStationWithValidHits());
      track.set_outermostStationWithValidHits(it.hitPattern().outermostMuonStationWithValidHits());
      //std::cout<<"set hit pattern variables"<<std::endl;  
	    
      TrackBase::TrackQuality q = reco::TrackBase::qualityByName("highPurity");

      track.set_quality((it.quality(q) ? 1 : 0));

      track.set_innerPx(it.innerMomentum().x());
      track.set_innerPy(it.innerMomentum().y());
      track.set_innerPz(it.innerMomentum().z());
      track.set_innerOk(it.innerOk());
      track.set_innerX(it.innerPosition().x());
      track.set_innerY(it.innerPosition().y());
      track.set_innerZ(it.innerPosition().z());

      std::vector<int> rpcHitBx_;
      std::vector<double> rpcHitZ_;
      std::vector<double> rpcHitRho_;
      std::vector<double> rpcHitPhi_;
      std::vector<int> rpcHitRegion_;

      //Loop over the hits in the track
      //std::cout<<"number of valid hits is: "<<it.numberOfValidHits()<<std::endl;
      for(size_t i=0; i<it.recHitsSize(); i++) {
	TrackingRecHitRef myRef = it.recHit(i);
	const TrackingRecHit *rechit = myRef.get();
	//std::cout<<"got hit number "<<i<<std::endl;

	if(rechit->isValid()){
	  const GeomDet* geomDet = theTrackingGeometry->idToDet(rechit->geographicalId());

	  if ( (rechit)->geographicalId().det() == DetId::Muon){

	    //DT Hits
	    if(geomDet->subDetector() == GeomDetEnumerators::DT) {
	      //std::cout<<"have DT hit"<<std::endl;
	    }

	    //CSC Hits
	    else if (geomDet->subDetector() == GeomDetEnumerators::CSC) {
	    }

	    //RPC Hits
	    else if ( (rechit)->geographicalId().subdetId() == MuonSubdetId::RPC ){
	      //else if (geomDet->subDetector() == GeomDetEnumerators::RPCBarrel) {
	      //else if (geomDet->subDetector() == GeomDetEnumerators::RPCEndcap) {
	      //std::cout<<"have RPC hit"<<std::endl;
	      RPCDetId rollId = (RPCDetId)(rechit)->geographicalId();

	      typedef std::pair<RPCRecHitCollection::const_iterator, RPCRecHitCollection::const_iterator> rangeRecHits;
	      rangeRecHits recHitCollection = rpcHits->get(rollId);

	      RPCRecHitCollection::const_iterator recHitC;
	      int size = 0;
	      double z = -99.;
	      double rho = -99.;
	      double phi = -99.;
	      int region = -99;
	      int bx=-99;

	      //std::cout<<"\t \t Looping on the rechits of the same roll"<<std::endl;
	      for(recHitC = recHitCollection.first; recHitC != recHitCollection.second ; recHitC++) {
		const RPCDetId detId = static_cast<const RPCDetId>(recHitC->rpcId());
		const RPCRoll* roll = dynamic_cast<const RPCRoll*>(rpcGeom->roll(detId));
		const GlobalPoint rhitglobal = roll->toGlobal(recHitC->localPosition());

		z = rhitglobal.z();
		//std::cout<<"rpc rec hit z is: "<<z<<std::endl;
		rho = rhitglobal.perp();
		phi = rhitglobal.phi();
		region = detId.region(); //Region id: 0 for Barrel, +/-1 For +/- Endcap.
		bx = (*recHitC).BunchX();
		//std::cout<<"rpc rec hit bx is: "<<bx<<std::endl;
		size++;
	      }
	      //std::cout<<"rpc rec hit size is: "<<size<<std::endl;
	      if(size!=1){
		//std::cout<<"\t \t \t more than one rechit in this roll discarded for filling histograms"<<std::endl;
	      }
	      else{
		//std::cout<<"starting to pushback"<<std::endl;
		rpcHitZ_.push_back(z);
		rpcHitRho_.push_back(rho);
		rpcHitPhi_.push_back(phi);
		rpcHitRegion_.push_back(region);
		rpcHitBx_.push_back(bx);
		//std::cout<<"done with pushback"<<std::endl;
	      }

	      //the layer associated with this hit
	      //RPCDetId myLayer(rechit.geographicalId().rawId());

	      //Loop over segments in the current track
	      //for(std::vector<int>::iterator positionIt = positionRPC.begin(); positionIt != positionRPC.end(); positionIt++) {
	      //}

	      //CSCDetId myChamber((*segmentRPC).geographicalId().rawId());
	      //myLayer.chamberId();

	    }
	    //std::cout<<"done with RPCs"<<std::endl;

	  } //end of hit is in muon system
	    //std::cout<<"done with muon hits"<<std::endl;
	} //end of is valid hit
	//std::cout<<"done with valid hits"<<std::endl;
      }//end of loop over valid hits
      //std::cout<<"done with loop over hits"<<std::endl;
      
      if(!rpcHitZ_.empty()){
	//std::cout<<"rpcHitZ is not empty"<<std::endl;
	track.set_rpcHitZ(rpcHitZ_);
	track.set_rpcHitRho(rpcHitRho_);
	track.set_rpcHitPhi(rpcHitPhi_);
	track.set_rpcHitRegion(rpcHitRegion_);
	track.set_rpcHitBx(rpcHitBx_);
	//std::cout<<"filled track rpc Hit variables"<<std::endl;
      }
      
      // Match the DSA to the SA. This is needed because DSA are not in the reco::Muon and we need
      // to access timing information from the reco::Muon. The DSA is a refit of the SA, the timing
      // of the hits is the same (but do not use anything with IP or beamspot constraint).
      // Analyze the short info stored directly in reco::Muon
      //From displaced muons search https://github.com/msolmaz/Dilepton_Analysis_Macros/blob/master/TreeProducer/TreeProducer/plugins/LeptonAnalysis.cc
      const math::XYZPoint & rsaInnerPoint(it.innerPosition());
      const math::XYZPoint & rsaOuterPoint(it.outerPosition());

      float minDxIn = 1000.;
      float minDyIn = 1000.;
      float minDzIn = 1000.;
      float minDxOut = 1000.;
      float minDyOut = 1000.;
      float minDzOut = 1000.;

      // Loop over the standAloneMuons and take the one with the closest inner and outer position.
      // Only save the timing if the matching is close enough (<5cm in x,y and <50cm in z).
      const reco::Muon * matchedSA = 0;
      int imucount = 0;
      int imucountMatch = -1;
      if (muons.isValid()){
	for (reco::MuonCollection::const_iterator sa=muons->begin(); sa!=muons->end(); ++sa, ++imucount) {
	  if( sa->isStandAloneMuon() ) {
	    
	    // std::cout << "pseudoLeptonProducer: filling timing information" << std::endl;
	    
	    const math::XYZPoint & saInnerPoint(sa->standAloneMuon()->innerPosition());
	    const math::XYZPoint & saOuterPoint(sa->standAloneMuon()->outerPosition());
	    if( fabs(saInnerPoint.x() - rsaInnerPoint.x()) < minDxIn &&
		fabs(saInnerPoint.y() - rsaInnerPoint.y()) < minDyIn &&
		fabs(saOuterPoint.x() - rsaOuterPoint.x()) < minDxOut &&
		fabs(saOuterPoint.y() - rsaOuterPoint.y()) < minDyOut ) {
	      minDxIn = fabs(saInnerPoint.x() - rsaInnerPoint.x());
	      minDyIn = fabs(saInnerPoint.y() - rsaInnerPoint.y());
	      minDzIn = fabs(saInnerPoint.z() - rsaInnerPoint.z());
	      minDxOut = fabs(saOuterPoint.x() - rsaOuterPoint.x());
	      minDyOut = fabs(saOuterPoint.y() - rsaOuterPoint.y());
	      minDzOut = fabs(saOuterPoint.z() - rsaOuterPoint.z());
	            
	      // Check for good matching and fill timing information
	      if( minDxIn > 5 || minDyIn > 5 || minDxOut > 5 || minDyOut > 5 || minDzIn > 50 || minDzOut > 50 ) continue;
	      
	      matchedSA = &*sa;
	      imucountMatch = imucount;
	    } //end of diff in position between RSA and SA
	  }//end of if SA muon
	}//end of loop over reco::muons 
      }//end of if muon collection is valid

      if( matchedSA != 0 && imucountMatch != -1 ) {
        // Save the MuonTimeExtra information
	reco::MuonRef muonR(muons,imucountMatch);

        // Analyze the MuonTimeExtra information
	reco::MuonTimeExtra tofdt = timeMapDT[muonR];

	// Store DT TOF Variables
	track.set_dtTofDirection(tofdt.direction());
	track.set_dtTofNDof(tofdt.nDof());
	track.set_dtTofInverseBeta(tofdt.inverseBeta());
	track.set_dtTofInverseBetaErr(tofdt.inverseBetaErr());
	track.set_dtTofFreeInverseBeta(tofdt.freeInverseBeta());
	track.set_dtTofFreeInverseBetaErr(tofdt.freeInverseBetaErr());
	track.set_dtTofTimeAtIpInOut(tofdt.timeAtIpInOut());
	track.set_dtTofTimeAtIpInOutErr(tofdt.timeAtIpInOutErr());
	track.set_dtTofTimeAtIpOutIn(tofdt.timeAtIpOutIn());
	track.set_dtTofTimeAtIpOutInErr(tofdt.timeAtIpOutInErr());
      }//end of if match to SA exists
      else{
        track.set_dtTofDirection(-999.);
        track.set_dtTofNDof(-999.);
        track.set_dtTofInverseBeta(-999.);
        track.set_dtTofInverseBetaErr(-999.);
        track.set_dtTofFreeInverseBeta(-999.);
        track.set_dtTofFreeInverseBetaErr(-999.);
        track.set_dtTofTimeAtIpInOut(-999.);
        track.set_dtTofTimeAtIpInOutErr(-999.);
        track.set_dtTofTimeAtIpOutIn(-999.);
        track.set_dtTofTimeAtIpOutInErr(-999.);
      }

      candDelayedMuonsTracks->push_back(track);

    }//end of loop over DSAs
  }//end of if DSAs is valid

  iEvent.put(candDelayedMuonsTracks);
}



//define this as a plug-in
DEFINE_FWK_MODULE(DelayedMuonsCandProducer);

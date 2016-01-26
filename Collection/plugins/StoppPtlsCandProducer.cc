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
  cscRecHitsTag_    (iConfig.getParameter<edm::InputTag> ("cscRecHitsTag")),
  cscSegmentsTag_   (iConfig.getParameter<edm::InputTag> ("cscSegmentsTag")),
  caloTowerTag_     (iConfig.getUntrackedParameter<edm::InputTag> ("EventTag",edm::InputTag("towerMaker"))),
  DTRecHitsTag_     (iConfig.getParameter<edm::InputTag> ("DTRecHitsTag")),
  DT4DSegmentsTag_  (iConfig.getParameter<edm::InputTag> ("DT4DSegmentsTag")),
  hcalNoiseFilterResultTag_ (iConfig.getUntrackedParameter<edm::InputTag> ("hcalNoiseFilterResultTag",edm::InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"))),
  jetTag_           (iConfig.getUntrackedParameter<edm::InputTag> ("jetTag",edm::InputTag("ak4CaloJets"))),
  rpcRecHitsTag_    (iConfig.getParameter<edm::InputTag> ("rpcRecHitsTag")),
  rbxTag_           (iConfig.getUntrackedParameter<edm::InputTag> ("rbxTag", edm::InputTag("hcalnoise"))),
  verticesTag_      (iConfig.getUntrackedParameter<edm::InputTag> ("verticesTag", edm::InputTag("offlinePrimaryVertices"))),

  jetMinEnergy_(iConfig.getUntrackedParameter<double>("jetMinEnergy", 1.)),
  jetMaxEta_(iConfig.getUntrackedParameter<double>("jetMaxEta", 3.)),
  towerMinEnergy_(iConfig.getUntrackedParameter<double>("towerMinEnergy", 1.)),
  towerMaxEta_(iConfig.getUntrackedParameter<double>("towerMaxEta", 1.3))
{
    produces<std::vector<CandidateCscHit> > ();
    produces<std::vector<CandidateCscSeg> > ();
    //produces<std::vector<CandidateEvent> > ();
    produces<std::vector<CandidateDTSeg> > ();
    produces<std::vector<CandidateJet> > ();
    produces<std::vector<CandidateRpcHit> > ();

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
    doCscHits(iEvent, iSetup);
    doCscSegments(iEvent, iSetup);
    doEvents(iEvent, iSetup);
    doMuonDTs(iEvent, iSetup);
    doMuonRPCs(iEvent, iSetup);
}


void StoppPtlsCandProducer::doCscHits(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<CSCRecHit2DCollection> hits;
  iEvent.getByLabel(cscRecHitsTag_, hits);
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


void StoppPtlsCandProducer::doCscSegments(edm::Event& iEvent, const edm::EventSetup& iSetup){
  // get the segments
  edm::Handle<CSCSegmentCollection> segments;
  iEvent.getByLabel(cscSegmentsTag_, segments);

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

void StoppPtlsCandProducer::doEvents(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  auto_ptr<vector<CandidateEvent> > events(new vector<CandidateEvent> ());
  
  CandidateEvent event;
  //cout<<iEvent.id().run()<<":" << iEvent.luminosityBlock() << ":" << iEvent.id().event() << endl;
  
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

void StoppPtlsCandProducer::doMuonDTs(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::ESHandle<DTGeometry> dtGeom;
  iSetup.get<MuonGeometryRecord>().get(dtGeom);

  edm::Handle<DTRecSegment4DCollection> all4DSegments;
  iEvent.getByLabel(DT4DSegmentsTag_, all4DSegments);
  edm::Handle<DTRecHitCollection> dtRecHits;
  iEvent.getByLabel(DTRecHitsTag_, dtRecHits);

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
      candDTs->push_back(candDTSeg);
    }//finish loop over all segments in chamber
  }//finish loop over all chambers
  // save the vector
  iEvent.put(candDTs);
}

void StoppPtlsCandProducer::doMuonRPCs(edm::Event& iEvent, const edm::EventSetup& iSetup){
  edm::Handle<RPCRecHitCollection> hits;
  iEvent.getByLabel(rpcRecHitsTag_, hits);
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
    
    candRpcHits->push_back(candRpcHit); 
  }//loop on rpc hits
  iEvent.put(candRpcHits);
}

void StoppPtlsCandProducer::pulseShapeVariables(const vector<double> &samples, unsigned &ipeak, double &total, double &r1, double &r2, double &rpeak, double &router){

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
  /*
  //  Dump diagnostic information
  LogDebug ("StoppedHSCPTreeProducer")  <<"--------------------";
  LogDebug ("StoppedHSCPTreeProducer")  <<"NOISE SUMMARY OUTPUT";
  for (uint i=0;i<samples.size();++i)
  LogDebug ("StoppedHSCPTreeProducer")  <<samples[i]<<"\t";
  LogDebug ("StoppedHSCPTreeProducer")  <<"total = "<<total<<"  foursample = "<<foursample;
  LogDebug ("StoppedHSCPTreeProducer")  <<"ipeak = "<<ipeak;
  if (ipeak<(int)HBHEDataFrame::MAXSAMPLES)
  LogDebug ("StoppedHSCPTreeProducer")  <<"Peak value = "<<samples.at(ipeak);
  else
  LogDebug ("StoppedHSCPTreeProducer")  <<"Peak value = N/A";
  LogDebug ("StoppedHSCPTreeProducer")  <<"R1 = "<<r1;
  LogDebug ("StoppedHSCPTreeProducer")  <<"R2 = "<<r2;
  LogDebug ("StoppedHSCPTreeProducer")  <<"Router = "<<router;
  LogDebug ("StoppedHSCPTreeProducer")  <<"Rpeak = "<<rpeak;
  */ 
} 
//define this as a plug-in
DEFINE_FWK_MODULE(StoppPtlsCandProducer);

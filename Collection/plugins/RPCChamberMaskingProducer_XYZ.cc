#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "StoppPtls/Collection/plugins/RPCChamberMaskingProducer_XYZ.h"

#include <iostream>
#include <fstream>

RPCChamberMaskingProducer_XYZ::RPCChamberMaskingProducer_XYZ(const edm::ParameterSet &cfg) :
  rpcMaskingCoordinatesFile_ (cfg.getParameter<string>("rpcMaskingCoordinatesFile")),
  candidateRpcHitsTag_ (cfg.getParameter<edm::InputTag>("candidateRpcHitsTag"))
{

  produces<std::vector<CandidateRpcHit> > ();

  token_ = consumes<vector<CandidateRpcHit> > (candidateRpcHitsTag_);

  clog<<"inFile is: "<<rpcMaskingCoordinatesFile_.c_str()<<endl;
  ifstream inFile;
  inFile.open(rpcMaskingCoordinatesFile_.c_str());
  double x_1(0.), x_2(0.), y_1(0.), y_2(0.), z_1(0.), z_2(0.);
  nChambersToMask = 0;

  if (!inFile || !inFile.good()) {
    clog << "ERROR [RPCChamberMaskingProducer_XYZ]: Could not find file: " << rpcMaskingCoordinatesFile_
	 << "; will cause a seg fault." << endl;
    exit(1);
  }
  else{
    while (inFile >> x_1 >> x_2 >> y_1 >> y_2 >> z_1 >> z_2){
      x1.push_back(x_1);
      x2.push_back(x_2);
      y1.push_back(y_1);
      y2.push_back(y_2);
      z1.push_back(z_1);
      z2.push_back(z_2);
      nChambersToMask++;
    }//end of while loop
  }//end of if inFile good

  clog<<"There are "<<nChambersToMask<<" lines in the text file (and that many chambers to mask)"<<endl;
  inFile.close();
}

RPCChamberMaskingProducer_XYZ::~RPCChamberMaskingProducer_XYZ() {}

bool RPCChamberMaskingProducer_XYZ::isNotMaskedRpcHit(double rpcHitX, double rpcHitY, double rpcHitZ){
  //loop over r1's and r2's, phi1's, phi2's, and z1's, z2's from input text file, see if rpc hit r, phi, z is within the masking regions

  bool notMasked = true;
  for(int i=0; i<nChambersToMask; i++){
    if(rpcHitX>=x1.at(i) && rpcHitX<x2.at(i) && rpcHitY>=y1.at(i) && rpcHitY<y2.at(i) && rpcHitZ>=z1.at(i) && rpcHitZ<=z2.at(i)){
      //clog<<"rpc hit ("<<rpcHitR<<", "<<rpcHitPhi<<", "<<rpcHitZ<<") will be masked because it is in the range: "<<r1.at(i)<<" to "<<r2.at(i)<<", "<<phi1.at(i)<<" to "<<phi2.at(i)<<", "<<z1.at(i)<<" to "<<z2.at(i)<<endl;
      notMasked = false;
      break;
    }
    else{
      //clog<<"rpc hit ("<<rpcHitR<<", "<<rpcHitPhi<<", "<<rpcHitZ<<") is not masked"<<endl;
    }
  }

  return notMasked;
}//end of isNotMaskedRpcHit

void RPCChamberMaskingProducer_XYZ::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) {
  //get original collection of rpc hits
  edm::Handle<vector<CandidateRpcHit> > rpchits;
  // edm::EDGetTokenT<vector<CandidateRpcHit> > token_ = consumes<vector<CandidateRpcHit> > (candidateRpcHitsTag_);
//iEvent.getByLabel(candidateRpcHitsTag_, rpchits);
  iEvent.getByToken(token_, rpchits);

  auto_ptr<vector<CandidateRpcHit> > candNotMaskedRpcHits(new vector<CandidateRpcHit> ());

  //clog<<"beginning to loop over rpc hits for run "<<iEvent.id().run()<<" and event "<<iEvent.id().event()<<endl;
  for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
    if(isNotMaskedRpcHit((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z())) {

      //make new candidate rpc hit collection containing only unmasked rpc hits
      CandidateRpcHit candNotMaskedRpcHit;
      candNotMaskedRpcHit.set_x((rpchits->at(i)).x());
      candNotMaskedRpcHit.set_y((rpchits->at(i)).y());
      candNotMaskedRpcHit.set_r((rpchits->at(i)).r());
      candNotMaskedRpcHit.set_z((rpchits->at(i)).z());
      candNotMaskedRpcHit.set_rho((rpchits->at(i)).rho());
      candNotMaskedRpcHit.set_phi((rpchits->at(i)).phi());
      candNotMaskedRpcHit.set_region((rpchits->at(i)).region());
      candNotMaskedRpcHit.set_bx((rpchits->at(i)).bx());
    
      candNotMaskedRpcHits->push_back(candNotMaskedRpcHit); 
    }//end of if isNotMaskedRpchit
  }//end of loop over rpc hits
  iEvent.put(candNotMaskedRpcHits);

}  //end of produce

DEFINE_FWK_MODULE(RPCChamberMaskingProducer_XYZ);

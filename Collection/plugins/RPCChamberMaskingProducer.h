#ifndef RPCCHAMBERMASKING_PRODUCER
#define RPCCHAMBERMASKING_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
//#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"

#include "DataFormats/Math/interface/deltaR.h"
#include <string>
#include "TFile.h"

class RPCChamberMaskingProducer : public edm::EDProducer{
 public:
  RPCChamberMaskingProducer (const edm::ParameterSet &);
  ~RPCChamberMaskingProducer ();
  
 private:
  int nChambersToMask;
  std::vector<double> r1;
  std::vector<double> r2;
  std::vector<double> phi1;
  std::vector<double> phi2;
  std::vector<double> z1;
  std::vector<double> z2;

  void produce(edm::Event&, const edm::EventSetup&);

  string rpcMaskingCoordinatesFile_;
  edm::InputTag candidateRpcHitsTag_;
  bool isNotMaskedRpcHit(double rpcHitR, double rpcHitPhi, double rpcHitZ);
};
#endif

#ifndef RPCCHAMBERMASKINGXYZ_PRODUCER
#define RPCCHAMBERMASKINGXYZ_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
//#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"

#include "DataFormats/Math/interface/deltaR.h"
#include <string>
#include "TFile.h"

class RPCChamberMaskingProducer_XYZ : public edm::EDProducer{
 public:
  RPCChamberMaskingProducer_XYZ (const edm::ParameterSet &);
  ~RPCChamberMaskingProducer_XYZ ();
  
 private:
  int nChambersToMask;
  std::vector<double> x1;
  std::vector<double> x2;
  std::vector<double> y1;
  std::vector<double> y2;
  std::vector<double> z1;
  std::vector<double> z2;

  void produce(edm::Event&, const edm::EventSetup&);

  string rpcMaskingCoordinatesFile_;
  edm::InputTag candidateRpcHitsTag_;
  bool isNotMaskedRpcHit(double rpcHitX, double rpcHitY, double rpcHitZ);

  edm::EDGetTokenT<vector<CandidateRpcHit> > token_;
};
#endif

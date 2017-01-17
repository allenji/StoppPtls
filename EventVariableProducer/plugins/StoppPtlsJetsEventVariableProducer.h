#ifndef STOPPPTLSJETSEVENTVARIABLEPRODUCER_H
#define STOPPPTLSJETSEVENTVARIABLEPRODUCER_H

#include "TFile.h"
#include "TH1.h"
#include <math.h>

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

#include "StoppPtls/Collection/interface/CandidateJet.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"

using namespace std;

class StoppPtlsJetsEventVariableProducer : public EventVariableProducer
{
 public:
  StoppPtlsJetsEventVariableProducer (const edm::ParameterSet &);
  ~StoppPtlsJetsEventVariableProducer ();
  
 private:
  void AddVariables(const edm::Event &);
  int chamberType(int, int);


  edm::EDGetTokenT<vector<TYPE(jets)> > jetsToken_;
  edm::EDGetTokenT<vector<TYPE(dtsegs)> > dtsegsToken_;
  edm::EDGetTokenT<vector<TYPE(cscsegs)> > cscsegsToken_;
  edm::EDGetTokenT<vector<TYPE(rpchits)> > rpchitsToken_;

};


#endif

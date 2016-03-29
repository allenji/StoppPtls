#ifndef STOPPPTLSEVENTVARIABLEPRODUCER_H
#define STOPPPTLSEVENTVARIABLEPRODUCER_H

#include "TFile.h"
#include "TH1.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

using namespace std;

class StoppPtlsEventVariableProducer : public EventVariableProducer
{
 public:
  StoppPtlsEventVariableProducer (const edm::ParameterSet &);
  ~StoppPtlsEventVariableProducer ();
  
 private:
  void AddVariables(const edm::Event &);
  int chamberType(int, int);

  string livetimeRootFile_;
  TFile* file;

  TH1D* run_livetime_hist;
  TH1D* fill_livetime_hist;


};


#endif

#ifndef GetLivetime_h
#define GetLivetime_h

#include <memory>
#include <iostream>
#include <fstream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "StoppPtls/Livetime/interface/Livetime.h"
#include "StoppPtls/Livetime/interface/Constants.h"
#include "StoppPtls/Livetime/interface/LhcFills.h"

using namespace std;

class GetLivetime : public edm::EDAnalyzer {
  
 public:
  explicit GetLivetime(const edm::ParameterSet& iConfig);
  ~GetLivetime();
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

 private:
  virtual void analyze (const edm::Event& iEvent, const edm::EventSetup& iSetup) override;
  virtual void endJob() override;

  LhcFills lhcFills_;
  Livetime livetime_;   
  unsigned nEvents_;

  edm::Service<TFileService> fs_;
  TH1D* run_livetime_hist;
  TH1D* fill_livetime_hist;
};
#endif

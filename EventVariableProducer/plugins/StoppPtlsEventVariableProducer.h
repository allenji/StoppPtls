#ifndef STOPPPTLSEVENTVARIABLEPRODUCER_H
#define STOPPPTLSEVENTVARIABLEPRODUCER_H

#include "TFile.h"
#include "TH1.h"
#include "TLorentzVector.h"

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
  double Eta(double, double, double, double);

  string livetimeRootFile_;
  TFile* file;

  TH1D* run_livetime_hist;
  TH1D* fill_livetime_hist;

  edm::EDGetTokenT<vector<TYPE(events)> > eventsToken_;
  edm::EDGetTokenT<vector<TYPE(mcparticles)> > mcparticlesToken_;

  edm::InputTag stoppedParticlesNameTag_;
  edm::EDGetTokenT<std::vector<std::string> > stoppedParticlesNameToken_;
  edm::InputTag stoppedParticlesXTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesXToken_;
  edm::InputTag stoppedParticlesYTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesYToken_;
  edm::InputTag stoppedParticlesZTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesZToken_;
  edm::InputTag stoppedParticlesTimeTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesTimeToken_;
  edm::InputTag stoppedParticlesPdgIdTag_;
  edm::EDGetTokenT<std::vector<int> > stoppedParticlesPdgIdToken_;
  edm::InputTag stoppedParticlesMassTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesMassToken_;
  edm::InputTag stoppedParticlesChargeTag_;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesChargeToken_;

};


#endif

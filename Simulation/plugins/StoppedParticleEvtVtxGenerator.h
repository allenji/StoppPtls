#include "IOMC/EventVertexGenerators/interface/BaseEvtVtxGenerator.h"
#include <fstream>

namespace CLHEP {
  class HepRandomEngine;
}


class StoppedParticleEvtVtxGenerator : public BaseEvtVtxGenerator 
{
public:
  StoppedParticleEvtVtxGenerator(const edm::ParameterSet & p);
  virtual ~StoppedParticleEvtVtxGenerator();

  virtual void produce( edm::Event& iEvent, const edm::EventSetup& iSetup);

  void getStoppingPoint(edm::Event& iEvent); 

  /// return a new event vertex
  virtual HepMC::FourVector newVertex(CLHEP::HepRandomEngine*) const override;
  
  virtual TMatrixD* GetInvLorentzBoost() const override {
    return 0;
  }
private:

  bool verbose;

  edm::EDGetTokenT<edm::HepMCProduct> sourceToken;

  // input
  bool readFromFile;
  std::string fileName;
  std::ifstream* file;
  //std::string stopPointProducer;
  edm::EDGetTokenT<std::vector<std::string> > stoppedParticlesName;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesX;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesY;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesZ;
  edm::EDGetTokenT<std::vector<float> > stoppedParticlesTime;
  edm::EDGetTokenT<std::vector<int> > stoppedParticlesPdgId;

  // time smearing
  double timeMin;
  double timeMax;

  bool putTwoStoppedInSameEvent;
  int stoppedParticleNumber;
  int nStoppedParticles;
  bool isStoppedEvent;

  // stopped particle vertex
  std::vector<float> vx_;
  std::vector<float> vy_;
  std::vector<float> vz_;
  std::vector<float> vt_;
  std::vector<int> ids_;

  float vx;
  float vy;
  float vz;
  float vt;
  int id;

};

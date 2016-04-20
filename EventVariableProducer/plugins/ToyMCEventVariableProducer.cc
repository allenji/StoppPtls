#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/ToyMCEventVariableProducer.h"

ToyMCEventVariableProducer::ToyMCEventVariableProducer(const edm::ParameterSet &cfg) :
      EventVariableProducer(cfg)
{
}

ToyMCEventVariableProducer::~ToyMCEventVariableProducer()
{
}

void 
ToyMCEventVariableProducer::AddVariables(const edm::Event & event) {
  (*eventvariables)["run"] = event.id().run();
  (*eventvariables)["lb"] = event.luminosityBlock();


}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ToyMCEventVariableProducer);

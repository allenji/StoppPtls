#ifndef STOPPPTLSEVENTVARIABLEPRODUCERTOYMC_H
#define STOPPPTLSEVENTVARIABLEPRODUCERTOYMC_H

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

class ToyMCEventVariableProducer : public EventVariableProducer
{
  public:
    ToyMCEventVariableProducer (const edm::ParameterSet &);
    ~ToyMCEventVariableProducer ();

  private:
    void AddVariables(const edm::Event &);
};


#endif


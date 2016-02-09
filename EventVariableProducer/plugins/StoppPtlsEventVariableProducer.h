#ifndef STOPPPTLSEVENTVARIABLEPRODUCER_H
#define STOPPPTLSEVENTVARIABLEPRODUCER_H

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

class StoppPtlsEventVariableProducer : public EventVariableProducer
{
  public:
    StoppPtlsEventVariableProducer (const edm::ParameterSet &);
    ~StoppPtlsEventVariableProducer ();

  private:
    void AddVariables(const edm::Event &);
    int chamberType(int, int);
};


#endif

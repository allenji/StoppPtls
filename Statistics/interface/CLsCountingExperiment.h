#ifndef CLsCountingExperiment_h
#define CLsCountingExperiment_h

#include "StoppPtls/Statistics/interface/CountingExperiment.h"

class CLsCountingExperiment : public CountingExperiment {
 public:
  CLsCountingExperiment (double fBackground, double fBackgroundSigma, double fBackgroundN, double fBackgroundAlpha, double fScale, double fScaleSigma);
  virtual ~CLsCountingExperiment();
  virtual double cl95limit (int nObserved, bool fPlot = false);
  virtual CountingExperiment* clone(double fBackground, double fBackgroundSigma, double fBackgroundN, double fBackgroundAlpha,  double fScale, double fScaleSigma) const;
  
 private:

};

#endif

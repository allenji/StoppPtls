#ifndef CountingExperiment_h
#define CountingExperiment_h

#include <vector>

class TH1D;

class CountingExperiment {
 public:
  CountingExperiment (double fBackground, double fBackgroundSigma, double fBackgroundN, double fBackgroundAlpha, double fScale, double fScaleSigma);
  virtual ~CountingExperiment ();
  double background () const {return mBackground;}
  double backgroundSigma () const {return mBackgroundSigma;}
  double backgroundN () const {return mBackgroundN;}
  double backgroundAlpha () const {return mBackgroundAlpha;}
  double scale () const {return mScale;}
  double scaleSigma () const {return mScaleSigma;}

  virtual double cl95limit (int nObserved, bool fPlot = false) = 0;
  std::vector<double>  cl95ExpectedLimit ();
  double coverage (double fTrueSignal, double fPrecision = 0.2);
  TH1D* plotCoverage (const char* fId, int fBins, double fMinSignal, double fMaxSignal, bool fShowProgress = true);
  virtual CountingExperiment* clone(double fBackground, double fBackgroundSigma, double fBackgroundN, double fBackgroundAlpha, double fScale, double fScaleSigma) const = 0;
 private:
  double mBackground;
  double mBackgroundSigma;
  double mBackgroundN;
  double mBackgroundAlpha;
  double mScale;
  double mScaleSigma;
};
#endif

#ifndef CANDIDATEDELAYEDMUONSTRACK_H
#define CANDIDATEDELAYEDMUONSTRACK_H

#include <vector>

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/MuonReco/interface/Muon.h"

using namespace std;

class CandidateDelayedMuonsTrack : public reco::Track{
 public:
  CandidateDelayedMuonsTrack ();
  CandidateDelayedMuonsTrack (const reco::Track &);
  //CandidateDelayedMuonsTrack (const reco::Track &, const vector<reco::Track> &, const vector<reco::Muon> &);
  ~CandidateDelayedMuonsTrack ();

  const int nStationsWithAnyHits() const;
  const int nCscChambersWithAnyHits() const;
  const int nDtChambersWithAnyHits() const;
  const int nRpcChambersWithAnyHits() const;
  const int innermostStationWithAnyHits() const;
  const int outermostStationWithAnyHits() const;
  const int nStationsWithValidHits() const;
  const int nCscChambersWithValidHits() const;
  const int nDtChambersWithValidHits() const;
  const int nRpcChambersWithValidHits() const;
  const int nValidMuonHits() const;
  const int nValidCscHits() const;
  const int nValidDtHits() const;
  const int nValidRpcHits() const;
  const int innermostStationWithValidHits() const;
  const int outermostStationWithValidHits() const;
  const int quality() const;
  const double innerPx() const;
  const double innerPy() const;
  const double innerPz() const;
  const bool innerOk() const;
  const double innerX() const;
  const double innerY() const;
  const double innerZ() const;
  const vector<double> rpcHitZ() const;
  const vector<double> rpcHitRho() const;
  const vector<double> rpcHitPhi() const;
  const vector<int> rpcHitRegion() const;
  const vector<int> rpcHitBx() const;
  const int dtTofDirection() const;
  const int dtTofNDof() const;
  const double dtTofInverseBeta() const;
  const double dtTofInverseBetaErr() const;
  const double dtTofFreeInverseBeta() const;
  const double dtTofFreeInverseBetaErr() const;
  const double dtTofTimeAtIpInOut() const;
  const double dtTofTimeAtIpInOutErr() const;
  const double dtTofTimeAtIpOutIn() const;
  const double dtTofTimeAtIpOutInErr() const;

  void set_nStationsWithAnyHits(int value) {nStationsWithAnyHits_ = value;} 
  void set_nCscChambersWithAnyHits(int value) {nCscChambersWithAnyHits_ = value;}
  void set_nDtChambersWithAnyHits(int value) {nDtChambersWithAnyHits_ = value;} 
  void set_nRpcChambersWithAnyHits(int value) {nRpcChambersWithAnyHits_ = value;} 
  void set_innermostStationWithAnyHits(int value) {innermostStationWithAnyHits_ = value;}
  void set_outermostStationWithAnyHits(int value) {outermostStationWithAnyHits_ = value;}  
  void set_nStationsWithValidHits(int value) {nStationsWithValidHits_ = value;} 
  void set_nCscChambersWithValidHits(int value) {nCscChambersWithValidHits_ = value;} 
  void set_nDtChambersWithValidHits(int value) {nDtChambersWithValidHits_ = value;} 
  void set_nRpcChambersWithValidHits(int value) {nRpcChambersWithValidHits_ = value;}
  void set_nValidMuonHits(int value) {nValidMuonHits_ = value;} 
  void set_nValidCscHits(int value) {nValidCscHits_ = value;}
  void set_nValidDtHits(int value) {nValidDtHits_ = value;} 
  void set_nValidRpcHits(int value) {nValidRpcHits_ = value;}
  void set_innermostStationWithValidHits(int value) {innermostStationWithValidHits_ = value;}
  void set_outermostStationWithValidHits(int value) {outermostStationWithValidHits_ = value;}
  void set_quality(int value) {quality_ = value;}
  void set_innerPx(double value) {innerPx_ = value;}
  void set_innerPy(double value) {innerPy_ = value;}
  void set_innerPz(double value) {innerPz_ = value;}
  void set_innerOk(bool value) {innerOk_ = value;}
  void set_innerX(double value) {innerX_ = value;}
  void set_innerY(double value) {innerY_ = value;}
  void set_innerZ(double value) {innerZ_ = value;}
  void set_rpcHitZ(vector<double> value) {rpcHitZ_ = value;}
  void set_rpcHitRho(vector<double> value) {rpcHitRho_ = value;}
  void set_rpcHitPhi(vector<double> value) {rpcHitPhi_ = value;}
  void set_rpcHitRegion(vector<int> value) {rpcHitRegion_ = value;}
  void set_rpcHitBx(vector<int> value) {rpcHitBx_ = value;}
  void set_dtTofDirection(int value) {dtTofDirection_ = value;}
  void set_dtTofNDof(int value) {dtTofNDof_ = value;}
  void set_dtTofInverseBeta(double value) {dtTofInverseBeta_ = value;}
  void set_dtTofInverseBetaErr(double value) {dtTofInverseBetaErr_ = value;}
  void set_dtTofFreeInverseBeta(double value) {dtTofFreeInverseBeta_ = value;}
  void set_dtTofFreeInverseBetaErr(double value) {dtTofFreeInverseBetaErr_ = value;}
  void set_dtTofTimeAtIpInOut(double value) {dtTofTimeAtIpInOut_ = value;}
  void set_dtTofTimeAtIpInOutErr(double value) {dtTofTimeAtIpInOutErr_ = value;}
  void set_dtTofTimeAtIpOutIn(double value) {dtTofTimeAtIpOutIn_ = value;}
  void set_dtTofTimeAtIpOutInErr(double value) {dtTofTimeAtIpOutInErr_ = value;}

 private:
  int nStationsWithAnyHits_;
  int nCscChambersWithAnyHits_;
  int nDtChambersWithAnyHits_;
  int nRpcChambersWithAnyHits_;
  int innermostStationWithAnyHits_;
  int outermostStationWithAnyHits_;
  int nStationsWithValidHits_;
  int nCscChambersWithValidHits_;
  int nDtChambersWithValidHits_;
  int nRpcChambersWithValidHits_;
  int nValidMuonHits_;
  int nValidCscHits_;
  int nValidDtHits_;
  int nValidRpcHits_;
  int innermostStationWithValidHits_;
  int outermostStationWithValidHits_;
  int quality_;
  double innerPx_;
  double innerPy_;
  double innerPz_;
  bool innerOk_;
  double innerX_;
  double innerY_;
  double innerZ_;
  vector<double> rpcHitZ_;
  vector<double> rpcHitRho_;
  vector<double> rpcHitPhi_;
  vector<int> rpcHitRegion_;
  vector<int> rpcHitBx_;
  int dtTofDirection_;
  int dtTofNDof_;
  double dtTofInverseBeta_;
  double dtTofInverseBetaErr_;
  double dtTofFreeInverseBeta_;
  double dtTofFreeInverseBetaErr_;
  double dtTofTimeAtIpInOut_;
  double dtTofTimeAtIpInOutErr_;
  double dtTofTimeAtIpOutIn_;
  double dtTofTimeAtIpOutInErr_;
};


#endif

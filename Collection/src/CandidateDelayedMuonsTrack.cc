#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "StoppPtls/Collection/interface/CandidateDelayedMuonsTrack.h"

//#define INVALID_VALUE (numeric_limits<int>::min ())
//#define IS_INVALID(x) (x <= INVALID_VALUE + 1)

CandidateDelayedMuonsTrack::CandidateDelayedMuonsTrack () :
  nStationsWithAnyHits_(INVALID_VALUE),
  nCscChambersWithAnyHits_(INVALID_VALUE),
  nDtChambersWithAnyHits_(INVALID_VALUE),
  nRpcChambersWithAnyHits_(INVALID_VALUE),
  innermostStationWithAnyHits_(INVALID_VALUE),
  outermostStationWithAnyHits_(INVALID_VALUE),
  nStationsWithValidHits_(INVALID_VALUE),
  nCscChambersWithValidHits_(INVALID_VALUE),
  nDtChambersWithValidHits_(INVALID_VALUE),
  nRpcChambersWithValidHits_(INVALID_VALUE),
  nValidMuonHits_(INVALID_VALUE),
  nValidCscHits_(INVALID_VALUE),
  nValidDtHits_(INVALID_VALUE),
  nValidRpcHits_(INVALID_VALUE),
  innermostStationWithValidHits_(INVALID_VALUE),
  outermostStationWithValidHits_(INVALID_VALUE),
  quality_(INVALID_VALUE),
  innerPx_(INVALID_VALUE),
  innerPy_(INVALID_VALUE),
  innerPz_(INVALID_VALUE),
  innerOk_(INVALID_VALUE),
  innerX_(INVALID_VALUE),
  innerY_(INVALID_VALUE),
  innerZ_(INVALID_VALUE) ,
  rpcHitZ_(0),
  rpcHitRho_(0),
  rpcHitPhi_(0),
  rpcHitRegion_(0),
  rpcHitBx_(0),
  dtTofDirection_(-999),
  dtTofNDof_(-999),
  dtTofInverseBeta_(-999),
  dtTofInverseBetaErr_(-999),
  dtTofFreeInverseBeta_(-999),
  dtTofFreeInverseBetaErr_(-999),
  dtTofTimeAtIpInOut_(-999),
  dtTofTimeAtIpInOutErr_(-999),
  dtTofTimeAtIpOutIn_(-999),
  dtTofTimeAtIpOutInErr_(-999)
{
}

CandidateDelayedMuonsTrack::CandidateDelayedMuonsTrack (const reco::Track &track) :
  reco::Track (track),
  nStationsWithAnyHits_(INVALID_VALUE),
  nCscChambersWithAnyHits_(INVALID_VALUE),
  nDtChambersWithAnyHits_(INVALID_VALUE),
  nRpcChambersWithAnyHits_(INVALID_VALUE),
  innermostStationWithAnyHits_(INVALID_VALUE),
  outermostStationWithAnyHits_(INVALID_VALUE),
  nStationsWithValidHits_(INVALID_VALUE),
  nCscChambersWithValidHits_(INVALID_VALUE),
  nDtChambersWithValidHits_(INVALID_VALUE),
  nRpcChambersWithValidHits_(INVALID_VALUE),
  nValidMuonHits_(INVALID_VALUE),
  nValidCscHits_(INVALID_VALUE),
  nValidDtHits_(INVALID_VALUE),
  nValidRpcHits_(INVALID_VALUE),
  innermostStationWithValidHits_(INVALID_VALUE),
  outermostStationWithValidHits_(INVALID_VALUE),
  quality_(INVALID_VALUE),
  innerPx_(INVALID_VALUE),
  innerPy_(INVALID_VALUE),
  innerPz_(INVALID_VALUE),
  innerOk_(INVALID_VALUE),
  innerX_(INVALID_VALUE),
  innerY_(INVALID_VALUE),
  innerZ_(INVALID_VALUE),
  rpcHitZ_(0),
  rpcHitRho_(0),
  rpcHitPhi_(0),
  rpcHitRegion_(0),
  rpcHitBx_(0),
  dtTofDirection_(-999),
  dtTofNDof_(-999),
  dtTofInverseBeta_(-999),
  dtTofInverseBetaErr_(-999),
  dtTofFreeInverseBeta_(-999),
  dtTofFreeInverseBetaErr_(-999),
  dtTofTimeAtIpInOut_(-999),
  dtTofTimeAtIpInOutErr_(-999),
  dtTofTimeAtIpOutIn_(-999),
  dtTofTimeAtIpOutInErr_(-999)
{
}

CandidateDelayedMuonsTrack::~CandidateDelayedMuonsTrack ()
{
}


const int CandidateDelayedMuonsTrack::nStationsWithAnyHits() const
{
  return this->nStationsWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::nCscChambersWithAnyHits() const
{
  return this->nCscChambersWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::nDtChambersWithAnyHits() const
{
  return this->nDtChambersWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::nRpcChambersWithAnyHits() const
{
  return this->nRpcChambersWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::innermostStationWithAnyHits() const
{
  return this->innermostStationWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::outermostStationWithAnyHits() const
{
  return this->outermostStationWithAnyHits_;
}

const int CandidateDelayedMuonsTrack::nStationsWithValidHits() const
{
  return this->nStationsWithValidHits_;
}

const int CandidateDelayedMuonsTrack::nCscChambersWithValidHits() const
{
  return this->nCscChambersWithValidHits_;
}

const int CandidateDelayedMuonsTrack::nDtChambersWithValidHits() const
{
  return this->nDtChambersWithValidHits_;
}

const int CandidateDelayedMuonsTrack::nRpcChambersWithValidHits() const
{
  return this->nRpcChambersWithValidHits_;
}

const int CandidateDelayedMuonsTrack::nValidMuonHits() const
{
  return this->nValidMuonHits_;
}

const int CandidateDelayedMuonsTrack::nValidCscHits() const
{
  return this->nValidCscHits_;
}

const int CandidateDelayedMuonsTrack::nValidDtHits() const
{
  return this->nValidDtHits_;
}

const int CandidateDelayedMuonsTrack::nValidRpcHits() const
{
  return this->nValidRpcHits_;
}

const int CandidateDelayedMuonsTrack::innermostStationWithValidHits() const
{
  return this->innermostStationWithValidHits_;
}

const int CandidateDelayedMuonsTrack::outermostStationWithValidHits() const
{
  return this->outermostStationWithValidHits_;
}

const int CandidateDelayedMuonsTrack::quality() const
{
  return this->quality_;
}

const double CandidateDelayedMuonsTrack::innerPx() const
{
  return this->innerPx_;
}

const double CandidateDelayedMuonsTrack::innerPy() const
{
  return this->innerPy_;
}

const double CandidateDelayedMuonsTrack::innerPz() const
{
  return this->innerPz_;
}

const bool CandidateDelayedMuonsTrack::innerOk() const
{
  return this->innerOk_;
}

const double CandidateDelayedMuonsTrack::innerX() const
{
  return this->innerX_;
}

const double CandidateDelayedMuonsTrack::innerY() const
{
  return this->innerY_;
}

const double CandidateDelayedMuonsTrack::innerZ() const
{
  return this->innerZ_;
}

const vector<double> CandidateDelayedMuonsTrack::rpcHitZ() const
{
  return this->rpcHitZ_;
}

const vector<double> CandidateDelayedMuonsTrack::rpcHitRho() const
{
  return this->rpcHitRho_;
}

const vector<double> CandidateDelayedMuonsTrack::rpcHitPhi() const
{
  return this->rpcHitPhi_;
}

const vector<int> CandidateDelayedMuonsTrack::rpcHitRegion() const
{
  return this->rpcHitRegion_;
}

const vector<int> CandidateDelayedMuonsTrack::rpcHitBx() const
{
  return this->rpcHitBx_;
}

const int CandidateDelayedMuonsTrack::dtTofDirection() const
{
  return this->dtTofDirection_;
}

const int CandidateDelayedMuonsTrack::dtTofNDof() const
{
  return this->dtTofNDof_;
}

const double CandidateDelayedMuonsTrack::dtTofInverseBeta() const
{
  return this->dtTofInverseBeta_;
}

const double CandidateDelayedMuonsTrack::dtTofInverseBetaErr() const
{
  return this->dtTofInverseBetaErr_;
}

const double CandidateDelayedMuonsTrack::dtTofFreeInverseBeta() const
{
  return this->dtTofFreeInverseBeta_;
}

const double CandidateDelayedMuonsTrack::dtTofFreeInverseBetaErr() const
{
  return this->dtTofFreeInverseBetaErr_;
}

const double CandidateDelayedMuonsTrack::dtTofTimeAtIpInOut() const
{
  return this->dtTofTimeAtIpInOut_;
}

const double CandidateDelayedMuonsTrack::dtTofTimeAtIpInOutErr() const
{
  return this->dtTofTimeAtIpInOutErr_;
}

const double CandidateDelayedMuonsTrack::dtTofTimeAtIpOutIn() const
{
  return this->dtTofTimeAtIpOutIn_;
}

const double CandidateDelayedMuonsTrack::dtTofTimeAtIpOutInErr() const
{
  return this->dtTofTimeAtIpOutInErr_;
}

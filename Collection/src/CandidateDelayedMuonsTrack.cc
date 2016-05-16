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
  dtTofDirection_(INVALID_VALUE),
  dtTofNDof_(INVALID_VALUE),
  dtTofInverseBeta_(INVALID_VALUE),
  dtTofInverseBetaErr_(INVALID_VALUE),
  dtTofFreeInverseBeta_(INVALID_VALUE),
  dtTofFreeInverseBetaErr_(INVALID_VALUE),
  dtTofTimeAtIpInOut_(INVALID_VALUE),
  dtTofTimeAtIpInOutErr_(INVALID_VALUE),
  dtTofTimeAtIpOutIn_(INVALID_VALUE),
  dtTofTimeAtIpOutInErr_(INVALID_VALUE)
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
  dtTofDirection_(INVALID_VALUE),
  dtTofNDof_(INVALID_VALUE),
  dtTofInverseBeta_(INVALID_VALUE),
  dtTofInverseBetaErr_(INVALID_VALUE),
  dtTofFreeInverseBeta_(INVALID_VALUE),
  dtTofFreeInverseBetaErr_(INVALID_VALUE),
  dtTofTimeAtIpInOut_(INVALID_VALUE),
  dtTofTimeAtIpInOutErr_(INVALID_VALUE),
  dtTofTimeAtIpOutIn_(INVALID_VALUE),
  dtTofTimeAtIpOutInErr_(INVALID_VALUE)
{
}

CandidateDelayedMuonsTrack::~CandidateDelayedMuonsTrack ()
{
}

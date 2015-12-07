#include "StoppPtls/Collection/interface/CandidateJet.h"
CandidateJet::CandidateJet()
{
}

CandidateJet::CandidateJet(const reco::CaloJet &calojet):
  reco::CaloJet (calojet)
{
}

CandidateJet::~CandidateJet()
{
}

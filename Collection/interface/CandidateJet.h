#ifndef CANDIDATEJET_H 
#define CANDIDATEJET_H 
#include "DataFormats/JetReco/interface/CaloJet.h" 
class CandidateJet : public reco::CaloJet {
  public:
    CandidateJet();
    CandidateJet(const reco::CaloJet &);
    ~CandidateJet();
};

#endif



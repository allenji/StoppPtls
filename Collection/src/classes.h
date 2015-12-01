#include <vector>
#include "DataFormats/Common/interface/Wrapper.h"
#include "StoppPtls/Collection/interface/CandidateCscHit.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"


namespace {
  struct StoppPtls_CandidateDTProducer {
    CandidateCscHit                       candidateCscHit0;
    std::vector<CandidateCscHit>               candidateCscHit1;
    edm::Wrapper<CandidateCscHit>         candidateCscHit2;
    edm::Wrapper<std::vector<CandidateCscHit> > candidateCscHit3;

    CandidateCscSeg                       candidateCscSeg0;
    std::vector<CandidateCscSeg>               candidateCscSeg1;
    edm::Wrapper<CandidateCscSeg>         candidateCscSeg2;
    edm::Wrapper<std::vector<CandidateCscSeg> > candidateCscSeg3;

    CandidateDTSeg                       candidateDTSeg0;
    std::vector<CandidateDTSeg>               candidateDTSeg1;
    edm::Wrapper<CandidateDTSeg>         candidateDTSeg2;
    edm::Wrapper<std::vector<CandidateDTSeg> > candidateDTSeg3;

    CandidateRpcHit                       candidateRpcHit0;
    std::vector<CandidateRpcHit>               candidateRpcHit1;
    edm::Wrapper<CandidateRpcHit>         candidateRpcHit2;
    edm::Wrapper<std::vector<CandidateRpcHit> > candidateRpcHit3;
  };
}

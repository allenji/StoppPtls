//Based on AOD data format specified in OSUT3Analysis/AnaTools/interface/DataFormatAOD.h
//Add definition/include for jet collection


#ifndef CUSTOM_DATA_FORMAT

  #include "OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h"

  #undef jets_TYPE

  #define jets_TYPE CandidateJet
  #undef events_TYPE
  #define events_TYPE CandidateEvent

  #undef events_INVALID
  
  #define cschits_TYPE CandidateCscHit
  #define cscsegs_TYPE CandidateCscSeg
  #define dtsegs_TYPE CandidateDTSeg
  #define rpchits_TYPE CandidateRpcHit

  #include "DataFormats/JetReco/interface/CaloJet.h"
  #include "StoppPtls/Collection/interface/CandidateCscHit.h"
  #include "StoppPtls/Collection/interface/CandidateCscSeg.h"
  #include "StoppPtls/Collection/interface/CandidateDTSeg.h"
  #include "StoppPtls/Collection/interface/CandidateEvent.h"
  #include "StoppPtls/Collection/interface/CandidateJet.h"
  #include "StoppPtls/Collection/interface/CandidateRpcHit.h"
#endif

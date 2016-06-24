//Based on AOD data format specified in OSUT3Analysis/AnaTools/interface/DataFormatAOD.h
//Add definition/include for jet collection


#ifndef CUSTOM_DATA_FORMAT

#include "OSUT3Analysis/AnaTools/interface/DataFormatAOD.h"

#undef jets_TYPE
#define jets_TYPE CandidateJet
#undef jets_INVALID

#undef events_TYPE
#define events_TYPE CandidateEvent
#undef events_INVALID

#undef cschits_TYPE
#undef cscsegs_TYPE
#undef dtsegs_TYPE
#undef rpchits_TYPE

#define cschits_TYPE CandidateCscHit
#define cscsegs_TYPE CandidateCscSeg
#define dtsegs_TYPE CandidateDTSeg
#define rpchits_TYPE CandidateRpcHit

#undef cschits_INVALID
#undef cscsegs_INVALID
#undef dtsegs_INVALID
#undef rpchits_INVALID

// Redefining to avoid editing the objectProducer right now, need to do it later...
#undef electrons_TYPE
#define electrons_TYPE INVALID_TYPE
#define electrons_INVALID

#undef basicjets_TYPE
#define basicjets_TYPE INVALID_TYPE
#define basicjets_INVALID

#undef photons_TYPE
#define photons_TYPE INVALID_TYPE
#define photons_INVALID

#undef taus_TYPE
#define taus_TYPE INVALID_TYPE
#define taus_INVALID

#undef tracks_TYPE
#define tracks_TYPE CandidateDelayedMuonsTrack
#undef tracks_INVALID

#undef secondaryTracks_TYPE
#define secondaryTracks_TYPE CandidateDelayedMuonsTrack
#undef secondaryTracks_INVALID

#undef prescales_TYPE
#define prescales_TYPE pat::PackedTriggerPrescales
#undef prescales_INVALID

#undef  mcparticles_TYPE
#define  mcparticles_TYPE reco::GenParticle
#undef  mcparticles_INVALID

//#undef  genjets_TYPE
//#define  genjets_TYPE reco::GenJet
//#undef  genjets_INVALID

#include "DataFormats/JetReco/interface/CaloJet.h"
#include "StoppPtls/Collection/interface/CandidateCscHit.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateEvent.h"
#include "StoppPtls/Collection/interface/CandidateJet.h"
#include "StoppPtls/Collection/interface/CandidateRpcHit.h"
#include "StoppPtls/Collection/interface/CandidateDelayedMuonsTrack.h"
// a dirty trick to avoid bug in the InfoPrinter.cc, which required a prescale, which I cannot find temporarily for AOD format.
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
// a dirty trick to avoid complie error in the  OriginalFormatProducer.cc, included all header we need for MINI_AOD
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#endif

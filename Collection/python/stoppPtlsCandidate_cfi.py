import FWCore.ParameterSet.Config as cms

candidateStoppPtls = cms.EDProducer ("CandidateCscHitProducer",
    cscRecHitsTag = cms.InputTag ("csc2DRecHits", ""),
    cscSegmentsTag = cms.InputTag ("cscSegments", ""),
    DTRecHitsTag = cms.InputTag ("dt1DRecHits", ""),
    DT4DSegmentsTag = cms.InputTag ("dt4DSegments",""),
    rpcRecHitsTag = cms.InputTag ("rpcRecHits","")
)

import FWCore.ParameterSet.Config as cms

candidateStoppPtlsJets = cms.EDProducer ("StoppPtlsJetsCandProducer",
                                         cscRecHitsTag = cms.InputTag ("csc2DRecHits", ""),
                                         cscSegmentsTag = cms.InputTag ("cscSegments", ""),
                                         DTRecHitsTag = cms.InputTag ("dt1DRecHits", ""),
                                         DT4DSegmentsTag = cms.InputTag ("dt4DSegments",""),
                                         rpcRecHitsTag = cms.InputTag ("rpcRecHits",""),
                                         )

import FWCore.ParameterSet.Config as cms

candidateDelayedMuons = cms.EDProducer ("DelayedMuonsCandProducer",
                                        displacedStandAloneMuonTag = cms.InputTag ("displacedStandAloneMuons",""),
                                        muonTag = cms.InputTag ("muons",""),
                                        timeTag = cms.InputTag ("muons","dt"),
                                        rpcRecHitsTag = cms.InputTag ("rpcRecHits",""),
                                        )

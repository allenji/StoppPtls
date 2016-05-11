import FWCore.ParameterSet.Config as cms

candidateStoppPtls = cms.EDProducer ("StoppPtlsCandProducer",
                                     isMC = cms.untracked.bool(False),
                                     producer = cms.untracked.string("g4SimHits")
                                     )

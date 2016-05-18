import FWCore.ParameterSet.Config as cms

candidateStoppPtls = cms.EDProducer ("StoppPtlsCandProducer",
                                     isMC = cms.untracked.bool(False),
                                     #producer = cms.untracked.string("g4SimHits"),
                                     stoppedParticlesName = cms.InputTag("g4SimHits", "StoppedParticlesName"),
                                     stoppedParticlesX = cms.InputTag("g4SimHits", "StoppedParticlesX"),
                                     stoppedParticlesY = cms.InputTag("g4SimHits", "StoppedParticlesY"),
                                     stoppedParticlesZ = cms.InputTag("g4SimHits", "StoppedParticlesZ"),
                                     stoppedParticlesTime = cms.InputTag("g4SimHits", "StoppedParticlesTime"),
                                     stoppedParticlesPdgId = cms.InputTag("g4SimHits", "StoppedParticlesPdgId"),
                                     stoppedParticlesMass = cms.InputTag("g4SimHits", "StoppedParticlesMass"),
                                     stoppedParticlesCharge = cms.InputTag("g4SimHits", "StoppedParticlesCharge"),
                                     )

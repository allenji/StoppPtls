import FWCore.ParameterSet.Config as cms

VtxSmeared = cms.EDProducer("StoppedParticleEvtVtxGenerator",
                            src = cms.InputTag("generatorSmeared"),
                            StoppedParticlesName = cms.InputTag("g4SimHits","StoppedParticlesName","SIM"),
                            StoppedParticlesX = cms.InputTag("g4SimHits","StoppedParticlesX","SIM"),
                            StoppedParticlesY = cms.InputTag("g4SimHits","StoppedParticlesY","SIM"),
                            StoppedParticlesZ = cms.InputTag("g4SimHits","StoppedParticlesZ","SIM"),
                            StoppedParticlesTime = cms.InputTag("g4SimHits","StoppedParticlesTime","SIM"),
                            StoppedParticlesPdgId = cms.InputTag("g4SimHits","StoppedParticlesPdgId","SIM"),
                            readFromFile = cms.untracked.bool(False),
                            stoppedData = cms.string (""),
                            timeOffsetMin = cms.double (-5.), # offset by 7.5 ns to adjast trigger time "0" with senter of 25ns interval
                            timeOffsetMax = cms.double (20.), # --"--
                            PutTwoStoppedInSameEvent = cms.untracked.bool(True),
                            StoppedParticleNumber = cms.untracked.int32(0),
                            verbose = cms.untracked.bool (False)
)

import FWCore.ParameterSet.Config as cms

delayedMuonsOutputCommands = cms.untracked.vstring(
    'keep *_*_Stopped*_SIM',
    'keep *_generator_*_SIM',
    'keep *_VtxSmeared_*_SIM2',
    "keep *_genParticles_*_SIM2",
    "keep *_*_*_STOPPPTLS",
)

stoppedParticlesJetsOutputCommands = cms.untracked.vstring(
    "keep *_candidateStoppPtls_*_*",
    "keep *_genParticles_*_*",
    "keep recoGenJets_*_*_*",
    "keep recoGenMETs_*_*_*",
    "keep *_TriggerResults_*_*",
    "keep *_*_*_STOPPPTLS",
    )

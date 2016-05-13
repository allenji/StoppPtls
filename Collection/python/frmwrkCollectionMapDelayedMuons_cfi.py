import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  triggers           = cms.InputTag  ('TriggerResults',        '', 'HLT'),
  events             = cms.InputTag  ('candidateStoppPtls',    '', 'STOPPPTLS'),
  tracks             = cms.InputTag  ('candidateDelayedMuons', '', 'STOPPPTLS'),
  #mcparticles        = cms.InputTag  ('genParticles',          '', 'HLT'),
  mcparticles        = cms.InputTag  ('VtxSmeared',            '', 'SIM2'),
)


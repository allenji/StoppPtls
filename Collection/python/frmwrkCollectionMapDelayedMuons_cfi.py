import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  triggers           = cms.InputTag  ('TriggerResults',         '', 'HLT'),
  events             = cms.InputTag  ('candidateStoppPtls',     '', 'STOPPPTLS'),
  tracks             = cms.InputTag  ('candidateDelayedMuons',  '', 'STOPPPTLS'),
  secondaryTracks    = cms.InputTag  ('candidateDelayedMuons',  '', 'STOPPPTLS'),
  jets               = cms.InputTag  ('candidateStoppPtls',     '', 'STOPPPTLS'),
  cschits            = cms.InputTag  ('candidateStoppPtlsJets', '', 'STOPPPTLS'),
  cscsegs            = cms.InputTag  ('candidateStoppPtlsJets', '', 'STOPPPTLS'),
  dtsegs             = cms.InputTag  ('candidateStoppPtlsJets', '', 'STOPPPTLS'),
  rpchits            = cms.InputTag  ('candidateStoppPtlsJets', '', 'STOPPPTLS'),
  mcparticles        = cms.InputTag  ('genParticles',           '', 'SIM2'),
)

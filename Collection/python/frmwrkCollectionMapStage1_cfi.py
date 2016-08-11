import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  events            =  cms.InputTag  ('candidateStoppPtls', '', 'STOPPPTLS'),
  mcparticles        = cms.InputTag  ('genParticles',       '', 'SIM'),
)

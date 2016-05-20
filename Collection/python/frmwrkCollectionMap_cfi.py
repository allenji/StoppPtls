import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  triggers          =  cms.InputTag  ('TriggerResults',                 '',                       'HLT'),
  events            =  cms.InputTag  ('candidateStoppPtls',               ''),
  jets              =  cms.InputTag  ('candidateStoppPtls',                    ''),
  cschits           =  cms.InputTag  ('candidateStoppPtlsJets',''),
  cscsegs           =  cms.InputTag  ('candidateStoppPtlsJets',''),
  dtsegs            =  cms.InputTag  ('candidateStoppPtlsJets',''),
  rpchits           =  cms.InputTag  ('candidateStoppPtlsJets',''),
  mcparticles       =  cms.InputTag  ('genParticles','','HLT'),
  genjets           =  cms.InputTag  ('ak4GenJets','','HLT')
)

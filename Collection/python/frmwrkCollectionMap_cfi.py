import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  triggers          =  cms.InputTag  ('TriggerResults',                 '',                       'HLT'),
  events            =  cms.InputTag  ('candidateStoppPtls',               ''),
  jets              =  cms.InputTag  ('candidateStoppPtls',                    ''),
  cschits           =  cms.InputTag  ('candidateStoppPtls',''),
  cscsegs           =  cms.InputTag  ('candidateStoppPtls',''),
  dtsegs            =  cms.InputTag  ('candidateStoppPtls',''),
  rpchits           =  cms.InputTag  ('candidateStoppPtls','')
)

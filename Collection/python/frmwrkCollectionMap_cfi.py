import FWCore.ParameterSet.Config as cms

collectionMap_Custom = cms.PSet (
  triggers          =  cms.InputTag  ('TriggerResults',                 '',                       'HLT'),
  events            =  cms.InputTag  ('candidateStoppPtls',               ''),
  jets              =  cms.InputTag  ('candidateStoppPtls',                    ''),
  cschits           =  cms.InputTag  ('candidateStoppPtlsJets',''), #2016
  cscsegs           =  cms.InputTag  ('candidateStoppPtlsJets',''), #2016
  dtsegs            =  cms.InputTag  ('candidateStoppPtlsJets',''), #2016
  rpchits           =  cms.InputTag  ('candidateStoppPtlsJets',''), #2016
  #cschits           =  cms.InputTag  ('candidateStoppPtls',''), #2015
  #cscsegs           =  cms.InputTag  ('candidateStoppPtls',''), #2015
  #dtsegs            =  cms.InputTag  ('candidateStoppPtls',''), #2015
  #rpchits           =  cms.InputTag  ('candidateStoppPtls',''), #2015
  mcparticles       =  cms.InputTag  ('genParticles','','HLT'),
  genjets           =  cms.InputTag  ('ak4GenJets','','HLT')
)

import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("RPCHits3DPlot")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        'file:/data/users/weifengji/condor/stage2SPntuplesSample/stage2RECO_HSCPgluino_1200_1044/readfile_energyScan/HSCPgluino2gchi0_745R5_MCRUN2_74_V9_SPntuples_4.root',
    ),
)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.rpchitsPlotting = cms.EDProducer ("RPCHits3DPlotter",

             candidateRpcHitsTag = cms.InputTag  ('candidateStoppPtls',''),

                         )

process.rpcPlotting = cms.Path(process.rpchitsPlotting)

process.endPath = cms.EndPath()

process.schedule = cms.Schedule(*[process.rpcPlotting,  process.endPath ])

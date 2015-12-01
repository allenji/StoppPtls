import FWCore.ParameterSet.Config as cms
import os

process = cms.Process ('STOPPPTLS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (15)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
    "file:/data/users/weifengji/condor/stage2RECOSample/gluino_gluon_100/stage2RECO_Spring15_1000_894/HSCPgluino-RunIISpring15_RECO_0.root"
    ),
)

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.candidateStoppPtls = cms.EDProducer ("CandidateCscHitProducer",
    cscRecHitsTag = cms.InputTag ("csc2DRecHits", ""),
    cscSegmentsTag = cms.InputTag ("cscSegments", ""),
    DTRecHitsTag = cms.InputTag ("dt1DRecHits", ""),
    DT4DSegmentsTag = cms.InputTag ("dt4DSegments",""),
    rpcRecHitsTag = cms.InputTag ("rpcRecHits","")
)

process.myPath = cms.Path(process.candidateStoppPtls)

process.load('Configuration.EventContent.EventContent_cff')

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECOSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string("RECOWithStoppedParticleEvents_1.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
)

#process.RECOSIMoutput.outputCommands.append ("drop *")
process.RECOSIMoutput.outputCommands.append ("keep *_candidateStoppPtls_*_*")
process.RECOSIMoutput.outputCommands.append ("keep *_*_*_RECO")
process.myEndPath = cms.EndPath (process.RECOSIMoutput)

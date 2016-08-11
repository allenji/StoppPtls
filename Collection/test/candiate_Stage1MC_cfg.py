import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("STOPPPTLS")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10)
    #input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "file:/mnt/hadoop/se/store/mc/RunIIWinter15GS/HSCPgluino_M-1000_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/HSCP_customise_MCRUN2_71_V1-v2/10000/062BA341-8901-E511-8E4A-002590D6004A.root"
    ),
)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_RunIIFall15DR76_v1', '')

#load producers
process.load('StoppPtls/Collection/stoppPtlsCandidate_cfi')
process.candidateStoppPtls.isMC = True
process.eventproducer = cms.Path(    process.candidateStoppPtls    )


process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string("GENWithStoppedParticleEvents.root"),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    #SelectEvents = cms.untracked.PSet(
        #SelectEvents = cms.vstring('generation_step')
    #)
)
process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RAWSIMoutput.outputCommands.append("keep *_genParticles_*_SIM")
process.RAWSIMoutput.outputCommands.append("keep *_*_*_STOPPPTLS")

process.myEndPath = cms.EndPath (process.RAWSIMoutput)
process.schedule = cms.Schedule(process.eventproducer, process.myEndPath)

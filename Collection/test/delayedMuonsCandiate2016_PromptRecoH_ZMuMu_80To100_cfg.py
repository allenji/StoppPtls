import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("STOPPPTLS")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.Skims_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    #input = cms.untracked.int32 (1000)
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        #'/store/data/Run2015D/NoBPTX/AOD/16Dec2015-v1/50000/0A09722C-FDAF-E511-A96E-001E67E6F616.root'
        #'/store/data/Run2016C/NoBPTX/RECO/PromptReco-v2/000/275/419/00000/1E52F317-F439-E611-81F8-02163E0143A1.root'
        #'/store/data/Run2016C/NoBPTX/AOD/PromptReco-v2/000/275/419/00000/C8A87E13-F439-E611-BDD1-02163E011DC3.root'
        #'file:./C8A87E13-F439-E611-BDD1-02163E011DC3.root' #AOD
        #"file:/home/jalimena/StoppedParticles2016/CMSSW_8_0_15/src/RecoMuon/MuonIdentification/test/5EB8577E-2C45-E611-A6A4-02163E0133A4.root" #RECO
        '/store/data/Run2016H/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/281/613/00000/08356928-5A85-E611-A976-02163E014333.root', #RAW-RECO
        ),
                             )

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v14', '')

#HLT bit filter
#no further HLT path filter for zmumu skim, already using all single and double (isolated too) muon triggers

#do ZMuMu 80 to 100 GeV skim
process.load('DPGAnalysis.Skims.ZMuSkim_cff')
process.dimuonsZMuSkim.cut = cms.string('mass > 80 && mass < 100 && charge=0')

#rerun muon timing with pruning off
process.muontiming.TimingFillerParameters.DTTimingParameters.PruneCut = cms.double(10000.)

#load producers
process.load('StoppPtls/Collection/stoppPtlsCandidate_cfi')
process.load('StoppPtls/Collection/stoppPtlsJetsCandidate_cfi')
process.load('StoppPtls/Collection/delayedMuonsCandidate_cfi')
process.candidateDelayedMuons.timeTag = cms.InputTag ("muontiming","dt")
process.eventproducer = cms.Path(
    process.muontiming * process.candidateStoppPtls * process.candidateStoppPtlsJets * process.candidateDelayedMuons
    )

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECOSIM'),
        filterName = cms.untracked.string('ZMu')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string("RECOWithStoppedParticleEvents.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('ZMuSkimPath')
    )
)

process.RECOSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_VtxSmeared_*_SIM2')
process.RECOSIMoutput.outputCommands.append("keep *_genParticles_*_SIM2")
process.RECOSIMoutput.outputCommands.append("drop *_fixedGridRho*_*_RECO")
process.RECOSIMoutput.outputCommands.append("keep *_*_*_STOPPPTLS")


process.myEndPath = cms.EndPath (process.RECOSIMoutput)
process.schedule = cms.Schedule(process.ZMuSkimPath,process.eventproducer, process.myEndPath)

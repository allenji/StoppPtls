import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("STOPPPTLS")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.MessageLogger.cerr.FwkReport.reportEvery = 100

#process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.options = cms.untracked.PSet( SkipEvent = cms.untracked.vstring( 'ProductNotFound' ) )

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
        #'file:/home/jalimena/StoppedParticles2017/CMSSW_9_2_7_patch1/src/EXONoBPTXSkim.root'
        '/store/backfill/1/data/Tier0_REPLAY_vocms015/NoBPTX/USER/EXONoBPTXSkim-PromptReco-v148/000/300/156/00000/3082B5CD-607B-E711-874E-02163E01A4E0.root'
        ),
                             )

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v9', '')

#HLT bit filter
process.load('HLTrigger.HLTfilters.hltHighLevel_cfi')
process.hltHighLevel.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltHighLevel.throw = cms.bool(False)
process.hltHighLevel.HLTPaths = cms.vstring(
    "HLT_L2Mu10_NoVertex_NoBPTX_*",
    "HLT_L2Mu10_NoVertex_NoBPTX3BX_*",
    "HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_*",
    "HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_*",
)

process.filter_step = cms.Path(process.hltHighLevel)

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

# Apply lumi mask; comment out to process all events  
#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/StoppedHSCP/Ntuples/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

from StoppPtls.Collection.outputCommands import *
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
    fileName = cms.untracked.string("RECOWithStoppedParticleEvents.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('filter_step')
    )
)
process.RECOSIMoutput.outputCommands.extend(delayedMuonsOutputCommands)

process.myEndPath = cms.EndPath (process.RECOSIMoutput)
process.schedule = cms.Schedule(process.filter_step, process.eventproducer, process.myEndPath)

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
      "file:/data/users/jalimena/condor/Stage2RecoMchampsSeparateEventsParticle0/mchamp600_DigiHltSeparateEventsParticle0/hist_0.root"
        #"file:/home/jalimena/StoppedParticles2015/cleanAreaForStage2Production/CMSSW_7_6_5/src/StoppPtls/Simulation/reco/stage2RECO.root"
    ),
)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_RunIIFall15DR76_v1', '')

#HLT bit filter
#process.load('HLTrigger.HLTfilters.hltHighLevel_cfi')
#process.hltHighLevel.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
#process.hltHighLevel.throw = cms.bool(False)
#process.hltHighLevel.HLTPaths = cms.vstring(
    #"HLT_L2Mu10_NoVertex_NoBPTX_*",
    #"HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_*",
    #"HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_*",
    #"HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_*",
#)

#process.filter_step = cms.Path(process.hltHighLevel)

#load producers
process.load('StoppPtls/Collection/stoppPtlsCandidate_cfi')
process.load('StoppPtls/Collection/stoppPtlsJetsCandidate_cfi')
process.load('StoppPtls/Collection/delayedMuonsCandidate_cfi')
process.candidateStoppPtls.isMC = True
process.eventproducer = cms.Path(
    process.candidateStoppPtls * process.candidateStoppPtlsJets * process.candidateDelayedMuons
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
    #SelectEvents = cms.untracked.PSet(
      #SelectEvents = cms.vstring('filter_step')
    #)
)
process.RECOSIMoutput.outputCommands.extend(delayedMuonsOutputCommands)

process.myEndPath = cms.EndPath (process.RECOSIMoutput)
#process.schedule = cms.Schedule(process.filter_step, process.eventproducer, process.myEndPath)
process.schedule = cms.Schedule(process.eventproducer, process.myEndPath)

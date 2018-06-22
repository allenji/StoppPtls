import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("STOPPPTLS")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
      "root://cmsxrootd-site.fnal.gov//store/data/Run2015D/NoBPTX/RECO/PromptReco-v4/000/258/750/00000/F205BC24-4672-E511-AA15-02163E01473C.root"
      #"file:/home/weifengji/StoppedParticles_Run2/AnalysisFramework/CMSSW_7_4_5_ROOT5/src/StoppPtls/Collection/test/MyOutputFile_numEvent100.root"
    ),
)

process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

#HLT bit filter
process.load('HLTrigger.HLTfilters.hltHighLevel_cfi')
process.hltHighLevel.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltHighLevel.throw = cms.bool(False)
process.hltHighLevel.HLTPaths = cms.vstring(
    "HLT_JetE30_NoBPTX_*",
    "HLT_JetE30_NoBPTX_NoHalo_*",
    "HLT_JetE30_NoBPTX3BX_NoHalo_*",
    "HLT_JetE50_NoBPTX3BX_NoHalo_*"
)

process.hltStoppedHSCPHpdFilter = cms.EDFilter( "HLTHPDFilter",
    inputTag = cms.InputTag( "hbhereco" ),
    energy = cms.double( -99.0 ),
    hpdSpikeEnergy = cms.double( 10.0 ),
    hpdSpikeIsolationEnergy = cms.double( 1.0 ),
    rbxSpikeEnergy = cms.double( 50.0 ),
    rbxSpikeUnbalance = cms.double( 0.2 )
)

# add a flag indicating the HBHE noise 
process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minNumIsolatedNoiseChannels = cms.int32(999999)
process.HBHENoiseFilterResultProducer.minIsolatedNoiseSumE = cms.double(999999.)
process.HBHENoiseFilterResultProducer.minIsolatedNoiseSumEt = cms.double(999999.)

#load producer
process.load('StoppPtls/Collection/stoppPtlsCandidate_cfi')
process.load('StoppPtls/Collection/stoppPtlsJetsCandidate_cfi')
process.candidateStoppPtls.isMC = False

process.filter_step = cms.Path(process.hltHighLevel*process.hltStoppedHSCPHpdFilter)

process.noisefilter = cms.Path(
    process.HBHENoiseFilterResultProducer
)
process.eventproducer = cms.Path(
    process.candidateStoppPtls*process.candidateStoppPtlsJets
)

process.load('Configuration.EventContent.EventContent_cff')

# Apply lumi mask; comment out to process all events  
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/StoppedHSCP/Ntuples/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt').getCMSSWString().split(',')
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

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
    fileName = cms.untracked.string("RECOWithStoppedParticleEvents_data.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('filter_step')
    )
)
process.RECOSIMoutput.outputCommands.extend(stoppedParticlesJetsOutputCommands)

process.myEndPath = cms.EndPath (process.RECOSIMoutput)
process.schedule = cms.Schedule(process.filter_step, process.noisefilter, process.eventproducer, process.myEndPath)

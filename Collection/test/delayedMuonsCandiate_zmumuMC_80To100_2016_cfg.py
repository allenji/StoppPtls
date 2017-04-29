import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("STOPPPTLS")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.Skims_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    #input = cms.untracked.int32 (10)
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        '/store/mc/RunIISummer16DR80Premix/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/04925D7B-18D1-E611-8E8E-001E67586A2F.root'
    ),
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v1_mc', '')

#HLT bit filter
#not needed since HLT filter already applied in zmumu skim

#do zmumu skim
process.load('DPGAnalysis.Skims.ZMuSkim_cff')
process.dimuonsZMuSkim.cut = cms.string('mass > 80 && mass < 100 && charge=0')

#rerun muon timing with pruning off
#process.muontiming.TimingFillerParameters.DTTimingParameters.PruneCut = cms.double(10000.)

#load producers
process.load('StoppPtls/Collection/stoppPtlsCandidate_cfi')
process.load('StoppPtls/Collection/stoppPtlsJetsCandidate_cfi')
process.load('StoppPtls/Collection/delayedMuonsCandidate_cfi')
process.candidateStoppPtls.isMC = True
#process.candidateDelayedMuons.timeTag = cms.InputTag ("muontiming","dt")

process.eventproducer = cms.Path(
    #process.muontiming * process.candidateStoppPtls * process.candidateStoppPtlsJets * process.candidateDelayedMuons
    process.candidateStoppPtls * process.candidateStoppPtlsJets * process.candidateDelayedMuons
    )

# Apply lumi mask; comment out to process all events  
#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/StoppedHSCP/Ntuples/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

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

process.RECOSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RECOSIMoutput.outputCommands.append("keep *_genParticles_*_SIM")
process.RECOSIMoutput.outputCommands.append("drop *_fixedGridRho*_*_RECO")
process.RECOSIMoutput.outputCommands.append("keep *_*_*_STOPPPTLS")

process.myEndPath = cms.EndPath (process.RECOSIMoutput)
process.schedule = cms.Schedule(process.ZMuSkimPath,process.eventproducer, process.myEndPath)

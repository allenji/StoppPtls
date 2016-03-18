import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("UnmaskedRpcHitsStoppPtls")
process.load('Configuration/StandardSequences/Services_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        'file:/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_7_4_5_ROOT5/src/StoppPtls/Collection/python/RECOWithStoppedParticleEvents_data.root',
    ),
)

process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')


#rpc chamber masking producer
process.rpcChamberMasking = cms.EDProducer ("RPCChamberMaskingProducer",
                                            rpcMaskingCoordinatesFile = cms.string("rpcChambersToMask.txt"),
                                            candidateRpcHitsTag = cms.InputTag  ('candidateStoppPtls',''),
                                            )
process.eventproducer = cms.Path(process.rpcChamberMasking)

process.load('Configuration.EventContent.EventContent_cff')

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
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string("RECOWithStoppedParticleEventsAndUnmaskedRpcHitCollection_data.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    #SelectEvents = cms.untracked.PSet(
      #SelectEvents = cms.vstring('')
    #)
)

process.RECOSIMoutput.outputCommands.append ("drop *")
process.RECOSIMoutput.outputCommands.append ("keep *_candidateStoppPtls_*_*")
#process.RECOSIMoutput.outputCommands.append ("keep *_*_*_RECO")
process.RECOSIMoutput.outputCommands.append ("keep *_TriggerResults_*_*")
#process.RECOSIMoutput.outputCommands.append ("keep *_ak4CaloJets_*_*")

process.RECOSIMoutput.outputCommands.append ("keep *_*_*_STOPPPTLS")
process.RECOSIMoutput.outputCommands.append ("keep *_*_*_UnmaskedRpcHitsStoppPtls")

process.myEndPath = cms.EndPath (process.RECOSIMoutput)
process.schedule = cms.Schedule(process.eventproducer, process.myEndPath)

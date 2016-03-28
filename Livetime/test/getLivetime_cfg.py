import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("Livetime")
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

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo.root'),
)

process.getLivetimeAnalyzer = cms.EDAnalyzer("GetLivetime",
                                     )

process.p = cms.Path(process.getLivetimeAnalyzer)


# Apply lumi mask; comment out to process all events  
#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/StoppedHSCP/Ntuples/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

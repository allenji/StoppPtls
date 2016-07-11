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
        #"root://cms-xrd-global.cern.ch//store/user/wji/NoBPTX/Run2015D-PromptReco-v3_SP-controlSample_v2_Mar06/160307_172200/0004/RECOWithStoppedParticleEvents_data_4188.root"
    ),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo.root'),
)

process.getLivetimeAnalyzer = cms.EDAnalyzer("GetLivetime",
        RunMin = cms.untracked.uint32(235000),
        RunMax = cms.untracked.uint32(265000),
        FillMin = cms.untracked.uint32(3000),
        FillMax = cms.untracked.uint32(5000),
                                     )

process.p = cms.Path(process.getLivetimeAnalyzer)


# Apply lumi mask; comment out to process all events
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '../../Livetime/data/cosmics_json_238361_263584_HcalGood_rmk.txt').getVLuminosityBlockRange()  

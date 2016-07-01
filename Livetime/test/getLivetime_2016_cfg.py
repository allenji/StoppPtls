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
        'file:/data/users/weifengji/condor/070116_RPCChamberMasking_2/Data2016_readinlocal/hist_0.root',
        #"root://cms-xrd-global.cern.ch//store/user/wji/NoBPTX/Run2015D-PromptReco-v3_SP-controlSample_v2_Mar06/160307_172200/0004/RECOWithStoppedParticleEvents_data_4188.root"
    ),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo.root'),
)

process.getLivetimeAnalyzer = cms.EDAnalyzer("GetLivetime",
        RunMin = cms.uint32(273158),
        RunMax = cms.uint32(275125),
        FillMin = cms.uint32(4915),
        FillMax = cms.uint32(5021),
                                     )

process.p = cms.Path(process.getLivetimeAnalyzer)


# Apply lumi mask; comment out to process all events
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '../../Livetime/data/cosmics_json_238361_263584_HcalGood_rmk.txt').getVLuminosityBlockRange()  

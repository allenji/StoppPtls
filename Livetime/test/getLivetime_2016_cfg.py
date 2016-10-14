import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("Livetime")
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet (
    #input = cms.untracked.int32 (-1)
    input = cms.untracked.int32 (1000)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        #'file:/data/users/weifengji/condor/070116_RPCChamberMasking_2/Data2016_readinlocal/hist_0.root',
        #"root://cms-xrd-global.cern.ch//store/user/wji/NoBPTX/Run2015D-PromptReco-v3_SP-controlSample_v2_Mar06/160307_172200/0004/RECOWithStoppedParticleEvents_data_4188.root"
        #'file:/home/jalimena/StoppedParticles2016/CMSSW_8_0_16/src/StoppPtls/Collection/test/RECOWithStoppedParticleEvents.root'
        'file:/data/users/weifengji/NoBPTX_2016SearchSP_Aug23/crab_Run2016F-PromptReco-v1_OSUT3Ntuples_Oct14/NoBPTX_2016collisions_OSUT3Ntuples_1.root'
    ),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo.root'),
)


process.getLivetimeAnalyzer = cms.EDAnalyzer("GetLivetime",
                                             events            =  cms.InputTag  ('candidateStoppPtls',               ''),
                                             RunMin = cms.uint32(273158),
                                             RunMax = cms.uint32(280385),
                                             FillMin = cms.uint32(4915),
                                             FillMax = cms.uint32(5288),
                                             InstLumiMin = cms.int32(0), #times E30 cm^-2 s^-1
                                             InstLumiMax = cms.int32(15000), #times E30 cm^-2 s^-1 
                                             )

process.p = cms.Path(process.getLivetimeAnalyzer)


# Apply lumi mask; comment out to process all events
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '../../Livetime/data/cosmics_json_238361_263584_HcalGood_rmk.txt').getVLuminosityBlockRange()  

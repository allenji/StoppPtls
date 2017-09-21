import FWCore.ParameterSet.Config as cms
###########################################################
##### Set up process #####
###########################################################
process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.source = cms.Source ('PoolSource',
                             fileNames = cms.untracked.vstring (
        # 'root://xrootd.ba.infn.it//store/user/wulsin/AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1/AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1/d66ce63f45b0919f1bcc6fe69cbbc5b1/AMSB_chargino_RECO_9_1_ELT.root',
        #'file:./step1_SingleMuPt250.root'
        #'file:./stage2_GEN-HLT_mchamp600.root'
        'file:./hist.root'
        #'file:/data/users/jalimena/condor/Stage2GenSimMchampsSeparateEventsParticle0/mchamp600/hist_0.root'
        #'file:/data/users/jalimena/condor/Stage2GenSimGluinosSeparateEventsParticle0/gluino2000/hist_25.root'
        #'file:/data/users/jalimena/condor/TestStage2Gluino/gluino2000/hist_11.root'
        )
                             )

process.maxEvents = cms.untracked.PSet (
#input = cms.untracked.int32 (-1)
input = cms.untracked.int32 (10)
)

###########################################################
##### Set up the analyzer #####
###########################################################
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer ('ParticleListDrawer',
                                             maxEventsToPrint = cms.untracked.int32(-1),
                                             printVertex = cms.untracked.bool(True),
                                             src = cms.InputTag("genParticles")
                                             #src = cms.InputTag("genParticlePlusGEANT")
                                             )

process.myPath = cms.Path (process.particleListDrawer)

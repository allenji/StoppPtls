import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
        #'file:/home/jalimena/StoppedParticles2015/CMSSW_7_6_5/src/StoppPtls/Collection/test/RECOWithStoppedParticleEvents.root'
        #'file:/data/users/jalimena/condor/Stage2NtupleMchampsSeparateEventsParticle0/mchamp600_RecoSeparateEventsParticle0/hist_0.root'
        #'file:/data/users/jalimena/condor/NoBPTX2015Ntuples/NoBPTX_2015C_16Dec2015/hist_0.root'
        #'file:/data/users/jalimena/condor/NoBPTX2016Ntuples/NoBPTX_2016B_PromptReco/hist_0.root'
        'file:/data/users/jalimena/condor/NoBPTX2016Ntuples_NoDtTimingPruning/NoBPTX_2016B_PromptReco/hist_0.root'
        #'file:/home/jalimena/StoppedParticles2016/CMSSW_8_0_16/src/StoppPtls/Collection/python/NoBPTX_2016collisions_OSUT3Ntuples.root'
        ),
                             )

# FIXME:  set_input does not work (because of error with /usr/bin/file) in CMSSW_7_4_5_ROOT5   
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
# set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/")

# sample ROOT file
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_10_2_Dzw.root")

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
    #input = cms.untracked.int32 (-1)
    #input = cms.untracked.int32 (10)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from StoppPtls.Collection.frmwrkCollectionMapDelayedMuons_cfi import collectionMap_Custom

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet (
    #cms.PSet (
        #inputCollections = cms.vstring("eventvariables"),
        #inputVariable = cms.string("1.0/livetimeByRun")
        #inputVariable = cms.string("1.0/livetimeByFill")
    #),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = ["StoppPtlsEventVariableProducer"]
variableProducers.append("StoppPtlsJetsEventVariableProducer")
variableProducers.append("DelayedMuonsEventVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from StoppPtls.DelayedMuonsAnalysis.Cuts import *
from StoppPtls.DelayedMuonsAnalysis.EventSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from StoppPtls.DelayedMuonsAnalysis.Histograms import *
from StoppPtls.StandardAnalysis.Histograms import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

selections = []
selections.append(NoCuts)
selections.append(GenPlotsSelection)
selections.append(TriggerSelection)
selections.append(ControlTriggerSelection)
selections.append(PrePreSelection)
selections.append(PreSelectionUpperOnly)
selections.append(PreSelectionUpperLower)
selections.append(PreSelectionUpperLowerTurnOnDen)
selections.append(PreSelectionUpperLowerTurnOnNum)
selections.append(DelayedMuonsUpperOnlySelection)
selections.append(DelayedMuonsUpperLowerSelection)

histograms = cms.VPSet()
histograms.append(DelayedMuonsStoppedParticleHistograms)
histograms.append(Muon0Histograms)
histograms.append(Muon1Histograms)
histograms.append(NeutralinoHistograms)
#histograms.append(NeutralinoNLSPHistograms)
histograms.append(EventHistograms)
histograms.append(UpperDSAHistograms)
histograms.append(LowerDSAHistograms)
histograms.append(NumberOfObjectsHistograms)
histograms.append(NumberOfDelayedMuonsObjectsHistograms)
histograms.append(DelayedMuonsObjectsVsTimeHistograms)
histograms.append(DeltaDSAHistograms)
histograms.append(UppervsLowerDSAHistograms)
histograms.append(UppervsUpperDSAHistograms)
histograms.append(LowervsLowerDSAHistograms)
histograms.append(VsDeltaDSAHistograms)

scalingfactorproducers = []

add_channels(process, selections, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, True)

#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/StpPtls_controlSample_2015.root")
process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/NoBPTX_2015D.root")

process.StoppPtlsEventVariableProducer.stoppedParticlesName = cms.InputTag("g4SimHits", "StoppedParticlesName")
process.StoppPtlsEventVariableProducer.stoppedParticlesX = cms.InputTag("g4SimHits", "StoppedParticlesX")
process.StoppPtlsEventVariableProducer.stoppedParticlesY = cms.InputTag("g4SimHits", "StoppedParticlesY")
process.StoppPtlsEventVariableProducer.stoppedParticlesZ = cms.InputTag("g4SimHits", "StoppedParticlesZ")
process.StoppPtlsEventVariableProducer.stoppedParticlesTime = cms.InputTag("g4SimHits", "StoppedParticlesTime")
process.StoppPtlsEventVariableProducer.stoppedParticlesPdgId = cms.InputTag("g4SimHits", "StoppedParticlesPdgId")
process.StoppPtlsEventVariableProducer.stoppedParticlesMass = cms.InputTag("g4SimHits", "StoppedParticlesMass")
process.StoppPtlsEventVariableProducer.stoppedParticlesCharge = cms.InputTag("g4SimHits", "StoppedParticlesCharge")

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")

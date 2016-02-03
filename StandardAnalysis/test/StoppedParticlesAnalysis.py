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
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
        'file:/home/weifengji/StoppedParticles_Run2/AnalysisFramework_Dev/CMSSW_7_4_5_ROOT5/src/StoppPtls/Collection/python/RECOWithStoppedParticleEvents_data.root',
        #'file:/home/jalimena/StoppedParticles2015/CMSSW_7_4_5_ROOT5/src/StoppPtls/Collection/python/RECOWithStoppedParticleEvents_MC_g2qqchi_1200_1000.root'
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
    input = cms.untracked.int32 (1000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD
from StoppPtls.Collection.frmwrkCollectionMap_cfi import collectionMap_Custom

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet (
    #cms.PSet (
    #    inputCollections = cms.vstring("muons"),
    #    inputVariable = cms.string("pt")
    #),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = ["StoppPtlsEventVariableProducer"]
#variableProducers.append("MyVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from OSUT3Analysis.ExampleAnalysis.MyProtoEventSelections import *
from StoppPtls.StandardAnalysis.Cuts import *
from StoppPtls.StandardAnalysis.EventSelections import *

#StoppPtlsSelection = cms.PSet(
#  name = cms.string("adumbtest"),
#  triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
#  cuts = cms.VPSet(
#   cutOuterRpc,
#   cutOuterDT,
#  )
#)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.ExampleAnalysis.MyProtoHistogramDefinitions import *
from StoppPtls.StandardAnalysis.Histograms import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

histograms = cms.VPSet()
histograms.append(StoppedParticleHistograms)
histograms.append(GenParticleHistograms)
histograms.append(EventHistograms)
histograms.append(NumberOfObjectsHistograms)
histograms.append(NoiseHistograms)
histograms.append(JetHistograms)
histograms.append(LeadingJetHistograms)
histograms.append(SecondJetHistograms)
histograms.append(DtSegmentHistograms)
histograms.append(CscSegmentHistograms)
histograms.append(RpcHitsHistograms)
histograms.append(OtherDtHistograms)
histograms.append(OtherRpcHistograms)
histograms.append(TowerHistograms)
histograms.append(HpdHistograms)


# add_channels (process, [StoppPtlsSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [HaloSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [CosmicSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [NoiseSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [SecondJetSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [NoCuts], histograms, weights, collectionMap_Custom, variableProducers, False)

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

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

from StoppPtls.Collection.frmwrkCollectionMapDelayedMuons_cfi import collectionMap_Custom
#from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD

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

variableProducers = ["ToyMCEventVariableProducer"]
#variableProducers.append("MyVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from StoppPtls.DelayedMuonsAnalysis.EventSelections import *

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

#from OSUT3Analysis.ExampleAnalysis.MyProtoHistogramDefinitions import *
#from StoppPtls.StandardAnalysis.Histograms import *
from StoppPtls.ToyMC_DelayedMuons.Histograms import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

selections = []
#selections.append(StoppPtlsSelection)
#selections.append(HaloSelection)
#selections.append(HaloControlSelection)
#selections.append(HaloTagAndProbeSelection)
#selections.append(CosmicSelection)
#selections.append(CosmicControlSelection)
#selections.append(NoiseSelection)
#selections.append(NoiseControlSelection)
#selections.append(AltNoiseControlSelection)
#selections.append(Rpc_study)
#selections.append(PrePreSelection)
#selections.append(TriggerSelection)
#selections.append(SecondJetSelection)
#selections.append(NoCuts)

histograms = cms.VPSet()
histograms.append(ToyMCRunLbHistogram_2016)
#histograms.append(StoppedParticleHistograms)
#histograms.append(GenParticleHistograms)
#histograms.append(NeutralinoHistograms)
#histograms.append(GluonHistograms)
#histograms.append(UHistograms)
#histograms.append(UbarHistograms)
#histograms.append(GenJetHistograms)
#histograms.append(EventHistograms)
#histograms.append(NumberOfObjectsHistograms)
#histograms.append(ObjectsVsTimeHistograms)
#histograms.append(RpcHitsVsTimeHistograms)
#histograms.append(NoiseHistograms)
#histograms.append(JetHistograms)
#histograms.append(LeadingJetHistograms)
#histograms.append(SecondJetHistograms)
#histograms.append(DtSegmentHistograms)
#histograms.append(CscSegmentHistograms)
#histograms.append(RpcHitsHistograms)
#histograms.append(OtherDtHistograms)
#histograms.append(OtherCscHistograms)
#histograms.append(OtherRpcHistograms)
#histograms.append(TowerHistograms)
#histograms.append(HpdHistograms)
scalingfactorproducers = []

#add_channels (process, selections, histograms, weights, collectionMap_Custom, variableProducers, False)

#add_channels (process, [NoCuts], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
add_channels (process, [TriggerSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/StpPtls_controlSample_2015.root")
#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/NoBPTX_2015D.root")

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

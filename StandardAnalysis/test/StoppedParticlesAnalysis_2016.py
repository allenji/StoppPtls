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
                                 #'file:/home/weifengji/StoppedParticles_Run2/SPAnalysis_2016_Oct10/CMSSW_8_0_19_patch1/src/StoppPtls/Collection/python/NoBPTX_2016collisions_OSUT3Ntuples.root',
                                 'file:/home/weifengji/StoppedParticles_Run2/SPAnalysis_2016_Oct10/CMSSW_8_0_19_patch1/src/StoppPtls/Collection/python/NoBPTX_2016collisions_OSUT3Ntuples_Feb9_2.root',
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
    #    inputCollections = cms.vstring("eventvariables"),
    #    inputVariable = cms.string("1.0/livetimeByRun")
        #inputVariable = cms.string("1.0/livetimeByFill")
    #),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = ["StoppPtlsLivetimeEventVariableProducer"]
variableProducers.append("StoppPtlsJetsEventVariableProducer")

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

selections = []
selections.append(StoppPtlsSelection_2016)
selections.append(StoppPtlsSelection_2016_jetEnergySmeared)
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
#histograms.append(ToyMCRunLbHistogram)
#histograms.append(StoppedParticleHistograms)
#histograms.append(GenParticleHistograms)
#histograms.append(NeutralinoHistograms)
#histograms.append(GluonHistograms)
#histograms.append(UHistograms)
#histograms.append(UbarHistograms)
#histograms.append(GenJetHistograms)
#histograms.append(LeadingJetHistograms)

histograms.append(EventHistograms)
histograms.append(NumberOfObjectsHistograms)
#histograms.append(ObjectsVsTimeHistograms)
#histograms.append(RpcHitsVsTimeHistograms)
histograms.append(NoiseHistograms)
#histograms.append(JetHistograms)
histograms.append(LeadingJetHistograms)
#histograms.append(SecondJetHistograms)
histograms.append(DtSegmentHistograms)
histograms.append(CscSegmentHistograms)
histograms.append(RpcHitsHistograms)
histograms.append(OtherDtHistograms)
histograms.append(OtherCscHistograms)
histograms.append(OtherRpcHistograms)
histograms.append(TowerHistograms)
histograms.append(HpdHistograms)
histograms.append(HaloBeamFilterHistograms)
histograms.append(JetCscHistogram)
histograms.append(numIsolatedNoiseChannelsHistograms)
'''
histograms.append(CscCscHistogram)
histograms.append(DtSegmentHistograms)
'''

scalingfactorproducers = []

add_channels (process, selections, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

#add_channels (process, [StoppPtlsSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicRunNum], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [StoppPtlsSelection_2016], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [EventSelection_PlotLeadingJetEM], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [TriggerSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [TriggerSelection_2016], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HaloSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HaloControlSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRiched], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloCscPlot], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotBeam1], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotBeam2], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotNoPos], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotNoNeg], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmiBackgroundEventSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRiched], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoCuts], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HaloTagAndProbeSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicPassSpecificRegion], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseControlSelectionTight], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseControlSelectionTight_2016], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [TriggerSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelection1], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelection2], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelection3], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelection4], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelectionMC1], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelectionMC2], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelectionMC3], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelectionMC4], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicControlSelectionMC5], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CosmicSelection_2016], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseControlSelectionTight], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [PrePreSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
# add_channels (process, [TriggerSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
# add_channels (process, [SecondJetSelection], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoCuts], histograms, weights, collectionMap_Custom, variableProducers, False)
#add_channels (process, [Rpc_study], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseFilterPass], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoiseFilterVeto], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HCalNoiseAndFilterPass], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HCalNoiseAndFilterVeto], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicCoarse], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicCoarse2], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicFilter], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicStrict], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CscRGt400], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [NoCuts], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CscNHit3], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CscNHit6], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [CscAllStudy], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [selectedHaloNCscNearJet], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [selectedHaloByBeamHaloFilter], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HaloControlTaggedByVetoSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotBeam1], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRiched], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [makeHaloNCscPlotBeam2], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [HaloControlTaggedByFilterSelection], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [haloCoarse], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [haloStrict], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [cosmicOuterDTNoCsc], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseBasic], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRiched], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRichedGT1CSC], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRichedGT1DT], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [testHaloBeamFilter], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [testHaloBeamFilterWithCosmicVeto], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [testHaloBeamFilterOnNoiseEvent], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseRBXRichedGT1CSC1DT], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseStrict], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseAfterRBXCleaning], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [noiseNoDtCsc], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [haloBasic], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, [N90NoiseStudy], histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/weifengji/condor/082816_AN_LivetimeAndRunInfo2016Control/NoBPTX_CosJet_2016BCDE_PromptReco.root")
process.StoppPtlsLivetimeEventVariableProducer.livetimeRootFile = cms.string("/data/users/weifengji/condor/101816_LivetimeFG/NoBPTX_Jet_2016FG_PromptReco.root")
#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/weifengji/condor/092016_2016ControlLivetime/NoBPTX_CosJet_2016BCDE_PromptReco.root")
#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/NoBPTX_2015D.root")

process.StoppPtlsJetsEventVariableProducer.jetEnergyResolutionWidth = cms.double(0.25)

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

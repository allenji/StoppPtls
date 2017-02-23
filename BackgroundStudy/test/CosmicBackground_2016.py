import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

process = cms.Process ('CosmicBackgroundAnalysis')

process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
                                 'file:/data/users/weifengji/condor/070416_RPCMasking_2/Data2016_readinlocal/hist_0.root',
        #'file:/home/jalimena/StoppedParticles2015/CMSSW_7_4_5_ROOT5/src/StoppPtls/Collection/python/RECOWithStoppedParticleEvents_MC_g2qqchi_1200_1000.root'
        ),
                             )

process.TFileService = cms.Service ('TFileService',
        fileName = cms.string ('hist.root')
        )

process.maxEvents = cms.untracked.PSet (
        input = cms.untracked.int32 (-1)
        )

from StoppPtls.Collection.frmwrkCollectionMap_cfi import collectionMap_Custom

weights = cms.VPSet (
    )

variableProducers = ["StoppPtlsEventVariableProducer"]
variableProducers.append("StoppPtlsJetsEventVariableProducer")

from StoppPtls.BackgroundStudy.CosmicBkgCutDefinition_2016_SP import *
from StoppPtls.BackgroundStudy.CosmicBkgHistogram import *
#apply to cosmic MC
selections_untagged = []
selections_untagged.append(untagged_cosmic_cut)

#apply to cosmic MC
selections = []
selections.append(full_cosmics)

#apply to data
selections_data = []
selections_data.append(CosmicSelection)

histograms = cms.VPSet()
histograms.append(CosmicBackgroundHistograms)

scalingfactorproducers = []

# used for cosmic MC
#add_channels (process, selections_untagged, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)
#add_channels (process, selections, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

# used for data
add_channels (process, selections_data, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/StpPtls_controlSample_2015.root")
#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/NoBPTX_2015D.root")

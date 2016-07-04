import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

process = cms.Process ('HaloBackgroundAnalysis')

process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
        #'file:/store/user/weifengji/HSCPgluino_UUbarChi0_13TeV-pythia6/RunIISpring15-74x_mcRun2_StoppPtls_gluino_1200_chi0_1000//StoppedParticleNtuples_MC_gluino2uubarchi0_0.root',
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

from StoppPtls.BackgroundStudy.HaloBkgCutDefinition_2016 import *
from StoppPtls.BackgroundStudy.HaloBkgHistogram import *

selections = []
selections.append(HaloTagAndProbeSelection)
selections.append(IncomingOnly) 
selections.append(IncomingOnlyBeam1)
selections.append(IncomingOnlyBeam2)
selections.append(OutgoingOnly)
selections.append(OutgoingOnlyBeam1)
selections.append(OutgoingOnlyBeam2)
selections.append(Both)
selections.append(BothBeam1)
selections.append(BothBeam2)
selections.append(All)
selections.append(AllBeam1)
selections.append(AllBeam2)
selections.append(HaloControlSelection)
selections.append(HaloControlBeam1)
selections.append(HaloControlBeam2)

histograms = cms.VPSet()
histograms.append(HaloBackgroundHistograms)

scalingfactorproducers = []

add_channels (process, selections, histograms, weights, scalingfactorproducers, collectionMap_Custom, variableProducers, False)

process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/StpPtls_controlSample_2015.root")
#process.StoppPtlsEventVariableProducer.livetimeRootFile = cms.string("/data/users/jalimena/condor/Livetime/NoBPTX_2015D.root")

import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *

#########################################################
# Event selections for cosmic tagging inefficiency
untagged_cosmic_cut = cms.PSet(
    name = cms.string("untaggedCosmics"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)

untagged_cosmic_cut.cuts.append(cutCscSegNumber)
untagged_cosmic_cut.cuts.append(cutOuterDT)
untagged_cosmic_cut.cuts.append(cutDTPair)
untagged_cosmic_cut.cuts.append(cutMaxDeltaJetPhi)
untagged_cosmic_cut.cuts.append(newNOuterAllRPCHitsDeltaR)

full_cosmics = cms.PSet(
    name = cms.string("fullCosmicsNoCutsOrHLTApplied"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        )
)
###########################################
# Event selections for cosmic control data
CosmicNMinusOneSelection = cms.PSet(
    name = cms.string("CosmicNMinusOneSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutNoise,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter
    )
)


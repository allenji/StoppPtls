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

# these  are old deprecated veto
#untagged_cosmic_cut.cuts.append(cutCscSegNumber)
#untagged_cosmic_cut.cuts.append(cutOuterDT)
#untagged_cosmic_cut.cuts.append(cutDTPair)
#untagged_cosmic_cut.cuts.append(cutMaxDeltaJetPhi)
#untagged_cosmic_cut.cuts.append(newNOuterAllBarrelRPCHitsDeltaR)
untagged_cosmic_cut.cuts.append(cutDummy)
untagged_cosmic_cut.cuts.append(cutJetEta)
untagged_cosmic_cut.cuts.append(cutNDTStation3)
untagged_cosmic_cut.cuts.append(cutNDTStation4)
untagged_cosmic_cut.cuts.append(cutDTPair)
untagged_cosmic_cut.cuts.append(cutMaxDeltaJetPhiNoDTST4)
untagged_cosmic_cut.cuts.append(cutCloseOuterAllDTPairDeltaPhi0p5)
untagged_cosmic_cut.cuts.append(cutMinDeltaRDTST4RPCInner3Layers)
untagged_cosmic_cut.cuts.append(newNOuterAllBarrelRPCHitsDeltaRDeltar)

full_cosmics = cms.PSet(
    name = cms.string("fullCosmicsNoCutsOrHLTApplied"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        cutJetEta,
        )
)
###########################################
# Event selections for cosmic control data
CosmicSelection = cms.PSet(
    name = cms.string("CosmicNMinusOneSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutCscSegNumber,
      cutHavingNoCscSegNHit56,
      cutNoise,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutMaxiEtaDiffSameiRbx,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter
    )
)
CosmicSelection.cuts.append(cutCosmics)
CosmicSelection.cuts.append(cutNumberOfDT)
#CosmicSelection.cuts.append(cutMoreOuterDT)



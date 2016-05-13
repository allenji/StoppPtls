import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *

#full analysis selection
DelayedMuonsSelection = cms.PSet(
    name = cms.string("DelayedMuonsSelection"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      #cutOuterDT,
      #cutDSAEnergy,
      #cutDSAEta,
    )
)

#Halo N-1 Selection (full selection except halo veto)
#For nCscSeg plot
HaloControlSelection = cms.PSet(
    name = cms.string("BeamHaloControlSelection"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
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


#Pre Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PrePreSelection = cms.PSet(
    name = cms.string("PrePreSelection"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      )
)

#Signal Trigger Selection
#For vertex number plot
TriggerSelection = cms.PSet(
    name = cms.string("TriggerSelection"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
        cutDummy,
      )
)


#No cuts (including no trigger) selection
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        )
    )

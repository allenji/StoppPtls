import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *
from StoppPtls.DelayedMuonsAnalysis.Cuts import *

#No cuts (including no trigger) selection
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
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

#Gen Plots Selection (only not in cavern walls)
#For stopped particle and generator muon plots
GenPlotsSelection = cms.PSet(
    name = cms.string("GenPlotsSelection"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutNotCavernWalls,
      )
)

#PrePre Selection (only pt>10 GeV cut)
#For jetE, jetEta plots
PrePreSelection = cms.PSet(
    name = cms.string("PrePreSelection"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutNotCavernWalls,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreDSAPt,
      )
)

#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutNotCavernWalls,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreMaxNDSAs,
      cutPreDSAPt,
      cutPreDSANDtChambersWithValidHits,
      cutPreDSANValidRpcHits,
      cutPreDSADtTofNDof,
      cutPreDSANValidCscHits,
      )
    )

#full analysis selection
DelayedMuonsSelection = copy.deepcopy(PreSelection)
DelayedMuonsSelection.name = cms.string("DelayedMuonsSelection")
DelayedMuonsSelection.cuts.append(cutDSAPt)
#DelayedMuonsSelection.cuts.append(cutDSAEta)
DelayedMuonsSelection.cuts.append(cutDSANDtChambersWithValidHits)
DelayedMuonsSelection.cuts.append(cutDSANValidRpcHits)
#DelayedMuonsSelection.cuts.append(cutDSADtTofTimeInOut)
DelayedMuonsSelection.cuts.append(cutDSADtTofTimeInOutErr)

#full analysis upper and lower selection
DelayedMuonsUpperLowerSelection = copy.deepcopy(PreSelection)
DelayedMuonsUpperLowerSelection.name = cms.string("DelayedMuonsUpperLowerSelection")
##DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAEta)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
##DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerSelection.cuts.append(cutLowerDSARpcBxPattern)

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
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"),
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
        cutDummy,
        cutNotCavernWalls,
        )
    )

#PrePre Selection (only pt>10 GeV cut)
#For jetE, jetEta plots
cutPreDSAPtGeneric = copy.deepcopy(cutPreDSAPtUpperOnly)
cutPreDSAPtGeneric.alias = cms.string("DSA Track $p_{T}$ > 10 \GeV")
PrePreSelection = cms.PSet(
    name = cms.string("PrePreSelection"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreDSAPtGeneric,
      cutPrePreDSADtTofNDofUpperOnly,
      )
)

#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelectionUpperOnly = cms.PSet(
    name = cms.string("PreSelectionUpperOnly"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAsUpperOnly,
      cutPreMaxNDSAsUpperOnly,
      cutPreDSAUpperOnly,
      cutPreDSAPtUpperOnly,
      cutPreDSANDtChambersWithValidHitsUpperOnly,
      cutPreDSANValidRpcHitsUpperOnly,
      cutPreDSADtTofNDofUpperOnly,
      cutPreDSANValidCscHitsUpperOnly,
      )
    )

#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelectionUpperLower = cms.PSet(
    name = cms.string("PreSelectionUpperLower"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreMaxNDSAs,
      cutPreDSAUpperAndLower,
      cutPreDSAPt,
      cutPreDSANDtChambersWithValidHits,
      cutPreDSANValidRpcHits,
      cutPreDSADtTofNDof,
      cutPreDSANValidCscHits,
      )
    )

#full analysis selection
DelayedMuonsUpperOnlySelection = copy.deepcopy(PreSelectionUpperOnly)
DelayedMuonsUpperOnlySelection.name = cms.string("DelayedMuonsUpperOnlySelection")
DelayedMuonsUpperOnlySelection.cuts.append(cutDSAPt)
#DelayedMuonsUpperOnlySelection.cuts.append(cutDSAEta)
DelayedMuonsUpperOnlySelection.cuts.append(cutDSANDtChambersWithValidHits)
DelayedMuonsUpperOnlySelection.cuts.append(cutDSANValidRpcHits)
#DelayedMuonsUpperOnlySelection.cuts.append(cutDSADtTofTimeInOut)
DelayedMuonsUpperOnlySelection.cuts.append(cutDSADtTofTimeInOutErr)

#full analysis upper and lower selection
DelayedMuonsUpperLowerSelection = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection.name = cms.string("DelayedMuonsUpperLowerSelection")
##DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAEta)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
##DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerSelection.cuts.append(cutLowerDSARpcBxPattern)

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
TriggerSelection2015 = cms.PSet(
    name = cms.string("TriggerSelection2015"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
        cutDummy,
      )
)

TriggerSelection2016 = copy.deepcopy(TriggerSelection2015)
TriggerSelection2016.name = cms.string("TriggerSelection2016")
#TriggerSelection2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
TriggerSelection2016.triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_v")

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

PrePreSelection2015 = cms.PSet(
    name = cms.string("PrePreSelection2015"),
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

PrePreSelection2016 = copy.deepcopy(PrePreSelection2015)
PrePreSelection2016.name = cms.string("PrePreSelection2016")
#PrePreSelection2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
PrePreSelection2016.triggers = cms.vstring("")


#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelectionUpperOnly2015 = cms.PSet(
    name = cms.string("PreSelectionUpperOnly2015"),
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

PreSelectionUpperOnly2016 = copy.deepcopy(PreSelectionUpperOnly2015)
PreSelectionUpperOnly2016.name = cms.string("PreSelectionUpperOnly2016")
#PreSelectionUpperOnly2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
PreSelectionUpperOnly2016.triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_v")

#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelectionUpperLower2015 = cms.PSet(
    name = cms.string("PreSelectionUpperLower2015"),
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

PreSelectionUpperLower2016 = copy.deepcopy(PreSelectionUpperLower2015)
PreSelectionUpperLower2016.name = cms.string("PreSelectionUpperLower2016")
#PreSelectionUpperLower2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
PreSelectionUpperLower2016.triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_v")

#full analysis selection
DelayedMuonsUpperOnlySelection2015 = copy.deepcopy(PreSelectionUpperOnly2015)
DelayedMuonsUpperOnlySelection2015.name = cms.string("DelayedMuonsUpperOnlySelection2015")
DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSAPt)
#DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSAEta)
DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSANDtChambersWithValidHits)
DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSANValidRpcHits)
#DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSADtTofTimeInOut)
DelayedMuonsUpperOnlySelection2015.cuts.append(cutDSADtTofTimeInOutErr)

DelayedMuonsUpperOnlySelection2016 = copy.deepcopy(DelayedMuonsUpperOnlySelection2015)
DelayedMuonsUpperOnlySelection2016.name = cms.string("DelayedMuonsUpperOnlySelection2016")
#DelayedMuonsUpperOnlySelection2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
DelayedMuonsUpperOnlySelection2016.triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_v")

#full analysis upper and lower selection
DelayedMuonsUpperLowerSelection2015 = copy.deepcopy(PreSelectionUpperLower2015)
DelayedMuonsUpperLowerSelection2015.name = cms.string("DelayedMuonsUpperLowerSelection2015")
##DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSAPt)
#DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSAEta)
#DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
##DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2015.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerSelection2015.cuts.append(cutLowerDSARpcBxPattern)

DelayedMuonsUpperLowerSelection2016 = copy.deepcopy(DelayedMuonsUpperLowerSelection2015)
DelayedMuonsUpperLowerSelection2016.name = cms.string("DelayedMuonsUpperLowerSelection2016")
#DelayedMuonsUpperLowerSelection2016.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")
DelayedMuonsUpperLowerSelection2016.triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_v")

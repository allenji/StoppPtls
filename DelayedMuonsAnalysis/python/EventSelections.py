import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *
from StoppPtls.StandardAnalysis.Cuts import *
from StoppPtls.DelayedMuonsAnalysis.Cuts import *

#No cuts (including no trigger) selection
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        )
    )

NoCutsStage1 = cms.PSet(
    name = cms.string("NoCutsStage1"),
    #triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        cutDummyStage1
        )
    )

#Signal Trigger Selection
#For vertex number plot
TriggerSelection = cms.PSet(
    name = cms.string("TriggerSelection"),
    #triggers = cms.vstring("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
        cutDummy,
      )
)


NoBPTX3BXControlTriggerSelection = cms.PSet(
    name = cms.string("NoBPTX3BXControlTriggerSelection"),
    triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
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
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreDSAPtGeneric,
      cutPrePreDSADtTofNDofUpperOnly,
      )
)

PrePreSelectionUpperLower = cms.PSet(
    name = cms.string("PrePreSelectionUpperLower"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreDSAUpperAndLower,
      cutPreDSAPt,
      )
)

#for trigger purity study, on data, cosmic data, and signal MC
#no upper lower cut, no dt tof cut
TriggerPuritySelection = cms.PSet(
    name = cms.string("TriggerPuritySelection"),
    #triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    triggers = cms.vstring("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutDSAPtUpperOnly,
      cutPreDSANDtChambersWithValidHitsUpperOnly,
      cutPreDSANValidRpcHitsUpperOnly,
      cutPreDSANValidCscHitsUpperOnly,
      )
    )

#Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PreSelectionUpperOnly = cms.PSet(
    name = cms.string("PreSelectionUpperOnly"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
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
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      #cutPreMaxNDSAs,
      cutPreDSAUpperAndLower,
      cutPreDSAPt,
      cutPreDSANDtChambersWithValidHits,
      cutPreDSANValidRpcHits,
      cutPreDSADtTofNDof,
      cutPreDSANValidCscHits,
      )
    )

#preselection with no trigger
PreSelectionUpperLowerNoTrigger = copy.deepcopy(PreSelectionUpperLower)
PreSelectionUpperLowerNoTrigger.name = cms.string("PreSelectionUpperLowerNoTrigger")
PreSelectionUpperLowerNoTrigger.triggers = cms.vstring("")

PreSelectionUpperLowerZMuMu = cms.PSet(
    name = cms.string("PreSelectionUpperLowerZMuMu"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutPreMinNDSAs,
      cutPreDSAUpperAndLower,
      cutPreDSAPt,
      cutPreDSANDtChambersWithValidHits,
      cutPreDSANValidRpcHits,
      cutPreDSANValidCscHits,
      )
    )

#for trigger turn on: run over ntuples where only control triggers are used in the selection
PreSelectionUpperLowerAtLeast4ValidDtChambers = copy.deepcopy(PreSelectionUpperLower)
PreSelectionUpperLowerAtLeast4ValidDtChambers.name = cms.string("PreSelectionUpperLowerAtLeast4ValidDtChambers")
addSingleCut(PreSelectionUpperLowerAtLeast4ValidDtChambers.cuts,cutPreDSAAtLeast4DtChambersWithValidHits,cutPreDSAPt)
removeCuts(PreSelectionUpperLowerAtLeast4ValidDtChambers.cuts,[cutPreDSANDtChambersWithValidHits])


#For HLT turn-on curve: denominator is preselection with no additional trigger applied
PreSelectionUpperLowerTurnOnDen = copy.deepcopy(PreSelectionUpperLowerAtLeast4ValidDtChambers)
PreSelectionUpperLowerTurnOnDen.name = cms.string("PreSelectionUpperLowerTurnOnDen")
PreSelectionUpperLowerTurnOnDen.triggers = cms.vstring("")

#For HLT turn-on curve: numerator is preselection plus signal trigger
PreSelectionUpperLowerTurnOnNum35 = copy.deepcopy(PreSelectionUpperLowerAtLeast4ValidDtChambers)
PreSelectionUpperLowerTurnOnNum35.name = cms.string("PreSelectionUpperLowerTurnOnNum35")
PreSelectionUpperLowerTurnOnNum35.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")

#For HLT turn-on curve: numerator is preselection plus signal trigger
PreSelectionUpperLowerTurnOnNum40 = copy.deepcopy(PreSelectionUpperLowerAtLeast4ValidDtChambers)
PreSelectionUpperLowerTurnOnNum40.name = cms.string("PreSelectionUpperLowerTurnOnNum40")
PreSelectionUpperLowerTurnOnNum40.triggers = cms.vstring("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v")


LooseTurnOnDen = cms.PSet(
    name = cms.string("LooseTurnOnDen"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutPreMinNDSAsUpperOnly,
      cutDSAPtUpperOnly,
      cutPreDSAAtLeast4DtChambersWithValidHitsUpperOnly,
      cutPreDSANValidRpcHitsUpperOnly,
      cutPreDSANValidCscHitsUpperOnly,
      )
    )

#For HLT turn-on curve: numerator is preselection plus signal trigger
LooseTurnOnNum35 = copy.deepcopy(LooseTurnOnDen)
LooseTurnOnNum35.name = cms.string("LooseTurnOnNum35")
LooseTurnOnNum35.triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v")

#For HLT turn-on curve: numerator is preselection plus signal trigger
LooseTurnOnNum40 = copy.deepcopy(LooseTurnOnDen)
LooseTurnOnNum40.name = cms.string("LooseTurnOnNum40")
LooseTurnOnNum40.triggers = cms.vstring("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v")



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
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOutClosureTest)
DelayedMuonsUpperLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)

#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeOutIn)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeOutInClosureTest)

DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut.name = cms.string("DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut")
removeCuts(DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut.cuts,[cutLowerDSADtTofFreeInverseBeta])

DelayedMuonsUpperLowerOnlyThroughTimeOutInErr = copy.deepcopy(DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut)
DelayedMuonsUpperLowerOnlyThroughTimeOutInErr.name = cms.string("DelayedMuonsUpperLowerOnlyThroughTimeOutInErr")
removeCuts(DelayedMuonsUpperLowerOnlyThroughTimeOutInErr.cuts,[cutUpperLowerDSADeltaTimeInOut])


DelayedMuonsUpperLowerSelection2 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2.name = cms.string("DelayedMuonsUpperLowerSelection2")
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSAUpperP52Inverted)

#full selection with no trigger
DelayedMuonsUpperLowerNoTrigger = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerNoTrigger.name = cms.string("DelayedMuonsUpperLowerNoTrigger")
DelayedMuonsUpperLowerNoTrigger.triggers = cms.vstring("")

DelayedMuonsUpperLowerZMuMu = copy.deepcopy(PreSelectionUpperLowerZMuMu)
DelayedMuonsUpperLowerZMuMu.name = cms.string("DelayedMuonsUpperLowerZMuMu")
DelayedMuonsUpperLowerZMuMu.cuts.append(cutPreDSADtTofNDof)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerZMuMu.cuts.append(cutLowerDSADtTofFreeInverseBeta)

DelayedMuonsUpperLowerPtSmearedSelection = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerPtSmearedSelection.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelection")
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSAPtSmeared)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)


#ABCD regions
#first split into 2 regions (AB and CD) by applying RPC timing cut
DelayedMuonsUpperLowerSelectionRegionAB = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerSelectionRegionAB.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAB")
#DelayedMuonsUpperLowerSelectionRegionAB.cuts.append(cutLowerDSARpcBxPatternInverted)
DelayedMuonsUpperLowerSelectionRegionAB.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverageInverted)

DelayedMuonsUpperLowerSelectionRegionCD = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerSelectionRegionCD.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCD")
#DelayedMuonsUpperLowerSelectionRegionCD.cuts.append(cutLowerDSARpcBxPattern)
DelayedMuonsUpperLowerSelectionRegionCD.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)

#now split into 4 regions (A,B,C,D) by applying the various p cuts
DelayedMuonsUpperLowerSelectionRegionAUpperP52 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP52.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP52")
DelayedMuonsUpperLowerSelectionRegionAUpperP52.cuts.append(cutUpperLowerDSAUpperP52Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP52 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP52.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP52")
DelayedMuonsUpperLowerSelectionRegionBUpperP52.cuts.append(cutUpperLowerDSAUpperP52)

DelayedMuonsUpperLowerSelectionRegionCUpperP52 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP52.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP52")
DelayedMuonsUpperLowerSelectionRegionCUpperP52.cuts.append(cutUpperLowerDSAUpperP52Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP52 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP52.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP52")
DelayedMuonsUpperLowerSelectionRegionDUpperP52.cuts.append(cutUpperLowerDSAUpperP52)


DelayedMuonsUpperLowerSelectionRegionAUpperP53 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP53.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP53")
DelayedMuonsUpperLowerSelectionRegionAUpperP53.cuts.append(cutUpperLowerDSAUpperP53Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP53 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP53.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP53")
DelayedMuonsUpperLowerSelectionRegionBUpperP53.cuts.append(cutUpperLowerDSAUpperP53)

DelayedMuonsUpperLowerSelectionRegionCUpperP53 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP53.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP53")
DelayedMuonsUpperLowerSelectionRegionCUpperP53.cuts.append(cutUpperLowerDSAUpperP53Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP53 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP53.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP53")
DelayedMuonsUpperLowerSelectionRegionDUpperP53.cuts.append(cutUpperLowerDSAUpperP53)


DelayedMuonsUpperLowerSelectionRegionAUpperP55 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP55.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP55")
DelayedMuonsUpperLowerSelectionRegionAUpperP55.cuts.append(cutUpperLowerDSAUpperP55Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP55 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP55.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP55")
DelayedMuonsUpperLowerSelectionRegionBUpperP55.cuts.append(cutUpperLowerDSAUpperP55)

DelayedMuonsUpperLowerSelectionRegionCUpperP55 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP55.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP55")
DelayedMuonsUpperLowerSelectionRegionCUpperP55.cuts.append(cutUpperLowerDSAUpperP55Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP55 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP55.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP55")
DelayedMuonsUpperLowerSelectionRegionDUpperP55.cuts.append(cutUpperLowerDSAUpperP55)


DelayedMuonsUpperLowerSelectionRegionAUpperP60 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP60.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP60")
DelayedMuonsUpperLowerSelectionRegionAUpperP60.cuts.append(cutUpperLowerDSAUpperP60Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP60 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP60.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP60")
DelayedMuonsUpperLowerSelectionRegionBUpperP60.cuts.append(cutUpperLowerDSAUpperP60)

DelayedMuonsUpperLowerSelectionRegionCUpperP60 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP60.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP60")
DelayedMuonsUpperLowerSelectionRegionCUpperP60.cuts.append(cutUpperLowerDSAUpperP60Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP60 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP60.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP60")
DelayedMuonsUpperLowerSelectionRegionDUpperP60.cuts.append(cutUpperLowerDSAUpperP60)


DelayedMuonsUpperLowerSelectionRegionAUpperP63 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP63.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP63")
DelayedMuonsUpperLowerSelectionRegionAUpperP63.cuts.append(cutUpperLowerDSAUpperP63Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP63 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP63.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP63")
DelayedMuonsUpperLowerSelectionRegionBUpperP63.cuts.append(cutUpperLowerDSAUpperP63)

DelayedMuonsUpperLowerSelectionRegionCUpperP63 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP63.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP63")
DelayedMuonsUpperLowerSelectionRegionCUpperP63.cuts.append(cutUpperLowerDSAUpperP63Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP63 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP63.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP63")
DelayedMuonsUpperLowerSelectionRegionDUpperP63.cuts.append(cutUpperLowerDSAUpperP63)


DelayedMuonsUpperLowerSelectionRegionAUpperP65 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP65.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP65")
DelayedMuonsUpperLowerSelectionRegionAUpperP65.cuts.append(cutUpperLowerDSAUpperP65Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP65 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP65.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP65")
DelayedMuonsUpperLowerSelectionRegionBUpperP65.cuts.append(cutUpperLowerDSAUpperP65)

DelayedMuonsUpperLowerSelectionRegionCUpperP65 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP65.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP65")
DelayedMuonsUpperLowerSelectionRegionCUpperP65.cuts.append(cutUpperLowerDSAUpperP65Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP65 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP65.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP65")
DelayedMuonsUpperLowerSelectionRegionDUpperP65.cuts.append(cutUpperLowerDSAUpperP65)


DelayedMuonsUpperLowerSelectionRegionAUpperP70 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP70.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP70")
DelayedMuonsUpperLowerSelectionRegionAUpperP70.cuts.append(cutUpperLowerDSAUpperP70Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP70 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP70.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP70")
DelayedMuonsUpperLowerSelectionRegionBUpperP70.cuts.append(cutUpperLowerDSAUpperP70)

DelayedMuonsUpperLowerSelectionRegionCUpperP70 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP70.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP70")
DelayedMuonsUpperLowerSelectionRegionCUpperP70.cuts.append(cutUpperLowerDSAUpperP70Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP70 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP70.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP70")
DelayedMuonsUpperLowerSelectionRegionDUpperP70.cuts.append(cutUpperLowerDSAUpperP70)


DelayedMuonsUpperLowerSelectionRegionAUpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP90")
DelayedMuonsUpperLowerSelectionRegionAUpperP90.cuts.append(cutUpperLowerDSAUpperP90Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP90")
DelayedMuonsUpperLowerSelectionRegionBUpperP90.cuts.append(cutUpperLowerDSAUpperP90)

DelayedMuonsUpperLowerSelectionRegionCUpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP90")
DelayedMuonsUpperLowerSelectionRegionCUpperP90.cuts.append(cutUpperLowerDSAUpperP90Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP90")
DelayedMuonsUpperLowerSelectionRegionDUpperP90.cuts.append(cutUpperLowerDSAUpperP90)


DelayedMuonsUpperLowerSelectionRegionAUpperP100 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP100.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP100")
DelayedMuonsUpperLowerSelectionRegionAUpperP100.cuts.append(cutUpperLowerDSAUpperP100Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP100 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP100.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP100")
DelayedMuonsUpperLowerSelectionRegionBUpperP100.cuts.append(cutUpperLowerDSAUpperP100)

DelayedMuonsUpperLowerSelectionRegionCUpperP100 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP100.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP100")
DelayedMuonsUpperLowerSelectionRegionCUpperP100.cuts.append(cutUpperLowerDSAUpperP100Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP100 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP100.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP100")
DelayedMuonsUpperLowerSelectionRegionDUpperP100.cuts.append(cutUpperLowerDSAUpperP100)


DelayedMuonsUpperLowerSelectionRegionAUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP110.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP110")
DelayedMuonsUpperLowerSelectionRegionAUpperP110.cuts.append(cutUpperLowerDSAUpperP110Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP110.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP110")
DelayedMuonsUpperLowerSelectionRegionBUpperP110.cuts.append(cutUpperLowerDSAUpperP110)

DelayedMuonsUpperLowerSelectionRegionCUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP110.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP110")
DelayedMuonsUpperLowerSelectionRegionCUpperP110.cuts.append(cutUpperLowerDSAUpperP110Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP110.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP110")
DelayedMuonsUpperLowerSelectionRegionDUpperP110.cuts.append(cutUpperLowerDSAUpperP110)


DelayedMuonsUpperLowerSelectionRegionAUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP120.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP120")
DelayedMuonsUpperLowerSelectionRegionAUpperP120.cuts.append(cutUpperLowerDSAUpperP120Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP120.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP120")
DelayedMuonsUpperLowerSelectionRegionBUpperP120.cuts.append(cutUpperLowerDSAUpperP120)

DelayedMuonsUpperLowerSelectionRegionCUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP120.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP120")
DelayedMuonsUpperLowerSelectionRegionCUpperP120.cuts.append(cutUpperLowerDSAUpperP120Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP120.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP120")
DelayedMuonsUpperLowerSelectionRegionDUpperP120.cuts.append(cutUpperLowerDSAUpperP120)


DelayedMuonsUpperLowerSelectionRegionAUpperP130 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP130.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP130")
DelayedMuonsUpperLowerSelectionRegionAUpperP130.cuts.append(cutUpperLowerDSAUpperP130Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP130 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP130.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP130")
DelayedMuonsUpperLowerSelectionRegionBUpperP130.cuts.append(cutUpperLowerDSAUpperP130)

DelayedMuonsUpperLowerSelectionRegionCUpperP130 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP130.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP130")
DelayedMuonsUpperLowerSelectionRegionCUpperP130.cuts.append(cutUpperLowerDSAUpperP130Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP130 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP130.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP130")
DelayedMuonsUpperLowerSelectionRegionDUpperP130.cuts.append(cutUpperLowerDSAUpperP130)


DelayedMuonsUpperLowerSelectionRegionAUpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP150")
DelayedMuonsUpperLowerSelectionRegionAUpperP150.cuts.append(cutUpperLowerDSAUpperP150Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP150")
DelayedMuonsUpperLowerSelectionRegionBUpperP150.cuts.append(cutUpperLowerDSAUpperP150)

DelayedMuonsUpperLowerSelectionRegionCUpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP150")
DelayedMuonsUpperLowerSelectionRegionCUpperP150.cuts.append(cutUpperLowerDSAUpperP150Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP150")
DelayedMuonsUpperLowerSelectionRegionDUpperP150.cuts.append(cutUpperLowerDSAUpperP150)


DelayedMuonsUpperLowerSelectionRegionAUpperP160 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP160.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP160")
DelayedMuonsUpperLowerSelectionRegionAUpperP160.cuts.append(cutUpperLowerDSAUpperP160Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP160 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP160.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP160")
DelayedMuonsUpperLowerSelectionRegionBUpperP160.cuts.append(cutUpperLowerDSAUpperP160)

DelayedMuonsUpperLowerSelectionRegionCUpperP160 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP160.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP160")
DelayedMuonsUpperLowerSelectionRegionCUpperP160.cuts.append(cutUpperLowerDSAUpperP160Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP160 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP160.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP160")
DelayedMuonsUpperLowerSelectionRegionDUpperP160.cuts.append(cutUpperLowerDSAUpperP160)


DelayedMuonsUpperLowerSelectionRegionAUpperP170 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP170.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP170")
DelayedMuonsUpperLowerSelectionRegionAUpperP170.cuts.append(cutUpperLowerDSAUpperP170Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP170 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP170.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP170")
DelayedMuonsUpperLowerSelectionRegionBUpperP170.cuts.append(cutUpperLowerDSAUpperP170)

DelayedMuonsUpperLowerSelectionRegionCUpperP170 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP170.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP170")
DelayedMuonsUpperLowerSelectionRegionCUpperP170.cuts.append(cutUpperLowerDSAUpperP170Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP170 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP170.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP170")
DelayedMuonsUpperLowerSelectionRegionDUpperP170.cuts.append(cutUpperLowerDSAUpperP170)


DelayedMuonsUpperLowerSelectionRegionAUpperP190 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP190.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP190")
DelayedMuonsUpperLowerSelectionRegionAUpperP190.cuts.append(cutUpperLowerDSAUpperP190Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP190 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP190.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP190")
DelayedMuonsUpperLowerSelectionRegionBUpperP190.cuts.append(cutUpperLowerDSAUpperP190)

DelayedMuonsUpperLowerSelectionRegionCUpperP190 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP190.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP190")
DelayedMuonsUpperLowerSelectionRegionCUpperP190.cuts.append(cutUpperLowerDSAUpperP190Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP190 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP190.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP190")
DelayedMuonsUpperLowerSelectionRegionDUpperP190.cuts.append(cutUpperLowerDSAUpperP190)


DelayedMuonsUpperLowerSelectionRegionAUpperP200 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP200.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP200")
DelayedMuonsUpperLowerSelectionRegionAUpperP200.cuts.append(cutUpperLowerDSAUpperP200Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP200 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP200.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP200")
DelayedMuonsUpperLowerSelectionRegionBUpperP200.cuts.append(cutUpperLowerDSAUpperP200)

DelayedMuonsUpperLowerSelectionRegionCUpperP200 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP200.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP200")
DelayedMuonsUpperLowerSelectionRegionCUpperP200.cuts.append(cutUpperLowerDSAUpperP200Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP200 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP200.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP200")
DelayedMuonsUpperLowerSelectionRegionDUpperP200.cuts.append(cutUpperLowerDSAUpperP200)


DelayedMuonsUpperLowerSelectionRegionAUpperP230 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP230.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP230")
DelayedMuonsUpperLowerSelectionRegionAUpperP230.cuts.append(cutUpperLowerDSAUpperP230Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP230 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP230.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP230")
DelayedMuonsUpperLowerSelectionRegionBUpperP230.cuts.append(cutUpperLowerDSAUpperP230)

DelayedMuonsUpperLowerSelectionRegionCUpperP230 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP230.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP230")
DelayedMuonsUpperLowerSelectionRegionCUpperP230.cuts.append(cutUpperLowerDSAUpperP230Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP230 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP230.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP230")
DelayedMuonsUpperLowerSelectionRegionDUpperP230.cuts.append(cutUpperLowerDSAUpperP230)


DelayedMuonsUpperLowerSelectionRegionAUpperP240 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP240.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP240")
DelayedMuonsUpperLowerSelectionRegionAUpperP240.cuts.append(cutUpperLowerDSAUpperP240Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP240 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP240.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP240")
DelayedMuonsUpperLowerSelectionRegionBUpperP240.cuts.append(cutUpperLowerDSAUpperP240)

DelayedMuonsUpperLowerSelectionRegionCUpperP240 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP240.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP240")
DelayedMuonsUpperLowerSelectionRegionCUpperP240.cuts.append(cutUpperLowerDSAUpperP240Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP240 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP240.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP240")
DelayedMuonsUpperLowerSelectionRegionDUpperP240.cuts.append(cutUpperLowerDSAUpperP240)


DelayedMuonsUpperLowerSelectionRegionAUpperP260 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP260.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP260")
DelayedMuonsUpperLowerSelectionRegionAUpperP260.cuts.append(cutUpperLowerDSAUpperP260Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP260 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP260.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP260")
DelayedMuonsUpperLowerSelectionRegionBUpperP260.cuts.append(cutUpperLowerDSAUpperP260)

DelayedMuonsUpperLowerSelectionRegionCUpperP260 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP260.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP260")
DelayedMuonsUpperLowerSelectionRegionCUpperP260.cuts.append(cutUpperLowerDSAUpperP260Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP260 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP260.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP260")
DelayedMuonsUpperLowerSelectionRegionDUpperP260.cuts.append(cutUpperLowerDSAUpperP260)


DelayedMuonsUpperLowerSelectionRegionAUpperP290 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP290.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP290")
DelayedMuonsUpperLowerSelectionRegionAUpperP290.cuts.append(cutUpperLowerDSAUpperP290Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP290 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP290.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP290")
DelayedMuonsUpperLowerSelectionRegionBUpperP290.cuts.append(cutUpperLowerDSAUpperP290)

DelayedMuonsUpperLowerSelectionRegionCUpperP290 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP290.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP290")
DelayedMuonsUpperLowerSelectionRegionCUpperP290.cuts.append(cutUpperLowerDSAUpperP290Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP290 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP290.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP290")
DelayedMuonsUpperLowerSelectionRegionDUpperP290.cuts.append(cutUpperLowerDSAUpperP290)



#for closure test
#ABCD regions
#first split into 2 regions (AB and CD) by applying RPC timing cut
DelayedMuonsUpperLowerClosureTestSelectionRegionAB = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerClosureTestSelectionRegionAB.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionAB")
DelayedMuonsUpperLowerClosureTestSelectionRegionAB.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverageInvertedClosureTest)

DelayedMuonsUpperLowerClosureTestSelectionRegionCD = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerClosureTestSelectionRegionCD.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionCD")
DelayedMuonsUpperLowerClosureTestSelectionRegionCD.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverageClosureTest)

#now split into 4 regions (A,B,C,D) by applying the various p cuts
DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionAB)
DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP110.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP110")
DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP110.cuts.append(cutUpperLowerDSAUpperP110Inverted)

DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionAB)
DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP110.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP110")
DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP110.cuts.append(cutUpperLowerDSAUpperP110)

DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionCD)
DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP110.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP110")
DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP110.cuts.append(cutUpperLowerDSAUpperP110Inverted)

DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionCD)
DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP110.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP110")
DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP110.cuts.append(cutUpperLowerDSAUpperP110)


DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionAB)
DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP120.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP120")
DelayedMuonsUpperLowerClosureTestSelectionRegionAUpperP120.cuts.append(cutUpperLowerDSAUpperP120Inverted)

DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionAB)
DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP120.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP120")
DelayedMuonsUpperLowerClosureTestSelectionRegionBUpperP120.cuts.append(cutUpperLowerDSAUpperP120)

DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionCD)
DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP120.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP120")
DelayedMuonsUpperLowerClosureTestSelectionRegionCUpperP120.cuts.append(cutUpperLowerDSAUpperP120Inverted)

DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerClosureTestSelectionRegionCD)
DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP120.name = cms.string("DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP120")
DelayedMuonsUpperLowerClosureTestSelectionRegionDUpperP120.cuts.append(cutUpperLowerDSAUpperP120)





#for ABCD method systematic
DelayedMuonsUpperLowerSelectionRegionA1UpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionA1UpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA1UpperP90")
DelayedMuonsUpperLowerSelectionRegionA1UpperP90.cuts.append(cutUpperLowerDSAUpperP90Inverted)

DelayedMuonsUpperLowerSelectionRegionA2UpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionA2UpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA2UpperP90")
DelayedMuonsUpperLowerSelectionRegionA2UpperP90.cuts.append(cutUpperLowerDSAUpperPGreater90Less150)

DelayedMuonsUpperLowerSelectionRegionC1UpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionC1UpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionC1UpperP90")
DelayedMuonsUpperLowerSelectionRegionC1UpperP90.cuts.append(cutUpperLowerDSAUpperP90Inverted)

DelayedMuonsUpperLowerSelectionRegionC2UpperP90 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionC2UpperP90.name = cms.string("DelayedMuonsUpperLowerSelectionRegionC2UpperP90")
DelayedMuonsUpperLowerSelectionRegionC2UpperP90.cuts.append(cutUpperLowerDSAUpperPGreater90Less150)











DelayedMuonsUpperLowerSelectionRegionA1B1 = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerSelectionRegionA1B1.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA1B1")
DelayedMuonsUpperLowerSelectionRegionA1B1.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverageGreaterNeg1p2LessNeg0p9)

DelayedMuonsUpperLowerSelectionRegionA2B2 = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerSelectionRegionA2B2.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA2B2")
DelayedMuonsUpperLowerSelectionRegionA2B2.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverageLessNeg1p2)
 

DelayedMuonsUpperLowerSelectionRegionA1UpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionA1B1)
DelayedMuonsUpperLowerSelectionRegionA1UpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA1UpperP150")
DelayedMuonsUpperLowerSelectionRegionA1UpperP150.cuts.append(cutUpperLowerDSAUpperP150Inverted)

DelayedMuonsUpperLowerSelectionRegionA2UpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionA2B2)
DelayedMuonsUpperLowerSelectionRegionA2UpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionA2UpperP150")
DelayedMuonsUpperLowerSelectionRegionA2UpperP150.cuts.append(cutUpperLowerDSAUpperP150Inverted)


DelayedMuonsUpperLowerSelectionRegionB1UpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionA1B1)
DelayedMuonsUpperLowerSelectionRegionB1UpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionB1UpperP150")
DelayedMuonsUpperLowerSelectionRegionB1UpperP150.cuts.append(cutUpperLowerDSAUpperP150)

DelayedMuonsUpperLowerSelectionRegionB2UpperP150 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionA2B2)
DelayedMuonsUpperLowerSelectionRegionB2UpperP150.name = cms.string("DelayedMuonsUpperLowerSelectionRegionB2UpperP150")
DelayedMuonsUpperLowerSelectionRegionB2UpperP150.cuts.append(cutUpperLowerDSAUpperP150)






#pt smeared for signal systematic
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP52 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP52.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP52")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP52.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP52.cuts.append(cutUpperLowerDSAUpperPSmeared52)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP53 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP53.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP53")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP53.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP53.cuts.append(cutUpperLowerDSAUpperPSmeared53)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP55 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP55.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP55")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP55.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP55.cuts.append(cutUpperLowerDSAUpperPSmeared55)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP60 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP60.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP60")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP60.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP60.cuts.append(cutUpperLowerDSAUpperPSmeared60)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP63 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP63.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP63")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP63.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP63.cuts.append(cutUpperLowerDSAUpperPSmeared63)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP65 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP65.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP65")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP65.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP65.cuts.append(cutUpperLowerDSAUpperPSmeared65)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP70 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP70.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP70")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP70.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP70.cuts.append(cutUpperLowerDSAUpperPSmeared70)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP90 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP90.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP90")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP90.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP90.cuts.append(cutUpperLowerDSAUpperPSmeared90)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP100 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP100.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP100")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP100.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP100.cuts.append(cutUpperLowerDSAUpperPSmeared100)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP110 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP110.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP110")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP110.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP110.cuts.append(cutUpperLowerDSAUpperPSmeared110)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP120 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP120.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP120")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP120.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP120.cuts.append(cutUpperLowerDSAUpperPSmeared120)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP130 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP130.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP130")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP130.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP130.cuts.append(cutUpperLowerDSAUpperPSmeared130)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP150 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP150.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP150")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP150.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP150.cuts.append(cutUpperLowerDSAUpperPSmeared150)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP160 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP160.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP160")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP160.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP160.cuts.append(cutUpperLowerDSAUpperPSmeared160)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP170 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP170.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP170")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP170.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP170.cuts.append(cutUpperLowerDSAUpperPSmeared170)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP190 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP190.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP190")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP190.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP190.cuts.append(cutUpperLowerDSAUpperPSmeared190)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP200 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP200.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP200")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP200.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP200.cuts.append(cutUpperLowerDSAUpperPSmeared200)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP230 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP230.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP230")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP230.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP230.cuts.append(cutUpperLowerDSAUpperPSmeared230)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP240 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP240.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP240")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP240.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP240.cuts.append(cutUpperLowerDSAUpperPSmeared240)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP260 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP260.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP260")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP260.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP260.cuts.append(cutUpperLowerDSAUpperPSmeared260)

DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP290 = copy.deepcopy(DelayedMuonsUpperLowerPtSmearedSelection)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP290.name = cms.string("DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP290")
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP290.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)
DelayedMuonsUpperLowerPtSmearedSelectionRegionDUpperP290.cuts.append(cutUpperLowerDSAUpperPSmeared290)

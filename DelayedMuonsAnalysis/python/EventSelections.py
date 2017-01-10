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
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeOutInErr)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut2015)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut2016)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOutClosureTest)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeOutIn)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeOutInClosureTest)
DelayedMuonsUpperLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)


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

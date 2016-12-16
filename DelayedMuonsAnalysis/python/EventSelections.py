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
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAEta)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)

DelayedMuonsUpperLowerDTchambers2Selection = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerDTchambers2Selection.name = cms.string("DelayedMuonsUpperLowerDTchambers2Selection")
DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSAPt)
#DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSAEta)
DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerDTchambers2Selection.cuts.append(cutUpperLowerDSADeltaTimeInOut)

DelayedMuonsUpperLowerDTchambers3Selection = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerDTchambers3Selection.name = cms.string("DelayedMuonsUpperLowerDTchambers3Selection")
DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSAPt)
#DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSAEta)
DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSANDtChambersWithValidHitsTight)
DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSANValidRpcHits)
#DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSADtTofTimeInOut)
DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerDTchambers3Selection.cuts.append(cutUpperLowerDSADeltaTimeInOut)

DelayedMuonsUpperLowerDTchambers2FreeInvBetaLowerSelection = copy.deepcopy(DelayedMuonsUpperLowerDTchambers2Selection)
DelayedMuonsUpperLowerDTchambers2FreeInvBetaLowerSelection.name = cms.string("DelayedMuonsUpperLowerDTchambers2FreeInvBetaLowerSelection")
DelayedMuonsUpperLowerDTchambers2FreeInvBetaLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)

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


DelayedMuonsUpperLowerSelectionRegionAUpperP250 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP250.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP250")
DelayedMuonsUpperLowerSelectionRegionAUpperP250.cuts.append(cutUpperLowerDSAUpperP250Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP250 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP250.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP250")
DelayedMuonsUpperLowerSelectionRegionBUpperP250.cuts.append(cutUpperLowerDSAUpperP250)

DelayedMuonsUpperLowerSelectionRegionCUpperP250 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP250.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP250")
DelayedMuonsUpperLowerSelectionRegionCUpperP250.cuts.append(cutUpperLowerDSAUpperP250Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP250 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP250.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP250")
DelayedMuonsUpperLowerSelectionRegionDUpperP250.cuts.append(cutUpperLowerDSAUpperP250)


DelayedMuonsUpperLowerSelectionRegionAUpperP300 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP300.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP300")
DelayedMuonsUpperLowerSelectionRegionAUpperP300.cuts.append(cutUpperLowerDSAUpperP300Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP300 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP300.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP300")
DelayedMuonsUpperLowerSelectionRegionBUpperP300.cuts.append(cutUpperLowerDSAUpperP300)

DelayedMuonsUpperLowerSelectionRegionCUpperP300 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP300.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP300")
DelayedMuonsUpperLowerSelectionRegionCUpperP300.cuts.append(cutUpperLowerDSAUpperP300Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP300 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP300.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP300")
DelayedMuonsUpperLowerSelectionRegionDUpperP300.cuts.append(cutUpperLowerDSAUpperP300)


DelayedMuonsUpperLowerSelectionRegionAUpperP400 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionAUpperP400.name = cms.string("DelayedMuonsUpperLowerSelectionRegionAUpperP400")
DelayedMuonsUpperLowerSelectionRegionAUpperP400.cuts.append(cutUpperLowerDSAUpperP400Inverted)

DelayedMuonsUpperLowerSelectionRegionBUpperP400 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionAB)
DelayedMuonsUpperLowerSelectionRegionBUpperP400.name = cms.string("DelayedMuonsUpperLowerSelectionRegionBUpperP400")
DelayedMuonsUpperLowerSelectionRegionBUpperP400.cuts.append(cutUpperLowerDSAUpperP400)

DelayedMuonsUpperLowerSelectionRegionCUpperP400 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionCUpperP400.name = cms.string("DelayedMuonsUpperLowerSelectionRegionCUpperP400")
DelayedMuonsUpperLowerSelectionRegionCUpperP400.cuts.append(cutUpperLowerDSAUpperP400Inverted)

DelayedMuonsUpperLowerSelectionRegionDUpperP400 = copy.deepcopy(DelayedMuonsUpperLowerSelectionRegionCD)
DelayedMuonsUpperLowerSelectionRegionDUpperP400.name = cms.string("DelayedMuonsUpperLowerSelectionRegionDUpperP400")
DelayedMuonsUpperLowerSelectionRegionDUpperP400.cuts.append(cutUpperLowerDSAUpperP400)

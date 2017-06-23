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
cutPreDSAPtGeneric = copy.deepcopy(cutPreDSAPtExactlyOne)
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
      cutPrePreDSADtTofNDofExactlyOne,
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
      #cutPreDSAUpperAndLower,
      cutPreDSAExactly1UpperAndExactly1Lower,
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
      cutDSAPtExactlyOne,
      cutPreDSANDtChambersWithValidHitsExactlyOne,
      cutPreDSANValidRpcHitsExactlyOne,
      cutPreDSANValidCscHitsExactlyOne,
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
      cutPreMinNDSAsExactlyOne,
      cutPreMaxNDSAsExactlyOne,
      cutPreDSAUpperOnly,
      cutPreDSAPtExactlyOne,
      cutPreDSANDtChambersWithValidHitsExactlyOne,
      cutPreDSANValidRpcHitsExactlyOne,
      cutPreDSADtTofNDofExactlyOne,
      cutPreDSANValidCscHitsExactlyOne,
      )
    )

PreSelectionLowerOnly = cms.PSet(
    name = cms.string("PreSelectionLowerOnly"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAsExactlyOne,
      cutPreMaxNDSAsExactlyOne,
      cutPreDSALowerOnly,
      cutPreDSAPtExactlyOne,
      cutPreDSANDtChambersWithValidHitsExactlyOne,
      cutPreDSANValidRpcHitsExactlyOne,
      cutPreDSADtTofNDofExactlyOne,
      cutPreDSANValidCscHitsExactlyOne,
      )
    )


PreSelectionAtLeastOneUpper = cms.PSet(
    name = cms.string("PreSelectionAtLeastOneUpper"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAsExactlyOne,
      cutPreDSAAtLeastOneUpper,
      cutPreDSAPtAtLeastOne,
      cutPreDSANDtChambersWithValidHitsAtLeastOne,
      cutPreDSANValidRpcHitsAtLeastOne,
      cutPreDSADtTofNDofAtLeastOne,
      cutPreDSANValidCscHitsAtLeastOne,
      )
    )

PreSelectionAtLeastOneLower = cms.PSet(
    name = cms.string("PreSelectionAtLeastOneLower"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAsExactlyOne,
      cutPreDSAAtLeastOneLower,
      cutPreDSAPtAtLeastOne,
      cutPreDSANDtChambersWithValidHitsAtLeastOne,
      cutPreDSANValidRpcHitsAtLeastOne,
      cutPreDSADtTofNDofAtLeastOne,
      cutPreDSANValidCscHitsAtLeastOne,
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
      #cutPreDSAUpperAndLower,
      cutPreDSAExactly1UpperAndExactly1Lower,
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
      #cutPreDSAUpperAndLower,
      cutPreDSAExactly1UpperAndExactly1Lower,
      cutPreDSAPt,
      cutPreDSANDtChambersWithValidHits,
      cutPreDSANValidRpcHits,
      cutPreDSANValidCscHits,
      )
    )

PreSelectionExactly1UpperExactly1Lower = cms.PSet(
    name = cms.string("PreSelectionExactly1UpperExactly1Lower"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAs,
      cutPreDSAExactly1UpperAndExactly1Lower,
      cutPreDSA3DangleBackToBack,
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


LooseTurnOnDen = cms.PSet(
    name = cms.string("LooseTurnOnDen"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutPreMinNDSAsExactlyOne,
      cutDSAPtExactlyOne,
      cutPreDSAAtLeast4DtChambersWithValidHitsExactlyOne,
      cutPreDSANValidRpcHitsExactlyOne,
      cutPreDSANValidCscHitsExactlyOne,
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
DelayedMuonsUpperOnlySelection.cuts.append(cutDSANDtChambersWithValidHits)
DelayedMuonsUpperOnlySelection.cuts.append(cutDSANValidRpcHits)
DelayedMuonsUpperOnlySelection.cuts.append(cutDSADtTofTimeInOutErr)

DelayedMuonsLowerOnlySelection = copy.deepcopy(PreSelectionLowerOnly)
DelayedMuonsLowerOnlySelection.name = cms.string("DelayedMuonsLowerOnlySelection")
DelayedMuonsLowerOnlySelection.cuts.append(cutDSAPt)
DelayedMuonsLowerOnlySelection.cuts.append(cutDSANDtChambersWithValidHits)
DelayedMuonsLowerOnlySelection.cuts.append(cutDSANValidRpcHits)
DelayedMuonsLowerOnlySelection.cuts.append(cutDSADtTofTimeInOutErr)
DelayedMuonsLowerOnlySelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)


DelayedMuonsAtLeastOneUpperSelection = copy.deepcopy(PreSelectionAtLeastOneUpper)
DelayedMuonsAtLeastOneUpperSelection.name = cms.string("DelayedMuonsAtLeastOneUpperSelection")
DelayedMuonsAtLeastOneUpperSelection.cuts.append(cutDSAPtAtLeastOne)
DelayedMuonsAtLeastOneUpperSelection.cuts.append(cutDSANDtChambersWithValidHitsAtLeastOne)
DelayedMuonsAtLeastOneUpperSelection.cuts.append(cutDSANValidRpcHitsAtLeastOne)
DelayedMuonsAtLeastOneUpperSelection.cuts.append(cutDSADtTofTimeInOutErrAtLeastOne)

DelayedMuonsAtLeastOneLowerSelection = copy.deepcopy(PreSelectionAtLeastOneLower)
DelayedMuonsAtLeastOneLowerSelection.name = cms.string("DelayedMuonsAtLeastOneLowerSelection")
DelayedMuonsAtLeastOneLowerSelection.cuts.append(cutDSAPtAtLeastOne)
DelayedMuonsAtLeastOneLowerSelection.cuts.append(cutDSANDtChambersWithValidHitsAtLeastOne)
DelayedMuonsAtLeastOneLowerSelection.cuts.append(cutDSANValidRpcHitsAtLeastOne)
DelayedMuonsAtLeastOneLowerSelection.cuts.append(cutDSADtTofTimeInOutErrAtLeastOne)
DelayedMuonsAtLeastOneLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBetaAtLeastOne)

#full analysis upper and lower selection
DelayedMuonsUpperLowerSelection = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection.name = cms.string("DelayedMuonsUpperLowerSelection")
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
#DelayedMuonsUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOutClosureTest)


DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut = copy.deepcopy(DelayedMuonsUpperLowerSelection)
DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut.name = cms.string("DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut")
removeCuts(DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut.cuts,[cutLowerDSADtTofFreeInverseBeta])

DelayedMuonsUpperLowerOnlyThroughTimeOutInErr = copy.deepcopy(DelayedMuonsUpperLowerOnlyThroughDeltaTimeInOut)
DelayedMuonsUpperLowerOnlyThroughTimeOutInErr.name = cms.string("DelayedMuonsUpperLowerOnlyThroughTimeOutInErr")
removeCuts(DelayedMuonsUpperLowerOnlyThroughTimeOutInErr.cuts,[cutUpperLowerDSADeltaTimeInOut])


DelayedMuonsExactly1UpperExactly1LowerSelection = copy.deepcopy(PreSelectionExactly1UpperExactly1Lower)
DelayedMuonsExactly1UpperExactly1LowerSelection.name = cms.string("DelayedMuonsExactly1UpperExactly1LowerSelection")
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
#DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOutClosureTest)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)


DelayedMuonsUpperLowerSelection2 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2.name = cms.string("DelayedMuonsUpperLowerSelection2")
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2.cuts.append(cutLowerDSADtTofFreeInverseBeta)
#DelayedMuonsUpperLowerSelection2.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg50)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg45)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg40)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg35)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg30)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg25)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg20)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg15)

DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10 = copy.deepcopy(PreSelectionUpperLower)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.name = cms.string("DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10")
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerSelection2DeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg10)





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
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)

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


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

#tag
TagAndProbeDen = cms.PSet(
    name = cms.string("TagAndProbeDen"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v","HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_v","HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v"),
    #triggers = cms.vstring("HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v","HLT_L2Mu10_NoVertex_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutPreMinNDSAsExactlyOne,
      cutPreDSAUpperOnly,
      cutPreDSAPtAtLeastOne,
      cutPreDSANDtChambersWithValidHitsAtLeastOne,
      cutPreDSANValidRpcHitsAtLeastOne,
      cutPreDSADtTofNDofAtLeastOne,
      cutPreDSANValidCscHitsAtLeastOne,
      )
    )

#tag and probe
TagAndProbeNum = copy.deepcopy(TagAndProbeDen)
TagAndProbeNum.name = cms.string("TagAndProbeNum")
TagAndProbeNum.cuts.append(cutPreDSAExactly1UpperAndExactly1Lower)

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



DelayedMuonsExactly1UpperExactly1LowerSelection = copy.deepcopy(PreSelectionExactly1UpperExactly1Lower)
DelayedMuonsExactly1UpperExactly1LowerSelection.name = cms.string("DelayedMuonsExactly1UpperExactly1LowerSelection")
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSAPt)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
DelayedMuonsExactly1UpperExactly1LowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)


BackgroundExtrapolationUpperLowerSelection = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelection.name = cms.string("BackgroundExtrapolationUpperLowerSelection")
BackgroundExtrapolationUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg50)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg45)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg40)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg35)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg30)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg25)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg20)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg15)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg10)


BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg999ToNeg50.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg999ToNeg50)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg50ToNeg45.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg50ToNeg45)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg45ToNeg40.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg45ToNeg40)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg40ToNeg35.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg40ToNeg35)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg35ToNeg30.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg35ToNeg30)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg30ToNeg25.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg30ToNeg25)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg25ToNeg20.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg25ToNeg20)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg20ToNeg15.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg20ToNeg15)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg15ToNeg10.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg15ToNeg10)

BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5 = copy.deepcopy(PreSelectionUpperLower)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.name = cms.string("BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5")
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutUpperLowerDSAPt)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutUpperLowerDSANValidRpcHits)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutLowerDSADtTofFreeInverseBeta)
BackgroundExtrapolationUpperLowerSelectionDeltaTrpcTimeNeg10ToNeg7P5.cuts.append(cutUpperLowerDSADeltaRpcTimeNeg10ToNeg7P5)



UpperLowerZMuMuSelection = copy.deepcopy(PreSelectionUpperLowerZMuMu)
UpperLowerZMuMuSelection.name = cms.string("UpperLowerZMuMuSelection")
UpperLowerZMuMuSelection.cuts.append(cutPreDSADtTofNDof)
UpperLowerZMuMuSelection.cuts.append(cutUpperLowerDSAPt)
UpperLowerZMuMuSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
UpperLowerZMuMuSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
UpperLowerZMuMuSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
UpperLowerZMuMuSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)
UpperLowerZMuMuSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)

#full analysis upper and lower selection
FullUpperLowerSelection = copy.deepcopy(PreSelectionUpperLower)
FullUpperLowerSelection.name = cms.string("FullUpperLowerSelection")
FullUpperLowerSelection.cuts.append(cutUpperLowerDSAPt)
FullUpperLowerSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
FullUpperLowerSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
FullUpperLowerSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
FullUpperLowerSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)
FullUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
FullUpperLowerSelection.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)

FullUpperLowerPtSmearedSelection = copy.deepcopy(PreSelectionUpperLower)
FullUpperLowerPtSmearedSelection.name = cms.string("FullUpperLowerPtSmearedSelection")
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSAPtSmeared)
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSANDtChambersWithValidHits)
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSANValidRpcHits)
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADtTofTimeInOutErr)
FullUpperLowerPtSmearedSelection.cuts.append(cutLowerDSADtTofFreeInverseBeta)
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADeltaTimeInOut)
FullUpperLowerPtSmearedSelection.cuts.append(cutUpperLowerDSADeltaRpcHitBxAverage)

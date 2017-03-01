import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *

#full analysis selection
StoppPtlsSelection = cms.PSet(
    name = cms.string("StoppedParticlesSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutCscSegNumber,
      cutHavingNoCscSegNHit56,
      #cutCscSegNumber,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      #cutMaxDeltaJetPhi,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      cutMinDeltaROuterRpcInnerDT,
      #newNOuterAllBarrelRPCHitsDeltaR,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
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

#Full 2016 stopped particles analysis cuts
StoppPtlsSelection_2016 = cms.PSet(
    name = cms.string("StoppedParticlesSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    #triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutCscSegNumber,
      cutHavingNoCscSegNHit56,
      #cutNoBeamHaloCscNearJet,
      #cutMinDeltaPhiCscDt,
      #cutMinDeltaPhiCscPair,
      #cutOuterDT,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      #cutMaxDeltaJetPhi,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      #newNOuterAllBarrelRPCHitsDeltaR,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      #cutCscSeg,
      #cutNOuterCsc,
      #cutMinDeltaPhiCscDt,
      #cutMinDeltaPhiCscPair,
      #cutOneCscSeg,
      #cutMaxDeltaPhiCscDt,
      #cutMaxDeltaPhiCscPair,
      #cutOuterDT,
      #cutDTPair,
      #cutMaxDeltaJetPhi,
      #newNOuterAllBarrelRPCHitsDeltaR,
      #cutNoDT,
      #cutNoOuterBarrelRPC,
      #cutMinDeltaPhiOuterCscJet
      #cutNCaloTowerDiffRBX,
    )
)

#Halo Selection (invert halo veto)
HaloSelection = cms.PSet(
    name = cms.string("BeamHaloSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutCscSegNumberInverted
      )
)

#Halo N-1 Selection (full selection except halo veto)
#For nCscSeg plot
HaloControlSelection = cms.PSet(
    name = cms.string("BeamHaloControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutOuterDT,
      #cutDTPair,
      #cutMaxDeltaJetPhi,
      #newNOuterAllBarrelRPCHitsDeltaR,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
    )
)
######For closure test only
HaloControlSelectionClosure = cms.PSet(
    name = cms.string("BeamHaloControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergyInverted,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      CutHavingSpecificCsc,
      CutCscFilter
    )
)
SPEventSelctionClosure = cms.PSet(
    name = cms.string("SPSelectionClosure"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergyInverted,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      CutHavingSpecificCsc,
      CutCscFilter,
      cutCscSegNumber
    )
)

#Halo tag and probe Selection
HaloTagAndProbeSelection = cms.PSet(
    name = cms.string("BeamHaloTagAndProbeSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        cutJetNumber,
        cutCscSegNLayers,
        cutMinDeltaPhiCscJet
        )
)

#Cosmic Selection (invert cosmic veto and cut out halo)
CosmicSelection = cms.PSet(
    name = cms.string("CosmicMuonSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        #cosmics but not halo
        cutCscSegNumber 
        )
)

#Cosmic N-1 selection (full selection except cosmic veto)
#For RPC hits and DT segment plots
CosmicControlSelection = cms.PSet(
    name = cms.string("CosmicMuonControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutCscSegNumber,
      cutHavingNoCscSegNHit56,
      #cutNoBeamHaloCscNearJet,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
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

#Noise Selection (invert noise veto)
NoiseSelection = cms.PSet(
    name = cms.string("HcalNoiseSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutNoiseInverted
      )
)

#Noise N-1 ish Selection (preselection [cutJetEnergy + cutJetEta] + cosmic veto + halo veto)
#For noise filter result, n90jet, ntowiPhi, and other noise plots
NoiseControlSelection = cms.PSet(
    name = cms.string("HcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutCscSegNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutJetEnergy,
      cutJetEta,
    )
)

NoiseControlSelectionTight = cms.PSet(
    name = cms.string("HcalNoiseControlTightSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHavingNoCscSegNHit56,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
      cutJetEnergy,
      cutJetEta,
      cutNoise,
      #cutNTowerDiffiEtaSameiRbx,
      cutMaxiEtaDiffSameiRbx,
#      cutJetN90,
#      cutTowerIPhi,
#      cutTowerFraction,
#      cutNTowerSameiRbx,
    )
)

NoiseControlSelectionTight_2016 = cms.PSet(
    name = cms.string("HcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      #cutCscSegNumber,
      cutHavingNoCscSegNHit56,
      cutOuterDT,
      #cutOuterRpc,
      #cutRpcPair,
      #cutCloseRpcPair,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutDTPair,
      cutMaxDeltaJetPhi,
      #cutJetEnergy,
      #cutJetEta,
    )
)

#Alternate Noise N-1 ish Selection (preselection [cutJetEnergy + cutJetEta] + vertex veto + cosmic veto(no RPC hits) + halo veto)
AltNoiseControlSelection = cms.PSet(
    name = cms.string("AltHcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutVertexNumber,
      cutCscSegNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      cutJetEnergy,
      cutJetEta,
    )
)

#Pre Pre Selection (trigger + BX veto + vertex veto)
#For jetE, jetEta plots
PrePreSelection = cms.PSet(
    name = cms.string("PrePreSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      )
)

#Signal Trigger Selection
#For vertex number plot
TriggerSelection = cms.PSet(
    name = cms.string("TriggerSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutDummy,
      )
)

TriggerSelection_2016 = cms.PSet(
    name = cms.string("TriggerSelection2016"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_v"),
    cuts = cms.VPSet(
        CutHavingSpecificCsc,
        CutCscFilter,
       # CutCscEndcap,
       # CutCscStation,
        cutDummy,
      )
)

ControlTriggerSelection_2016 = cms.PSet(
    name = cms.string("ControlTriggerSelection2016"),
    triggers = cms.vstring("HLT_JetE30_NoBPTX_v"),
    cuts = cms.VPSet(
        cutDummy,
      )
)

#for trigger turn on: run over ntuples where only control triggers are used in the selection 

DenominatorTriggerTurnOnSelection2016 = cms.PSet(
    name = cms.string("DenominatorTriggerTurnOnSelection2016"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,        
        cutCscSegNumber,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        )
    )

NumeratorTriggerTurnOnSelection2016 = cms.PSet(
    name = cms.string("NumeratorTriggerTurnOnSelection2016"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_v"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutCscSegNumber,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        )
    )

#Selection for Second Jet analysis
SecondJetSelection = cms.PSet(
     name = cms.string("SecondJetSelection"),
     triggers = cms.vstring(),
     cuts = cms.VPSet(
     )
)

#Only stopped particle in EB or HB cut
StoppedParticleEBHBSelection = cms.PSet(
    name = cms.string("StoppedParticleEBHBSelection"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        cutStoppedParticleEBHB
        )
    )

#No cuts (including no trigger) selection
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        cutNIsolatedNoiseChannel,
        cutIsolatedNoiseSumE,
        cutIsolatedNoiseSumEt,
        cutJetEta,
        cutJetEnergyGt30,
        cutNoise,
        #cutHpdR1,
        #cutHpdR2,
        #cutHpdRPeak,
        #cutHpdRPeakSample,
        #cutHpdROuter,
        cutNoBeamHaloCscNearJet,
        #cutMinDeltaPhiCscPair,
        #cutMinDeltaPhiCscDt,
        cutMaxDeltaPhiCscDt,
        cutMaxDeltaPhiCscPair,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        #cutNoDT,
        #cutNoOuterBarrelRPC,
        cutMinDeltaPhiOuterCscJet,
        )
    )

Rpc_study = cms.PSet(
    name = cms.string("RpcStudy"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        cutCscSegNumber,
        cutDT,
    )
)

cosmicCoarse = cms.PSet(
    name = cms.string("cosmicCoarse"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutCosmicCoarse,
        cutJetEnergy,
        cutJetEta,
    )
)

haloCoarse = cms.PSet(
    name = cms.string("haloCoarse"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutHaloCoarse,
        cutJetEnergy,
        cutJetEta,
    )
)

cosmicStrict = cms.PSet(
    name = cms.string("cosmicStrict"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutCosmicStrict,
        cutCscSegNumber,
        #cutJetEnergy,
        cutJetEta,
    )
)

haloStrict = cms.PSet(
    name = cms.string("haloStrict"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutHaloStrict,
        cutNoise,
        cutDT,
        cutJetEnergy,
        cutJetEta,
        cutDeltaMinCscJet,
    )
)

noiseBasic = cms.PSet(
    name = cms.string("noiseBasic"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

noiseRBXRiched = cms.PSet(
    name = cms.string("noiseRBXRiched"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdR2Noise,
      cutJetEta,
      cutJetN90LT2,
      cutNoBeamHaloCscNearJet,
    )
)

noiseRBXRiched_oldHaloVeto = cms.PSet(
    name = cms.string("noiseRBXRichedOldHaloVeto"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdR2Noise,
      cutJetEta,
      cutJetN90LT2,
      cutNoBeamHaloCscNearJet,
      cutCscSegNumber,
    )
)

noiseRBXRiched_newHaloVeto = cms.PSet(
    name = cms.string("noiseRBXRichedNewHaloVeto"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdR2Noise,
      cutJetEta,
      cutJetN90LT2,
      cutNoBeamHaloCscNearJet,
      cutHavingNoCscSegNHit56,
    )
)

noiseRBXRiched_newHaloVetoSyst = cms.PSet(
    name = cms.string("noiseRBXRichedNewHaloVetoSyst"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdRPeakNoise,
      cutJetEta,
      cutPassNoiseTowerFraction,
      cutNoBeamHaloCscNearJet,
      cutHavingNoCscSegNHit56,
    )
)

noiseRBXRiched_oldCosmicVeto = cms.PSet(
    name = cms.string("noiseRBXRichedOldCosmicVeto"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdR2Noise,
      cutJetEta,
      cutJetN90LT2,
      cutNoBeamHaloCscNearJet,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

noiseRBXRiched_newCosmicVeto = cms.PSet(
    name = cms.string("noiseRBXRichedNewCosmicVeto"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdR2Noise,
      cutJetEta,
      cutJetN90LT2,
      cutNoBeamHaloCscNearJet,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
    )
)

noiseRBXRiched_newCosmicVetoSyst = cms.PSet(
    name = cms.string("noiseRBXRichedNewCosmicVetoSyst"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHpdRPeakNoise,
      cutJetEta,
      cutPassNoiseTowerFraction,
      cutNoBeamHaloCscNearJet,
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      cutMinDeltaRDTST4RPCInner3Layers,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
    )
)

noiseRBXRichedGT1CSC = cms.PSet(
    name = cms.string("noiseRBXRichedGT1CSC"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutTowerIPhiNoise,
      cutHpdR2Noise,
      cutDeltaMinCscJet,
#      cutJetEnergy,
      cutJetEta,
      #cutCscSegNumberInverted,
    )
)

noiseRBXRichedGT1DT = cms.PSet(
    name = cms.string("noiseRBXRichedGT1DT"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutTowerIPhiNoise,
      cutHpdR2Noise,
      cutDeltaMinCscJet,
#      cutJetEnergy,
      cutJetEta,
      cutNumberOfDT,
    )
)

noiseRBXRichedGT1CSC1DT = cms.PSet(
    name = cms.string("noiseRBXRichedGT1CSC1DT"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutTowerIPhiNoise,
      cutHpdR2Noise,
      cutDeltaMinCscJet,
#      cutJetEnergy,
      cutJetEta,
      cutCscSegNumberInverted,
      cutNumberOfDT,
    )
)

testHaloBeamFilter = cms.PSet(
    name = cms.string("testHaloBeamFilter"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
        #cutCscSegNumberInverted,
        cutCscSegNumberGT1,
    )
)

testHaloBeamFilterWithCosmicVeto = cms.PSet(
    name = cms.string("testHaloBeamFilterWithCosmicVeto"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
#        cutCscSegNumberInverted,
        cutCscSegNumberGT1,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
    )
)

testHaloBeamFilterOnNoiseEvent = cms.PSet(
    name = cms.string("testHaloBeamFilterOnNoiseEvent"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoiseInverted,
        cutBeamHaloFilter2016Tight
    )
)

makeHaloNCscPlotBeam1 = cms.PSet(
    name = cms.string("makeHaloNCscPlotBeam1"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutBeamHaloCscNearJet,
        cutNoise,
        #cutNCscSegJetDelta0p2,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        cutBeam1,
        cutNoCscNeg,
    )
)

makeHaloNCscPlotBeam2 = cms.PSet(
    name = cms.string("makeHaloNCscPlotBeam2"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutBeamHaloCscNearJet,
        cutNoise,
        #cutNCscSegJetDelta0p2,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        cutBeam2,
    )
)

makeHaloCscPlot = cms.PSet(
    name = cms.string("makeHaloCscPlot"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoiseInverted,
        cutDeltaMinCscJet,
        cutCscSegNumberGT1JET,
    )
)

makeHaloNCscPlotNoPos = cms.PSet(
    name = cms.string("makeHaloNCscPlotNoPos"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
        cutNCscSegJetDelta0p2,
        cutNoCscSegJetDeltaPhi0p2PosZ,
    )
)

makeHaloNCscPlotNoNeg = cms.PSet(
    name = cms.string("makeHaloNCscPlotNoNeg"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
        cutNCscSegJetDelta0p2,
        cutNoCscSegJetDeltaPhi0p2MinZ,
    )
)

CosmiBackgroundEventSelection = cms.PSet(
    name = cms.string("CosmicBackgroundSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
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
      cutHpdROuter,
      cutCosmics,
      cutNumberOfDT,
      cutMoreOuterDT,
    )
)

CscRGt400 = cms.PSet(
    name = cms.string("CSCRGt400"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutCscRDT400,
    )
)

CscNHit3 = cms.PSet(
    name = cms.string("CscNHit3"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutJetEta,
        cutJetNumber1,
        cutCscNHit3,
    )
)

CscNHit6 = cms.PSet(
    name = cms.string("CscNHit6"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutJetEta,
        cutJetNumber1,
        cutCscNHit6,
    )
)

CscAllStudy = cms.PSet(
    name = cms.string("CscAllStudy"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutJetEta,
        cutJetNumber1,
        cutDeltaPhiCscJet,
    )
)

selectedHaloNCscNearJet = cms.PSet(
    name = cms.string("selectedHaloNCscNearJet"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutBeamHaloCscNearJet,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
        #cutNCscSegJetDelta0p2,
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
#        cutPass2016TightHaloFilter,
    )
)
selectedHaloByBeamHaloFilter = cms.PSet(
    name = cms.string("selectedHaloByBeamHaloFilter"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        #cutBeamHaloCscNearJet,
        cutJetEnergy,
        cutJetEta,
        cutNoise,
        #cutNCscSegJetDelta0p2e
        cutOuterDT,
        cutDTPair,
        cutMaxDeltaJetPhi,
        newNOuterAllBarrelRPCHitsDeltaR,
        cutKillBy2016TightHaloFilter,
        cutNoBeamHaloCscNearJet,
#        cutPass2016TightHaloFilter,
    )
)

HaloControlTaggedByVetoSelection = cms.PSet(
    name = cms.string("HaloControlTaggedByVetoSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutBeamHaloCscNearJet,
      cutPass2016TightHaloFilter,
      #cutCscSegNumberOnekkkkkkk,
    )
)

HaloControlTaggedByFilterSelection = cms.PSet(
    name = cms.string("HaloControlTaggedByFilterSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutKillBy2016TightHaloFilter,
      #cutCscSegNumberOne,
    )
)

EventSelection_PlotLeadingJetEM = cms.PSet(
    name = cms.string("EventSelectionPlotLeadingJetEM"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutJetEnergy,
        #cutLeadingJetEMFractionGTp1,
        cutVertexNumber,
        #cutJetEta,
        cutJetN90,
        cutHavingNoCscSegNHit56,
        #cutTowerIPhi,
        #cutTowerFraction,
        #cutHpdR1,
        #cutHpdR2,
        #cutHpdRPeak,
        #cutHpdRPeakSample,
        #cutHpdROuter,
    )
)

CosmicControlSelection1 = cms.PSet(
    name = cms.string("CosmicMuonControlSelection1"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHavingNoCscSegNHit56,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

CosmicControlSelection2 = cms.PSet(
    name = cms.string("CosmicMuonControlSelection2"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHavingNoCscSegNHit56,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutOuterDT,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

CosmicControlSelection3 = cms.PSet(
    name = cms.string("CosmicMuonControlSelection3"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHavingNoCscSegNHit56,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutOuterDT,
      cutDTPair,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

CosmicControlSelection4 = cms.PSet(
    name = cms.string("CosmicMuonControlSelection4"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutHavingNoCscSegNHit56,
      cutNoise,
      cutMaxiEtaDiffSameiRbx,
      cutJetEnergy,
      cutJetEta,
      cutJetN90,
      cutTowerIPhi,
      cutTowerFraction,
      cutHpdR1,
      cutHpdR2,
      cutHpdRPeak,
      cutHpdRPeakSample,
      cutHpdROuter,
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
    )
)

CosmicControlSelectionMC1 = cms.PSet(
    name = cms.string("CosmicMuonControlSelectionMC1"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      #cutMaxDeltaJetPhi,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      #newNOuterAllBarrelRPCHitsDeltaR,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
      #cutMinDeltaRDTST4LeadingJet,
      cutMinDeltaRDTST4RPCInner3Layers,
      cutMinDeltaROuterRpcInnerDT,
    )
)
CosmicControlSelectionMC2 = cms.PSet(
    name = cms.string("CosmicMuonControlSelectionMC2"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutNDTStation3,
      cutNDTStation4,
      cutDTPair,
      #cutMaxDeltaJetPhi,
      cutMaxDeltaJetPhiNoDTST4,
      cutCloseOuterAllDTPairDeltaPhi0p5,
      #newNOuterAllBarrelRPCHitsDeltaR,
      newNOuterAllBarrelRPCHitsDeltaRDeltar,
      #cutOuterDT,
      #cutMaxDeltaJetPhi,
      #newNOuterAllBarrelRPCHitsDeltaR,
    )
)
CosmicControlSelectionMC3 = cms.PSet(
    name = cms.string("CosmicMuonControlSelectionMC3"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutOuterDT,
      cutDTPair,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)
CosmicControlSelectionMC4 = cms.PSet(
    name = cms.string("CosmicMuonControlSelectionMC4"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
    )
)

CosmicControlSelectionMC5 = cms.PSet(
    name = cms.string("CosmicMuonControlSelectionMC5"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
      cutOuterDT,
      cutDTPair,
      cutMaxDeltaJetPhi,
      newNOuterAllBarrelRPCHitsDeltaR,
    )
)

cosmicRunNum = cms.PSet(
    name = cms.string("cosmicRunNum"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutNIsolatedNoiseChannel,
        cutIsolatedNoiseSumE,
        cutIsolatedNoiseSumEt,
        cutNoise,
        cutJetEta,
        #cutJetEnergy,
        cutJetEnergyGt30,
        #cutNoise,
        #cutHpdR1,
        #cutHpdR2,
        #cutHpdRPeak,
        #cutHpdRPeakSample,
        #cutHpdROuter,
        #cutCscSegNumber,
        cutHavingNoCscSegNHit56,
        #cutNoBeamHaloCscNearJet,
        #cutMinDeltaPhiCscPair,
        #cutMinDeltaPhiCscDt,
        #cutOuterDT,
        #cutOneCscSeg,
        #cutDTPair,
        #cutMaxDeltaJetPhi,
        #newNOuterAllBarrelRPCHitsDeltaR,
        cutNDTStation3,
        cutNDTStation4,
        cutDTPair,
        #cutMaxDeltaJetPhi,
        cutMaxDeltaJetPhiNoDTST4,
        cutCloseOuterAllDTPairDeltaPhi0p5,
        cutMinDeltaRDTST4RPCInner3Layers,
        #newNOuterAllBarrelRPCHitsDeltaR,
        newNOuterAllBarrelRPCHitsDeltaRDeltar,
        #cutNOuterCsc,
        #cutMaxDeltaPhiCscDt,
        #cutMaxDeltaPhiCscPair,
        #cutMinDeltaPhiOuterCscJet,
        )
    )

cosmicPassSpecificRegion = cms.PSet(
    name = cms.string("cosmicPassSpecificRegion"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,
        cutHavingNoCscSegNHit56,
        cutNoise,
        cutJetEnergy,
        cutCosmicCoarse,
        cutNDTWhl0Seg4,
        cutNDTWhl0Seg10,
    )
)


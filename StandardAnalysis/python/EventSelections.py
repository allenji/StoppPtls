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
      cutCscSegNumber,
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
      cutHpdROuter,
      cutMaxiEtaDiffSameiRbx
    )
)

#Full 2016 stopped particles analysis cuts
StoppPtlsSelection_2016 = cms.PSet(
    name = cms.string("StoppedParticlesSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
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

#Halo tag and probe Selection
HaloTagAndProbeSelection = cms.PSet(
    name = cms.string("BeamHaloTagAndProbeSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
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
      cutCscSegNumber,
      cutOuterDT,
      #cutOuterRpc,
      #cutRpcPair,
      #cutCloseRpcPair,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutDTPair,
      cutMaxDeltaJetPhi,
      cutJetEnergy,
      cutJetEta,
      cutNoise,
      cutNTowerDiffiEtaSameiRbx,
#      cutMaxiEtaDiffSameiRbx,
#      cutJetN90,
#      cutTowerIPhi,
#      cutTowerFraction,
#      cutNTowerSameiRbx,
    )
)

NoiseControlSelectionTight_2016 = cms.PSet(
    name = cms.string("HcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutOuterDT,
      #cutOuterRpc,
      #cutRpcPair,
      #cutCloseRpcPair,
      newNOuterAllBarrelRPCHitsDeltaR,
      cutDTPair,
      cutMaxDeltaJetPhi,
      cutJetEnergy,
      cutJetEta,
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
        cutDummy
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
        cutJetEnergy,
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
        cutJetEnergy,
        cutJetEta,
    )
)

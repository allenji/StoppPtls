import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *

#full analysis selection
StoppPtlsSelection = cms.PSet(
    name = cms.string("StoppedParticlesSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutCscSegNumber,
      cutOuterDT,
      cutOuterRpc,
      cutRpcPair,
      cutCloseRpcPair,
      cutDTPair,
      cutMaxDeltaJetPhi,
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
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutCscSegNumberInverted
      )
)

#Halo N-1 Selection (full selection except halo veto)
#For nCscSeg plot
HaloControlSelection = cms.PSet(
    name = cms.string("BeamHaloControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      cutOuterDT,
      cutOuterRpc,
      cutRpcPair,
      cutCloseRpcPair,
      cutDTPair,
      cutMaxDeltaJetPhi,
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
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
        cutJetNumber,
        cutCscSegNLayers,
        cutMinDeltaPhiCscJet
        )
)

#Cosmic Selection (invert cosmic veto and cut out halo)
CosmicSelection = cms.PSet(
    name = cms.string("CosmicMuonSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
        #cosmics but not halo
        cutCosmics,
        cutCscSegNumber 
        )
)

#Cosmic N-1 selection (full selection except cosmic veto)
#For RPC hits and DT segment plots
CosmicControlSelection = cms.PSet(
    name = cms.string("CosmicMuonControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
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
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutNoiseInverted
      )
)

#Noise N-1 ish Selection (preselection [cutJetEnergy + cutJetEta] + cosmic veto + halo veto)
#For noise filter result, n90jet, ntowiPhi, and other noise plots
NoiseControlSelection = cms.PSet(
    name = cms.string("HcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutCscSegNumber,
      cutOuterDT,
      cutOuterRpc,
      cutRpcPair,
      cutCloseRpcPair,
      cutDTPair,
      cutMaxDeltaJetPhi,
      cutJetEnergy,
      cutJetEta,
    )
)

#Alternate Noise N-1 ish Selection (preselection [cutJetEnergy + cutJetEta] + vertex veto + cosmic veto(no RPC hits) + halo veto)
AltNoiseControlSelection = cms.PSet(
    name = cms.string("AltHcalNoiseControlSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
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
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      cutBx,
      cutVertexNumber,
      )
)

#Signal Trigger Selection
#For vertex number plot
TriggerSelection = cms.PSet(
    name = cms.string("TriggerSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_NoHalo_v"),
    cuts = cms.VPSet(
      )
)

#Selection for Second Jet analysis
SecondJetSelection = cms.PSet(
     name = cms.string("SecondJetSelection"),
     triggers = cms.vstring(),
     cuts = cms.VPSet(
     )
)

#No cuts (including no trigger) selection
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(""), 
    cuts = cms.VPSet(
        )
    )

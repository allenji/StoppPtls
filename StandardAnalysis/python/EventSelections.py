import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *

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

SecondJetSelection = cms.PSet(
     name = cms.string("SecondJetSelection"),
     triggers = cms.vstring(),
     cuts = cms.VPSet(
     )
)

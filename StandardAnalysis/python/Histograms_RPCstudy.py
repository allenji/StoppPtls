import FWCore.ParameterSet.Config as cms

RpcStudyHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("maxRPCDeltaPhi"),
            title = cms.string("Maximum RPC #Delta#phi; Maximum RPC #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxRPCDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("nCloseRPCPairs"),
            title = cms.string("Number of Close RPC Pairs; Number of Close RPC Pairs"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nCloseRPCPairs"),
        ),
        cms.PSet (
            name = cms.string("nOppositeRPCPairs"),
            title = cms.string("Number of Opposite RPC Pairs; Number of Opposite RPC pairs"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nOppositeRPCPairs"),
        ),
        cms.PSet (
            name = cms.string("nOuterRPC"),
            title = cms.string("Number of RPC Hits with r>560 cm; Number of Outer RPC Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("outerRPC"),
        ),
        cms.PSet (
            name = cms.string("nInnerRPC"),
            title = cms.string("Number of RPC Hits with r<560 cm; Number of Inner RPC Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("innerRPC"),
        ),
        cms.PSet (
            name = cms.string("nLJetRPCPairsDeltaPhiST1"),
            title = cms.string("Leading jet RPC pairs(deltaphi < 1); Number of pairs"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nLJetRPCPairsDeltaPhiST1"),
        ),
        cms.PSet (
            name = cms.string("nLJetRPCPairsDeltaPhiGT1"),
            title = cms.string("Leading jet RPC pairs(deltaphi > 1); Number of pairs"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nLJetRPCPairsDeltaPhiGT1"),
        ),
        cms.PSet (
            name = cms.string("nLJetRPCPairsDeltaPhiGT1p5"),
            title = cms.string("Leading jet RPC pairs(deltaphi > 1.5); Number of pairs"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nLJetRPCPairsDeltaPhiGT1p5"),
        ),
        cms.PSet (
            name = cms.string("nLJetRPCPairsDeltaPhiGT0p5"),
            title = cms.string("Leading jet RPC pairs(deltaphi > 0.5); Number of pairs"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nLJetRPCPairsDeltaPhiGT0p5"),
        ),
    )
)

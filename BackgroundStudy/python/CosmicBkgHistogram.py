import FWCore.ParameterSet.Config as cms

CosmicBackgroundHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
      cms.PSet (
        name = cms.string("DTBarrelRPC"),
        title = cms.string("nBarrelRPC vs nDT; number of barrel RPC hits; number of DT segments"),
        binsX = cms.untracked.vdouble(30, 0, 30),
        binsY = cms.untracked.vdouble(30, 0, 30),
        inputVariables = cms.vstring("outerRPCbarrel", "dtSegN"),
      )
    )
)

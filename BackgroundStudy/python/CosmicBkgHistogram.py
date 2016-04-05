import FWCore.ParameterSet.Config as cms

CosmicBackgroundHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
      cms.PSet (
        name = cms.string("DTBarrelRPC"),
        title = cms.string("nBarrelRPC vs nDT; number of DT segments; number of barrel RPC hits"),
        binsX = cms.untracked.vdouble(15, 0, 30),
        binsY = cms.untracked.vdouble(15, 0, 30),
        inputVariables = cms.vstring("dtSegN", "RPCbarrel"),
      )
    )
)

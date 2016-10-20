import FWCore.ParameterSet.Config as cms

CosmicBackgroundHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
      cms.PSet (
        name = cms.string("DTRPC"),
        title = cms.string("nRPC vs nDT; number of DT segments; number of RPC hits"),
        binsX = cms.untracked.vdouble(15, 0, 30),
        binsY = cms.untracked.vdouble(15, 0, 30),
        inputVariables = cms.vstring("dtSegN", "rpcHitN"),
      ),
      cms.PSet (
        name = cms.string("DTBarrelRPC"),
        title = cms.string("nBarrelRPC vs nDT; number of DT segments; number of barrel RPC hits"),
        binsX = cms.untracked.vdouble(15, 0, 30),
        binsY = cms.untracked.vdouble(15, 0, 30),
        inputVariables = cms.vstring("dtSegN", "RPCbarrel"),
      ),
      cms.PSet (
        name = cms.string("DTOuterBarrelRPC"),
        title = cms.string("nOuterBarrelRPC vs nDT; number of DT segments; number of outer barrel RPC hits"),
        binsX = cms.untracked.vdouble(15, 0, 30),
        binsY = cms.untracked.vdouble(15, 0, 15),
        inputVariables = cms.vstring("dtSegN", "outerRPCbarrel"),
      ),
      cms.PSet (
        name = cms.string("leadingJetEtaPhi"),
        title = cms.string("Eta vs Phi; phi; eta"),
        binsX = cms.untracked.vdouble(10, -3.5, 3.5),
        binsY = cms.untracked.vdouble(10, -1.5, 1.5),
        inputVariables = cms.vstring("leadingJetPhi", "leadingJetEta"),
      )
    )
)

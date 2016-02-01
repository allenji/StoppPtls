import FWCore.ParameterSet.Config as cms
secondJetHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jet_N"),
            title = cms.string("Number of Jets"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("jetnumber"),
        ),
        cms.PSet (
            name = cms.string("secondJetEnergy"),
            title = cms.string("Second Leading Jet Energy"),
            binsX = cms.untracked.vdouble(30, 0, 150),
            inputVariables = cms.vstring("secondJetEnergy"),
        ),
        cms.PSet (
            name = cms.string("leadingJetEnergy"),
            title = cms.string("Leading Jet Energy"),
            binsX = cms.untracked.vdouble(30, 0, 900),
            inputVariables = cms.vstring("leadingJetEnergy"),
        ),
    )
)

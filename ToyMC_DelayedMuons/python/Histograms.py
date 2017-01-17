import FWCore.ParameterSet.Config as cms
ToyMCRunLbHistogram = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet(
        cms.PSet (
            name = cms.string("runlb"),
            title = cms.string("Run vs LS; Run number; lumi section"),
            binsX = cms.untracked.vdouble(7000,254000, 261000),
            #binsX = cms.untracked.vdouble(45000, 235000, 280000),
            binsY = cms.untracked.vdouble(4000, 0, 4000),
            inputVariables = cms.vstring("run","lb"),
            )
    )
)
ToyMCRunLbHistogram_2016 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet(
        cms.PSet (
            name = cms.string("runlb"),
            title = cms.string("Run vs LS; Run number; lumi section"),
            binsX = cms.untracked.vdouble(12000,273000, 285000),
            #binsX = cms.untracked.vdouble(45000, 235000, 280000),
            binsY = cms.untracked.vdouble(4000, 0, 4000),
            inputVariables = cms.vstring("run","lb"),
            )
    )
)

import FWCore.ParameterSet.Config as cms

HaloBackgroundHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
      cms.PSet (
        name = cms.string("meanCscX_meanCscY"),
        title = cms.string("Mean CSC Segment X vs Y; Mean CSC Segment X; Mean CSC Segment Y"),
        binsX = cms.untracked.vdouble(100, -400, 400),
        binsY = cms.untracked.vdouble(100, -400, 400),
        inputVariables = cms.vstring("meanCscX", "meanCscY"),
      ),
      cms.PSet (
        name = cms.string("meanCscR_meanCscPhi"),
        title = cms.string("Mean CSC Segment R vs Phi; Mean CSC Segment R; Mean CSC Segment Phi"),
        binsX = cms.untracked.vdouble(100, 0, 600),
        binsY = cms.untracked.vdouble(64, -3.2, 3.2),
        inputVariables = cms.vstring("meanCscR", "meanCscPhi"),
      ),
    )
)

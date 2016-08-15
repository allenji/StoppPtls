import FWCore.ParameterSet.Config as cms

###############################################
##### Set up the histograms to be plotted #####
###############################################

Gluino0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("gluino0Mass"),
            title = cms.string("Generator Gluino Mass; Generator Gluino Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino0Mass"),
        ),
        cms.PSet (
            name = cms.string("gluino0Charge"),
            title = cms.string("Generator Gluino Charge; Generator Gluino Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("gluino0Charge"),
        ),
        cms.PSet (
            name = cms.string("gluino0P"),
            title = cms.string("Generator Gluino Momentum; Generator Gluino p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino0P"),
        ),
        cms.PSet (
            name = cms.string("gluino0Pt"),
            title = cms.string("Generator Gluino Transverse Momentum; Generator Gluino p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino0Pt"),
        ),
        cms.PSet (
            name = cms.string("gluino0Px"),
            title = cms.string("Generator Gluino x Component of Momentum; Generator Gluino p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino0Px"),
        ),
        cms.PSet (
            name = cms.string("gluino0Py"),
            title = cms.string("Generator Gluino y Component of Momentum; Generator Gluino p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino0Py"),
        ),
        cms.PSet (
            name = cms.string("gluino0Pz"),
            title = cms.string("Generator Gluino z Component of Momentum; Generator Gluino p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino0Pz"),
        ),
        cms.PSet (
            name = cms.string("gluino0Eta"),
            title = cms.string("Generator Gluino Pseudorapidity; Generator Gluino #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("gluino0Eta"),
        ),
        cms.PSet (
            name = cms.string("gluino0Phi"),
            title = cms.string("Generator Gluino #phi; Generator Gluino #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("gluino0Phi"),
            ),
        cms.PSet (
            name = cms.string("gluino0Beta"),
            title = cms.string("Generator Gluino #beta; Generator Gluino #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("gluino0Beta"),
        ),
)
)

Gluino1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("gluino1Mass"),
            title = cms.string("Generator Gluino Mass; Generator Gluino Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino1Mass"),
        ),
        cms.PSet (
            name = cms.string("gluino1Charge"),
            title = cms.string("Generator Gluino Charge; Generator Gluino Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("gluino1Charge"),
        ),
        cms.PSet (
            name = cms.string("gluino1P"),
            title = cms.string("Generator Gluino Momentum; Generator Gluino p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino1P"),
        ),
        cms.PSet (
            name = cms.string("gluino1Pt"),
            title = cms.string("Generator Gluino Transverse Momentum; Generator Gluino p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluino1Pt"),
        ),
        cms.PSet (
            name = cms.string("gluino1Px"),
            title = cms.string("Generator Gluino x Component of Momentum; Generator Gluino p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino1Px"),
        ),
        cms.PSet (
            name = cms.string("gluino1Py"),
            title = cms.string("Generator Gluino y Component of Momentum; Generator Gluino p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino1Py"),
        ),
        cms.PSet (
            name = cms.string("gluino1Pz"),
            title = cms.string("Generator Gluino z Component of Momentum; Generator Gluino p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("gluino1Pz"),
        ),
        cms.PSet (
            name = cms.string("gluino1Eta"),
            title = cms.string("Generator Gluino Pseudorapidity; Generator Gluino #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("gluino1Eta"),
        ),
        cms.PSet (
            name = cms.string("gluino1Phi"),
            title = cms.string("Generator Gluino #phi; Generator Gluino #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("gluino1Phi"),
            ),
        cms.PSet (
            name = cms.string("gluino1Beta"),
            title = cms.string("Generator Gluino #beta; Generator Gluino #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("gluino1Beta"),
        ),
)
)

Stop0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stop0Mass"),
            title = cms.string("Generator Stop Mass; Generator Stop Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop0Mass"),
        ),
        cms.PSet (
            name = cms.string("stop0Charge"),
            title = cms.string("Generator Stop Charge; Generator Stop Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stop0Charge"),
        ),
        cms.PSet (
            name = cms.string("stop0P"),
            title = cms.string("Generator Stop Momentum; Generator Stop p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop0P"),
        ),
        cms.PSet (
            name = cms.string("stop0Pt"),
            title = cms.string("Generator Stop Transverse Momentum; Generator Stop p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop0Pt"),
        ),
        cms.PSet (
            name = cms.string("stop0Px"),
            title = cms.string("Generator Stop x Component of Momentum; Generator Stop p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop0Px"),
        ),
        cms.PSet (
            name = cms.string("stop0Py"),
            title = cms.string("Generator Stop y Component of Momentum; Generator Stop p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop0Py"),
        ),
        cms.PSet (
            name = cms.string("stop0Pz"),
            title = cms.string("Generator Stop z Component of Momentum; Generator Stop p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop0Pz"),
        ),
        cms.PSet (
            name = cms.string("stop0Eta"),
            title = cms.string("Generator Stop Pseudorapidity; Generator Stop #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stop0Eta"),
        ),
        cms.PSet (
            name = cms.string("stop0Phi"),
            title = cms.string("Generator Stop #phi; Generator Stop #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stop0Phi"),
            ),
        cms.PSet (
            name = cms.string("stop0Beta"),
            title = cms.string("Generator Stop #beta; Generator Stop #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stop0Beta"),
        ),
)
)

Stop1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stop1Mass"),
            title = cms.string("Generator Stop Mass; Generator Stop Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop1Mass"),
        ),
        cms.PSet (
            name = cms.string("stop1Charge"),
            title = cms.string("Generator Stop Charge; Generator Stop Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stop1Charge"),
        ),
        cms.PSet (
            name = cms.string("stop1P"),
            title = cms.string("Generator Stop Momentum; Generator Stop p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop1P"),
        ),
        cms.PSet (
            name = cms.string("stop1Pt"),
            title = cms.string("Generator Stop Transverse Momentum; Generator Stop p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stop1Pt"),
        ),
        cms.PSet (
            name = cms.string("stop1Px"),
            title = cms.string("Generator Stop x Component of Momentum; Generator Stop p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop1Px"),
        ),
        cms.PSet (
            name = cms.string("stop1Py"),
            title = cms.string("Generator Stop y Component of Momentum; Generator Stop p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop1Py"),
        ),
        cms.PSet (
            name = cms.string("stop1Pz"),
            title = cms.string("Generator Stop z Component of Momentum; Generator Stop p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stop1Pz"),
        ),
        cms.PSet (
            name = cms.string("stop1Eta"),
            title = cms.string("Generator Stop Pseudorapidity; Generator Stop #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stop1Eta"),
        ),
        cms.PSet (
            name = cms.string("stop1Phi"),
            title = cms.string("Generator Stop #phi; Generator Stop #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stop1Phi"),
            ),
        cms.PSet (
            name = cms.string("stop1Beta"),
            title = cms.string("Generator Stop #beta; Generator Stop #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stop1Beta"),
        ),
)
)

Mchamp0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("mchamp0Mass"),
            title = cms.string("Generator Mchamp Mass; Generator Mchamp Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp0Mass"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Charge"),
            title = cms.string("Generator Mchamp Charge; Generator Mchamp Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("mchamp0Charge"),
        ),
        cms.PSet (
            name = cms.string("mchamp0P"),
            title = cms.string("Generator Mchamp Momentum; Generator Mchamp p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp0P"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Pt"),
            title = cms.string("Generator Mchamp Transverse Momentum; Generator Mchamp p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp0Pt"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Px"),
            title = cms.string("Generator Mchamp x Component of Momentum; Generator Mchamp p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp0Px"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Py"),
            title = cms.string("Generator Mchamp y Component of Momentum; Generator Mchamp p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp0Py"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Pz"),
            title = cms.string("Generator Mchamp z Component of Momentum; Generator Mchamp p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp0Pz"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Eta"),
            title = cms.string("Generator Mchamp Pseudorapidity; Generator Mchamp #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("mchamp0Eta"),
        ),
        cms.PSet (
            name = cms.string("mchamp0Phi"),
            title = cms.string("Generator Mchamp #phi; Generator Mchamp #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("mchamp0Phi"),
            ),
        cms.PSet (
            name = cms.string("mchamp0Beta"),
            title = cms.string("Generator Mchamp #beta; Generator Mchamp #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("mchamp0Beta"),
        ),
)
)

Mchamp1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("mchamp1Mass"),
            title = cms.string("Generator Mchamp Mass; Generator Mchamp Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp1Mass"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Charge"),
            title = cms.string("Generator Mchamp Charge; Generator Mchamp Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("mchamp1Charge"),
        ),
        cms.PSet (
            name = cms.string("mchamp1P"),
            title = cms.string("Generator Mchamp Momentum; Generator Mchamp p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp1P"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Pt"),
            title = cms.string("Generator Mchamp Transverse Momentum; Generator Mchamp p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchamp1Pt"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Px"),
            title = cms.string("Generator Mchamp x Component of Momentum; Generator Mchamp p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp1Px"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Py"),
            title = cms.string("Generator Mchamp y Component of Momentum; Generator Mchamp p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp1Py"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Pz"),
            title = cms.string("Generator Mchamp z Component of Momentum; Generator Mchamp p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("mchamp1Pz"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Eta"),
            title = cms.string("Generator Mchamp Pseudorapidity; Generator Mchamp #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("mchamp1Eta"),
        ),
        cms.PSet (
            name = cms.string("mchamp1Phi"),
            title = cms.string("Generator Mchamp #phi; Generator Mchamp #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("mchamp1Phi"),
            ),
        cms.PSet (
            name = cms.string("mchamp1Beta"),
            title = cms.string("Generator Mchamp #beta; Generator Mchamp #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("mchamp1Beta"),
        ),
)
)

StoppedGluino0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedGluino0Mass"),
            title = cms.string("Stopped Generator Gluino Mass; Stopped Generator Gluino Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino0Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Charge"),
            title = cms.string("Stopped Generator Gluino Charge; Stopped Generator Gluino Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedGluino0Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0P"),
            title = cms.string("Stopped Generator Gluino Momentum; Stopped Generator Gluino p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino0P"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Pt"),
            title = cms.string("Stopped Generator Gluino Transverse Momentum; Stopped Generator Gluino p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino0Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Px"),
            title = cms.string("Stopped Generator Gluino x Component of Momentum; Stopped Generator Gluino p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino0Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Py"),
            title = cms.string("Stopped Generator Gluino y Component of Momentum; Stopped Generator Gluino p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino0Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Pz"),
            title = cms.string("Stopped Generator Gluino z Component of Momentum; Stopped Generator Gluino p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino0Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Eta"),
            title = cms.string("Stopped Generator Gluino Pseudorapidity; Stopped Generator Gluino #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedGluino0Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino0Phi"),
            title = cms.string("Stopped Generator Gluino #phi; Stopped Generator Gluino #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedGluino0Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedGluino0Beta"),
            title = cms.string("Stopped Generator Gluino #beta; Stopped Generator Gluino #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedGluino0Beta"),
        ),
)
)

StoppedGluino1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedGluino1Mass"),
            title = cms.string("Stopped Generator Gluino Mass; Stopped Generator Gluino Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino1Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Charge"),
            title = cms.string("Stopped Generator Gluino Charge; Stopped Generator Gluino Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedGluino1Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1P"),
            title = cms.string("Stopped Generator Gluino Momentum; Stopped Generator Gluino p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino1P"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Pt"),
            title = cms.string("Stopped Generator Gluino Transverse Momentum; Stopped Generator Gluino p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedGluino1Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Px"),
            title = cms.string("Stopped Generator Gluino x Component of Momentum; Stopped Generator Gluino p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino1Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Py"),
            title = cms.string("Stopped Generator Gluino y Component of Momentum; Stopped Generator Gluino p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino1Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Pz"),
            title = cms.string("Stopped Generator Gluino z Component of Momentum; Stopped Generator Gluino p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedGluino1Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Eta"),
            title = cms.string("Stopped Generator Gluino Pseudorapidity; Stopped Generator Gluino #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedGluino1Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedGluino1Phi"),
            title = cms.string("Stopped Generator Gluino #phi; Stopped Generator Gluino #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedGluino1Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedGluino1Beta"),
            title = cms.string("Stopped Generator Gluino #beta; Stopped Generator Gluino #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedGluino1Beta"),
        ),
)
)

StoppedStop0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedStop0Mass"),
            title = cms.string("Stopped Generator Stop Mass; Stopped Generator Stop Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop0Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Charge"),
            title = cms.string("Stopped Generator Stop Charge; Stopped Generator Stop Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedStop0Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0P"),
            title = cms.string("Stopped Generator Stop Momentum; Stopped Generator Stop p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop0P"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Pt"),
            title = cms.string("Stopped Generator Stop Transverse Momentum; Stopped Generator Stop p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop0Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Px"),
            title = cms.string("Stopped Generator Stop x Component of Momentum; Stopped Generator Stop p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop0Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Py"),
            title = cms.string("Stopped Generator Stop y Component of Momentum; Stopped Generator Stop p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop0Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Pz"),
            title = cms.string("Stopped Generator Stop z Component of Momentum; Stopped Generator Stop p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop0Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Eta"),
            title = cms.string("Stopped Generator Stop Pseudorapidity; Stopped Generator Stop #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedStop0Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop0Phi"),
            title = cms.string("Stopped Generator Stop #phi; Stopped Generator Stop #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedStop0Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedStop0Beta"),
            title = cms.string("Stopped Generator Stop #beta; Stopped Generator Stop #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedStop0Beta"),
        ),
)
)

StoppedStop1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedStop1Mass"),
            title = cms.string("Stopped Generator Stop Mass; Stopped Generator Stop Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop1Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Charge"),
            title = cms.string("Stopped Generator Stop Charge; Stopped Generator Stop Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedStop1Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1P"),
            title = cms.string("Stopped Generator Stop Momentum; Stopped Generator Stop p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop1P"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Pt"),
            title = cms.string("Stopped Generator Stop Transverse Momentum; Stopped Generator Stop p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedStop1Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Px"),
            title = cms.string("Stopped Generator Stop x Component of Momentum; Stopped Generator Stop p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop1Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Py"),
            title = cms.string("Stopped Generator Stop y Component of Momentum; Stopped Generator Stop p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop1Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Pz"),
            title = cms.string("Stopped Generator Stop z Component of Momentum; Stopped Generator Stop p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedStop1Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Eta"),
            title = cms.string("Stopped Generator Stop Pseudorapidity; Stopped Generator Stop #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedStop1Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedStop1Phi"),
            title = cms.string("Stopped Generator Stop #phi; Stopped Generator Stop #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedStop1Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedStop1Beta"),
            title = cms.string("Stopped Generator Stop #beta; Stopped Generator Stop #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedStop1Beta"),
        ),
)
)

StoppedMchamp0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedMchamp0Mass"),
            title = cms.string("Stopped Generator Mchamp Mass; Stopped Generator Mchamp Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp0Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Charge"),
            title = cms.string("Stopped Generator Mchamp Charge; Stopped Generator Mchamp Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedMchamp0Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0P"),
            title = cms.string("Stopped Generator Mchamp Momentum; Stopped Generator Mchamp p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp0P"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Pt"),
            title = cms.string("Stopped Generator Mchamp Transverse Momentum; Stopped Generator Mchamp p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp0Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Px"),
            title = cms.string("Stopped Generator Mchamp x Component of Momentum; Stopped Generator Mchamp p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp0Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Py"),
            title = cms.string("Stopped Generator Mchamp y Component of Momentum; Stopped Generator Mchamp p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp0Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Pz"),
            title = cms.string("Stopped Generator Mchamp z Component of Momentum; Stopped Generator Mchamp p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp0Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Eta"),
            title = cms.string("Stopped Generator Mchamp Pseudorapidity; Stopped Generator Mchamp #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedMchamp0Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Phi"),
            title = cms.string("Stopped Generator Mchamp #phi; Stopped Generator Mchamp #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedMchamp0Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedMchamp0Beta"),
            title = cms.string("Stopped Generator Mchamp #beta; Stopped Generator Mchamp #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedMchamp0Beta"),
        ),
)
)

StoppedMchamp1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stoppedMchamp1Mass"),
            title = cms.string("Stopped Generator Mchamp Mass; Stopped Generator Mchamp Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp1Mass"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Charge"),
            title = cms.string("Stopped Generator Mchamp Charge; Stopped Generator Mchamp Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("stoppedMchamp1Charge"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1P"),
            title = cms.string("Stopped Generator Mchamp Momentum; Stopped Generator Mchamp p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp1P"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Pt"),
            title = cms.string("Stopped Generator Mchamp Transverse Momentum; Stopped Generator Mchamp p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("stoppedMchamp1Pt"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Px"),
            title = cms.string("Stopped Generator Mchamp x Component of Momentum; Stopped Generator Mchamp p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp1Px"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Py"),
            title = cms.string("Stopped Generator Mchamp y Component of Momentum; Stopped Generator Mchamp p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp1Py"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Pz"),
            title = cms.string("Stopped Generator Mchamp z Component of Momentum; Stopped Generator Mchamp p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -5000, 5000),
            inputVariables = cms.vstring("stoppedMchamp1Pz"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Eta"),
            title = cms.string("Stopped Generator Mchamp Pseudorapidity; Stopped Generator Mchamp #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("stoppedMchamp1Eta"),
        ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Phi"),
            title = cms.string("Stopped Generator Mchamp #phi; Stopped Generator Mchamp #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("stoppedMchamp1Phi"),
            ),
        cms.PSet (
            name = cms.string("stoppedMchamp1Beta"),
            title = cms.string("Stopped Generator Mchamp #beta; Stopped Generator Mchamp #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("stoppedMchamp1Beta"),
        ),
)
)

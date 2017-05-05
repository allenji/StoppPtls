import FWCore.ParameterSet.Config as cms
from StoppPtls.StandardAnalysis.Histograms import *
import copy

###############################################
##### Set up the histograms to be plotted #####
###############################################

#Event histograms defined in StoppPtls/StandardAnalysis/python/Histograms.py

DelayedMuonsStoppedParticleHistograms = copy.deepcopy(StoppedParticleHistograms)
DelayedMuonsStoppedParticleHistograms.inputCollection = cms.vstring("eventvariables")
DelayedMuonsStoppedParticleHistograms.histograms.append(
    cms.PSet (
        name = cms.string("stoppedParticleEta"),
        title = cms.string("Stopped Particle #eta; Stopped Particle #eta"),
        binsX = cms.untracked.vdouble(100, -5, 5),
        inputVariables = cms.vstring("stoppedParticleEta"),
        ),
    )
DelayedMuonsStoppedParticleHistograms.histograms.append(
    cms.PSet (
        name = cms.string("stoppedParticleRegion"),
        title = cms.string("Stopped Particle Region; Stopped Particle Region"),
        binsX = cms.untracked.vdouble(8, 0, 8),
        inputVariables = cms.vstring("stoppedParticleRegion"),
        ),
    )
DelayedMuonsStoppedParticleHistograms.histograms.append(
    cms.PSet (
        name = cms.string("nStoppedParticles"),
        title = cms.string("Number of Stopped Particles; Number of Stopped Particles"),
        binsX = cms.untracked.vdouble(4, 0, 4),
        inputVariables = cms.vstring("nStoppedParticles"),
        ),
    )
DelayedMuonsStoppedParticleHistograms.histograms.append(
    cms.PSet (
        name = cms.string("rhadronCharge"),
        title = cms.string("Abs R-hadron Charge; Abs R-hadron Charge"),
        binsX = cms.untracked.vdouble(5, 0, 5),
        inputVariables = cms.vstring("abs(rhadronCharge)"),
        ),
    )

Muon0Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muon0Mass"),
            title = cms.string("Generator Muon Mass; Generator Muon Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("muon0Mass"),
        ),
        cms.PSet (
            name = cms.string("muon0Charge"),
            title = cms.string("Generator Muon Charge; Generator Muon Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("muon0Charge"),
        ),
        cms.PSet (
            name = cms.string("muon0P"),
            title = cms.string("Generator Muon Momentum; Generator Muon p [GeV]"),
            binsX = cms.untracked.vdouble(150, 0, 1500),
            inputVariables = cms.vstring("muon0P"),
        ),
        cms.PSet (
            name = cms.string("muon0Pt"),
            title = cms.string("Generator Muon Transverse Momentum; Generator Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(150, 0, 1500),
            inputVariables = cms.vstring("muon0Pt"),
        ),
        cms.PSet (
            name = cms.string("muon0Px"),
            title = cms.string("Generator Muon x Component of Momentum; Generator Muon p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon0Px"),
        ),
        cms.PSet (
            name = cms.string("muon0Py"),
            title = cms.string("Generator Muon y Component of Momentum; Generator Muon p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon0Py"),
        ),
        cms.PSet (
            name = cms.string("muon0Pz"),
            title = cms.string("Generator Muon z Component of Momentum; Generator Muon p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon0Pz"),
        ),
        cms.PSet (
            name = cms.string("muon0Eta"),
            title = cms.string("Generator Muon Pseudorapidity; Generator Muon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("muon0Eta"),
        ),
        cms.PSet (
            name = cms.string("muon0Phi"),
            title = cms.string("Generator Muon #phi; Generator Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("muon0Phi"),
            ),
)
)

Muon1Histograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muon1Mass"),
            title = cms.string("Generator Muon Mass; Generator Muon Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("muon1Mass"),
        ),
        cms.PSet (
            name = cms.string("muon1Charge"),
            title = cms.string("Generator Muon Charge; Generator Muon Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("muon1Charge"),
        ),
        cms.PSet (
            name = cms.string("muon1P"),
            title = cms.string("Generator Muon Momentum; Generator Muon p [GeV]"),
            binsX = cms.untracked.vdouble(150, 0, 1500),
            inputVariables = cms.vstring("muon1P"),
        ),
        cms.PSet (
            name = cms.string("muon1Pt"),
            title = cms.string("Generator Muon Transverse Momentum; Generator Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(150, 0, 1500),
            inputVariables = cms.vstring("muon1Pt"),
        ),
        cms.PSet (
            name = cms.string("muon1Px"),
            title = cms.string("Generator Muon x Component of Momentum; Generator Muon p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon1Px"),
        ),
        cms.PSet (
            name = cms.string("muon1Py"),
            title = cms.string("Generator Muon y Component of Momentum; Generator Muon p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon1Py"),
        ),
        cms.PSet (
            name = cms.string("muon1Pz"),
            title = cms.string("Generator Muon z Component of Momentum; Generator Muon p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("muon1Pz"),
        ),
        cms.PSet (
            name = cms.string("muon1Eta"),
            title = cms.string("Generator Muon Pseudorapidity; Generator Muon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("muon1Eta"),
        ),
        cms.PSet (
            name = cms.string("muon1Phi"),
            title = cms.string("Generator Muon #phi; Generator Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("muon1Phi"),
            ),
)
)

NeutralinoNLSPHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("neutralinoNLSPMass"),
            title = cms.string("#tilde{#chi^{0}_{2}} Mass; #tilde{#chi^{0}_{2}} Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("neutralinoNLSPMass"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPP"),
            title = cms.string("#tilde{#chi^{0}_{2}} Momentum; #tilde{#chi^{0}_{2}} p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("neutralinoNLSPP"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPPt"),
            title = cms.string("#tilde{#chi^{0}_{2}} Transverse Momentum; #tilde{#chi^{0}_{2}} p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("neutralinoNLSPPt"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPPx"),
            title = cms.string("#tilde{#chi^{0}_{2}} x Component of Momentum; #tilde{#chi^{0}_{2}} p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("neutralinoNLSPPx"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPPy"),
            title = cms.string("#tilde{#chi^{0}_{2}} y Component of Momentum; #tilde{#chi^{0}_{2}} p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("neutralinoNLSPPy"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPPz"),
            title = cms.string("#tilde{#chi^{0}_{2}} z Component of Momentum; #tilde{#chi^{0}_{2}} p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("neutralinoNLSPPz"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPEta"),
                title = cms.string("#tilde{#chi^{0}_{2}} Pseudorapidity; #tilde{#chi^{0}_{2}} #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("neutralinoNLSPEta"),
        ),
        cms.PSet (
            name = cms.string("neutralinoNLSPPhi"),
            title = cms.string("#tilde{#chi^{0}_{2}} #phi; #tilde{#chi^{0}_{2}} #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("neutralinoNLSPPhi"),
            ),
)
)

UpperDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("Upper DSA Track Momentum; Upper DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("Upper DSA Track p_{T}; Upper DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("eta"),
            title = cms.string("Upper DSA Track Pseudorapidity; Upper DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("phi"),
            title = cms.string("Upper DSA Track #phi; Upper DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("ndof"),
            title = cms.string("Upper DSA Track Number of DOF; Upper DSA Track Number of DOF"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("ndof"),
            ),
        cms.PSet (
            name = cms.string("normalizedChi2"),
            title = cms.string("Upper DSA Track #chi^{2}/dof; Upper DSA Track #chi^{2}/dof"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("normalizedChi2"),
            ),
        cms.PSet (
            name = cms.string("charge"),
            title = cms.string("Upper DSA Track Charge; Upper DSA Track Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("charge"),
            ),
        cms.PSet (
            name = cms.string("qOverPt"),
            title = cms.string("Upper DSA Track q/p_{T}; Upper DSA Track q/p_{T}"),
            binsX = cms.untracked.vdouble(100, -0.2, 0.2),
            inputVariables = cms.vstring("1.0*charge/pt"),
            ),
        cms.PSet (
            name = cms.string("dxy"),
            title = cms.string("Upper DSA Track d_{xy}; Upper DSA Track d_{xy} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dxy"),
            ),
        cms.PSet (
            name = cms.string("dz"),
            title = cms.string("Upper DSA Track d_{z}; Upper DSA Track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dz"),
            ),
        cms.PSet (
            name = cms.string("vx"),
            title = cms.string("Upper DSA Track v_{x}; Upper DSA Track v_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vx"),
            ),
        cms.PSet (
            name = cms.string("vy"),
            title = cms.string("Upper DSA Track v_{y}; Upper DSA Track v_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vy"),
            ),
        cms.PSet (
            name = cms.string("vz"),
            title = cms.string("Upper DSA Track v_{z}; Upper DSA Track v_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vz"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithAnyHits"),
            title = cms.string("Number of Muon Stations with Any Hits in Upper DSA Track; Number of Muon Stations with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithAnyHits"),
            title = cms.string("Number of CSC Chambers with Any Hits in Upper DSA Track; Number of CSC Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithAnyHits"),
            title = cms.string("Number of DT Chambers with Any Hits in Upper DSA Track; Number of DT Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithAnyHits"),
            title = cms.string("Number of RPC Chambers with Any Hits in Upper DSA Track; Number of RPC Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithValidHits"),
            title = cms.string("Number of Muon Stations with Valid Hits in Upper DSA Track; Number of Muon Stations with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithValidHits"),
            title = cms.string("Number of CSC Chambers with Valid Hits in Upper DSA Track; Number of CSC Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithValidHits"),
            title = cms.string("Number of DT Chambers with Valid Hits in Upper DSA Track; Number of DT Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithValidHits"),
            title = cms.string("Number of RPC Chambers with Valid Hits in Upper DSA Track; Number of RPC Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nValidMuonHits"),
            title = cms.string("Number of Valid Muon Hits in Upper DSA Track; Number of Valid Muon Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(60, 0, 60),
            inputVariables = cms.vstring("nValidMuonHits"),
            ),
        cms.PSet (
            name = cms.string("nValidCscHits"),
            title = cms.string("Number of Valid CSC Valid Hits in Upper DSA Track; Number of Valid CSC Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nValidCscHits"),
            ),
        cms.PSet (
            name = cms.string("nValidDtHits"),
            title = cms.string("Number of Valid DT Hits in Upper DSA Track; Number of Valid DT Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nValidDtHits"),
            ),
        cms.PSet (
            name = cms.string("nValidRpcHits"),
            title = cms.string("Number of Valid RPC Hits in Upper DSA Track; Number of Valid RPC Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nValidRpcHits"),
            ),
        cms.PSet (
            name = cms.string("innermostStationWithValidHits"),
            title = cms.string("Innermost Station with Valid Hits in Upper DSA Track; Innermost Station with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("innermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("outermostStationWithValidHits"),
            title = cms.string("Outermost Station with Valid Hits in Upper DSA Track; Outermost Station with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("outermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("quality"),
            title = cms.string("Upper DSA Track Quality; Upper DSA Track Quality"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("quality"),
            ),
        cms.PSet (
            name = cms.string("innerPx"),
            title = cms.string("Upper DSA Track Inner p_{x}; Upper DSA Track Inner p_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPx"),
            ),
        cms.PSet (
            name = cms.string("innerPy"),
            title = cms.string("Upper DSA Track Inner p_{y}; Upper DSA Track Inner p_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPy"),
            ),
        cms.PSet (
            name = cms.string("innerPz"),
            title = cms.string("Upper DSA Track Inner p_{z}; Upper DSA Track Inner p_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPz"),
            ),
        cms.PSet (
            name = cms.string("innerX"),
            title = cms.string("Upper DSA Track Inner x; Upper DSA Track Inner x [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerX"),
            ),
        cms.PSet (
            name = cms.string("innerY"),
            title = cms.string("Upper DSA Track Inner y; Upper DSA Track Inner y [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerY"),
            ),
        cms.PSet (
            name = cms.string("innerZ"),
            title = cms.string("Upper DSA Track Inner z; Upper DSA Track Inner z [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerZ"),
            ),
        cms.PSet (
            name = cms.string("dtTofDirection"),
            title = cms.string("Upper DSA Track TOF Direction; Upper DSA Track TOF Direction"),
            binsX = cms.untracked.vdouble(3, -1, 2),
            inputVariables = cms.vstring("dtTofDirection"),
            ),
        cms.PSet (
            name = cms.string("dtTofNDof"),
            title = cms.string("Upper DSA Track TOF nDOF; Upper DSA Track TOF nDOF"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("dtTofNDof"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta"),
            #title = cms.string("Upper DSA Track #beta^{-1}_{Free}; Upper DSA Track #beta^{-1}_{Free}"),
            title = cms.string("Upper DSA Track #beta^{-1}; Upper DSA Track #beta^{-1}"), #for pas
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBetaErr"),
            title = cms.string("Upper DSA Track #beta^{-1}_{Free} Error; Upper DSA Track #beta^{-1}_{Free} Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofFreeInverseBetaErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut"),
            #title = cms.string("Upper DSA Track TimeInOut; Upper DSA Track TimeInOut [ns]"),
            title = cms.string("Upper DSA Track TimeInOut; Upper DSA Track t_{DT} [ns]"), #for pas
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOutErr"),
            title = cms.string("Upper DSA Track TimeInOut Error; Upper DSA Track TimeInOut Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn"),
            title = cms.string("Upper DSA Track TimeOutIn; Upper DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr"),
            title = cms.string("Upper DSA Track TimeOutIn Error; Upper DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr"),
            ),
        cms.PSet (
            name = cms.string("nRpcTimingHits"),
            title = cms.string("Number of RPC Hits in Upper DSA Track; Number of RPC Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcTimingHits"),
            ),
        cms.PSet (
            name = cms.string("rpcHitBxPattern"),
            title = cms.string("Upper DSA Track RPC Hit BX Pattern; Upper DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("rpcHitBxAverage"),
            title = cms.string("Upper DSA Track RPC Hit BX Average; Upper DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("rpcHitTime"),
            title = cms.string("Upper DSA Track t_{RPC}; Upper DSA Track t_{RPC} [ns]"),
            binsX = cms.untracked.vdouble(120, -60, 60),
            inputVariables = cms.vstring("25.0*rpcHitBxAverage"),
            ),
        )
    )

LowerDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("Lower DSA Track Momentum; Lower DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("Lower DSA Track p_{T}; Lower DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("eta"),
            title = cms.string("Lower DSA Track Pseudorapidity; Lower DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("phi"),
            title = cms.string("Lower DSA Track #phi; Lower DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("ndof"),
            title = cms.string("Lower DSA Track Number of DOF; Lower DSA Track Number of DOF"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("ndof"),
            ),
        cms.PSet (
            name = cms.string("normalizedChi2"),
            title = cms.string("Lower DSA Track #chi^{2}/dof; Lower DSA Track #chi^{2}/dof"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("normalizedChi2"),
            ),
        cms.PSet (
            name = cms.string("charge"),
            title = cms.string("Lower DSA Track Charge; Lower DSA Track Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("charge"),
            ),
        cms.PSet (
            name = cms.string("qOverPt"),
            title = cms.string("Lower DSA Track q/p_{T}; Lower DSA Track q/p_{T}"),
            binsX = cms.untracked.vdouble(100, -0.2, 0.2),
            inputVariables = cms.vstring("1.0*charge/pt"),
            ),
        cms.PSet (
            name = cms.string("dxy"),
            title = cms.string("Lower DSA Track d_{xy}; Lower DSA Track d_{xy} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dxy"),
            ),
        cms.PSet (
            name = cms.string("dz"),
            title = cms.string("Lower DSA Track d_{z}; Lower DSA Track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dz"),
            ),
        cms.PSet (
            name = cms.string("vx"),
            title = cms.string("Lower DSA Track v_{x}; Lower DSA Track v_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vx"),
            ),
        cms.PSet (
            name = cms.string("vy"),
            title = cms.string("Lower DSA Track v_{y}; Lower DSA Track v_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vy"),
            ),
        cms.PSet (
            name = cms.string("vz"),
            title = cms.string("Lower DSA Track v_{z}; Lower DSA Track v_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vz"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithAnyHits"),
            title = cms.string("Number of Muon Stations with Any Hits in Lower DSA Track; Number of Muon Stations with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithAnyHits"),
            title = cms.string("Number of CSC Chambers with Any Hits in Lower DSA Track; Number of CSC Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithAnyHits"),
            title = cms.string("Number of DT Chambers with Any Hits in Lower DSA Track; Number of DT Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithAnyHits"),
            title = cms.string("Number of RPC Chambers with Any Hits in Lower DSA Track; Number of RPC Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithValidHits"),
            title = cms.string("Number of Muon Stations with Valid Hits in Lower DSA Track; Number of Muon Stations with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithValidHits"),
            title = cms.string("Number of CSC Chambers with Valid Hits in Lower DSA Track; Number of CSC Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithValidHits"),
            title = cms.string("Number of DT Chambers with Valid Hits in Lower DSA Track; Number of DT Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithValidHits"),
            title = cms.string("Number of RPC Chambers with Valid Hits in Lower DSA Track; Number of RPC Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nValidMuonHits"),
            title = cms.string("Number of Valid Muon Hits in Lower DSA Track; Number of Valid Muon Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(60, 0, 60),
            inputVariables = cms.vstring("nValidMuonHits"),
            ),
        cms.PSet (
            name = cms.string("nValidCscHits"),
            title = cms.string("Number of Valid CSC Valid Hits in Lower DSA Track; Number of Valid CSC Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nValidCscHits"),
            ),
        cms.PSet (
            name = cms.string("nValidDtHits"),
            title = cms.string("Number of Valid DT Hits in Lower DSA Track; Number of Valid DT Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nValidDtHits"),
            ),
        cms.PSet (
            name = cms.string("nValidRpcHits"),
            title = cms.string("Number of Valid RPC Hits in Lower DSA Track; Number of Valid RPC Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nValidRpcHits"),
            ),
        cms.PSet (
            name = cms.string("innermostStationWithValidHits"),
            title = cms.string("Innermost Station with Valid Hits in Lower DSA Track; Innermost Station with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("innermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("outermostStationWithValidHits"),
            title = cms.string("Outermost Station with Valid Hits in Lower DSA Track; Outermost Station with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("outermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("quality"),
            title = cms.string("Lower DSA Track Quality; Lower DSA Track Quality"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("quality"),
            ),
        cms.PSet (
            name = cms.string("innerPx"),
            title = cms.string("Lower DSA Track Inner p_{x}; Lower DSA Track Inner p_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPx"),
            ),
        cms.PSet (
            name = cms.string("innerPy"),
            title = cms.string("Lower DSA Track Inner p_{y}; Lower DSA Track Inner p_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPy"),
            ),
        cms.PSet (
            name = cms.string("innerPz"),
            title = cms.string("Lower DSA Track Inner p_{z}; Lower DSA Track Inner p_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPz"),
            ),
        cms.PSet (
            name = cms.string("innerX"),
            title = cms.string("Lower DSA Track Inner x; Lower DSA Track Inner x [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerX"),
            ),
        cms.PSet (
            name = cms.string("innerY"),
            title = cms.string("Lower DSA Track Inner y; Lower DSA Track Inner y [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerY"),
            ),
        cms.PSet (
            name = cms.string("innerZ"),
            title = cms.string("Lower DSA Track Inner z; Lower DSA Track Inner z [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerZ"),
            ),
        cms.PSet (
            name = cms.string("dtTofDirection"),
            title = cms.string("Lower DSA Track TOF Direction; Lower DSA Track TOF Direction"),
            binsX = cms.untracked.vdouble(3, -1, 2),
            inputVariables = cms.vstring("dtTofDirection"),
            ),
        cms.PSet (
            name = cms.string("dtTofNDof"),
            title = cms.string("Lower DSA Track TOF nDOF; Lower DSA Track TOF nDOF"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("dtTofNDof"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta"),
            #title = cms.string("Lower DSA Track #beta^{-1}_{Free}; Lower DSA Track #beta^{-1}_{Free}"),
            title = cms.string("Lower DSA Track #beta^{-1}; Lower DSA Track #beta^{-1}"), #for pas
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBetaErr"),
            title = cms.string("Lower DSA Track #beta^{-1}_{Free} Error; Lower DSA Track #beta^{-1}_{Free} Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofFreeInverseBetaErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut"),
            #title = cms.string("Lower DSA Track TimeInOut; Lower DSA Track TimeInOut [ns]"),
            title = cms.string("Lower DSA Track TimeInOut; Lower DSA Track t_{DT} [ns]"), #for pas
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOutErr"),
            title = cms.string("Lower DSA Track TimeInOut Error; Lower DSA Track TimeInOut Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn"),
            title = cms.string("Lower DSA Track TimeOutIn; Lower DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr"),
            title = cms.string("Lower DSA Track TimeOutIn Error; Lower DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr"),
            ),
        cms.PSet (
            name = cms.string("nRpcTimingHits"),
            title = cms.string("Number of RPC Hits in Lower DSA Track; Number of RPC Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcTimingHits"),
            ),
        cms.PSet (
            name = cms.string("rpcHitBxPattern"),
            title = cms.string("Lower DSA Track RPC Hit BX Pattern; Lower DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("rpcHitBxAverage"),
            title = cms.string("Lower DSA Track RPC Hit BX Average; Lower DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("rpcHitTime"),
            title = cms.string("Lower DSA Track t_{RPC}; Lower DSA Track t_{RPC} [ns]"),
            binsX = cms.untracked.vdouble(120, -60, 60),
            inputVariables = cms.vstring("25.0*rpcHitBxAverage"),
            ),
        )
    )

SmearedMomentumDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("pSmearedUpper"),
            title = cms.string("Upper DSA Track Smeared Momentum; Upper DSA Track Smeared p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pSmearedUpper"),
            ),
        cms.PSet (
            name = cms.string("ptSmearedUpper"),
            title = cms.string("Upper DSA Track Smeared Transverse Momentum; Upper DSA Track Smeared p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("ptSmearedUpper"),
            ),
        cms.PSet (
            name = cms.string("pSmearedLower"),
            title = cms.string("Lower DSA Track Smeared Momentum; Lower DSA Track Smeared p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pSmearedLower"),
            ),
        cms.PSet (
            name = cms.string("ptSmearedLower"),
            title = cms.string("Lower DSA Track Smeared Transverse Momentum; Lower DSA Track Smeared p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("ptSmearedLower"),
            ),
        )
)

#trigger turn on histos: same as upper DSA histos except plot p/pt to 200 GeV and bin width is 2 GeV
TriggerTurnOnUpperDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("; DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("; DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("eta"),
            title = cms.string("; DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("phi"),
            title = cms.string("; DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
)
)

TriggerPurityDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("; DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("; DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("eta"),
            title = cms.string("; DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("phi"),
            title = cms.string("; DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
)
)

NumberOfDelayedMuonsObjectsHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nTracks"),
            title = cms.string("Number of Upper DSA Tracks; Number of Upper DSA Tracks"),
            binsX = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("nTracks"),
            ),
        cms.PSet (
            name = cms.string("nSecondaryTracks"),
            title = cms.string("Number of Lower DSA Tracks; Number of Lower DSA Tracks"),
            binsX = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("nSecondaryTracks"),
            ),
        )
)

DelayedMuonsObjectsVsTimeHistograms = cms.PSet(
    inputCollection = cms.vstring("events","eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("run_nTracks"),
            title = cms.string("Run Number vs Number of Upper DSA Tracks; Run; Number of Upper DSA Tracks"),
            binsX = cms.untracked.vdouble(1000, 235000, 280000),
            binsY = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("event.run","eventvariable.nTracks"),
            ),
        cms.PSet (
            name = cms.string("fill_nTracks"),
            title = cms.string("Fill Number vs Number of Upper DSA Tracks; Fill; Number of Upper DSA Tracks"),
            binsX = cms.untracked.vdouble(300, 3000, 6000),
            binsY = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("event.fill","eventvariable.nTracks"),
            ),
        cms.PSet (
            name = cms.string("run_nSecondaryTracks"),
            title = cms.string("Run Number vs Number of Lower DSA racks; Run; Number of Lower DSA Tracks"),
            binsX = cms.untracked.vdouble(1000, 235000, 280000),
            binsY = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("event.run","eventvariable.nSecondaryTracks"),
            ),
        cms.PSet (
            name = cms.string("fill_nSecondaryTracks"),
            title = cms.string("Fill Number vs Number of Lower DSA Tracks; Fill; Number of Lower DSA Tracks"),
            binsX = cms.untracked.vdouble(300, 3000, 6000),
            binsY = cms.untracked.vdouble(7, 0, 7),
            inputVariables = cms.vstring("event.fill","eventvariable.nSecondaryTracks"),
            ),
        )
)

DeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpInOut"),
            #title = cms.string("#Delta DSA Track TimeInOut; #Delta DSA Track TimeInOut [ns]"),
            title = cms.string("#Delta DSA Track t_{DT}; #Delta t_{DT} [ns]"), #for pas
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpOutIn"),
            title = cms.string("#Delta DSA Track TimeOutIn; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("delta_dtTofFreeInverseBeta"),
            title = cms.string("#Delta DSA Track #beta^{-1}_{Free}; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("delta_rpcHitBxAverage"),
            title = cms.string("#Delta DSA Track RPC Hit BX Average; #Delta DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("delta_rpcTime"),
            title = cms.string("#Delta DSA Track t_{RPC}; #Delta t_{RPC} [ns]"),
            binsX = cms.untracked.vdouble(120, -60, 60),
            inputVariables = cms.vstring("25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("resolution_qOverPt"),
            title = cms.string("DSA Track q/p_{T} Resolution; DSA Track q/p_{T} Resolution"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("((track.charge)/(track.pt) - (secondaryTrack.charge)/(secondaryTrack.pt))/(1.414*(secondaryTrack.charge)/(secondaryTrack.pt))"),
            ),

        )
    )

UppervsLowerDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("Upper vs Lower DSA Track Momentum; Upper DSA Track p [GeV]; Lower DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("track.p","secondaryTrack.p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("Upper vs Lower DSA Track Transverse Momentum; Upper DSA Track p_{T} [GeV]; Lower DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("track.pt","secondaryTrack.pt"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut"),
            title = cms.string("Upper vs Lower DSA Track TimeInOut; Upper DSA Track TimeInOut [ns]; Lower DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.dtTofTimeAtIpInOut","secondaryTrack.dtTofTimeAtIpInOut"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn"),
            title = cms.string("Upper vs Lower DSA Track TimeOutIn; Upper DSA Track TimeOutIn [ns]; Lower DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.dtTofTimeAtIpOutIn","secondaryTrack.dtTofTimeAtIpOutIn"),
        ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta"),
            title = cms.string("Upper vs Lower DSA Track #beta^{-1}_{Free}; Upper DSA Track #beta^{-1}_{Free}; Lower DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("track.dtTofFreeInverseBeta","secondaryTrack.dtTofFreeInverseBeta"),
        ),
        )
    )

UppervsUpperDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofTimeAtIpOutIn"),
            title = cms.string("Upper DSA Track TimeInOut vs TimeOutIn; Upper DSA Track TimeInOut [ns]; Upper DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -50, 150),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut","dtTofTimeAtIpOutIn"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofFreeInverseBeta"),
            title = cms.string("Upper DSA Track TimeInOut vs #beta^{-1}_{Free}; Upper DSA Track TimeInOut [ns]; Upper DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut","dtTofFreeInverseBeta"),
        ),
        cms.PSet (
            name = cms.string("p_rpcHitBxPattern"),
            title = cms.string("Upper DSA Track p vs RPC Hit BX Pattern; Upper DSA Track p [GeV]; Upper DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("p","rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("p_rpcHitBxAverage"),
            title = cms.string("Upper DSA Track p vs RPC Hit BX Average; Upper DSA Track p [GeV]; Upper DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("p","rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("pt_rpcHitBxPattern"),
            title = cms.string("Upper DSA Track p_{T} vs RPC Hit BX Pattern; Upper DSA Track p_{T} [GeV]; Upper DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("pt","rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("pt_rpcHitBxAverage"),
            title = cms.string("Upper DSA Track p_{T} vs RPC Hit BX Average; Upper DSA Track p_{T} [GeV]; Upper DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("pt","rpcHitBxAverage"),
            ),
        )
    )

LowervsLowerDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofTimeAtIpOutIn"),
            title = cms.string("Lower DSA Track TimeInOut vs TimeOutIn; Lower DSA Track TimeInOut [ns]; Lower DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -50, 150),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut","dtTofTimeAtIpOutIn"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofFreeInverseBeta"),
            title = cms.string("Lower DSA Track TimeInOut vs #beta^{-1}_{Free}; Lower DSA Track TimeInOut [ns]; Lower DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut","dtTofFreeInverseBeta"),
        ),
        cms.PSet (
            name = cms.string("p_rpcHitBxPattern"),
            title = cms.string("Lower DSA Track p vs RPC Hit BX Pattern; Lower DSA Track p [GeV]; Lower DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("p","rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("p_rpcHitBxAverage"),
            title = cms.string("Lower DSA Track p vs RPC Hit BX Average; Lower DSA Track p [GeV]; Lower DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("p","rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("pt_rpcHitBxPattern"),
            title = cms.string("Lower DSA Track p_{T} vs RPC Hit BX Pattern; Lower DSA Track p_{T} [GeV]; Lower DSA Track RPC Hit BX Pattern"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(9, 0, 9),
            inputVariables = cms.vstring("pt","rpcHitBxPattern"),
            ),
        cms.PSet (
            name = cms.string("pt_rpcHitBxAverage"),
            title = cms.string("Lower DSA Track p_{T} vs RPC Hit BX Average; Lower DSA Track p_{T} [GeV]; Lower DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("pt","rpcHitBxAverage"),
            ),
        )
    )

VsDeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpInOut_delta_dtTofFreeInverseBeta"),
            title = cms.string("#Delta DSA Track TimeInOut vs #Delta DSA Track #beta^{-1}_{Free}; #Delta DSA Track TimeInOut [ns]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut","track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpInOut_delta_dtTofTimeAtIpOutIn"),
            title = cms.string("#Delta DSA Track TimeInOut vs #Delta DSA Track TimeOutIn; #Delta DSA Track TimeInOut [ns]; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut","track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        )
    )

UpperVsDeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("pUpper_delta_dtTofTimeAtIpInOut"),
            title = cms.string("Upper DSA Track p vs #Delta DSA Track TimeInOut; Upper DSA Track p [GeV]; #Delta DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.p","track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("pUpper_delta_dtTofTimeAtIpOutIn"),
            title = cms.string("Upper DSA Track p vs #Delta DSA Track TimeOutIn; Upper DSA Track p [GeV]; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.p","track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("pUpper_delta_dtTofFreeInverseBeta"),
            title = cms.string("Upper DSA Track p vs #Delta DSA Track #beta^{-1}_{Free}; Upper DSA Track p [GeV]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("track.p","track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("pUpper_delta_rpcHitBxAverage"),
            title = cms.string("Upper DSA Track p vs #Delta DSA Track RPC Hit BX Average; Upper DSA Track p [GeV]; #Delta DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("track.p","track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("pUpper_delta_rpcTime"),
            title = cms.string("Upper DSA Track p vs #Delta DSA Track t_{RPC}; p_{upper} [GeV]; #Delta t_{RPC} [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -60, 60),
            inputVariables = cms.vstring("track.p","25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("pUpper_resolution_qOverPt"),
            title = cms.string("Upper DSA Track p vs q/p_{T} Resolution; Upper DSA Track p [GeV]; DSA Track q/p_{T} Resolution"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("track.p","((track.charge)/(track.pt) - (secondaryTrack.charge)/(secondaryTrack.pt))/(1.414*(secondaryTrack.charge)/(secondaryTrack.pt))"),
            ),
        cms.PSet (
            name = cms.string("ptUpper_delta_dtTofTimeAtIpInOut"),
            title = cms.string("Upper DSA Track p_{T} vs #Delta DSA Track TimeInOut; Upper DSA Track p_{T} [GeV]; #Delta DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.pt","track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("ptUpper_delta_dtTofTimeAtIpOutIn"),
            title = cms.string("Upper DSA Track p_{T} vs #Delta DSA Track TimeOutIn; Upper DSA Track p_{T} [GeV]; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("track.pt","track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("ptUpper_delta_dtTofFreeInverseBeta"),
            title = cms.string("Upper DSA Track p_{T} vs #Delta DSA Track #beta^{-1}_{Free}; Upper DSA Track p_{T} [GeV]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("track.pt","track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("ptUpper_delta_rpcHitBxAverage"),
            title = cms.string("Upper DSA Track p_{T} vs #Delta DSA Track RPC Hit BX Average; Upper DSA Track p_{T} [GeV]; #Delta DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("track.pt","track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("ptUpper_resolution_qOverPt"),
            title = cms.string("Upper DSA Track p_{T} vs q/p_{T} Resolution; Upper DSA Track p_{T} [GeV]; DSA Track q/p_{T} Resolution"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("track.pt","((track.charge)/(track.pt) - (secondaryTrack.charge)/(secondaryTrack.pt))/(1.414*(secondaryTrack.charge)/(secondaryTrack.pt))"),
            ),
        )
    )

LowerVsDeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("pLower_delta_dtTofTimeAtIpInOut"),
            title = cms.string("Lower DSA Track p vs #Delta DSA Track TimeInOut; Lower DSA Track p [GeV]; #Delta DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("secondaryTrack.p","track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("pLower_delta_dtTofTimeAtIpOutIn"),
            title = cms.string("Lower DSA Track p vs #Delta DSA Track TimeOutIn; Lower DSA Track p [GeV]; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("secondaryTrack.p","track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("pLower_delta_dtTofFreeInverseBeta"),
            title = cms.string("Lower DSA Track p vs #Delta DSA Track #beta^{-1}_{Free}; Lower DSA Track p [GeV]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("secondaryTrack.p","track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("pLower_delta_rpcHitBxAverage"),
            title = cms.string("Lower DSA Track p vs #Delta DSA Track RPC Hit BX Average; Lower DSA Track p [GeV]; #Delta DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("secondaryTrack.p","track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("pLower_resolution_qOverPt"),
            title = cms.string("Lower DSA Track p vs q/p_{T} Resolution; Lower DSA Track p [GeV]; DSA Track q/p_{T} Resolution"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("secondaryTrack.p","((track.charge)/(track.pt) - (secondaryTrack.charge)/(secondaryTrack.pt))/(1.414*(secondaryTrack.charge)/(secondaryTrack.pt))"),
            ),
        cms.PSet (
            name = cms.string("ptLower_delta_dtTofTimeAtIpInOut"),
            title = cms.string("Lower DSA Track p_{T} vs #Delta DSA Track TimeInOut; Lower DSA Track p_{T} [GeV]; #Delta DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("secondaryTrack.pt","track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("ptLower_delta_dtTofTimeAtIpOutIn"),
            title = cms.string("Lower DSA Track p_{T} vs #Delta DSA Track TimeOutIn; Lower DSA Track p_{T} [GeV]; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("secondaryTrack.pt","track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("ptLower_delta_dtTofFreeInverseBeta"),
            title = cms.string("Lower DSA Track p_{T} vs #Delta DSA Track #beta^{-1}_{Free}; Lower DSA Track p_{T} [GeV]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("secondaryTrack.pt","track.dtTofFreeInverseBeta - secondaryTrack.dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("ptLower_delta_rpcHitBxAverage"),
            title = cms.string("Lower DSA Track p_{T} vs #Delta DSA Track RPC Hit BX Average; Lower DSA Track p_{T} [GeV]; #Delta DSA Track RPC Hit BX Average"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(120, -3, 3),
            inputVariables = cms.vstring("secondaryTrack.pt","track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage"),
            ),
        cms.PSet (
            name = cms.string("ptLower_resolution_qOverPt"),
            title = cms.string("Lower DSA Track p_{T} vs q/p_{T} Resolution; Lower DSA Track p_{T} [GeV]; DSA Track q/p_{T} Resolution"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("secondaryTrack.pt","((track.charge)/(track.pt) - (secondaryTrack.charge)/(secondaryTrack.pt))/(1.414*(secondaryTrack.charge)/(secondaryTrack.pt))"),
            ),
        )
    )


import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################

#StoppedParticle, Gen Particle, Event histograms defined in StoppPtls/StandardAnalysis/python/Histograms.py

#define gen particle mchamps and muons here, like GluonHistograms:
MchampHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("mchampMass"),
            title = cms.string("g Mass; g Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("mchampMass"),
        ),
        cms.PSet (
            name = cms.string("mchampP"),
            title = cms.string("g Momentum; g p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("mchampP"),
        ),
        cms.PSet (
            name = cms.string("mchampPt"),
            title = cms.string("g Transverse Momentum; g p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("mchampPt"),
        ),
        cms.PSet (
            name = cms.string("mchampPx"),
            title = cms.string("g x Component of Momentum; g p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("mchampPx"),
        ),
        cms.PSet (
            name = cms.string("mchampPy"),
            title = cms.string("g y Component of Momentum; g p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("mchampPy"),
        ),
        cms.PSet (
            name = cms.string("mchampPz"),
            title = cms.string("g z Component of Momentum; g p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("mchampPz"),
        ),
        cms.PSet (
            name = cms.string("mchampEta"),
            title = cms.string("g Pseudorapidity; g #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("mchampEta"),
        ),
        cms.PSet (
            name = cms.string("mchampPhi"),
            title = cms.string("g #phi; g #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("mchampPhi"),
            ),
)
)


DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p"),
            title = cms.string("DSA Track Momentum; DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p"),
        ),
        cms.PSet (
            name = cms.string("pt"),
            title = cms.string("DSA Track p_{T}; DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("eta"),
            title = cms.string("DSA Track Pseudorapidity; DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("phi"),
            title = cms.string("DSA Track #phi; DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("ndof"),
            title = cms.string("DSA Track Number of DOF; DSA Track Number of DOF"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("ndof"),
            ),
        cms.PSet (
            name = cms.string("normalizedChi2"),
            title = cms.string("DSA Track #chi^{2}/dof; DSA Track #chi^{2}/dof"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("normalizedChi2"),
            ),
        cms.PSet (
            name = cms.string("charge"),
            title = cms.string("DSA Track Charge; DSA Track Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("charge"),
            ),
        cms.PSet (
            name = cms.string("dxy"),
            title = cms.string("DSA Track d_{xy}; DSA Track d_{xy} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dxy"),
            ),
        cms.PSet (
            name = cms.string("dz"),
            title = cms.string("DSA Track d_{z}; DSA Track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dz"),
            ),
        cms.PSet (
            name = cms.string("vx"),
            title = cms.string("DSA Track v_{x}; DSA Track v_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vx"),
            ),
        cms.PSet (
            name = cms.string("vy"),
            title = cms.string("DSA Track v_{y}; DSA Track v_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vy"),
            ),
        cms.PSet (
            name = cms.string("vz"),
            title = cms.string("DSA Track v_{z}; DSA Track v_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vz"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithAnyHits"),
            title = cms.string("Number of Muon Stations with Any Hits in DSA Track; Number of Muon Stations with Any Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithAnyHits"),
            title = cms.string("Number of CSC Chambers with Any Hits in DSA Track; Number of CSC Chambers with Any Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithAnyHits"),
            title = cms.string("Number of DT Chambers with Any Hits in DSA Track; Number of DT Chambers with Any Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithAnyHits"),
            title = cms.string("Number of RPC Chambers with Any Hits in DSA Track; Number of RPC Chambers with Any Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithAnyHits"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithValidHits"),
            title = cms.string("Number of Muon Stations with Valid Hits in DSA Track; Number of Muon Stations with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithValidHits"),
            title = cms.string("Number of CSC Chambers with Valid Hits in DSA Track; Number of CSC Chambers with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithValidHits"),
            title = cms.string("Number of DT Chambers with Valid Hits in DSA Track; Number of DT Chambers with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithValidHits"),
            title = cms.string("Number of RPC Chambers with Valid Hits in DSA Track; Number of RPC Chambers with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("nValidMuonHits"),
            title = cms.string("Number of Valid Muon Hits in DSA Track; Number of Valid Muon Hits in DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidMuonHits"),
            ),
        cms.PSet (
            name = cms.string("nValidCscHits"),
            title = cms.string("Number of Valid CSC Valid Hits in DSA Track; Number of Valid CSC Hits in DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidCscHits"),
            ),
        cms.PSet (
            name = cms.string("nValidDtHits"),
            title = cms.string("Number of Valid DT Hits in DSA Track; Number of Valid DT  Hits in DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidDtHits"),
            ),
        cms.PSet (
            name = cms.string("nValidRpcHits"),
            title = cms.string("Number of Valid RPC Hits in DSA Track; Number of Valid RPC Hits in DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nValidRpcHits"),
            ),
        cms.PSet (
            name = cms.string("innermostStationWithValidHits"),
            title = cms.string("Innermost Station with Valid Hits in DSA Track; Innermost Station with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("innermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("outermostStationWithValidHits"),
            title = cms.string("Outermost Station with Valid Hits in DSA Track; Outermost Station with Valid Hits in DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("outermostStationWithValidHits"),
            ),
        cms.PSet (
            name = cms.string("quality"),
            title = cms.string("DSA Track Quality; DSA Track Quality"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("quality"),
            ),
        cms.PSet (
            name = cms.string("innerPx"),
            title = cms.string("DSA Track Inner p_{x}; DSA Track Inner p_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPx"),
            ),
        cms.PSet (
            name = cms.string("innerPy"),
            title = cms.string("DSA Track Inner p_{y}; DSA Track Inner p_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPy"),
            ),
        cms.PSet (
            name = cms.string("innerPz"),
            title = cms.string("DSA Track Inner p_{z}; DSA Track Inner p_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPz"),
            ),
        cms.PSet (
            name = cms.string("innerX"),
            title = cms.string("DSA Track Inner x; DSA Track Inner x [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerX"),
            ),
        cms.PSet (
            name = cms.string("innerY"),
            title = cms.string("DSA Track Inner y; DSA Track Inner y [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerY"),
            ),
        cms.PSet (
            name = cms.string("innerZ"),
            title = cms.string("DSA Track Inner z; DSA Track Inner z [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerZ"),
            ),
        cms.PSet (
            name = cms.string("dtTofDirection"),
            title = cms.string("DSA Track TOF Direction; DSA Track TOF Direction"),
            binsX = cms.untracked.vdouble(3, -1, 2),
            inputVariables = cms.vstring("dtTofDirection"),
            ),
        cms.PSet (
            name = cms.string("dtTofNDof"),
            title = cms.string("DSA Track TOF nDOF; DSA Track TOF nDOF"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("dtTofNDof"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta"),
            title = cms.string("DSA Track #beta^{-1}_{Free}; DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBetaErr"),
            title = cms.string("DSA Track #beta^{-1}_{Free} Error; DSA Track #beta^{-1}_{Free} Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofFreeInverseBetaErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut"),
            title = cms.string("DSA Track TimeInOut; DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOutErr"),
            title = cms.string("DSA Track TimeInOut Error; DSA Track TimeInOut Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn"),
            title = cms.string("DSA Track TimeOutIn; DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr"),
            title = cms.string("DSA Track TimeOutIn Error; DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr"),
            ),
        )
    )

NumberOfDelayedMuonsObjectsHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nTracks"),
            title = cms.string("Number of DSA Tracks; Number of DSA Tracks"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("nTracks"),
            ),
        )
)

DelayedMuonsObjectsVsTimeHistograms = cms.PSet(
    inputCollection = cms.vstring("events","eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("run_nTracks"),
            title = cms.string("Run Number vs Number of DSA Tracks; Run; Number of DSA Tracks"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.nTracks"),
            ),
        cms.PSet (
            name = cms.string("fill_nTracks"),
            title = cms.string("Fill Number vs Number of DSA Tracks; Fill; Number of DSA Tracks"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.fill","eventvariable.nTracks"),
            ),
        )
)

Upper0DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p_upper0"),
            title = cms.string("Upper DSA Track Momentum; Upper DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p_upper0"),
        ),
        cms.PSet (
            name = cms.string("pt_upper0"),
            title = cms.string("Upper DSA Track p_{T}; Upper DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt_upper0"),
        ),
        cms.PSet (
            name = cms.string("eta_upper0"),
            title = cms.string("Upper DSA Track Pseudorapidity; Upper DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta_upper0"),
        ),
        cms.PSet (
            name = cms.string("phi_upper0"),
            title = cms.string("Upper DSA Track #phi; Upper DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi_upper0"),
            ),
        cms.PSet (
            name = cms.string("ndof_upper0"),
            title = cms.string("Upper DSA Track Number of DOF; Upper DSA Track Number of DOF"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("ndof_upper0"),
            ),
        cms.PSet (
            name = cms.string("normalizedChi2_upper0"),
            title = cms.string("Upper DSA Track #chi^{2}/dof; Upper DSA Track #chi^{2}/dof"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("normalizedChi2_upper0"),
            ),
        cms.PSet (
            name = cms.string("charge_upper0"),
            title = cms.string("Upper DSA Track Charge; Upper DSA Track Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("charge_upper0"),
            ),
        cms.PSet (
            name = cms.string("dxy_upper0"),
            title = cms.string("Upper DSA Track d_{xy}; Upper DSA Track d_{xy} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dxy_upper0"),
            ),
        cms.PSet (
            name = cms.string("dz_upper0"),
            title = cms.string("Upper DSA Track d_{z}; Upper DSA Track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dz_upper0"),
            ),
        cms.PSet (
            name = cms.string("vx_upper0"),
            title = cms.string("Upper DSA Track v_{x}; Upper DSA Track v_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vx_upper0"),
            ),
        cms.PSet (
            name = cms.string("vy_upper0"),
            title = cms.string("Upper DSA Track v_{y}; Upper DSA Track v_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vy_upper0"),
            ),
        cms.PSet (
            name = cms.string("vz_upper0"),
            title = cms.string("Upper DSA Track v_{z}; Upper DSA Track v_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vz_upper0"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithAnyHits_upper0"),
            title = cms.string("Number of Muon Stations with Any Hits in Upper DSA Track; Number of Muon Stations with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithAnyHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithAnyHits_upper0"),
            title = cms.string("Number of CSC Chambers with Any Hits in Upper DSA Track; Number of CSC Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithAnyHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithAnyHits_upper0"),
            title = cms.string("Number of DT Chambers with Any Hits in Upper DSA Track; Number of DT Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithAnyHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithAnyHits_upper0"),
            title = cms.string("Number of RPC Chambers with Any Hits in Upper DSA Track; Number of RPC Chambers with Any Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithAnyHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithValidHits_upper0"),
            title = cms.string("Number of Muon Stations with Valid Hits in Upper DSA Track; Number of Muon Stations with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithValidHits_upper0"),
            title = cms.string("Number of CSC Chambers with Valid Hits in Upper DSA Track; Number of CSC Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithValidHits_upper0"),
            title = cms.string("Number of DT Chambers with Valid Hits in Upper DSA Track; Number of DT Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithValidHits_upper0"),
            title = cms.string("Number of RPC Chambers with Valid Hits in Upper DSA Track; Number of RPC Chambers with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nValidMuonHits_upper0"),
            title = cms.string("Number of Valid Muon Hits in Upper DSA Track; Number of Valid Muon Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidMuonHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nValidCscHits_upper0"),
            title = cms.string("Number of Valid CSC Valid Hits in Upper DSA Track; Number of Valid CSC Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidCscHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nValidDtHits_upper0"),
            title = cms.string("Number of Valid DT Hits in Upper DSA Track; Number of Valid DT  Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidDtHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("nValidRpcHits_upper0"),
            title = cms.string("Number of Valid RPC Hits in Upper DSA Track; Number of Valid RPC Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nValidRpcHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("innermostStationWithValidHits_upper0"),
            title = cms.string("Innermost Station with Valid Hits in Upper DSA Track; Innermost Station with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("innermostStationWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("outermostStationWithValidHits_upper0"),
            title = cms.string("Outermost Station with Valid Hits in Upper DSA Track; Outermost Station with Valid Hits in Upper DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("outermostStationWithValidHits_upper0"),
            ),
        cms.PSet (
            name = cms.string("quality_upper0"),
            title = cms.string("Upper DSA Track Quality; Upper DSA Track Quality"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("quality_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerPx_upper0"),
            title = cms.string("Upper DSA Track Inner p_{x}; Upper DSA Track Inner p_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPx_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerPy_upper0"),
            title = cms.string("Upper DSA Track Inner p_{y}; Upper DSA Track Inner p_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPy_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerPz_upper0"),
            title = cms.string("Upper DSA Track Inner p_{z}; Upper DSA Track Inner p_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPz_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerX_upper0"),
            title = cms.string("Upper DSA Track Inner x; Upper DSA Track Inner x [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerX_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerY_upper0"),
            title = cms.string("Upper DSA Track Inner y; Upper DSA Track Inner y [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerY_upper0"),
            ),
        cms.PSet (
            name = cms.string("innerZ_upper0"),
            title = cms.string("Upper DSA Track Inner z; Upper DSA Track Inner z [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerZ_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofDirection_upper0"),
            title = cms.string("Upper DSA Track TOF Direction; Upper DSA Track TOF Direction"),
            binsX = cms.untracked.vdouble(3, -1, 2),
            inputVariables = cms.vstring("dtTofDirection_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofNDof_upper0"),
            title = cms.string("Upper DSA Track TOF nDOF; Upper DSA Track TOF nDOF"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("dtTofNDof_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta_upper0"),
            title = cms.string("Upper DSA Track #beta^{-1}_{Free}; Upper DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBetaErr_upper0"),
            title = cms.string("Upper DSA Track #beta^{-1}_{Free} Error; Upper DSA Track #beta^{-1}_{Free} Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofFreeInverseBetaErr_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_upper0"),
            title = cms.string("Upper DSA Track TimeInOut; Upper DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOutErr_upper0"),
            title = cms.string("Upper DSA Track TimeInOut Error; Upper DSA Track TimeInOut Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn_upper0"),
            title = cms.string("Upper DSA Track TimeOutIn; Upper DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn_upper0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr_upper0"),
            title = cms.string("Upper DSA Track TimeOutIn Error; Upper DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr_upper0"),
            ),
        )
)

Lower0DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p_lower0"),
            title = cms.string("Lower DSA Track Momentum; Lower DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p_lower0"),
        ),
        cms.PSet (
            name = cms.string("pt_lower0"),
            title = cms.string("Lower DSA Track p_{T}; Lower DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt_lower0"),
        ),
        cms.PSet (
            name = cms.string("eta_lower0"),
            title = cms.string("Lower DSA Track Pseudorapidity; Lower DSA Track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta_lower0"),
        ),
        cms.PSet (
            name = cms.string("phi_lower0"),
            title = cms.string("Lower DSA Track #phi; Lower DSA Track #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi_lower0"),
            ),
        cms.PSet (
            name = cms.string("ndof_lower0"),
            title = cms.string("Lower DSA Track Number of DOF; Lower DSA Track Number of DOF"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("ndof_lower0"),
            ),
        cms.PSet (
            name = cms.string("normalizedChi2_lower0"),
            title = cms.string("Lower DSA Track #chi^{2}/dof; Lower DSA Track #chi^{2}/dof"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("normalizedChi2_lower0"),
            ),
        cms.PSet (
            name = cms.string("charge_lower0"),
            title = cms.string("Lower DSA Track Charge; Lower DSA Track Charge"),
            binsX = cms.untracked.vdouble(10, -5, 5),
            inputVariables = cms.vstring("charge_lower0"),
            ),
        cms.PSet (
            name = cms.string("dxy_lower0"),
            title = cms.string("Lower DSA Track d_{xy}; Lower DSA Track d_{xy} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dxy_lower0"),
            ),
        cms.PSet (
            name = cms.string("dz_lower0"),
            title = cms.string("Lower DSA Track d_{z}; Lower DSA Track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("dz_lower0"),
            ),
        cms.PSet (
            name = cms.string("vx_lower0"),
            title = cms.string("Lower DSA Track v_{x}; Lower DSA Track v_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vx_lower0"),
            ),
        cms.PSet (
            name = cms.string("vy_lower0"),
            title = cms.string("Lower DSA Track v_{y}; Lower DSA Track v_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vy_lower0"),
            ),
        cms.PSet (
            name = cms.string("vz_lower0"),
            title = cms.string("Lower DSA Track v_{z}; Lower DSA Track v_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("vz_lower0"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithAnyHits_lower0"),
            title = cms.string("Number of Muon Stations with Any Hits in Lower DSA Track; Number of Muon Stations with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithAnyHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithAnyHits_lower0"),
            title = cms.string("Number of CSC Chambers with Any Hits in Lower DSA Track; Number of CSC Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithAnyHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithAnyHits_lower0"),
            title = cms.string("Number of DT Chambers with Any Hits in Lower DSA Track; Number of DT Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithAnyHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithAnyHits_lower0"),
            title = cms.string("Number of RPC Chambers with Any Hits in Lower DSA Track; Number of RPC Chambers with Any Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithAnyHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nStationsWithValidHits_lower0"),
            title = cms.string("Number of Muon Stations with Valid Hits in Lower DSA Track; Number of Muon Stations with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nStationsWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nCscChambersWithValidHits_lower0"),
            title = cms.string("Number of CSC Chambers with Valid Hits in Lower DSA Track; Number of CSC Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscChambersWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nDtChambersWithValidHits_lower0"),
            title = cms.string("Number of DT Chambers with Valid Hits in Lower DSA Track; Number of DT Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nDtChambersWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nRpcChambersWithValidHits_lower0"),
            title = cms.string("Number of RPC Chambers with Valid Hits in Lower DSA Track; Number of RPC Chambers with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nRpcChambersWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nValidMuonHits_lower0"),
            title = cms.string("Number of Valid Muon Hits in Lower DSA Track; Number of Valid Muon Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidMuonHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nValidCscHits_lower0"),
            title = cms.string("Number of Valid CSC Valid Hits in Lower DSA Track; Number of Valid CSC Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidCscHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nValidDtHits_lower0"),
            title = cms.string("Number of Valid DT Hits in Lower DSA Track; Number of Valid DT  Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("nValidDtHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("nValidRpcHits_lower0"),
            title = cms.string("Number of Valid RPC Hits in Lower DSA Track; Number of Valid RPC Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nValidRpcHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("innermostStationWithValidHits_lower0"),
            title = cms.string("Innermost Station with Valid Hits in Lower DSA Track; Innermost Station with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("innermostStationWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("outermostStationWithValidHits_lower0"),
            title = cms.string("Outermost Station with Valid Hits in Lower DSA Track; Outermost Station with Valid Hits in Lower DSA Track"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("outermostStationWithValidHits_lower0"),
            ),
        cms.PSet (
            name = cms.string("quality_lower0"),
            title = cms.string("Lower DSA Track Quality; Lower DSA Track Quality"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("quality_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerPx_lower0"),
            title = cms.string("Lower DSA Track Inner p_{x}; Lower DSA Track Inner p_{x} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPx_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerPy_lower0"),
            title = cms.string("Lower DSA Track Inner p_{y}; Lower DSA Track Inner p_{y} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPy_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerPz_lower0"),
            title = cms.string("Lower DSA Track Inner p_{z}; Lower DSA Track Inner p_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerPz_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerX_lower0"),
            title = cms.string("Lower DSA Track Inner x; Lower DSA Track Inner x [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerX_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerY_lower0"),
            title = cms.string("Lower DSA Track Inner y; Lower DSA Track Inner y [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerY_lower0"),
            ),
        cms.PSet (
            name = cms.string("innerZ_lower0"),
            title = cms.string("Lower DSA Track Inner z; Lower DSA Track Inner z [cm]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("innerZ_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofDirection_lower0"),
            title = cms.string("Lower DSA Track TOF Direction; Lower DSA Track TOF Direction"),
            binsX = cms.untracked.vdouble(3, -1, 2),
            inputVariables = cms.vstring("dtTofDirection_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofNDof_lower0"),
            title = cms.string("Lower DSA Track TOF nDOF; Lower DSA Track TOF nDOF"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("dtTofNDof_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta_lower0"),
            title = cms.string("Lower DSA Track #beta^{-1}_{Free}; Lower DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBetaErr_lower0"),
            title = cms.string("Lower DSA Track #beta^{-1}_{Free} Error; Lower DSA Track #beta^{-1}_{Free} Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofFreeInverseBetaErr_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_lower0"),
            title = cms.string("Lower DSA Track TimeInOut; Lower DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOutErr_lower0"),
            title = cms.string("Lower DSA Track TimeInOut Error; Lower DSA Track TimeInOut Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn_lower0"),
            title = cms.string("Lower DSA Track TimeOutIn; Lower DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn_lower0"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr_lower0"),
            title = cms.string("Lower DSA Track TimeOutIn Error; Lower DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr_lower0"),
            ),
        )
    )

DeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpInOut"),
            title = cms.string("#Delta DSA Track TimeInOut; #Delta DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_upper0 - dtTofTimeAtIpInOut_lower0"),
            ),
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpOutIn"),
            title = cms.string("#Delta DSA Track TimeOutIn; #Delta DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn_upper0 - dtTofTimeAtIpOutIn_lower0"),
            ),
        cms.PSet (
            name = cms.string("delta_dtTofFreeInverseBeta"),
            title = cms.string("#Delta DSA Track #beta^{-1}_{Free}; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta_upper0 - dtTofFreeInverseBeta_lower0"),
            ),
        )
    )

Upper0vsLower0DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("p_upper0_lower0"),
            title = cms.string("Upper vs Lower DSA Track Momentum; Upper DSA Track p [GeV]; Lower DSA Track p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("p_upper0","p_lower0"),
        ),
        cms.PSet (
            name = cms.string("pt_upper0_lower0"),
            title = cms.string("Upper vs Lower DSA Track Transverse Momentum; Upper DSA Track p_{T} [GeV]; Lower DSA Track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("pt_upper0","pt_lower0"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_upper0_lower0"),
            title = cms.string("Upper vs Lower DSA Track TimeInOut; Upper DSA Track TimeInOut [ns]; Lower DSA Track TimeInOut [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            binsY = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_upper0","dtTofTimeAtIpInOut_lower0"),
        ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutIn_upper0_lower0"),
            title = cms.string("Upper vs Lower DSA Track TimeOutIn; Upper DSA Track TimeOutIn [ns]; Lower DSA Track TimeOutIn [ns]"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            binsY = cms.untracked.vdouble(400, -100, 100),
            inputVariables = cms.vstring("dtTofTimeAtIpOutIn_upper0","dtTofTimeAtIpOutIn_lower0"),
        ),
        cms.PSet (
            name = cms.string("dtTofFreeInverseBeta_upper0_lower0"),
            title = cms.string("Upper vs Lower DSA Track #beta^{-1}_{Free}; Upper DSA Track #beta^{-1}_{Free}; Lower DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofFreeInverseBeta_upper0","dtTofFreeInverseBeta_lower0"),
        ),
        )
    )

Upper0vsUpper0DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofFreeInverseBeta_upper0"),
            title = cms.string("Upper DSA Track TimeInOut vs #beta^{-1}_{Free}; Upper DSA Track TimeInOut [ns]; Upper DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_upper0","dtTofFreeInverseBeta_upper0"),
        ),
#p vs RPC BX pattern
        )
    )

Lower0vsLower0DSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dtTofTimeAtIpInOut_dtTofFreeInverseBeta_lower0"),
            title = cms.string("Lower DSA Track TimeInOut vs #beta^{-1}_{Free}; Lower DSA Track TimeInOut [ns]; Lower DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_lower0","dtTofFreeInverseBeta_lower0"),
        ),
#p vs RPC BX pattern
        )
    )

VsDeltaDSAHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("delta_dtTofTimeAtIpInOut_delta_dtTofFreeInverseBeta"),
            title = cms.string("#Delta DSA Track TimeInOut vs #Delta DSA Track #beta^{-1}_{Free}; #Delta DSA Track TimeInOut [ns]; #Delta DSA Track #beta^{-1}_{Free}"),
            binsX = cms.untracked.vdouble(400, -100, 100),
            binsY = cms.untracked.vdouble(120, -6, 6),
            inputVariables = cms.vstring("dtTofTimeAtIpInOut_upper0 - dtTofTimeAtIpInOut_lower0","dtTofFreeInverseBeta_upper0 - dtTofFreeInverseBeta_lower0"),
            ),
        )
    )

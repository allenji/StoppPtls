
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
            inputVariables = cms.vstring("dtTofTimeAtIpInOutErr"),
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
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr"),
            ),
        cms.PSet (
            name = cms.string("dtTofTimeAtIpOutInErr"),
            title = cms.string("DSA Track TimeOutIn Error; DSA Track TimeOutIn Error"),
            binsX = cms.untracked.vdouble(120, 0, 30),
            inputVariables = cms.vstring("dtTofTimeAtIpOutInErr"),
            ),
        )
    )

NumberOfObjectsHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nDtSeg"),
            title = cms.string("Number of DT Segments; Number of DT Segments"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("dtSegN"),
            ),
        cms.PSet (
            name = cms.string("nCscSeg"),
            title = cms.string("Number of CSC Segments; Number of CSC Segments"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("cscSegN"),
            ),
        cms.PSet (
            name = cms.string("nRpcHit"),
            title = cms.string("Number of RPC Hits; Number of RPC Hits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("rpcHitN"),
            ),
        )
)

ObjectsVsTimeHistograms = cms.PSet(
    inputCollection = cms.vstring("events","eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("run_nDtSeg"),
            title = cms.string("Run Number vs Number of DT Segments; Run; Number of DT Segments"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.dtSegN"),
            ),
        cms.PSet (
            name = cms.string("fill_nDtSeg"),
            title = cms.string("Fill Number vs Number of DT Segments; Fill; Number of DT Segments"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.fill","eventvariable.dtSegN"),
            ),
        cms.PSet (
            name = cms.string("run_nCscSeg"),
            title = cms.string("Run Number vs Number of CSC Segments; Run; Number of CSC Segments"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.cscSegN"),
            ),
        cms.PSet (
            name = cms.string("fill_nCscSeg"),
            title = cms.string("Fill Number vs Number of CSC Segments; Fill; Number of CSC Segments"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.fill","eventvariable.cscSegN"),
            ),
        cms.PSet (
            name = cms.string("run_nRpcHit"),
            title = cms.string("Run Number vs Number of RPC Hits; Run; Number of RPC Hits"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.rpcHitN"),
            ),
        cms.PSet (
            name = cms.string("fill_nRpcHit"),
            title = cms.string("Fill Number vs Number of RPC Hits; Fill; Number of RPC Hits"),
            binsX = cms.untracked.vdouble(400, 3000, 5000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.fill","eventvariable.rpcHitN"),
            ),
        cms.PSet (
            name = cms.string("run_nJet"),
            title = cms.string("Run Number vs Number of DSA Tracks; Run; Number of DSA Tracks"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.jetN"),
            ),
        cms.PSet (
            name = cms.string("fill_nJet"),
            title = cms.string("Fill Number vs Number of DSA Tracks; Fill; Number of DSA Tracks"),
            binsX = cms.untracked.vdouble(400, 3000, 5000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.fill","eventvariable.jetN"),
            ),
        )
)


DtSegmentHistograms = cms.PSet(
    inputCollection = cms.vstring("dtsegs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dtSegWheel"),
            title = cms.string("DT Segment Wheel; DT Segment Wheel"),
            binsX = cms.untracked.vdouble(6, -3,3),
            inputVariables = cms.vstring("wheel"),
        ),
        cms.PSet (
            name = cms.string("dtSegStation"),
            title = cms.string("DT Segment Station; DT Segment Station"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("station"),
        ),
        cms.PSet (
            name = cms.string("dtSegSector"),
            title = cms.string("DT Segment Sector; DT Segment Sector"),
            binsX = cms.untracked.vdouble(15, 0, 15),
            inputVariables = cms.vstring("sector"),
        ),
        cms.PSet (
            name = cms.string("dtSegX"),
            title = cms.string("DT Segment X; DT Segment X [cm]"),
            binsX = cms.untracked.vdouble(100, -1500, 1500),
            inputVariables = cms.vstring("x"),
        ),
        cms.PSet (
            name = cms.string("dtSegY"),
            title = cms.string("DT Segment Y; DT Segment Y [cm]"),
            binsX = cms.untracked.vdouble(100, -1500, 1500),
            inputVariables = cms.vstring("y"),
        ),
        cms.PSet (
            name = cms.string("dtSegZ"),
            title = cms.string("DT Segment Z; DT Segment Z [cm]"),
            binsX = cms.untracked.vdouble(100, -1500, 1500),
            inputVariables = cms.vstring("z"),
        ),
        cms.PSet (
            name = cms.string("dtSegR"),
            title = cms.string("DT Segment Radius; DT Segment Radius [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("r"),
        ),
        cms.PSet (
            name = cms.string("dtSegRho"),
            title = cms.string("DT Segment #rho; DT Segment #rho"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("rho"),
            ),
        cms.PSet (
            name = cms.string("dtSegPhi"),
            title = cms.string("DT Segment #phi; DT Segment #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            )
        )
)

CscSegmentHistograms = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("cscSegEndcap"),
            title = cms.string("CSC Segment Endcap; CSC Segment Endcap"),
            binsX = cms.untracked.vdouble(3, 0, 3),
            inputVariables = cms.vstring("endcap"),
        ),
        cms.PSet (
            name = cms.string("cscSegRing"),
            title = cms.string("CSC Segment Ring; CSC Segment Ring"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("ring"),
        ),
        cms.PSet (
            name = cms.string("cscSegStation"),
            title = cms.string("CSC Segment Station; CSC Segment Station"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("station"),
        ),
        cms.PSet (
            name = cms.string("cscSegChamber"),
            title = cms.string("CSC Segment Chamber; CSC Segment Chamber"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("chamber"),
        ),
        cms.PSet (
            name = cms.string("cscSegNHits"),
            title = cms.string("CSC Segment Number of Hits; CSC Segment Number of Hits"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nHits"),
        ),
        cms.PSet (
            name = cms.string("cscSegX"),
            title = cms.string("CSC Segment X; CSC Segment X [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("x"),
        ),
        cms.PSet (
            name = cms.string("cscSegY"),
            title = cms.string("CSC Segment Y; CSC Segment Y [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("y"),
        ),
        cms.PSet (
            name = cms.string("cscSegZ"),
            title = cms.string("CSC Segment Z; CSC Segment Z [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("z"),
        ),
        cms.PSet (
            name = cms.string("cscSegTime"),
            title = cms.string("CSC Segment Time; CSC Segment Time [ns]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("time"),
        ),
        cms.PSet (
            name = cms.string("cscSegR"),
            title = cms.string("CSC Segment Radius; CSC Segment Radius [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("r"),
        ),
        cms.PSet (
            name = cms.string("cscSegPhi"),
            title = cms.string("CSC Segment #phi; CSC Segment #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("cscSegX_cscSegY"),
            title = cms.string("CSC Segment x vs CSC Segment y; CSC Segment x [cm]; CSC Segment y [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            binsY = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("x","y"),
        ),
        cms.PSet (
            name = cms.string("cscSegZ_cscSegTime"),
            title = cms.string("CSC Segment z vs CSC Segment Time; CSC Segment Z [cm]; CSC Segment Time [ns]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("z","time"),
        )
        )
)

RpcHitsHistograms = cms.PSet(
    inputCollection = cms.vstring("rpchits"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("rpcHitRegion"),
            title = cms.string("RPC Hit Region; RPC Hit Region"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("region"),
        ),
        cms.PSet (
            name = cms.string("rpcHitX"),
            title = cms.string("RPC Hit X; RPC Hit X [cm]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("x"),
        ),
        cms.PSet (
            name = cms.string("rpcHitY"),
            title = cms.string("RPC Hit Y; RPC Hit Y [cm]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("y"),
        ),
        cms.PSet (
            name = cms.string("rpcHitZ"),
            title = cms.string("RPC Hit Z; RPC Hit Z [cm]"),
            binsX = cms.untracked.vdouble(100, -1500, 1500),
            inputVariables = cms.vstring("z"),
        ),
        cms.PSet (
            name = cms.string("rpcHitBx"),
            title = cms.string("RPC Hit BX; RPC Hit BX"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("bx"),
        ),
        cms.PSet (
            name = cms.string("rpcHitR"),
            title = cms.string("RPC Hit Radius; RPC Hit Radius [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("r"),
        ),
        cms.PSet (
            name = cms.string("rpcHitRho"),
            title = cms.string("RPC Hit #rho; RPC Hit #rho"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("rho"),
            ),
        cms.PSet (
            name = cms.string("rpcHitPhi"),
            title = cms.string("RPC Hit #phi; RPC Hit #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("rpcHitXVsY"),
            title = cms.string("RPC Hit X vs Y; RPC Hit X[cm]; RPC Hit Y[cm]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("x", "y"),
        ),
        cms.PSet (
            name = cms.string("rpcHitZVsR"),
            title = cms.string("RPC Hit Z vs R; RPC Hit Z[cm]; RPC Hit R[cm]"),
            binsX = cms.untracked.vdouble(120, -1200, 1200),
            binsY = cms.untracked.vdouble(75, 0, 750),
            inputVariables = cms.vstring("z", "r"),
        )
   )
)

OtherDtHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("maxDTDeltaPhi"),
            title = cms.string("Maximum DT #Delta#phi; Maximum DT #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("maxDTDeltaJetPhi"),
            title = cms.string("Maximum DT Segment-Jet #Delta#phi; Maximum DT Segment-Jet #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxDeltaJetPhi"),
        ),
        cms.PSet (
            name = cms.string("nOuterDT"),
            title = cms.string("Number of DT Segments with r>560 cm; Number of Outer DT Segments"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("outerDT"),
        ),
        cms.PSet (
            name = cms.string("nInnerDT"),
            title = cms.string("Number of DT Segments with r<560 cm; Number of Inner DT Segments"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("innerDT"),
        )
        )
)

OtherCscHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("minDeltaPhiCscJet"),
            title = cms.string("Minimum CSC Segment-Jet #Delta#phi; Minimum CSC Segment-Jet #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("minDeltaPhiCscJet"),
        ),
        cms.PSet (
            name = cms.string("nCscLayers"),
            title = cms.string("Number of Layers in CSC Segments; Number of Layers in CSC Segments"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("nCscLayers"),
            ),
        )
)

OtherRpcHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("maxRPCDeltaPhi"),
            title = cms.string("Maximum RPC #Delta#phi; Maximum RPC #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxRPCDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("maxRPCDeltaPhi_outer"),
            title = cms.string("Maximum Outer RPC #Delta#phi; Maximum Outer RPC #Delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxRPCDeltaPhi_outer"),
        ),
        cms.PSet (
            name = cms.string("nCloseRPCPairs"),
            title = cms.string("Number of Close RPC Pairs; Number of Close RPC Pairs"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nCloseRPCPairs"),
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
            name = cms.string("nOuterRPCbarrel"),
            title = cms.string("Number of RPC Barrel Hits with r>560 cm; Number of Outer RPC Barrel Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("outerRPCbarrel"),
        ),
        cms.PSet (
            name = cms.string("nInnerRPCbarrel"),
            title = cms.string("Number of RPC Barrel Hits with r<560 cm; Number of Inner RPC Barrel Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("innerRPCbarrel"),
        ),
        cms.PSet (
            name = cms.string("nRPCbarrel"),
            title = cms.string("Number of RPC Barrel Hits; Number of RPC Barrel Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("RPCbarrel"),
        ),
        cms.PSet (
            name = cms.string("nOuterRPCendcap"),
            title = cms.string("Number of RPC Endcap Hits with r>560 cm; Number of Outer RPC Endcap Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("outerRPCendcap"),
        ),
        cms.PSet (
            name = cms.string("nInnerRPCendcap"),
            title = cms.string("Number of RPC Endcap Hits with r<560 cm; Number of Inner RPC Endcap Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("innerRPCendcap"),
        ),
        cms.PSet (
            name = cms.string("nRPCendcap"),
            title = cms.string("Number of RPC Endcap Hits; Number of RPC Endcap Hits"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("RPCendcap"),
        ),
        cms.PSet (
            name = cms.string("nCloseOuterAllBarrelRPCPairDeltaR0p2"),
            title = cms.string("nCloseOuterAllBarrelRPCPairDeltaR < 0.2; Number of close outer barrel RPC pairs"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nCloseOuterAllBarrelRPCPairDeltaR0p2"),
        ),
        )
)


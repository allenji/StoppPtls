
import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################

#StoppedParticle, Gen Particle, Event histograms defined in StoppPtls/StandardAnalysis/python/Histograms.py

#define gen particle mchamps and muons here, like GluonHistograms:
GluonHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("gluonMass"),
            title = cms.string("g Mass; g Mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("gluonMass"),
        ),
        cms.PSet (
            name = cms.string("gluonP"),
            title = cms.string("g Momentum; g p [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("gluonP"),
        ),
        cms.PSet (
            name = cms.string("gluonPt"),
            title = cms.string("g Transverse Momentum; g p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("gluonPt"),
        ),
        cms.PSet (
            name = cms.string("gluonPx"),
            title = cms.string("g x Component of Momentum; g p_{x} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("gluonPx"),
        ),
        cms.PSet (
            name = cms.string("gluonPy"),
            title = cms.string("g y Component of Momentum; g p_{y} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("gluonPy"),
        ),
        cms.PSet (
            name = cms.string("gluonPz"),
            title = cms.string("g z Component of Momentum; g p_{z} [GeV]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("gluonPz"),
        ),
        cms.PSet (
            name = cms.string("gluonEta"),
            title = cms.string("g Pseudorapidity; g #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("gluonEta"),
        ),
        cms.PSet (
            name = cms.string("gluonPhi"),
            title = cms.string("g #phi; g #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("gluonPhi"),
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
            title = cms.string("Run Number vs Number of Jets; Run; Number of Jets"),
            binsX = cms.untracked.vdouble(1000, 235000, 265000),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("event.run","eventvariable.jetN"),
            ),
        cms.PSet (
            name = cms.string("fill_nJet"),
            title = cms.string("Fill Number vs Number of Jets; Fill; Number of Jets"),
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


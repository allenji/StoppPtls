import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################

EventHistograms = cms.PSet(
    inputCollection = cms.vstring("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("bxWrtBunch"),
            title = cms.string("BX With Respect To Bunch; bxWrtBunch"),
            binsX = cms.untracked.vdouble(200, 0, 200),
            inputVariables = cms.vstring("bxWrtBunch"),
        ),
        cms.PSet (
            name = cms.string("bx"),
            title = cms.string("BX; BX"),
            binsX = cms.untracked.vdouble(3600, 0, 3600),
            inputVariables = cms.vstring("bx"),
        ),
        cms.PSet (
            name = cms.string("run"),
            title = cms.string("Run Number; Run Number"),
            binsX = cms.untracked.vdouble(100, 0, 500000),
            inputVariables = cms.vstring("run"),
        ),
        cms.PSet (
            name = cms.string("fill"),
            title = cms.string("Fill Number; Fill Number"),
            binsX = cms.untracked.vdouble(500, 0, 5000),
            inputVariables = cms.vstring("fill"),
        ),
        cms.PSet (
            name = cms.string("nVtx"),
            title = cms.string("Number of Vertices; Number of Vertices"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nVtx"),
            )
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
        cms.PSet (
            name = cms.string("nJets"),
            title = cms.string("Number of Jets; Number of Jets"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("jetN"),
            ),
        cms.PSet (
            name = cms.string("nDtSeg_nRpcHit"),
            title = cms.string("Number of RPC Hits vs DT Segments; Number of DT Segments; Number of RPC Hits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("dtSegN","rpcHitN"),
            )
        )
)

NoiseHistograms = cms.PSet(
    inputCollection = cms.vstring("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("noise"),
            title = cms.string("Hcal Noise Filter Result; HCal Noise Filter Result"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("noiseFilterResult"),
        )
        )
)

JetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetEnergy"),
            title = cms.string("Jet Energy; Jet E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("energy"),
        ),
        cms.PSet (
            name = cms.string("jetEt"),
            title = cms.string("Jet E_{T}; Jet E_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("et"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Pseudorapidity; Jet #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet #phi; Jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
            ),
        cms.PSet (
            name = cms.string("jetN60"),
            title = cms.string("Jet n60; Jet n60"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("n60"),
            ),
        cms.PSet (
            name = cms.string("jetN90"),
            title = cms.string("Jet n90; Jet n90"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("n90"),
            )
        )
)

LeadingJetHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("leadingJetEnergy"),
            title = cms.string("Leading Jet Energy; Leading Jet E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("leadingJetEnergy"),
        ),
        cms.PSet (
            name = cms.string("leadingJetEt"),
            title = cms.string("Leading Jet E_{T}; Leading Jet E_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("leadingJetEt"),
        ),
        cms.PSet (
            name = cms.string("leadingJetEta"),
            title = cms.string("Leading Jet Pseudorapidity; Abs(Leading Jet #eta)"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("leadingJetEta"),
        ),
        cms.PSet (
            name = cms.string("leadingJetPhi"),
            title = cms.string("Leading Jet #phi; Leading Jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("leadingJetPhi"),
            ),
        cms.PSet (
            name = cms.string("leadingJetN60"),
            title = cms.string("Leading Jet n60; Leading Jet n60"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("leadingJetN60"),
            ),
        cms.PSet (
            name = cms.string("leadingJetN90"),
            title = cms.string("Leading Jet n90; Leading Jet n90"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("leadingJetN90"),
            )
        )
)

SecondJetHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("secondJetEnergy"),
            title = cms.string("Second Jet Energy; Second Jet E [GeV]"),
            binsX = cms.untracked.vdouble(30, 0, 150),
            inputVariables = cms.vstring("secondJetEnergy"),
        ),
        cms.PSet (
            name = cms.string("secondJetEt"),
            title = cms.string("Second Jet E_{T}; Second Jet E_{T} [GeV]"),
            binsX = cms.untracked.vdouble(30, 0, 150),
            inputVariables = cms.vstring("secondJetEt"),
        ),
        cms.PSet (
            name = cms.string("secondJetEta"),
            title = cms.string("Second Jet Pseudorapidity; Abs(Second Jet #eta)"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("secondJetEta"),
        ),
        cms.PSet (
            name = cms.string("secondJetPhi"),
            title = cms.string("Second Jet #phi; Second Jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("secondJetPhi"),
            ),
        cms.PSet (
            name = cms.string("secondJetN60"),
            title = cms.string("Second Jet n60; Second Jet n60"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("secondJetN60"),
            ),
        cms.PSet (
            name = cms.string("secondJetN90"),
            title = cms.string("Second Jet n90; Second Jet n90"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("secondJetN90"),
            )
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
        #cms.PSet (
            #name = cms.string("cscSegX"),
            #title = cms.string("CSC Segment X; CSC Segment X [cm]"),
            #binsX = cms.untracked.vdouble(300, -1500, 1500),
            #inputVariables = cms.vstring("x"),
        #),
        #cms.PSet (
            #name = cms.string("cscSegY"),
            #title = cms.string("CSC Segment Y; CSC Segment Y [cm]"),
            #binsX = cms.untracked.vdouble(300, -1500, 1500),
            #inputVariables = cms.vstring("y"),
        #),
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
            name = cms.string("cscSegZ_cscSegTime"),
            title = cms.string("CSC Segment Time vs CSC Segment Z; CSC Segment Z [cm]; CSC Segment Time [ns]"),
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
            name = cms.string("rpcSegRegion"),
            title = cms.string("RPC Hit Region; RPC Hit Region"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("region"),
        ),
        cms.PSet (
            name = cms.string("rpcSegX"),
            title = cms.string("RPC Hit X; RPC Hit X [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("x"),
        ),
        cms.PSet (
            name = cms.string("rpcSegY"),
            title = cms.string("RPC Hit Y; RPC Hit Y [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("y"),
        ),
        cms.PSet (
            name = cms.string("rpcSegZ"),
            title = cms.string("RPC Hit Z; RPC Hit Z [cm]"),
            binsX = cms.untracked.vdouble(300, -1500, 1500),
            inputVariables = cms.vstring("z"),
        ),
        #cms.PSet (
            #name = cms.string("rpcSegBX"),
            #title = cms.string("RPC Hit BX; RPC Hit BX"),
            #binsX = cms.untracked.vdouble(100, -10, 10),
            #inputVariables = cms.vstring("BunchX"),
        #),
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
            )
        )
)

OtherDtHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("maxDTDeltaPhi"),
            title = cms.string("Maximum DT #delta#phi; Maximum DT #delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("maxDTDeltaJetPhi"),
            title = cms.string("Maximum DT Segment-Jet #delta#phi; Maximum DT Segment-Jet #delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxDeltaJetPhi"),
        )
        )
)

OtherRpcHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("maxRPCDeltaPhi"),
            title = cms.string("Maximum RPC #delta#phi; Maximum RPC #delta#phi"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("maxRPCDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("nCloseRPCPairs"),
            title = cms.string("Number of Close RPC Pairs; Number of Close RPC Pairs"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("nCloseRPCPairs"),
        )
        )
)

TowerHistograms = cms.PSet(
    inputCollection = cms.vstring("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nTowerSameiPhi"),
            title = cms.string("Number of Towers at Same iPhi; Number of Towers at Same iPhi"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("nTowerSameiPhi"),
        ),
        cms.PSet (
            name = cms.string("leadingIPhiFractionValue"),
            title = cms.string("E_{iphi}/E_{jet}; E_{iphi}/E_{jet}"),
            binsX = cms.untracked.vdouble(200, 0, 2),
            inputVariables = cms.vstring("leadingIPhiFractionValue"),
        )
)
)

HpdHistograms = cms.PSet(
    inputCollection = cms.vstring("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("topHPD5R1"),
            title = cms.string("R_{1}; R_{1}"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("topHPD5R1"),
        ),
        cms.PSet (
            name = cms.string("topHPD5R2"),
            title = cms.string("R_{2}; R_{2}"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("topHPD5R2"),
        ),
        cms.PSet (
            name = cms.string("topHPD5RPeak"),
            title = cms.string("R_{Peak}; R_{Peak}"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("topHPD5RPeak"),
        ),
        cms.PSet (
            name = cms.string("topHPD5PeakSample"),
            title = cms.string("Peak Sample; Peak Sample"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("topHPD5PeakSample"),
        ),
        cms.PSet (
            name = cms.string("topHPD5ROuter"),
            title = cms.string("R_{Outer}; R_{Outer}"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("topHPD5ROuter"),
        )
        )
)

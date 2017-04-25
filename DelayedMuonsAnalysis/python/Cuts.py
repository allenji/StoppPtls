import FWCore.ParameterSet.Config as cms
import copy

########################################
#dummy cut
########################################
cutDummy = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

cutDummyStage1 = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

########################################
#not in cavern walls
#######################################
cutNotCavernWalls = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("stoppedParticleR < 728.5 && fabs(stoppedParticleZ) < 1080"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Not in Cavern Walls")
)

########################################
#bx
#######################################
cutBx = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("abs(bxWrtBunch) > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("BX veto")
)

########################################
#vertex
#######################################
cutVertexNumber = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nVtx = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Vertex veto")
)

########################################
#pre-preselection cuts
########################################

cutPrePreDSADtTofNDofUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 0 TOF nDof")
)

cutCscSegNumber = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string("= 0"),
    alias = cms.string("0 CSC Segments")
)

########################################
#preselection upper only DSA cuts
########################################
cutPreMinNDSAsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("> 0"),
    alias = cms.string("Number of DSA Tracks > 0")
)

cutPreMaxNDSAsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("< 6"),
    alias = cms.string("Number of DSA Tracks < 6")
)

cutPreDSAUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi > 0."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("At least one DSA track in upper hemisphere")
)

cutPreDSAPtUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 1 DT chambers with valid hits")
)

cutPreDSAAtLeast4DtChambersWithValidHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 3 DT chambers with valid hits")
)

cutPreDSANValidRpcHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 1 valid RPC hits")
)

cutPreDSADtTofNDofUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 7"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 7 TOF nDof")
)

cutPreDSANValidCscHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidCscHits < 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track 0 valid CSC hits")
)

cutDSAPtUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track $p_{T}$ > 50 \GeV")
)

########################################
#preselection upper and lower DSA cuts
########################################
cutPreMinNDSAs = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > -1 && secondaryTrack.pt > -1"),
    numberRequired = cms.string("> 0"),
    alias = cms.string("Number of DSA Tracks > 0")
)

cutPreMaxNDSAs = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > -1 && secondaryTrack.pt > -1"),
    numberRequired = cms.string("< 6"),
    alias = cms.string("Number of DSA Tracks < 6")
)

cutPreDSAUpperAndLower = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.phi > 0. && secondaryTrack.phi < 0."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("At least one DSA track in upper hemisphere and at least one DSA track in lower hemisphere")
)

cutPreDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > 10 && secondaryTrack.pt > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 1 && secondaryTrack.nDtChambersWithValidHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 1 DT chambers with valid hits")
)

cutPreDSAAtLeast4DtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 3 && secondaryTrack.nDtChambersWithValidHits > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 3 DT chambers with valid hits")
)

cutPreDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidRpcHits > 1 && secondaryTrack.nValidRpcHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 1 valid RPC hits")
)

cutPreDSADtTofNDof = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofNDof > 7 && secondaryTrack.dtTofNDof > 7"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 7 TOF nDof")
)

cutPreDSANValidCscHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidCscHits < 1 && secondaryTrack.nValidCscHits < 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks 0 valid CSC hits")
)

########################################
#final selection DSA cuts
########################################
cutDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track $p_{T}$ > 50 \GeV")
)

cutDSAEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track $|#eta|$ < 1.0")
)

cutDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 2 DT chambers with valid hits")
)

cutDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 2 valid RPC hits")
)

cutDSADtTofTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TimeInOut > -10 ns")
)

cutDSADtTofTimeInOutErr = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOutErr < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TimeInOut Error < 5 ns")
)

cutDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofDirection > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TOF Direction == 1")
)

cutDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track #beta_{Free}^{-1} > 0.5")
)




########################################
#upper and lower DSA selection cuts
########################################
cutUpperLowerDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > 50 && secondaryTrack.pt > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks $p_{T}$ > 50 \GeV")
)

cutUpperLowerDSAEta = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("abs(track.eta) < 1.0 && abs(secondaryTrack.eta) < 1.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks $|#eta|$ < 1.0")
)

cutUpperLowerDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 2 && secondaryTrack.nDtChambersWithValidHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 2 DT chambers with valid hits")
)

cutUpperLowerDSANDtChambersWithValidHitsTight = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 3 && secondaryTrack.nDtChambersWithValidHits > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 3 DT chambers with valid hits")
)

cutUpperLowerDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidRpcHits > 2 && secondaryTrack.nValidRpcHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 2 valid RPC hits")
)

cutUpperLowerDSADtTofTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpInOut > -10 && secondaryTrack.dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeInOut > -10 ns")
)

cutUpperLowerDSADtTofTimeInOutErr = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpInOutErr < 5 && secondaryTrack.dtTofTimeAtIpInOutErr < 5 && track.dtTofTimeAtIpInOutErr > -999 && secondaryTrack.dtTofTimeAtIpInOutErr > -999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeInOut Error < 5 ns")
)

cutUpperLowerDSADtTofTimeOutInErr = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpOutInErr < 5 && secondaryTrack.dtTofTimeAtIpOutInErr < 5 && track.dtTofTimeAtIpOutInErr > -999 && secondaryTrack.dtTofTimeAtIpOutInErr > -999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeOutIn Error < 5 ns")
)

cutUpperLowerDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofDirection > 0 && secondaryTrack.dtTofDirection > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks TOF Direction >= 1")
)

cutUpperLowerDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofFreeInverseBeta > 0.5 && secondaryTrack.dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks #beta_{Free}^{-1} > 0.5")
)

cutUpperLowerDSADeltaTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) > -20 && (track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta TimeInOut > -20 ns")
)

cutUpperLowerDSADeltaTimeInOutClosureTest = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) > -40 && (track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta TimeInOut > -40 ns")
)

cutUpperLowerDSADeltaTimeOutIn = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) > -30 && (track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta TimeOutIn > -30 ns")
)

cutUpperLowerDSADeltaTimeOutInClosureTest = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) > -40 && (track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta TimeOutIn > -40 ns")
)



########################################
#lower DSA cut
########################################

cutLowerDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("secondaryTracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Lower DSA Track #beta_{Free}^{-1} > 0.0")
)

########################################
#upper and lower DSA ABCD cuts
########################################

cutLowerDSARpcBxPattern = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("secondaryTrack.rpcHitBxPattern == 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Lower DSA Track RPC Hit BXs==0 ")
)

cutUpperLowerDSADeltaRpcHitBxAverage = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    #cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -0.9 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -0.3 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta RPC Hit BX Average > -0.3")
)

cutUpperLowerDSADeltaRpcHitBxAverageInverted = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) <= -0.3 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta RPC Hit BX Average <= -0.3")
)
 
cutUpperLowerDSAUpperP52 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 52."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 52 \GeV")
)

cutUpperLowerDSAUpperP52Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 52."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 52 \GeV")
)

cutUpperLowerDSAUpperP53 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 53."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 53 \GeV")
)

cutUpperLowerDSAUpperP53Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 53."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 53 \GeV")
)

cutUpperLowerDSAUpperP55 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 55."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 55 \GeV")
)

cutUpperLowerDSAUpperP55Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 55."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 55 \GeV")
)

cutUpperLowerDSAUpperP60 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 60."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 60 \GeV")
)

cutUpperLowerDSAUpperP60Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 60."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 60 \GeV")
)

cutUpperLowerDSAUpperP63 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 63."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 63 \GeV")
)

cutUpperLowerDSAUpperP63Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 63."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 63 \GeV")
)

cutUpperLowerDSAUpperP65 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 65."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 65 \GeV")
)

cutUpperLowerDSAUpperP65Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 65."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 65 \GeV")
)

cutUpperLowerDSAUpperP70 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 70."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 70 \GeV")
)

cutUpperLowerDSAUpperP70Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 70."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 70 \GeV")
)

cutUpperLowerDSAUpperP90 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 90."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 90 \GeV")
)

cutUpperLowerDSAUpperP90Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 90."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 90 \GeV")
)

cutUpperLowerDSAUpperP100 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 100."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 100 \GeV")
)

cutUpperLowerDSAUpperP100Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 100."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 100 \GeV")
)

cutUpperLowerDSAUpperP110 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 110."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 110 \GeV")
)

cutUpperLowerDSAUpperP110Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 110."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 110 \GeV")
)

cutUpperLowerDSAUpperP120 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 120."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 120 \GeV")
)

cutUpperLowerDSAUpperP120Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 120."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 120 \GeV")
)

cutUpperLowerDSAUpperP130 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 130."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 130 \GeV")
)

cutUpperLowerDSAUpperP130Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 130."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 130 \GeV")
)

cutUpperLowerDSAUpperP150 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 150."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 150 \GeV")
)

cutUpperLowerDSAUpperP150Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 150."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 150 \GeV")
)

cutUpperLowerDSAUpperP160 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 160."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 160 \GeV")
)

cutUpperLowerDSAUpperP160Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 160."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 160 \GeV")
)

cutUpperLowerDSAUpperP170 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 170."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 170 \GeV")
)

cutUpperLowerDSAUpperP170Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 170."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 170 \GeV")
)

cutUpperLowerDSAUpperP190 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 190."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 190 \GeV")
)

cutUpperLowerDSAUpperP190Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 190."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 190 \GeV")
)

cutUpperLowerDSAUpperP200 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 200."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 200 \GeV")
)

cutUpperLowerDSAUpperP200Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 200."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 200 \GeV")
)

cutUpperLowerDSAUpperP230 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 230."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 230 \GeV")
)

cutUpperLowerDSAUpperP230Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 230."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 230 \GeV")
)

cutUpperLowerDSAUpperP240 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 240."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 240 \GeV")
)

cutUpperLowerDSAUpperP240Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 240."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 240 \GeV")
)

cutUpperLowerDSAUpperP260 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 260."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 260 \GeV")
)

cutUpperLowerDSAUpperP260Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 260."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 260 \GeV")
)

cutUpperLowerDSAUpperP290 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 290."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p > 290 \GeV")
)

cutUpperLowerDSAUpperP290Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p <= 290."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track p < 290 \GeV")
)


########################################
#upper and lower DSA ABCD cuts for syst
########################################


cutUpperLowerDSAUpperPGreater90Less150 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("track.p > 90. && track.p < 150."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track 90 < p < 150 \GeV")
)

cutUpperLowerDSADeltaRpcHitBxAverageGreaterNeg1p2LessNeg0p9 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) <= -0.9 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -1.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("-1.2 < #Delta RPC Hit BX Average <= -0.9")
)

cutUpperLowerDSADeltaRpcHitBxAverageLessNeg1p2 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) <= -1.2 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("-1.2 < #Delta RPC Hit BX Average <= -0.9")
)

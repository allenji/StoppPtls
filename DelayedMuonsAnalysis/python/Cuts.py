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
    cutString = cms.string("bxWrtBunch > 1"),
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
    alias = cms.string("Upper DSA Track $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 1 DT chambers with valid hits")
)

cutPreDSANValidRpcHitsUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 1 valid RPC hits")
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
    alias = cms.string("Upper DSA Track 0 valid CSC hits")
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
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track $p_{T}$ > 40 \GeV")
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
    cutString = cms.string("track.pt > 40 && secondaryTrack.pt > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks $p_{T}$ > 40 \GeV")
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

cutUpperLowerDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofDirection > 0 && secondaryTrack.dtTofDirection > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks TOF Direction =>= 1")
)

cutUpperLowerDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofFreeInverseBeta > 0.5 && secondaryTrack.dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper and Lower DSA Tracks #beta_{Free}^{-1} > 0.5")
)

cutUpperLowerDSADeltaTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) > -22 && (track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta TimeInOut > -22 ns")
)

cutLowerDSARpcBxPattern = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("secondaryTrack.rpcHitBxPattern == 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Lower DSA Track RPC Hit BXs==0 ")
)

cutUpperLowerDSADeltaRpcHitBxAverage = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) > -1.0 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta RPC Hit BX Average > -1.0")
)

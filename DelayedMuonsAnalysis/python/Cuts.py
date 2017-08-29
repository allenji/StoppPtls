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

cutPrePreDSADtTofNDofExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track > 0 TOF nDof")
)

cutCscSegNumber = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string("= 0"),
    alias = cms.string("0 CSC Segments")
)

########################################
#preselection exactly 1 DSA cuts
########################################
cutPreMinNDSAsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("> 0"),
    alias = cms.string("Number of DSA Tracks > 0")
)

cutPreMaxNDSAsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("< 2"),
    alias = cms.string("Number of DSA Tracks < 2")
)

cutPreDSAUpperOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi > 0."),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Exactly one DSA track in upper hemisphere")
)

cutPreDSALowerOnly = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi < 0."),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Exactly one DSA track in lower hemisphere")
)

cutPreDSAPtExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHitsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track > 1 DT chambers with valid hits")
)

cutPreDSAAtLeast4DtChambersWithValidHitsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 3"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track > 3 DT chambers with valid hits")
)

cutPreDSANValidRpcHitsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track > 1 valid RPC hits")
)

cutPreDSADtTofNDofExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 7"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track > 7 TOF nDof")
)

cutPreDSANValidCscHitsExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidCscHits < 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track 0 valid CSC hits")
)

cutDSAPtExactlyOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("DSA Track $p_{T}$ > 50 \GeV")
)


########################################
#preselection at least 1 DSA cuts
########################################

cutPreDSAAtLeastOneUpper = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi > 0."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("At least one DSA track in upper hemisphere")
)

cutPreDSAAtLeastOneLower = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi < 0."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("At least one DSA track in lower hemisphere")
)

cutPreDSAPtAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 1 DT chambers with valid hits")
)

cutPreDSAAtLeast4DtChambersWithValidHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 3 DT chambers with valid hits")
)

cutPreDSANValidRpcHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track > 1 valid RPC hits")
)

cutPreDSADtTofNDofAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 7"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 7 TOF nDof")
)

cutPreDSANValidCscHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidCscHits < 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("DSA Track 0 valid CSC hits")
)

cutDSAPtAtLeastOne = cms.PSet(
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

cutPreDSAExactly1UpperAndExactly1Lower = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.phi > 0. && secondaryTrack.phi < 0."),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Exactly one DSA track in upper hemisphere and exactly one DSA track in lower hemisphere")
)

cutPreDSA3DangleBackToBack = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("acos((track.px*secondaryTrack.px + track.py*secondaryTrack.py + track.pz*secondaryTrack.pz)/sqrt((track.px*track.px + track.py*track.py + track.pz*track.pz)*(secondaryTrack.px*secondaryTrack.px + secondaryTrack.py*secondaryTrack.py + secondaryTrack.pz*secondaryTrack.pz))) > 3.04 && acos((track.px*secondaryTrack.px + track.py*secondaryTrack.py + track.pz*secondaryTrack.pz)/sqrt((track.px*track.px + track.py*track.py + track.pz*track.pz)*(secondaryTrack.px*secondaryTrack.px + secondaryTrack.py*secondaryTrack.py + secondaryTrack.pz*secondaryTrack.pz))) < 3.24"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("3.04 < 3D angle between upper and lower tracks < 3.24")
)

cutPreDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > 10 && secondaryTrack.pt > 10"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks $p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 1 && secondaryTrack.nDtChambersWithValidHits > 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 1 DT chambers with valid hits")
)

cutPreDSAAtLeast4DtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 3 && secondaryTrack.nDtChambersWithValidHits > 3"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 3 DT chambers with valid hits")
)

cutPreDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidRpcHits > 1 && secondaryTrack.nValidRpcHits > 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 1 valid RPC hits")
)

cutPreDSADtTofNDof = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofNDof > 7 && secondaryTrack.dtTofNDof > 7"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 7 TOF nDof")
)

cutPreDSANValidCscHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidCscHits < 1 && secondaryTrack.nValidCscHits < 1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks 0 valid CSC hits")
)

########################################
#final selection DSA cuts
########################################
cutDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track $p_{T}$ > 50 \GeV")
)

cutDSAEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track $|#eta|$ < 1.0")
)

cutDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 2"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track > 2 DT chambers with valid hits")
)

cutDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 2"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track > 2 valid RPC hits")
)

cutDSADtTofTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track TimeInOut > -10 ns")
)

cutDSADtTofTimeInOutErr = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOutErr < 5"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track TimeInOut Error < 5 ns")
)

cutDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofDirection > 0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track TOF Direction == 1")
)

cutDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper DSA Track #beta_{Free}^{-1} > 0.5")
)




########################################
#final selection DSA cuts
########################################
cutDSAPtAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track $p_{T}$ > 50 \GeV")
)

cutDSAEtaAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track $|#eta|$ < 1.0")
)

cutDSANDtChambersWithValidHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 2 DT chambers with valid hits")
)

cutDSANValidRpcHitsAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track > 2 valid RPC hits")
)

cutDSADtTofTimeInOutAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TimeInOut > -10 ns")
)

cutDSADtTofTimeInOutErrAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOutErr < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TimeInOut Error < 5 ns")
)

cutDSADtTofDirectionAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofDirection > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track TOF Direction == 1")
)

cutDSADtTofFreeInverseBetaAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Upper DSA Track #beta_{Free}^{-1} > 005")
)




########################################
#upper and lower DSA selection cuts
########################################
cutUpperLowerDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.pt > 50 && secondaryTrack.pt > 50"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks $p_{T}$ > 50 \GeV")
)

cutUpperLowerDSAPtSmeared = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("ptSmearedUpper > 50. && ptSmearedLower > 50."),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Smeared Upper and Lower DSA Tracks $p_{T}$ > 50 \GeV")
)

cutUpperLowerDSAEta = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("abs(track.eta) < 1.0 && abs(secondaryTrack.eta) < 1.0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks $|#eta|$ < 1.0")
)

cutUpperLowerDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 2 && secondaryTrack.nDtChambersWithValidHits > 2"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 2 DT chambers with valid hits")
)

cutUpperLowerDSANDtChambersWithValidHitsTight = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nDtChambersWithValidHits > 3 && secondaryTrack.nDtChambersWithValidHits > 3"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 3 DT chambers with valid hits")
)

cutUpperLowerDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.nValidRpcHits > 2 && secondaryTrack.nValidRpcHits > 2"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks > 2 valid RPC hits")
)

cutUpperLowerDSADtTofTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpInOut > -10 && secondaryTrack.dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeInOut > -10 ns")
)

cutUpperLowerDSADtTofTimeInOutErr = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpInOutErr < 5 && secondaryTrack.dtTofTimeAtIpInOutErr < 5 && track.dtTofTimeAtIpInOutErr > -999 && secondaryTrack.dtTofTimeAtIpInOutErr > -999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeInOut Error < 5 ns")
)

cutUpperLowerDSADtTofTimeOutInErr = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofTimeAtIpOutInErr < 5 && secondaryTrack.dtTofTimeAtIpOutInErr < 5 && track.dtTofTimeAtIpOutInErr > -999 && secondaryTrack.dtTofTimeAtIpOutInErr > -999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks TimeOutIn Error < 5 ns")
)

cutUpperLowerDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofDirection > 0 && secondaryTrack.dtTofDirection > 0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks TOF Direction >= 1")
)

cutUpperLowerDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("track.dtTofFreeInverseBeta > 0.5 && secondaryTrack.dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Upper and Lower DSA Tracks #beta_{Free}^{-1} > 0.5")
)

cutUpperLowerDSADeltaTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) > -20 && (track.dtTofTimeAtIpInOut - secondaryTrack.dtTofTimeAtIpInOut) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta TimeInOut > -20 ns")
)

cutUpperLowerDSADeltaTimeOutIn = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) > -30 && (track.dtTofTimeAtIpOutIn - secondaryTrack.dtTofTimeAtIpOutIn) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta TimeOutIn > -30 ns")
)



########################################
#lower DSA cut
########################################

cutLowerDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("secondaryTracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Lower DSA Track #beta_{Free}^{-1} > 0.0")
)

cutLowerDSADtTofFreeInverseBetaAtLeastOne = cms.PSet(
    inputCollection = cms.vstring("secondaryTracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Lower DSA Track #beta_{Free}^{-1} > 0.0")
)

########################################
#upper and lower DSA ABCD cuts
########################################

cutUpperLowerDSADeltaRpcTimeNeg50 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -50 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -50 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg45 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -45 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -45 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg40 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -40 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -40 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg35 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -35 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -35 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg30 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -30 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -30 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg25 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -25 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -25 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg20 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -20 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -20 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg15 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -15 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -15 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg10 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -10 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -10 ns")
)


cutUpperLowerDSADeltaRpcTimeNeg7p5 = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) > -7.5 && (track.rpcHitBxAverage - secondaryTrack.rpcHitBxAverage) < 999"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} > -7.5 ns")
)

cutUpperLowerDSADeltaRpcTimeNeg7p5Inverted = cms.PSet(
    inputCollection = cms.vstring("tracks","secondaryTracks"),
    cutString = cms.string("(25.0*track.rpcHitBxAverage - 25.0*secondaryTrack.rpcHitBxAverage) < -7.5"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("#Delta t_{RPC} < -7.5 ns")
)

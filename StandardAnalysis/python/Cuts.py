import FWCore.ParameterSet.Config as cms
import copy
cutJetBarrel = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 1.3"),
    numberRequired = cms.string(">= 1"),
)

###########################################
##jets
##########################################
cutJetEnergy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > 70"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{jet}$ > 70 \GeV")
)

cutLeadingJetEnergySmeared = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("leadingJetEnergySmeared > 70"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Smeared $E_{jet}$ > 70 \GeV")
)

########################################
##Stopped Particle in EB or HB
#######################################
cutStoppedParticleEBHB = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("(stoppedParticleR>=184 && stoppedParticleR<=295 && fabs(stoppedParticleZ<5000)) || (stoppedParticleR>=131 && stoppedParticleR<=184 && fabs(stoppedParticleZ<3760))"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Stopped Particle in EB or HB")
)

########################################
##bx
#######################################
cutBx = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("abs(bxWrtBunch) > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("BX veto")
)

########################################
##vertex
#######################################
cutVertexNumber = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nVtx = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Vertex veto")
)

#######################################
##CSCSeg-Halo veto
######################################
cutCscSegNumber = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string("= 0"),
    alias = cms.string("Halo veto")
)

cutCscSegNumberInverted = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Number of CSC Segments > 0")
)

cutCscSegNumberInverted_newVeto = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("havingCscDeltaJet0p4R3p4 = 1"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Csc Segment near leading jet > 0")
)


#######################################
##hcalnoise
#######################################
cutNoise = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("noiseFilterResult = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HCAL noise veto")
)

cutNoiseInverted = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("noiseFilterResult = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HCAL noise")
)

cutBeamHaloFilter2016Tight = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("globalTightHaloId2016 = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("beam halo filter veto 2016 tight")
)

#######################################
##towerIPhi
######################################
cutTowerIPhi = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nTowerSameiPhi < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nTowiPhi < 5")
)

#######################################
##towerIPhiFraction
#######################################
cutTowerFraction = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("leadingIPhiFractionValue < 0.95"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{i\phi}/E_{jet}$ < 0.95")
)

######################################
##hpdR1
######################################
cutHpdR1 = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5R1 > 0.15 ) && ( topHPD5R1 <= 1.0 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$R_{1}$ > 0.15")
)

######################################
##hpdR2
#####################################
cutHpdR2 = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5R2 > 0.1 ) && ( topHPD5R2 < 0.8 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$R_{2}$ > 0.1")
)

######################################
##hpdRpeak
#####################################
cutHpdRPeak = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5RPeak > 0.3 ) && ( topHPD5RPeak < 0.7 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("0.3 < $R_{Peak}$ < 0.7")
)

######################################
##hpdRPeakSample
######################################
cutHpdRPeakSample = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5PeakSample > 2 ) && ( topHPD5PeakSample < 6 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("2< Peak sample < 6")
)

######################################
##hpdROuter
######################################
cutHpdROuter = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5ROuter < 0.3 ) && ( topHPD5ROuter >= 0.0 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$R_{Outer}$ < 0.3")
)

######################################
##outerdt
#####################################
cutOuterDT = cms.PSet (
    inputCollection = cms.vstring("dtsegs"),
    cutString = cms.string("r > 560"),
    numberRequired = cms.string("< 1"),
    alias = cms.string("Number of Outer DT Segments = 0")
) 

#######################################
##outerRpc
######################################
cutOuterRpc = cms.PSet (
    inputCollection = cms.vstring("rpchits"),
    cutString = cms.string("r > 560"),
    numberRequired = cms.string("< 2"),
    alias = cms.string("Number of Outer RPC Hits < 2")
)

#######################################
##rpcPair
######################################
cutRpcPair = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("maxRPCDeltaPhi < 3"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("$max(\Delta\phi(RPCHit_{i}, RPCHit_{j}))$ < 3)")
)

######################################
##rpcClosePair
######################################
cutCloseRpcPair = cms.PSet(
    cutString = cms.string('nCloseRPCPairs < 2'),
    inputCollection = cms.vstring('eventvariables'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("Number of close RPC pairs < 2")
)

#######################################
##dtPair
######################################
cutDTPair = cms.PSet(
    cutString = cms.string('maxDeltaPhi < 1.57'),
    inputCollection = cms.vstring('eventvariables'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("max($#Delta#phi$(DT Segment$_{i}$, DT Segment$_{j}$)) < $#pi/2$")
)

######################################
##maxDeltaJetPhi
######################################
cutMaxDeltaJetPhi = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxDeltaJetPhi < 1'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("max($#Delta#phi$(DT Segment$_{i}$, Leading jet)) < 1")
)

#######################################
##select cosmics
#######################################
cutCosmics = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxDeltaPhi >= 1.57 || maxDeltaJetPhiNoDTST4 >= 1. || nDTStation3 > 0 || nDTStation4 > 1 || closeOuterAllDTPairDeltaPhi0p5 > 0 || minDeltaRDTST4RPCInner3Layers < 0.5 || nCloseOuterAllBarrelRPCPairDeltaR0p2Deltar > 0'),
    #cutString = cms.string('maxDeltaPhi >= 1.57 || maxDeltaJetPhi >= 1. || outerDT >= 1 || nCloseOuterAllBarrelRPCPairDeltaR0p2 >= 1 || minDeltaPhiCscDT <= 0.6 || (minDeltaPhiCscDT > 1.7 && minDeltaPhiCscDT < 3.2) || minDeltaPhiCscPair <= 0.3'),
    #cutString = cms.string('maxDeltaPhi >= 1.57 || maxDeltaJetPhi >= 1. || outerDT >= 1 || nCloseOuterAllBarrelRPCPairDeltaR0p2 >= 1 || NOuterCsc > 0'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("pass one of cosmic selections (OR of DT segments and RPC pair cuts)")
)
cutNumberOfDT = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('dtSegN >= 1'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("Has at least one DT seg")
)
cutMoreOuterDT = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('innerDT /  outerDT < 2'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("More outer DTs than inner ones")
)

#######################################
##jeteta
#######################################
cutJetEta = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetEta < 1'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("$\eta_{jet}$ < 1.0")
)
cutJetEta1p3 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetEta < 1.3'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("$\eta_{jet}$ < 1.3")
)

#######################################
##leadingjetN90
#######################################
cutJetN90 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetN90 > 3'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("n90$_{jet}$ > 3")
)


#######################################
##halo tag and probe selection
#######################################

#at least 1 jet
cutJetNumber = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > 0."),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nJets > 0")
)

#csc segments in at least 3 layers
cutCscSegNLayers = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    #cutString = cms.string("nCscLayers >= 3"),
    cutString = cms.string("nLayersNearJetDeltaPhi0p2 >= 2"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nCscLayers >= 2")
)

#min delta phi between csc seg and jet
cutMinDeltaPhiCscJet = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('minDeltaPhiCscJet > 0.4'),
    #cutString = cms.string('minDeltaPhiCscJet < 0.4'),
    numberRequired = cms.string('= 1'),
    #alias = cms.string("$\Delta\phi$(CSCSegment_{i}, Leading jet) < 0.4")
    alias = cms.string("$\Delta\phi$(CSCSegment_{i}, Leading jet) > 0.4")
)

########################################
## for rpc study
#######################################
cutDT = cms.PSet(
    inputCollection = cms.vstring("dtsegs"),
    cutString = cms.string("abs(r) > -1"),
    numberRequired = cms.string("= 0"),
    alias = cms.string("no DT segments")
)

cutInnerRPCBarrel = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('innerRPCbarrel >= 5'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("more than 4 inner barrel RPC hits"),
    )
newRPCMaxOuterRPCDeltaPhi = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxRPCDeltaPhi_outer < 2.3'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("maxOuterRPCDeltaPhi < 2.3"),
    )
newNOuterAllRPCHitsDeltaR = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nCloseOuterAllRpcPairDeltaR0p2 < 1'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nCloseOuterAllRpcPairDeltaR0p2 < 1"),
    )
newNOuterAllBarrelRPCHitsDeltaR = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nCloseOuterAllBarrelRPCPairDeltaR0p2 < 1'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Close Outer Barrel RPC Pairs < 1"),
    )
getBarrelRPCHits = cms.PSet(
    inputCollection = cms.vstring('rpchits'),
    cutString = cms.string('region = 0'),
    numberRequired = cms.string("> 0"),
    alias = cms.string("have more than one barrel RPC hits"),
    )
newTestNOuterAllRPCBarrelHitsDeltaR = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nCloseOuterAllBarrelRPCPairDeltaR0p2 > 10'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nCloseOuterAllBarrelRPCPairDeltaR0p2 > 10"),
    )
#dummy cut
cutDummy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

cutNTowerSameiRbx = cms.PSet(
    inputCollection = cms.vstring('events'),
    cutString = cms.string('nTowerSameiRbx < 30'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("nTowerSameiRbx < 30")
)

cutHaloCoarse = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("cscSegN > 2"),
    numberRequired = cms.string("> 0"),
)

cutHaloStrict = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("cscSegN > 10"),
    numberRequired = cms.string("> 0"),
)

cutCosmicCoarse = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("dtSegN > 4"),
    numberRequired = cms.string("> 0"),
)

cutCosmicStrict = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("dtSegN > 10"),
    numberRequired = cms.string("> 0"),
)

cutMaxiEtaDiffSameiRbx = cms.PSet(
    inputCollection = cms.vstring('events'),
    cutString = cms.string('maxiEtaDiffSameiRbx < 11'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("maxiEtaDiffSameiRbx < 11")
)

cutMaxiEtaDiffSameiRbxGeq11 = cms.PSet(
    inputCollection = cms.vstring('events'),
    cutString = cms.string('maxiEtaDiffSameiRbx >= 11'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("maxiEtaDiffSameiRbx >= 11")
)

cutNTowerDiffiEtaSameiRbx = cms.PSet(
    inputCollection = cms.vstring('events'),
    cutString = cms.string('nTowerDiffiEtaSameiRbx < 9'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("nTowerDiffiEtaSameiRbx < 9")
)

##################CSC##################
CutCscEndcap = cms.PSet(
    inputCollection = cms.vstring('cscsegs'),
    cutString = cms.string('endcap = 1'),
    numberRequired = cms.string('>= 1'),
    alias = cms.string("having cscsegs in endcap 1")
)

CutCscStation = cms.PSet(
    inputCollection = cms.vstring('cscsegs'),
    cutString = cms.string('station = 1'),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("having cscsegs in station 1")
)

CutHavingSpecificCsc = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('havingSpecificCsc'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("having cscsegs in endcap 1 station 1"),
)

CutCscFilter = cms.PSet(
    inputCollection = cms.vstring('cscsegs'),
    cutString = cms.string('endcap != 1 || station != 1'),
    numberRequired = cms.string('>= 1'),
    alias = cms.string("filter cscsegs"),
)

cutJetEnergyInverted = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy < 70"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{jet}$ < 70 \GeV")
)

cutTowerIPhiNoise = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nTowerSameiPhi > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nTowiPhi > 10")
)

cutHpdR2Noise = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("topHPD5R2 < 0.075"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$R_{2}$ < 0.075")
)

cutHpdRPeakNoise = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("topHPD5RPeak > 0.8"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$R_{Peak}$ > 0.8")
)

cutCscSegNumberOne = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of CSC Segments = 1")
)

cutDeltaMinCscJet = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("minDeltaPhiCscJet < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("minDeltaPhiCscJet < 0.2")
)

cutCscSegNumberGT1 = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Number of CSC Segments > 1")
)

cutCscSegNumberGT1JET = cms.PSet(
    inputCollection = cms.vstring("cscsegs","eventvariables"),
    cutString = cms.string("abs(cscsegs.phi - eventvariables.leadingJetPhi) < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("angle csc jet")
)

cutNCscSegJetDelta0p2 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2 > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("at least one csc segment within delptaphi 0.2 of leading jet")
)

cutNoCscSegJetDeltaPhi0p2PosZ = cms.PSet(
     inputCollection = cms.vstring("eventvariables"),
     cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapPosZ = 0"),
     numberRequired = cms.string("= 1"),
     alias = cms.string("no csc segment within deltaphi 0.2 of leading jet in pos endcap")
)

cutNoCscSegJetDeltaPhi0p2MinZ = cms.PSet(
     inputCollection = cms.vstring("eventvariables"),
     cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapMinZ = 0"),
     numberRequired = cms.string("= 1"),
     alias = cms.string("no csc segment within deltaphi 0.2 of leading jet in neg endcap")
)

cutCscSegNLayersNearJets = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nLayersNearJetDeltaPhi0p2 >= 2"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nCscLayersNearJetDeltaPhi0p2 >= 2")
)

cutBeam1 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("meanCscDirectionNearJetDeltaPhi0p2 >= 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Beam 1")
)

cutBeam2 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("meanCscDirectionNearJetDeltaPhi0p2 < 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Beam 2")
)

cutCscRDT400 = cms.PSet (
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("r > 340"),
    numberRequired = cms.string("= 0"),
    alias = cms.string("csc R > 160")
)

cutCscNHit3 = cms.PSet (
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits = 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nHits = 3")
)

cutCscNHit6 = cms.PSet (
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits = 6"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nHits = 6")
)

cutJetNumber1 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > 0."),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nJets = 1")
)
cutDeltaPhiCscJet = cms.PSet(
    inputCollection = cms.vstring("cscsegs","jets"),
    cutString = cms.string("abs ( deltaPhi (cscseg , jets) ) < 0.4"),
    numberRequired = cms.string("> 0"),
    alias = cms.string("deltaCscJet < 0.4")
)

cutBeamHaloCscNearJet = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("havingCscDeltaJet0p4R3p4 = 1"),
    numberRequired = cms.string("= 1"),
)

cutNoBeamHaloCscNearJet = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("havingCscDeltaJet0p4R3p4 = 0"),
    numberRequired = cms.string("= 1"),
)

cutPass2016TightHaloFilter = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("globalTightHaloId2016 = 1"),
    numberRequired = cms.string("= 1"),
)

cutKillBy2016TightHaloFilter = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("globalTightHaloId2016 = 0"),
    numberRequired = cms.string("= 1"),
)

cutNoCscPos = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapPosZ = 0"),
    numberRequired = cms.string("= 1"),
)

cutNoCscNeg = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapMinZ = 0"),
    numberRequired = cms.string("= 1"),
)


cutOneCscSeg = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("cscSegN = 1"),
    numberRequired = cms.string("= 1"),
)

cutNIsolatedNoiseChannel = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("numIsolatedNoiseChannels = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("numIsolatedNoiseChannels = 0")
)

cutIsolatedNoiseSumE = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("isolatedNoiseSumE <= 0"),
    numberRequired = cms.string("= 1"),
)

cutIsolatedNoiseSumEt = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("isolatedNoiseSumEt <= 0"),
    numberRequired = cms.string("= 1"),
)

cutJetEnergyGt30 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy >= 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{jet}$ > 50 \GeV")
)

cutMinDeltaPhiCscDt = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(minDeltaPhiCscDT > 0.6 && minDeltaPhiCscDT < 1.7) || minDeltaPhiCscDT = 999" ),
    numberRequired = cms.string("= 1"),
)

cutMinDeltaPhiCscPair = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("minDeltaPhiCscPair > 0.3"),
    numberRequired = cms.string("= 1"),
)

cutCscSeg = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("r <= 340"),
    numberRequired = cms.string(">= 1"),
)

cutNOuterCsc = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("NOuterCsc = 0"),
    numberRequired = cms.string("= 1"),
)

cutMaxDeltaPhiCscDt = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("maxDeltaPhiCscDT < 1" ),
    numberRequired = cms.string("= 1"),
)

cutMaxDeltaPhiCscPair = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("maxDeltaPhiCscPair < 1.5"),
    numberRequired = cms.string("= 1"),
)

cutNoDT = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("dtSegN = 0"),
    numberRequired = cms.string("= 1"),
    )

cutNoOuterBarrelRPC = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("outerRPCbarrel = 0"),
   numberRequired = cms.string("= 1"),
   )

cutMinDeltaPhiOuterCscJet = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("minDeltaPhiOuterCscJet > 1.3" ),
    numberRequired = cms.string("= 1"),
)

cutHavingNoCscSegNHit56 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("havingCscSegNHit56 = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("new halo veto")
)

cutNCaloTowerDiffRBX = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nTowerDiffRbxDeltaR0p5 < 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nTowerDiffRbxDeltaR0p5 < 2")
)

cutLeadingJetEMFractionGTp1 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("leadingJetEMFraction > 0.9" ),
    numberRequired = cms.string("= 1"),
)

cutJetN90LT2 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetN90 < 2'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("n90$_{jet}$ < 2")
)

cutJetN90Eq2 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetN90 = 2'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("n90$_{jet}$ = 2")
)


cutDTSegN1 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("dtSegN = 1"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of DT Segments = 1")
)

newNOuterAllBarrelRPCHitsDeltaREq1 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nCloseOuterAllBarrelRPCPairDeltaR0p2 = 1'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Close Outer Barrel RPC Pairs = 1"),
    )

newNOuterAllBarrelRPCHitsDeltaRDeltar = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nCloseOuterAllBarrelRPCPairDeltaR0p2Deltar = 0'),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Close Outer Barrel RPC Pairs with Deltar constraint = 0"),
    )

cutNDTStation3 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nDTStation3 = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of DT Segments in station 3 = 0")
)

cutNDTStation4 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nDTStation4 < 2"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of DT Segments in station 4 < 2")
)

cutCloseOuterAllDTPairDeltaPhi0p5 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("closeOuterAllDTPairDeltaPhi0p5 = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of close DT outer all pairs = 0")
)

cutMaxDeltaJetPhiNoDTST4 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxDeltaJetPhiNoDTST4 < 1'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("max($#Delta#phi$(DT Segment$_{i}$(no st 4), Leading jet)) < 1")
)

cutMinDeltaRDTST4RPCInner3Layers = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('minDeltaRDTST4RPCInner3Layers > 0.5'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("minDeltaRDTST4RPCInner3Layers > 0.5")
)
cutMinDeltaRDTST4LeadingJet = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('minDeltaRDTST4LeadingJet > 1.5'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("minDeltaRDTST4LeadingJet")
)

cutMinDeltaROuterRpcInnerDT = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('minDeltaROuterRPCInnerDT > 0.5'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("minDeltaROuterRpcInnerDT > 0.5")
)

cutNDTWhl0Seg4 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nDTWhl0Seg4 > 0'),
    numberRequired = cms.string('= 1'),
)

cutNDTWhl0Seg10 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('nDTWhl0Seg10 > 0'),
    numberRequired = cms.string('= 1'),
)

cutPassNoiseTowerFraction = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("leadingIPhiFractionValue >= 0.95"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{i\phi}/E_{jet}$ >= 0.95")
)


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
    cutString = cms.string("bxWrtBunch > 1"),
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
    cutString = cms.string("noiseFilterResult = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HCAL noise")
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
    cutString = cms.string("( topHPD5PeakSample > 0 ) && ( topHPD5PeakSample < 7 ) = 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Peak sample < 7")
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
    cutString = cms.string('maxDeltaPhi >= 1.57 || maxDeltaJetPhi >= 1. || outerDT >= 1 || nCloseOuterAllBarrelRPCPairDeltaR0p2 >= 1'),
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
    cutString = cms.string('( innerDT / outerDT) < 2'),
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
    cutString = cms.string("nCscLayers >= 3"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("nCscLayers >= 3")
)

#min delta phi between csc seg and jet
cutMinDeltaPhiCscJet = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('minDeltaPhiCscJet < 0.4'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("$\Delta\phi$(CSCSegment_{i}, Leading jet) < 0.4")
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


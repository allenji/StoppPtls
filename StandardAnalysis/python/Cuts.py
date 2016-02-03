import FWCore.ParameterSet.Config as cms
import copy

###########################################
##jets
##########################################
cutJetEnergy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > 70"),
    numberRequired = cms.string(">= 1")
)

########################################
##bx
#######################################
cutBx = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("bxWrtBunch > 1"),
    numberRequired = cms.string(">= 1")
)

########################################
##vertex
#######################################
cutVertexNumber = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nVtx = 0"),
    numberRequired = cms.string(">= 1")
)

#######################################
##CSCSeg-Halo veto
######################################
cutCscSegNumber = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string("= 0")
)

cutCscSegNumberInverted = cms.PSet(
    inputCollection = cms.vstring("cscsegs"),
    cutString = cms.string("nHits > -1"),
    numberRequired = cms.string(">= 1")
)


#######################################
##hcalnoise
#######################################
cutNoise = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("noiseFilterResult = 1"),
    numberRequired = cms.string(">= 1")
)

cutNoiseInverted = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("noiseFilterResult != 1"),
    numberRequired = cms.string(">= 1")
)

#######################################
##towerIPhi
######################################
cutTowerIPhi = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("nTowerSameiPhi < 5"),
    numberRequired = cms.string(">= 1")
)

#######################################
##towerIPhiFraction
#######################################
cutTowerFraction = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("leadingIPhiFractionValue < 0.95"),
    numberRequired = cms.string(">= 1")
)

######################################
##hpdR1
######################################
cutHpdR1 = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5R1 > 0.15 ) && ( topHPD5R1 <= 1.0 ) = 1"),
    numberRequired = cms.string(">= 1")
)

######################################
##hpdR2
#####################################
cutHpdR2 = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5R2 > 0.1 ) && ( topHPD5R2 < 0.8 ) = 1"),
    numberRequired = cms.string(">= 1")
)

######################################
##hpdRpeak
#####################################
cutHpdRPeak = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5RPeak > 0.3 ) && ( topHPD5RPeak < 0.7 ) = 1"),
    numberRequired = cms.string(">= 1")
)

######################################
##hpdRPeakSample
######################################
cutHpdRPeakSample = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5PeakSample > 0 ) && ( topHPD5PeakSample < 7 ) = 1"),
    numberRequired = cms.string(">= 1")
)

######################################
##hpdROuter
######################################
cutHpdROuter = cms.PSet(
    inputCollection = cms.vstring("events"),
    cutString = cms.string("( topHPD5ROuter < 0.3 ) && ( topHPD5ROuter >= 0.0 ) = 1"),
    numberRequired = cms.string(">= 1")
)

######################################
##outerdt
#####################################
cutOuterDT = cms.PSet (
    inputCollection = cms.vstring("dtsegs"),
    cutString = cms.string("r > 560"),
    numberRequired = cms.string("< 1")
) 

#######################################
##outerRpc
######################################
cutOuterRpc = cms.PSet (
    inputCollection = cms.vstring("rpchits"),
    cutString = cms.string("r > 560"),
    numberRequired = cms.string("< 2")
)

#######################################
##rpcPair
######################################
cutRpcPair = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("maxRPCDeltaPhi < 3"),
    numberRequired = cms.string("= 1")
)

######################################
##rpcClosePair
######################################
cutCloseRpcPair = cms.PSet(
    cutString = cms.string('nCloseRPCPairs < 2'),
    inputCollection = cms.vstring('eventvariables'),
    numberRequired = cms.string('= 1')
)

#######################################
##dtPair
######################################
cutDTPair = cms.PSet(
    cutString = cms.string('maxDeltaPhi < 1.57'),
    inputCollection = cms.vstring('eventvariables'),
    numberRequired = cms.string('= 1')
)

######################################
##maxDeltaJetPhi
######################################
cutMaxDeltaJetPhi = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxDeltaJetPhi < 1'),
    numberRequired = cms.string('= 1')
)

#######################################
##select cosmics
#######################################
cutCosmics = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('maxDeltaPhi >= 1.57 || maxDeltaJetPhi >= 1. || nCloseRPCPairs >= 2 || maxRPCDeltaPhi >= 3. || outerDT >= 1 || outerRPC >= 2'),
    numberRequired = cms.string('= 1')
)

#######################################
##jeteta
#######################################
cutJetEta = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetEta < 1'),
    numberRequired = cms.string('= 1')
)

#######################################
##leadingjetN90
#######################################
cutJetN90 = cms.PSet(
    inputCollection = cms.vstring('eventvariables'),
    cutString = cms.string('leadingJetN90 > 3'),
    numberRequired = cms.string('= 1')
)

import FWCore.ParameterSet.Config as cms
import copy

#jets
cutJetEnergy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > 70"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$E_{jet}$ > 70 \GeV")
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
##dtPair
######################################
cutDTPair = cms.PSet(
    cutString = cms.string('maxDeltaPhi < 1.57'),
    inputCollection = cms.vstring('eventvariables'),
    numberRequired = cms.string('= 1'),
    alias = cms.string("max($#Delta#phi$(DT Segment$_{i}$, DT Segment$_{j}$)) < $#pi/2$")
)

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


#dummy cut
cutDummy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)


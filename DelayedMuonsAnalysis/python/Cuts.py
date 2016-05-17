import FWCore.ParameterSet.Config as cms
import copy

########################################
#dummy cut
########################################
cutDummy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("energy > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
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
#preselection DSA cuts
########################################
cutPreMinNDSAs = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("> 0"),
    alias = cms.string("Number of DSA Tracks > 0")
)

cutPreMaxNDSAs = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("< 6"),
    alias = cms.string("Number of DSA Tracks < 6")
)

cutPreDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$p_{T}$ > 10 \GeV")
)

cutPreDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("> 1 DT chambers with valid hits")
)

cutPreDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("> 1 valid RPC hits")
)

cutPreDSADtTofNDof = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofNDof > 7"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("> 7 TOF nDof")
)

cutPreDSANValidCscHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidCscHits < 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("0 valid CSC hits")
)

########################################
#final selection DSA cuts
########################################
cutDSAPt = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$p_{T}$ > 40 \GeV")
)

cutDSAEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("$|#eta|$ < 1.0")
)

cutDSANDtChambersWithValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nDtChambersWithValidHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("> 2 DT chambers with valid hits")
)

cutDSANValidRpcHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("nValidRpcHits > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("> 2 valid RPC hits")
)

cutDSADtTofTimeInOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOut > -10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("TimeInOut > -10 ns")
)

cutDSADtTofTimeInOutErr = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofTimeAtIpInOutErr < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("TimeInOut Error < 5 ns")
)

cutDSADtTofDirection = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofDirection > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("TOF Direction == 1")
)

cutDSADtTofFreeInverseBeta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dtTofFreeInverseBeta > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#beta_{Free}^{-1} > 0.5")
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

import FWCore.ParameterSet.Config as cms
import copy

from StoppPtls.StandardAnalysis.Cuts import *
from StoppPtls.StandardAnalysis.EventSelections import *

##############################
#CUTS
#additional cuts for halo estimate

#incoming (time<-10) vs outgoing (time> -10) csc segments
cutSomeIncomingCsc = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nIncomingCscSegsNearJetDeltaPhi0p2 > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Incoming CSC Segments near jet > 0")
)

cutNoIncomingCsc = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nIncomingCscSegsNearJetDeltaPhi0p2 = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Incoming CSC Segments near jet = 0")
)

cutSomeOutgoingCsc = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nOutgoingCscSegsNearJetDeltaPhi0p2 > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Outgoing CSC Segments near jet > 0")
)

cutNoOutgoingCsc = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nOutgoingCscSegsNearJetDeltaPhi0p2 = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Number of Outgoing CSC Segments near jet = 0")
)

cutAllCsc = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nIncomingCscSegsNearJetDeltaPhi0p2 > 0 || nOutgoingCscSegsNearJetDeltaPhi0p2 > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("All near jet")
)

cutSomeCscPosEnd = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapPosZ > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Some Csc segments in + endcap")
)

cutNoCscPosEnd = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapPosZ = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("No Csc segments in + endcap")
)

cutSomeCscNegEnd = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapMinZ > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Some Csc segments in - endcap")
)

cutNoCscNegEnd = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapMinZ = 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("No Csc segments in - endcap")
)

cutCscAllEnd = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nCscNearJetDeltaPhi0p2EndcapMinZ > 0 || nCscNearJetDeltaPhi0p2EndcapPosZ > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Some Csc segments in both endcap")
)

#average of CSC segment directions in event determines which beam
cutBeam1 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("meanCscDirectionNearJetDeltaPhi0p2 > 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Beam 1 near jet")
)

cutBeam2 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("meanCscDirectionNearJetDeltaPhi0p2 < 0"),
    numberRequired = cms.string("= 1"),
    alias = cms.string("Beam 2 near jet")
)


################################
#SELECTIONS

#Halo tag and probe Selection 
HaloTagAndProbeSelection = cms.PSet(
    name = cms.string("BeamHaloTagAndProbeSelection"),
    triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_"),
    cuts = cms.VPSet(
        cutBx,
        cutVertexNumber,  
        cutJetNumber,
        cutJetEta,
        #cutJetEnergy,
        cutCscSegNLayersNearJets,
        )
)

#incoming only
IncomingOnly = copy.deepcopy(HaloTagAndProbeSelection)
IncomingOnly.name = cms.string("IncomingOnly")
#IncomingOnly.cuts.append(cutSomeIncomingCsc)
#$IncomingOnly.cuts.append(cutNoOutgoingCsc)

IncomingOnlyBeam1 = copy.deepcopy(IncomingOnly)
IncomingOnlyBeam1.name = cms.string("IncomingOnlyBeam1")
IncomingOnlyBeam1.cuts.append(cutBeam1)
IncomingOnlyBeam1.cuts.append(cutSomeCscPosEnd)
IncomingOnlyBeam1.cuts.append(cutNoCscNegEnd)

IncomingOnlyBeam2 = copy.deepcopy(IncomingOnly)
IncomingOnlyBeam2.name = cms.string("IncomingOnlyBeam2")
IncomingOnlyBeam2.cuts.append(cutBeam2)
IncomingOnlyBeam2.cuts.append(cutSomeCscNegEnd)
IncomingOnlyBeam2.cuts.append(cutNoCscPosEnd)


#outgoing only
OutgoingOnly = copy.deepcopy(HaloTagAndProbeSelection)
OutgoingOnly.name = cms.string("OutgoingOnly")
#OutgoingOnly.cuts.append(cutSomeOutgoingCsc)
#OutgoingOnly.cuts.append(cutNoIncomingCsc)

OutgoingOnlyBeam1 = copy.deepcopy(OutgoingOnly)
OutgoingOnlyBeam1.name = cms.string("OutgoingOnlyBeam1")
OutgoingOnlyBeam1.cuts.append(cutBeam1)
OutgoingOnlyBeam1.cuts.append(cutSomeCscNegEnd)
OutgoingOnlyBeam1.cuts.append(cutNoCscPosEnd)

OutgoingOnlyBeam2 = copy.deepcopy(OutgoingOnly)
OutgoingOnlyBeam2.name = cms.string("OutgoingOnlyBeam2")
OutgoingOnlyBeam2.cuts.append(cutBeam2)
OutgoingOnlyBeam2.cuts.append(cutSomeCscPosEnd)
OutgoingOnlyBeam2.cuts.append(cutNoCscNegEnd)


#both
Both = copy.deepcopy(HaloTagAndProbeSelection)
Both.name = cms.string("Both")
#Both.cuts.append(cutSomeOutgoingCsc)
#Both.cuts.append(cutSomeIncomingCsc)
Both.cuts.append(cutSomeCscPosEnd)
Both.cuts.append(cutSomeCscNegEnd)

BothBeam1 = copy.deepcopy(Both)
BothBeam1.name = cms.string("BothBeam1")
BothBeam1.cuts.append(cutBeam1)

BothBeam2 = copy.deepcopy(Both)
BothBeam2.name = cms.string("BothBeam2")
BothBeam2.cuts.append(cutBeam2)

#all
All = copy.deepcopy(HaloTagAndProbeSelection)
All.name = cms.string("All")
All.cuts.append(cutCscAllEnd)

AllBeam1 = copy.deepcopy(All)
AllBeam1.name = cms.string("AllBeam1")
AllBeam1.cuts.append(cutBeam1)

AllBeam2 = copy.deepcopy(All)
AllBeam2.name = cms.string("AllBeam2")
AllBeam2.cuts.append(cutBeam2)

#halo control (N-1) selection (+ some number of CSC segments)
HaloControlSelection.triggers = triggers = cms.vstring("HLT_JetE50_NoBPTX3BX_")
HaloControlSelection.cuts.append(cutCscSegNumberInverted_newVeto)

HaloControlBeam1 = copy.deepcopy(HaloControlSelection)
HaloControlBeam1.name = cms.string("HaloControlBeam1")
HaloControlBeam1.cuts.append(cutBeam1)

HaloControlBeam2 = copy.deepcopy(HaloControlSelection)
HaloControlBeam2.name = cms.string("HaloControlBeam2")
HaloControlBeam2.cuts.append(cutBeam2)

import FWCore.ParameterSet.Config as cms
import copy

basicSelection = cms.PSet(
    name = cms.string("BasicSelection"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("energy > 0"),
        numberRequired = cms.string(">0"),
    ),
)

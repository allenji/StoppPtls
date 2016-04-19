import FWCore.ParameterSet.Config as cms

process = cms.Process('PrintEventInfo')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #make sure the input files contains only observed events
    fileNames = cms.untracked.vstring('file:/data/users/weifengji/condor/temp/RunningAnalysisCutOnSearchWithSkim/NoBPTX_2015D_v4/StoppedParticlesSelection/skim_335.root',
        'file:/data/users/weifengji/condor/temp/RunningAnalysisCutOnSearchWithSkim/NoBPTX_2015D_v4/StoppedParticlesSelection/skim_489.root')
)
process.eventFilter = cms.EDFilter("PrintEventInfo",
                                   )
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        #    outputCommands = cms.untracked.vstring('drop *_*_*_SIM',
                                        #   'keep *_*_Stopped*_SIM',
                                        #   'keep *_generator_*_SIM',
                                        #   'keep *_*_*_HLT'),
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string('output_HBEB.root'),
                                        dataset = cms.untracked.PSet(
    filterName = cms.untracked.string(''),
                    dataTier = cms.untracked.string('')
    ),
                                        SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('filter_step')
    )
                                        )

process.RAWSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_VtxSmeared_*_HLT')
process.RAWSIMoutput.outputCommands.extend( [ "keep *_*_MuonCSCWireDigi_*" ] )
process.RAWSIMoutput.outputCommands.extend( [ "keep *_*_MuonCSCStripDigi_*" ] )
process.RAWSIMoutput.outputCommands.extend( [
    "keep *_genParticlePlusGeant_*_*",
    ] )



process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Any.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    ),
		SelectEvents = cms.untracked.PSet(
    		SelectEvents = cms.vstring('filter_step')
    )


)
process.RECOSIMoutput.outputCommands.extend( [
    "keep *_genParticlePlusGeant_*_*",
    ] )

process.RECOSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RECOSIMoutput.outputCommands.append('keep *_VtxSmeared_*_HLT')
process.RECOSIMoutput.outputCommands.append('keep *_*CaloJets*_*_*')

process.filter_step = cms.Path(process.eventFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(process.filter_step,process.endjob_step)



# Modify these variables to switch masses, input stopped points files, and flavor of RHadron
SPARTICLE_MASS=2400
NEUTRALINO_MASS=SPARTICLE_MASS/4.0
GRAVITINO_MASS=0.00001
DELAYED_MUONS=True
SAME_EVENT=False
PARTICLE_NUMBER=0

import FWCore.ParameterSet.Config as cms

process = cms.Process('StoppedEventFilter')
#process.Tracer = cms.Service("Tracer")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations  = cms.untracked.vstring( 'Info',
                                                                           'Errors',
                                                                           'Warnings',
                                                                           'Debug'),
                                    categories    = cms.untracked.vstring( 'eventNumber',
                                                                           'Root_Information',
                                                                           'EventSetupDependency'
                                                                           ),
                                    Info          = cms.untracked.PSet( threshold = cms.untracked.string('INFO'),
                                                                        Root_Information     = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
                                                                        EventSetupDependency = cms.untracked.PSet( limit = cms.untracked.int32(0) )
                                                                        ),
                                    Errors        = cms.untracked.PSet( threshold = cms.untracked.string('ERROR') ),
                                    Warnings      = cms.untracked.PSet( threshold = cms.untracked.string('WARNING') ),
                                    Debug         = cms.untracked.PSet( threshold =  cms.untracked.string('DEBUG') ),
                                    debugModules  = cms.untracked.vstring('*')
                                    )

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(10)
    input = cms.untracked.int32(-1)
    )

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring( 'g4SimHits','G4HadronicProcess' ),
    )

# Input source
process.source = cms.Source ("PoolSource",
                             fileNames=cms.untracked.vstring(
        'file:HSCPmchamp6_M_2400_TuneZ2star_13TeV_pythia6_cff_GEN_SIM.root'
        )
                             )

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string("HSCPgluino2400_neutralinoYYY_separateEvents_particle0_StoppedEventFilter.root"),
                                        dataset = cms.untracked.PSet( filterName = cms.untracked.string(''),
                                                                      dataTier = cms.untracked.string('GEN-SIM')
                                                                      ),
                                        SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('filter_step')
                                                                           )
                                        )

process.RAWSIMoutput.outputCommands.append('drop *_*_*_SIM')

process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_*') #keep StoppedParticles from stage 1
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_*') #keep unsmeared generator from StoppedEventFilter

process.eventFilter = cms.EDFilter("MCStoppedEventFilter",
                                   StoppedParticlesX = cms.InputTag("g4SimHits","StoppedParticlesX","SIM"),
                                   PutTwoStoppedInSameEvent = cms.untracked.bool(SAME_EVENT),
                                   StoppedParticleNumber = cms.untracked.int32(PARTICLE_NUMBER)
                                   )

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'MCRUN2_71_V1::All' #Run2 Stopped Particles stage 2 MC, stage 1 MC
#process.GlobalTag.globaltag = 'MCRUN2_71_V5::All' #Run2 stage 2 MC produced in 7_1_22
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '') #2017 MC produced in 93X

process.generator = cms.EDProducer("Pythia6HSCPGun",
                                   readFromFile = cms.untracked.bool(False),
                                   stoppedData = cms.string(''),
                                   StoppedParticlesName = cms.InputTag("g4SimHits","StoppedParticlesName","SIM"),
                                   StoppedParticlesX = cms.InputTag("g4SimHits","StoppedParticlesX","SIM"),
                                   StoppedParticlesY = cms.InputTag("g4SimHits","StoppedParticlesY","SIM"),
                                   StoppedParticlesZ = cms.InputTag("g4SimHits","StoppedParticlesZ","SIM"),
                                   StoppedParticlesTime = cms.InputTag("g4SimHits","StoppedParticlesTime","SIM"),
                                   IsDelayedMuons = cms.untracked.bool(DELAYED_MUONS),
                                   PutTwoStoppedInSameEvent = cms.untracked.bool(SAME_EVENT),
                                   StoppedParticleNumber = cms.untracked.int32(PARTICLE_NUMBER),
                                   PGunParameters = cms.PSet(MinPhi = cms.double(-3.14159265359),
                                                             ParticleID = cms.vint32(11),
                                                             neutralinoMass = cms.double(NEUTRALINO_MASS),
                                                             gravitinoMass = cms.double(GRAVITINO_MASS),
                                                             MinEta = cms.double(-10),
                                                             sparticleMass = cms.double(SPARTICLE_MASS),
                                                             MaxEta = cms.double(10),
                                                             MaxPhi = cms.double(3.14159265359),
                                                             diJetGluino = cms.bool(False),
                                                             #decayTable = cms.string('src/stage2ParticlesTable.txt') #for crab
                                                             decayTable = cms.string('../../../stage2ParticlesTable_gluino2400.txt') #for interactive:  where you do cmsenv
                                                             ),
                                   #pythiaPylistVerbosity = cms.untracked.int32(2),
                                   pythiaPylistVerbosity = cms.untracked.int32(3),
                                   #gluinoHadrons = cms.bool(False),
                                   gluinoHadrons = cms.bool(True),
                                   #stopHadrons = cms.bool(True),
                                   stopHadrons = cms.bool(False),
                                   #pythiaHepMCVerbosity = cms.untracked.bool(False),
                                   pythiaHepMCVerbosity = cms.untracked.bool(True),
                                   maxEventsToPrint = cms.untracked.int32(10),
                                   PythiaParameters = cms.PSet( 
        processParameters = cms.vstring('IMSS(1)=11          ! User defined processes',
                                        'IMSS(21) = 33       ! LUN number for SLHA File (must be 33) ',
                                        'IMSS(22) = 33       ! Read-in SLHA decay table ',
                                        'MDME(89,1) = 0       ! tau decay to whatever     ',
                                        'MDME(90,1) = 1       ! tau decay to mu and neutrinos     ',
                                        'MDME(91,1) = 0       ! tau decay to whatever     ',
                                        'MDME(92,1) = 0       ! tau decay to whatever     ',
                                        'MDME(93,1) = 0       ! tau decay to whatever     ',
                                        'MDME(94,1) = 0       ! tau decay to whatever     ',
                                        'MDME(95,1) = 0       ! tau decay to whatever     ',
                                        'MDME(96,1) = 0       ! tau decay to whatever     ',
                                        'MDME(97,1) = 0       ! tau decay to whatever     ',
                                        'MDME(98,1) = 0       ! tau decay to whatever     ',
                                        'MDME(99,1) = 0       ! tau decay to whatever     ',
                                        'MDME(100,1)= 0       ! tau decay to whatever     ',
                                        'MDME(101,1)= 0       ! tau decay to whatever     ',
                                        'MDME(102,1)= 0       ! tau decay to whatever     ',
                                        'MDME(103,1)= 0       ! tau decay to whatever     ',
                                        'MDME(104,1)= 0       ! tau decay to whatever     ',
                                        'MDME(105,1)= 0       ! tau decay to whatever     ',
                                        'MDME(106,1)= 0       ! tau decay to whatever     ',
                                        'MDME(107,1)= 0       ! tau decay to whatever     ',
                                        'MDME(108,1)= 0       ! tau decay to whatever     ',
                                        'MDME(109,1)= 0       ! tau decay to whatever     ',
                                        'MDME(110,1)= 0       ! tau decay to whatever     ',
                                        'MDME(111,1)= 0       ! tau decay to whatever     ',
                                        'MDME(112,1)= 0       ! tau decay to whatever     ',
                                        'MDME(113,1)= 0       ! tau decay to whatever     ',
                                        'MDME(114,1)= 0       ! tau decay to whatever     ',
                                        'MDME(115,1)= 0       ! tau decay to whatever     ',
                                        'MDME(116,1)= 0       ! tau decay to whatever     ',
                                        'MDME(117,1)= 0       ! tau decay to whatever     ',
                                        'MDME(118,1)= 0       ! tau decay to whatever     ',
                                        'MDME(119,1)= 0       ! tau decay to whatever     ',
                                        'MDME(120,1)= 0       ! tau decay to whatever     ',
                                        'MDME(121,1)= 0       ! tau decay to whatever     ',
                                        'MDME(122,1)= 0       ! tau decay to whatever     ',
                                        'MDME(123,1)= 0       ! tau decay to whatever     ',
                                        'MDME(124,1)= 0       ! tau decay to whatever     ',
                                        'MDME(125,1)= 0       ! tau decay to whatever     ',
                                        'MDME(126,1)= 0       ! tau decay to whatever     ',
                                        'MDME(127,1)= 0       ! tau decay to whatever     ',
                                        'MDME(128,1)= 0       ! tau decay to whatever     ',
                                        'MDME(129,1)= 0       ! tau decay to whatever     ',
                                        'MDME(130,1)= 0       ! tau decay to whatever     ',
                                        'MDME(131,1)= 0       ! tau decay to whatever     ',
                                        'MDME(132,1)= 0       ! tau decay to whatever     ',
                                        'MDME(133,1)= 0       ! tau decay to whatever     ',
                                        'MDME(134,1)= 0       ! tau decay to whatever     ',
                                        'MDME(135,1)= 0       ! tau decay to whatever     ',
                                        'MDME(136,1)= 0       ! tau decay to whatever     ',
                                        'MDME(137,1)= 0       ! tau decay to whatever     ',
                                        'MDME(138,1)= 0       ! tau decay to whatever     '                                        
                                        ),
                                                                parameterSets = cms.vstring('processParameters',
                                                                                            'SLHAParameters'),
                                                                SLHAParameters = cms.vstring('SLHAFILE=stage2ParticlesTable_gluino2400.txt')
                                                                )
                                   )

process.ProductionFilterSequence = cms.Sequence(process.generator)

# FR Extra stuff

# FR END Extra stuff

# Path and EndPath definitions
process.filter_step = cms.Path(process.eventFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.endjob_step,process.filter_step,process.RAWSIMoutput_step)

# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

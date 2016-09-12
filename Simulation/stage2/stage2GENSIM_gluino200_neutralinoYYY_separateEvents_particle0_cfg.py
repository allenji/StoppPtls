# Modify these variables to switch masses, input stopped points files, and flavor of RHadron
SPARTICLE_MASS=200
NEUTRALINO_MASS=SPARTICLE_MASS/4.0
GRAVITINO_MASS=0.00001
DELAYED_MUONS=True
SAME_EVENT=False
PARTICLE_NUMBER=0

import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM2')

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
process.load('Configuration.StandardSequences.GeometryDB_cff')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
    #input = cms.untracked.int32(-1)
    )

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring( 'g4SimHits','G4HadronicProcess' )
    )

# Input source
process.source = cms.Source ("PoolSource",
                             fileNames=cms.untracked.vstring(
        #'file:../stage1/step1_mchamp500.root'
        #'root://cmsxrootd.fnal.gov//store/mc/RunIIWinter15GS/HSCPmchamp6_M-600_TuneZ2star_13TeV_pythia6/GEN-SIM/HSCP_customise_MCRUN2_71_V1-v2/80000/8ADD9B8F-CDEF-E411-BE7E-00074305CD50.root'
        #'/store/mc/RunIIWinter15GS/HSCPgluino_M-100_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/HSCP_customise_MCRUN2_71_V1-v2/10000/18D0DCDC-9301-E511-B022-002590D600B6.root'
        #'/store/mc/RunIIWinter15GS/HSCPgluino_M-200_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/HSCP_customise_MCRUN2_71_V1-v2/10000/1EA7F398-0B02-E511-A978-8F2B71CB40F1.root'
        '/store/mc/RunIIWinter15GS/HSCPgluino_M-2000_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/HSCP_customise_MCRUN2_71_V1-v2/00000/0E4DC19D-6201-E511-833F-0022194FEC31.root'
        )
                             )

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string("hist.root"),
                                        dataset = cms.untracked.PSet( filterName = cms.untracked.string(''),
                                                                      dataTier = cms.untracked.string('GEN-SIM')
                                                                      ),
                                        SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('filter_step')
                                                                           )
                                        )

process.RAWSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RAWSIMoutput.outputCommands.append('drop *_generator_*_SIM2')

process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM') #keep StoppedParticles from stage 1
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_SIM') #keep generator from stage 1
process.RAWSIMoutput.outputCommands.append('keep *_VtxSmeared_*_SIM2') #keep VtxSmeared from stage 2

process.eventFilter = cms.EDFilter("MCStoppedEventFilter",
                                   #StoppedParticlesXLabel = cms.InputTag("StoppedParticlesX")
                                   PutTwoStoppedInSameEvent = cms.untracked.bool(SAME_EVENT),
                                   StoppedParticleNumber = cms.untracked.int32(PARTICLE_NUMBER)
                                   )

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'MCRUN2_71_V1::All' #Run2 Stopped Particles stage 2 MC, stage 1 MC
process.GlobalTag.globaltag = 'MCRUN2_71_V5::All' #Run2 stage 2 MC produced in 7_1_22

process.generator = cms.EDProducer("Pythia6HSCPGun",
                                   readFromFile = cms.untracked.bool(False),
                                   stoppedData = cms.string(''),
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
                                                             decayTable = cms.string('../../../stage2ParticlesTable_gluino200.txt') #for interactive:  where you do cmsenv
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
        SLHAParameters = cms.vstring('SLHAFILE=stage2ParticlesTable_gluino200.txt')
        )
                                   )

process.genParticles = cms.EDProducer("GenParticleProducer",
                                      saveBarCodes = cms.untracked.bool(True),
                                      #src = cms.InputTag("generator"),
                                      src = cms.InputTag("VtxSmeared"),
                                      abortOnUnknownPDGCode = cms.untracked.bool(False),
                                      )

process.ProductionFilterSequence = cms.Sequence(process.generator)

# FR Extra stuff
process.load('StoppPtls/Simulation/StoppedParticleEvtVtxGenerator_cfi')
process.VtxSmeared.PutTwoStoppedInSameEvent = SAME_EVENT
process.VtxSmeared.StoppedParticleNumber = PARTICLE_NUMBER
process.VtxSmeared.verbose = True

#Unknown particles is OK
process.genParticles.abortOnUnknownPDGCode = False

#Don't use shower library
process.g4SimHits.HCalSD.UseShowerLibrary = False

# FR END Extra stuff
#this is the only place in the GEN-SIM step, other than the input to genParticles above, where it matters to change the input collection to VtxSmeared
process.g4SimHits.Generator.HepMCProductLabel = cms.string("VtxSmeared")

# Path and EndPath definitions
process.filter_step = cms.Path(process.eventFilter)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
#put filter_step at end to avoid OscarProducer seg fault in beginRun
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step)
process.schedule.extend([process.endjob_step,process.filter_step,process.RAWSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1
process = customisePostLS1(process)


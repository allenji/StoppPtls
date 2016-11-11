from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Cosmic_fullDetector_adjustedTiming_MCRUN2_7122_V5'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step1_cosmicMC_cfg.py'

config.Data.outputPrimaryDataset = 'Cosmic'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 2000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'Cosmic_fullDetector_adjustedTiming_MCRUN2_7122_V5'

config.Site.storageSite = 'T3_US_OSU'

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/stoppPtlsCandidate_Data_2017SPTrigEff_cfg.py'

config.Data.inputDataset = ''
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 200
config.Data.lumiMask = '/home/weifengji/StoppedParticles_Run2/SPAnalysis_2017_Jan11/CMSSW_9_2_1/src/StoppPtls/Collection/test/Cert_13TeV_2017_HCAL_DCS_GOOD.txt'
config.Data.runRange = '295953-297666' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/wji/'
config.Data.publication = True

config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_Purdue'

config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    def forkAndSubmit(config): 
        p = Process(target=submit, args=(config,))
        p.start()
        p.join() 

    #for dataset in ['/NoBPTX/Run2015C-PromptReco-v1/RECO','/NoBPTX/Run2015C-PromptReco-v2/RECO','/NoBPTX/Run2015C-PromptReco-v3/RECO']:
    #for dataset in ['/NoBPTX/Run2015C-PromptReco-v1/RECO','/NoBPTX/Run2015D-PromptReco-v3/RECO', '/NoBPTX/Run2015D-PromptReco-v4/RECO']:
    for dataset in [ '/NoBPTX/Run2017A-PromptReco-v1/RECO', '/NoBPTX/Run2017A-PromptReco-v2/RECO', '/NoBPTX/Run2017A-PromptReco-v3/RECO', '/NoBPTX/Run2017B-PromptReco-v1/RECO']:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.split('/')[2]+'_trigEffStudy_JetAndMuonTrig_Cert_13TeV_2017_HCAL_DCS_GOOD_295953-297666_Jul5'
       # crabCommand('submit', config = config)
        forkAndSubmit(config)
        

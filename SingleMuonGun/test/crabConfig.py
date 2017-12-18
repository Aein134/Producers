from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_9_4_test_5000_v3' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_TF2_cfg.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 9000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.publishDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.publication = False
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign/ryan'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]

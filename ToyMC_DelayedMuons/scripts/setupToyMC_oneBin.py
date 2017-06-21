import os
import sys
import re
from decimal import Decimal
#2015
#livetime = 559080 
#parameters_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/parameters_2015.txt"
#searchLifetime_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/searchLifetimes_2015.txt"
#tdir = "2015"

#2016
livetime = 2119960 
parameters_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/parameters_2016.txt"
searchLifetime_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/searchLifetimes_2016.txt"
tdir = "2016"

os.mkdir(tdir)

cmd = "cp " + parameters_fpath + " "  + tdir + "/parameters.txt "
os.system(cmd)
cmd = "cp " + searchLifetime_fpath + " " +  tdir + "/searchLifetimes.txt "
os.system(cmd)
    
cmd = "python " + os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC/scripts/makeToyJobs.py " + tdir
os.system(cmd)

cmd = "runAnalysis.py -7 -o " + tdir
os.system(cmd)
cmd = "runAnalysis.py -8 -o " + tdir
os.system(cmd)
    
    

    
    

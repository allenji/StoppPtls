#!/usr/bin/python
import time
import os
import sys
import math
import copy
import re
from array import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local config file")

(arguments, args) = parser.parse_args()

if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

def backgroundError(bkg_stat, bkg_sys):
    return math.sqrt(pow(bkg_stat, 2) + pow(bkg_sys, 2))

def getParams(param_file):
    pf = open(param_file)
    gamma = False
    gammaN = 0
    alpha = 0
    signal_err = 0
    for line in pf:
        print line
        split_line = line.split()
        if split_line != []:
            if split_line[0] == "bgN":
                if float(split_line[1]) > -1:
                    gamma = True
                    gammaN = math.floor(float(split_line[1]))
                    gammaN = int(gammaN)
            if split_line[0] == "bgAlpha":
                alpha = float(split_line[1])
            if split_line[0] == "scaleUncert":
                signal_err = float(split_line[1])
    return signal_err, gamma, gammaN, alpha

def readToyMCResult(toymc_summary):
    toymc_result = {}
    toymc_file = open(toymc_summary)
    for line in toymc_file:
        split_line = line.split()
        toymc_result[split_line[0]] = split_line[1:]
    return toymc_result

def combineToyMCFile(toymc_summary1, toymc_summary2):
    toymc_result1 = readToyMCResult(toymc_summary1)
    toymc_result2 = readToyMCResult(toymc_summary2)
    common_lifetimes = set(toymc_result1.keys()).intersection(set(toymc_result2.keys()))
    toymc_result_combined = {}
    for lifetime in toymc_result1.keys():
        if lifetime in common_lifetimes:
            toymc_result_combined[lifetime] = [toymc_result1[lifetime], toymc_result2[lifetime]]
    return toymc_result_combined


def writeDataCard_temp(toymc_result, lifetime, bkg_estimate, bkg_process,  signal_error, dataset_name="StoppedPartiles"):
    event_yield = int(toymc_result[lifetime][6])
    bkg_nominal = bkg_estimate[0]['total']
    background = float(toymc_result[lifetime][2])   
    allprocess = ['signal'] + bkg_process
    lifetime = lifetime.replace(".", "p")
    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+dataset_name+"_"+lifetime+"s.txt")
    datacards = open("limits/"+arguments.outputDir+"/datacard_"+dataset_name+"_"+lifetime+"s.txt", "w")
    datacards.write('imax 1 number of channels\n')
    datacards.write('jmax '+str(len(bkg_process)) + ' number of backgrounds\n')
    datacards.write('kmax * number of nuisance parameters\n')
    datacards.write('\n')

    datacards.write('%-15s%-10d\n'%("bin", 1))
    datacards.write('%-15s%-10d\n'%("observation", event_yield))

    datacards.write('---------------------\n')
    datacards.write('%-25s'%("bin"))
    for i in range(0, len(allprocess)):
        datacards.write('%-10d'%(1))
    datacards.write('\n')
    datacards.write('%-25s'%("process"))
    for i in range(0, len(allprocess)):
        datacards.write('%-10s'%allprocess[i])
    datacards.write('\n')
    datacards.write('%-25s'%("process"))
    for i in range(0, len(allprocess)):
        datacards.write('%-10d'%i)
    datacards.write('\n')
    datacards.write('%-25s'%("rate"))
    for process in allprocess:
        if process == "signal":
            datacards.write('%-10d'%(1))
        else:
            output_bkg = bkg_estimate[0][process][1]  * background / bkg_nominal
            datacards.write('%-10.3f'%output_bkg)
    datacards.write('\n')
    datacards.write('---------------------\n')
    for process in allprocess:
        result = ['-'] * len(allprocess)
        if process == 'signal':
            result[allprocess.index(process)] = "%.4f"%(1 + signal_error)
            datacards.write("%-25s%-10s"%(process+"err", 'lnN'))
            for output in result:
                datacards.write("%-10s"%output)
            datacards.write('\n')
        else:
            if bkg_estimate[0][process][0] == 'lnN':
                result[allprocess.index(process)] = "%.4f"%(1 + backgroundError(bkg_estimate[0][process][2], bkg_estimate[0][process][3])/bkg_estimate[0][process][1])
                datacards.write("%-25s%-10s"%(process+"err", "lnN"))
                for output in result:
                    datacards.write("%-10s"%output)
                datacards.write('\n')
            if bkg_estimate[0][process][0] == 'gmN':
                result[allprocess.index(process)] = "%.4f"%(bkg_estimate[0][process][3])
                datacards.write("%-25s%-4s%-6.3f"%(process+"err", "gmN", bkg_estimate[0][process][2]* background / bkg_nominal))
                for output in result:
                    datacards.write("%-10s"%output)
                datacards.write('\n')
       #hardcoded
    datacards.write("%-10s%-10s%-10s%-10.4f\n"%("bkgsys","lnN","-",2.0))
    datacards.close() 
    

def writeDataCardCombine_temp(toymc_result_combined, signal_error, signal_eff, bkg_estimate,  bkg_process, dataset_name="StoppedParticles"):
    for lifetime in toymc_result_combined.keys():
        lifetime_str = lifetime.replace(".", "p")
        os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+dataset_name+"_"+lifetime_str+"s.txt")
        datacards = open("limits/"+arguments.outputDir+"/datacard_"+dataset_name+"_"+lifetime_str+"s.txt", "w")
        bkg_nominal = (bkg_estimate[0]['total'], bkg_estimate[1]['total'])
        bkg = (float(toymc_result_combined[lifetime][0][2]),float(toymc_result_combined[lifetime][1][2]))
        n_obs1 = int(toymc_result_combined[lifetime][0][6])
        n_obs2 = int(toymc_result_combined[lifetime][1][6])
        l_eff = (float(toymc_result_combined[lifetime][0][0])/1000,float(toymc_result_combined[lifetime][1][0])/1000)

        datacards.write("imax 2 number of bins\n")
        datacards.write("jmax * number of processes minus 1\n")
        datacards.write("kmax * number of nuisance parameters\n")
        datacards.write("----------------------------------------------------------------\n")
        allprocess = ["signal"] + bkg_process
        datacards.write("%-25s%-10s%-10s\n"%("bin", "ch1", "ch2"))
        datacards.write("%-25s%-10d%-10d\n"%("observation", n_obs1, n_obs2))
        datacards.write("----------------------------------------------------------------\n")
        # write process and rate info
        datacards.write("%-25s"%"bin")
        for channel in range(1, 3):
            for process in allprocess:
                datacards.write("%-10s"%("ch"+str(channel)))
        datacards.write("\n")
        datacards.write("%-25s"%"process")
        for channel in range(1, 3):
            for process in allprocess:
                datacards.write("%-10s"%process)
        datacards.write("\n")
        datacards.write("%-25s"%"process")
        for channel in range(1, 3):
            for process in allprocess:
                datacards.write("%-10s"%str(allprocess.index(process)))
        datacards.write("\n")
        datacards.write("%-25s"%"rate")
        for channel in range(0, 2):
            for process in allprocess:
                if process == 'signal':
                    datacards.write("%-10.7f"%(l_eff[channel]*signal_eff[channel]))
                else:
                    background = bkg_estimate[channel][process][1] * bkg[channel] / bkg_nominal[channel]
                    datacards.write("%-10.7f"%(background))
        datacards.write("\n")
        datacards.write("----------------------------------------------------------------\n")
        #signal syst error

        result = ['-'] * (len(allprocess)*2)
        for channel in range(0,2):
            result[len(allprocess)*channel + allprocess.index("signal")] = "%.4f"%(1+signal_error[channel])
        datacards.write("%-15s%-10s"%("signalsys", 'lnN'))
        for i in result:
            datacards.write("%-10s"%(i))
        datacards.write('\n')
        #stat uncertainty
        for channel in range(0, 2):
            for process in allprocess:
                result = ['-'] * (len(allprocess)*2)
                if process in bkg_estimate[0].keys():
                    if bkg_estimate[channel][process][0] == "lnN":
                        result[len(allprocess)*channel + allprocess.index(process)] = "%.4f"%(1 + bkg_estimate[channel][process][2]  / bkg_estimate[channel][process][1])
                        datacards.write("%-15s%-10s"%(process+str(channel)+"stat", 'lnN'))
                        for i in result:
                            datacards.write("%-10s"%(i))
                        datacards.write('\n')
                    if bkg_estimate[channel][process][0] == "gmN":
                        gammaN = "%.3f"%(bkg_estimate[channel][process][2]) 
                        gammaAlpha = "%.3f"%(bkg_estimate[channel][process][3] * bkg[channel] / bkg_nominal[channel])
                        result[len(allprocess)*channel + allprocess.index(process)] = gammaAlpha
                        datacards.write("%-15s%-4s%-6s"%(process+str(channel)+"stat", 'gmN', gammaN))
                        for i in result:
                            datacards.write("%-10s"%(i))
                        datacards.write('\n')
       #syst uncertainty
        for process in allprocess:
            result = ['-'] * (len(allprocess)*2)
            if process in bkg_estimate[0].keys():
                if bkg_estimate[channel][process][0] == "lnN":
                    for channel in range(0, 2):
                        result[len(allprocess)*channel + allprocess.index(process)] = "%.4f"%(1 + bkg_estimate[channel][process][3]  / bkg_estimate[channel][process][1])
                    datacards.write("%-15s%-10s"%(process+"sys", 'lnN'))
                    for i in result:
                        datacards.write("%-10s"%(i))
                    datacards.write('\n')
        datacards.write('%-10s%-10s%-10s%-10f%-10s%-10f\n'%('bkgsys', 'lnN', '-', 2.0, '-', 2.0))
        
                    



toymcDM = '/home/jalimena/StoppedParticles2016/CMSSW_8_0_26_patch2/src/ToyMCmchamps2016_30March_unblinded/mchamp2016_100/toymc.txt'
#toymc_result = readToyMCResult(toymc2016, toymcDM)
if combine is True:
    toymc_result = combineToyMCFile(toymc[0], toymc[1])
    signal_err1, gamma1, gammaN1, gammaalpha1 = getParams(param[0])
    print [signal_err1, gamma1, gammaN1, gammaalpha1]
    signal_err2, gamma2, gammaN2, gammaalpha2 = getParams(param[1])
    print [signal_err2, gamma2, gammaN2, gammaalpha2]
#toymc_result = combineToyMCFile(toymc2015, toymc2016)
    #for lifetime in toymc_result.keys():
        #writeDataCardCombine(toymc_result, [signal_err1, signal_err2], [signal_eff[0], signal_eff[1]], dataset_name, gamma1, gamma2, gammaN1, gammaN2, gammaalpha1, gammaalpha2)
    writeDataCardCombine_temp(toymc_result, [signal_err1, signal_err2], signal_eff, [bkg_estimate_1, bkg_estimate_2], bkg, dataset_name)
else:
    if year == 2015:
        print 'nimei'
        toymc_result = readToyMCResult(toymc[0])
        signal_err1, gamma1, gammaN1, gammaalpha1 = getParams(param[0])
        for lifetime in toymc_result.keys():
            writeDataCard_temp(toymc_result, lifetime, [bkg_estimate_1], bkg, signal_err1, dataset_name)
    if year == 2016:
        toymc_result = readToyMCResult(toymc[1])
        signal_err1, gamma1, gammaN1, gammaalpha1 = getParams(param[1])
        for lifetime in toymc_result.keys():
            writeDataCard_temp(toymc_result, lifetime, [bkg_estimate_2], bkg, signal_err1, dataset_name)

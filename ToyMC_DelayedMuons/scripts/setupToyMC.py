import os
import sys
import re
from decimal import Decimal
#livetime = 2119960
livetime = 559080
bkg_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/mchampBkg_2015.txt"
parameters_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/parameters_2015.txt"
searchLifetime_fpath = os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC_DelayedMuons/data/searchLifetimes_2015.txt"

print "Importing background file"
bkg_file = open(bkg_fpath, "r")
bkg_line = bkg_file.readline()

bkg_dic = {}
while bkg_line != "":
    print 1
    bkg_line_split = bkg_line.split()
    if bkg_line_split[0].isdigit():
        bkg_dic[bkg_line_split[0]] = bkg_line_split[1:]
    bkg_line = bkg_file.readline()
print "Finished importing background file"
        

#for mass in [100, 200, 400, 600, 800, 1000, 1400, 1800, 2200, 2600]:
for mass in [100, 400, 600, 1000, 1400]:
#for mass in [400]:
#for mass in range(2600, 2800, 200):
    tdir = "mchamp2015_" + str(mass)
    os.mkdir(tdir)

    cmd = "cp " + parameters_fpath + " "  + tdir + "/parameters.txt "
    os.system(cmd)
    cmd = "cp " + searchLifetime_fpath + " " +  tdir + "/searchLifetimes.txt "
    os.system(cmd)

    line4 = re.compile(r'(bgAlpha\s*)(\S*)')
    line3 = re.compile(r'(bgN\s*)(\S*)')
    line2 = re.compile(r'(bgRate_e\s*)(\S*)')
    line1 = re.compile(r'(bgRate\s*)(\S*)')
    paramfile_origin = open (parameters_fpath, "r")
    paramfile = open(tdir + "/parameters.txt", "w")
    for line in paramfile_origin.readlines():
        m1 = line1.match(line)
        m2 = line2.match(line)
        m3 = line3.match(line)
        m4 = line4.match(line)
        if ((not m1) and (not m2) and (not m3) and (not m4)):
            paramfile.write(line)
        elif m4:
            paramfile.write(m4.group(1))
            bkg_Alpha = '%.2E' % Decimal(float(bkg_dic[str(mass)][3]))
            paramfile.write(bkg_Alpha)
            paramfile.write("\n")
        elif m3:
            paramfile.write(m3.group(1))
            bkg_N = '%.4E' % Decimal(float(bkg_dic[str(mass)][2])/livetime)
            paramfile.write(bkg_N)
            paramfile.write("\n")
        elif m2:
            paramfile.write(m2.group(1))
            bkg_rate_e = '%.4E' % Decimal(float(bkg_dic[str(mass)][1])/livetime)
            paramfile.write(bkg_rate_e)
            paramfile.write("\n")
        elif m1:
            paramfile.write(m1.group(1))
            bkg_rate = '%.4E' % Decimal(float(bkg_dic[str(mass)][0])/livetime)
            paramfile.write(bkg_rate)
            paramfile.write("\n")
    paramfile.close()
    
    cmd = "python " + os.environ["CMSSW_BASE"] + "/src/StoppPtls/ToyMC/scripts/makeToyJobs.py " + tdir
    os.system(cmd)

    cmd = "runAnalysis.py -7 -o " + tdir
    os.system(cmd)
    cmd = "runAnalysis.py -8 -o " + tdir
    os.system(cmd)
    
    

    
    

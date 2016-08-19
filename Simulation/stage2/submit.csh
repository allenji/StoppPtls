#!/bin/tcsh
# to run use source *.csh

#echo mchamps...
#foreach i (100 200 400 600 800 1000 1400 1800 2200 2600) #Run2  
    #osusub.py -l localConfig_mchamp${i}_separateEvents_particle0.py -w Stage2GenSimMchampsSeparateEventsParticle0 -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
    #osusub.py -l localConfig_mchamp${i}_separateEvents_particle1.py -w Stage2GenSimMchampsSeparateEventsParticle1 -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
    #osusub.py -l localConfig_mchamp${i}_sameEvent.py -w Stage2GenSimMchampsSameEvent -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
#end

echo gluinos...
foreach i (100 200 400 600 800 1000 1200 1400 1600 1800 2000 2200 2400 2600) #Run2 
    osusub.py -l localConfig_gluino${i}_separateEvents_particle0.py -w Stage2GenSimGluinosSeparateEventsParticle0 -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
    osusub.py -l localConfig_gluino${i}_separateEvents_particle1.py -w Stage2GenSimGluinosSeparateEventsParticle1 -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
    #osusub.py -l localConfig_gluino${i}_sameEvent.py -w Stage2GenSimGluinosSameEvent -g -f process.RAWSIMoutput.fileName -t OSUT3Ntuple
end

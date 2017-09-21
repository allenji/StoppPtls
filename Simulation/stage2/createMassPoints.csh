#!/bin/tcsh
# to run use source *.csh

echo gluinos...
foreach i (100 200 400 600 800 1000 1200 1400 1600 1800 2000 2200 2400 2600) #Run2
    sed "s/XXX/$i/" stage2StoppedEventFilter_gluinoXXX_neutralinoYYY_separateEvents_particle0_cfg.py > stage2StoppedEventFilter_gluino${i}_neutralinoYYY_separateEvents_particle0_cfg.py
    sed "s/XXX/$i/" stage2StoppedEventFilter_gluinoXXX_neutralinoYYY_separateEvents_particle1_cfg.py > stage2StoppedEventFilter_gluino${i}_neutralinoYYY_separateEvents_particle1_cfg.py
    sed "s/XXX/$i/" stage2StoppedEventFilter_gluinoXXX_neutralinoYYY_sameEvent_cfg.py > stage2StoppedEventFilter_gluino${i}_neutralinoYYY_sameEvent_cfg.py

    sed "s/XXX/$i/" stage2GENSIM_gluinoXXX_neutralinoYYY_separateEvents_particle0_cfg.py > stage2GENSIM_gluino${i}_neutralinoYYY_separateEvents_particle0_cfg.py
    sed "s/XXX/$i/" stage2GENSIM_gluinoXXX_neutralinoYYY_separateEvents_particle1_cfg.py > stage2GENSIM_gluino${i}_neutralinoYYY_separateEvents_particle1_cfg.py
    sed "s/XXX/$i/" stage2GENSIM_gluinoXXX_neutralinoYYY_sameEvent_cfg.py > stage2GENSIM_gluino${i}_neutralinoYYY_sameEvent_cfg.py

    sed "s/XXX/$i/" localConfig_gluinoXXX_separateEvents_particle0.py > localConfig_gluino${i}_separateEvents_particle0.py
    sed "s/XXX/$i/" localConfig_gluinoXXX_separateEvents_particle1.py > localConfig_gluino${i}_separateEvents_particle1.py
    sed "s/XXX/$i/" localConfig_gluinoXXX_sameEvent.py > localConfig_gluino${i}_sameEvent_cfg.py
end

#echo stops...
#needs to be updated for run2
#foreach i (100 200 300 400 500 600 700 800 900 1000)
#    if ($i == '100') then 
    #set j=30
#    endif
#    if ($i == '200') then 
    #set j=75
#    endif
#    if ($i == '300') then 
    #set j=109
#    endif
#    if ($i == '400') then 
    #set j=214
#    endif
#    if ($i == '500') then 
    #set j=316
    #endif
    #if ($i == '600') then 
    #set j=417
    #endif
    #if ($i == '700') then 
    #set j=518
    #endif
    #if ($i == '800') then 
    #set j=618
    #endif
    #if ($i == '900') then 
    #set j=718
    #endif
    #if ($i == '1000') then 
    #set j=819
    #endif
    #sed "s/XXX/$i/" stage2GENSIM_stopXXX_neutralinoYYY_separateEvents_particle0_cfg.py |sed "s/YYY/$j/" > stage2GENSIM_stop${i}_neutralino${j}_separateEvents_particle0_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_stopXXX_neutralinoYYY_separateEvents_particle1_cfg.py |sed "s/YYY/$j/" > stage2GENSIM_stop${i}_neutralino${j}_separateEvents_particle1_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_stopXXX_neutralinoYYY_sameEvent_cfg.py |sed "s/YYY/$j/" > stage2GENSIM_stop${i}_neutralino${j}_sameEvent_cfg.py
#end

#echo staus... 
#foreach i (100 126 156 200 247 308 370 432 494)
    #sed "s/XXX/$i/" stage2GENSIM_gmstauXXX_gravitinop0001_separateEvents_particle0_cfg.py > stage2GENSIM_gmstau${i}_gravitinop0001_separateEvents_particle0_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_gmstauXXX_gravitinop0001_separateEvents_particle1_cfg.py > stage2GENSIM_gmstau${i}_gravitinop0001_separateEvents_particle1_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_gmstauXXX_gravitinop0001_sameEvent_cfg.py > stage2GENSIM_gmstau${i}_gravitinop0001_sameEvent_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_ppstauXXX_gravitinop0001_separateEvents_particle0_cfg.py > stage2GENSIM_ppstau${i}_gravitinop0001_separateEvents_particle0_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_ppstauXXX_gravitinop0001_separateEvents_particle1_cfg.py > stage2GENSIM_ppstau${i}_gravitinop0001_separateEvents_particle1_cfg.py
    #sed "s/XXX/$i/" stage2GENSIM_ppstauXXX_gravitinop0001_sameEvent_cfg.py > stage2GENSIM_ppstau${i}_gravitinop0001_sameEvent_cfg.py
#end


echo mchamps...
foreach i (100 200 400 600 800 1000 1400 1800 2200 2600) #Run2
    sed "s/XXX/$i/" stage2StoppedEventFilter_mchampXXX_sameEvent_cfg.py > stage2StoppedEventFilter_mchamp${i}_sameEvent_cfg.py
    sed "s/XXX/$i/" stage2StoppedEventFilter_mchampXXX_separateEvents_particle0_cfg.py > stage2StoppedEventFilter_mchamp${i}_separateEvents_particle0_cfg.py
    sed "s/XXX/$i/" stage2StoppedEventFilter_mchampXXX_separateEvents_particle1_cfg.py > stage2StoppedEventFilter_mchamp${i}_separateEvents_particle1_cfg.py

    sed "s/XXX/$i/" stage2GENSIM_mchampXXX_sameEvent_cfg.py > stage2GENSIM_mchamp${i}_sameEvent_cfg.py
    sed "s/XXX/$i/" stage2GENSIM_mchampXXX_separateEvents_particle0_cfg.py > stage2GENSIM_mchamp${i}_separateEvents_particle0_cfg.py
    sed "s/XXX/$i/" stage2GENSIM_mchampXXX_separateEvents_particle1_cfg.py > stage2GENSIM_mchamp${i}_separateEvents_particle1_cfg.py

    sed "s/XXX/$i/" localConfig_mchampXXX_separateEvents_particle0.py > localConfig_mchamp${i}_separateEvents_particle0.py
    sed "s/XXX/$i/" localConfig_mchampXXX_separateEvents_particle1.py > localConfig_mchamp${i}_separateEvents_particle1.py
    sed "s/XXX/$i/" localConfig_mchampXXX_sameEvent.py > localConfig_mchamp${i}_sameEvent_cfg.py
end



#echo mchamps...
#foreach i (100 200 300 400 500 600 700 800 900 1000)
#   foreach j in 3 6
#   sed "s/XXX/$i/" HSCPhipYYY_M_XXX_13TeV_pythia6_cff.py |sed "s/YYY/$j/" > result_new/HSCPmchamp${j}_M_${i}_TuneZ2star_13TeV_pythia6_cff.py
#   sed "s/XXX/$i/" particles_HIPYYY_stau_XXX_GeV.txt |sed "s/YYY/$j/"> result_new/particles_HIP${j}_stau_${i}_GeV.txt
#   sed "s/XXX/$i/" hscppythiapdtHIPYYYstauXXX.tbl |sed "s/YYY/$j/"> result_new/hscppythiapdtHIP${j}stau${i}.tbl    
    #   end 
#end


#let "j = $i/10"
#sed "s/XX/$j/" hscppythiapdtgluinoXXX.tbl > result_new/hscppythiapdtgluino${i}.tbl


echo "job is finished at" 
date

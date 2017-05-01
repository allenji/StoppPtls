#!/bin/bash
#for mass in 100 200 400 600 800 1000 1400 1800 2200 2600
for mass in 200 1000 2600
 
do
  python ../makeDataCardsFinal_DM.py -l localConfig_DMMchampCombined_$mass'.py' -c DelayedMuonCombinedMchamp_$mass
  python ../runLimits_DM.py -M HybridNew -l localConfig_DMMchampCombined_$mass'.py' -c DelayedMuonCombinedMchamp_$mass
done

#for mass in 400 600 800 1000 1200 1400 1600 1800 2000 2200 2400 2600
for mass in 400 1000 2600
#for mass in 400 1000 1200 1400 1600 1800 2000 2200 2400 2600
do
    python ../makeDataCardsFinal_DM.py -l localConfig_DMGluinoCombined_$mass'.py' -c DelayedMuonCombinedGluino_$mass
    python ../runLimits_DM.py -M HybridNew -l localConfig_DMGluinoCombined_$mass'.py' -c DelayedMuonCombinedGluino_$mass
done

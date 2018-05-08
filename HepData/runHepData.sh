python deltaTDT_muon.py
python deltaTRPC_muon.py
python ereco_calo_gluino2b_600GeV.py
python ereco_calo_gluino2b_1200GeV.py
python ereco_calo_gluino2b_1800GeV.py
python ereco_calo_stop2b_400GeV.py
python ereco_calo_stop2b_1000GeV.py
python ereco_calo_stop2b_600GeV.py
python ereco_calo_g3b_800and1000GeV.py
python ereco_calo_g3b_1800GeV.py
python HepData_muon_extrapolating.py
python limitsHepData_muon_glifetime.py
python limitsHepData_muon_gmass.py
python limitsHepData_muon_mchampmass.py
python limitsHepData_muon_mlifetime.py
python limitsHepData_sp_g2bmass.py
python limitsHepData_sp_g2bxsec.py
python limitsHepData_sp_g3bmass.py
python limitsHepData_sp_g3bxsec.py
python limitsHepData_sp_stopmass.py
python limitsHepData_sp_stopxsec.py
mkdir to_submit
mv lim_* to_submit/
mv background_extrapolating.yaml to_submit/
mv ereco_*.yaml to_submit/
mv delta*.yaml to_submit/
cp submission.yaml to_submit/
tar -cvzf submission.tar.gz to_submit/

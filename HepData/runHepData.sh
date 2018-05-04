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
cp submission.yaml to_submit/
tar -cvzf submission.tar.gz to_submit/

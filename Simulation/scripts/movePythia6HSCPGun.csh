#!/bin/csh
#
# movePythia6HSCPGun.csh moves the Pythia6HSCPGun module from
# the StoppPtls/Simulation package to the GeneratorInterface/Pythia6Interface
# package. For this script to work GeneratorInterface/Pythia6Interface 
# must already be checked out.
#
# This script should hopefully only be a temporary measure. In the long
# term, Pythia6HSCPGun should be added to the GeneratorInterface/Pythia6Interface
# package in CVS

mv $CMSSW_BASE/src/StoppPtls/Simulation/plugins/Pythia6HSCPGun.h $CMSSW_BASE/src/GeneratorInterface/Pythia6Interface/plugins/
mv $CMSSW_BASE/src/StoppPtls/Simulation/plugins/Pythia6HSCPGun.cc $CMSSW_BASE/src/GeneratorInterface/Pythia6Interface/plugins/
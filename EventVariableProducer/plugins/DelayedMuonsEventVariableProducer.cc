#include <iostream>
#include <fstream>
#include <TVector3.h>
#include "TFile.h"
#include "TH1.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "StoppPtls/EventVariableProducer/plugins/DelayedMuonsEventVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

DelayedMuonsEventVariableProducer::DelayedMuonsEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tracksToken_ = consumes<vector<TYPE(tracks)> >(collections_.getParameter<edm::InputTag>("tracks"));
}

DelayedMuonsEventVariableProducer::~DelayedMuonsEventVariableProducer()
{
}

void DelayedMuonsEventVariableProducer::AddVariables(const edm::Event & event) {
  
  edm::Handle<std::vector<CandidateDelayedMuonsTrack> > tracks;
  event.getByToken(tracksToken_, tracks);
  
  (*eventvariables)["nTracks"] = tracks->size();
  //std::cout<<"nTracks is: "<<tracks->size()<<std::endl;

  long unsigned int upper0_index = 999;
  long unsigned int upper1_index = 999;
  long unsigned int upper2_index = 999;
  long unsigned int lower0_index = 999;
  long unsigned int lower1_index = 999;
  long unsigned int lower2_index = 999;

  for(decltype(tracks->size()) i = 0; i != tracks->size(); ++i) {
    //std::cout<<"track phi is: "<<tracks->at(i).phi()<<std::endl;
    //std::cout<<"track pt is: "<<tracks->at(i).pt()<<std::endl;

    if(tracks->at(i).phi()>0.){
      if(i==0) upper0_index = i;
      if(i==1) upper1_index = i;
      if(i==2) upper2_index = i;
    }//end of if upper
    else{
      if(i==0) lower0_index = i;
      if(i==1) lower1_index = i;
      if(i==2) lower2_index = i;
    }//end of if lower

    //long unsigned int nRpcHits = tracks->at(i).rpcHitBx().size();
    //std::cout<<"number of rpc hits in track is: "<<nRpcHits<<std::endl;
    //std::cout<<"Rpc_Bx_Pattern is: "<<Rpc_Bx_Pattern(tracks,i,nRpcHits)<<std::endl;
    //std::cout<<"rpc_bx_average is: "<<Rpc_Bx_Average(tracks,i,nRpcHits)<<std::endl;

  }//end of loop over DSA tracks
  //std::cout<<std::endl;

  if(upper0_index!=999){
    (*eventvariables)["p_upper0"] =                         (tracks->at(upper0_index)).p();
    (*eventvariables)["pt_upper0"] =                        (tracks->at(upper0_index)).pt();
    (*eventvariables)["eta_upper0"] =                       (tracks->at(upper0_index)).eta();
    (*eventvariables)["phi_upper0"] =                       (tracks->at(upper0_index)).phi();
    (*eventvariables)["ndof_upper0"] =                      (tracks->at(upper0_index)).ndof();
    (*eventvariables)["normalizedChi2_upper0"] =            (tracks->at(upper0_index)).normalizedChi2();
    (*eventvariables)["charge_upper0"] =                    (tracks->at(upper0_index)).charge();
    (*eventvariables)["dxy_upper0"] =                       (tracks->at(upper0_index)).dxy();
    (*eventvariables)["dz_upper0"] =                        (tracks->at(upper0_index)).dz();
    (*eventvariables)["vx_upper0"] =                        (tracks->at(upper0_index)).vx();
    (*eventvariables)["vy_upper0"] =                        (tracks->at(upper0_index)).vy();
    (*eventvariables)["vz_upper0"] =                        (tracks->at(upper0_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_upper0"] =      (tracks->at(upper0_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_upper0"] =   (tracks->at(upper0_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_upper0"] =    (tracks->at(upper0_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_upper0"] =   (tracks->at(upper0_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_upper0"] =    (tracks->at(upper0_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_upper0"] = (tracks->at(upper0_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_upper0"] =  (tracks->at(upper0_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_upper0"] = (tracks->at(upper0_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_upper0"] =            (tracks->at(upper0_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_upper0"] =             (tracks->at(upper0_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_upper0"] =              (tracks->at(upper0_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_upper0"] =             (tracks->at(upper0_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_upper0"] = (tracks->at(upper0_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_upper0"] = (tracks->at(upper0_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_upper0"] = (tracks->at(upper0_index)).quality();
    (*eventvariables)["innerPx_upper0"] = (tracks->at(upper0_index)).innerPx();
    (*eventvariables)["innerPy_upper0"] = (tracks->at(upper0_index)).innerPy();
    (*eventvariables)["innerPz_upper0"] = (tracks->at(upper0_index)).innerPz();
    (*eventvariables)["innerOk_upper0"] = (tracks->at(upper0_index)).innerOk();
    (*eventvariables)["innerX_upper0"] =  (tracks->at(upper0_index)).innerX();
    (*eventvariables)["innerY_upper0"] =  (tracks->at(upper0_index)).innerY();
    (*eventvariables)["innerZ_upper0"] =  (tracks->at(upper0_index)).innerZ();
    (*eventvariables)["dtTofDirection_upper0"] =          (tracks->at(upper0_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_upper0"] =               (tracks->at(upper0_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_upper0"] =    (tracks->at(upper0_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_upper0"] = (tracks->at(upper0_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_upper0"] =      (tracks->at(upper0_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper0"] =   (tracks->at(upper0_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_upper0"] =      (tracks->at(upper0_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper0"] =   (tracks->at(upper0_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(upper0_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_upper0"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_upper0"] =            Rpc_Bx_Pattern(tracks,upper0_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_upper0"] =            Rpc_Bx_Average(tracks,upper0_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_upper0"] =                         -999;
    (*eventvariables)["pt_upper0"] =                        -999;
    (*eventvariables)["eta_upper0"] =                       -999;
    (*eventvariables)["phi_upper0"] =                       -999;
    (*eventvariables)["ndof_upper0"] =                      -999;
    (*eventvariables)["normalizedChi2_upper0"] =            -999;
    (*eventvariables)["charge_upper0"] =                    -999;
    (*eventvariables)["dxy_upper0"] =                       -999;
    (*eventvariables)["dz_upper0"] =                        -999;
    (*eventvariables)["vx_upper0"] =                        -999;
    (*eventvariables)["vy_upper0"] =                        -999;
    (*eventvariables)["vz_upper0"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_upper0"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_upper0"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_upper0"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_upper0"] =   -999;
    (*eventvariables)["nStationsWithValidHits_upper0"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_upper0"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_upper0"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_upper0"] = -999;
    (*eventvariables)["nValidMuonHits_upper0"] =            -999;
    (*eventvariables)["nValidCscHits_upper0"] =             -999;
    (*eventvariables)["nValidDtHits_upper0"] =              -999;
    (*eventvariables)["nValidRpcHits_upper0"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_upper0"] = -999;
    (*eventvariables)["outermostStationWithValidHits_upper0"] = -999;
    (*eventvariables)["quality_upper0"] = -999;
    (*eventvariables)["innerPx_upper0"] = -999;
    (*eventvariables)["innerPy_upper0"] = -999;
    (*eventvariables)["innerPz_upper0"] = -999;
    (*eventvariables)["innerOk_upper0"] = -999;
    (*eventvariables)["innerX_upper0"] =  -999;
    (*eventvariables)["innerY_upper0"] =  -999;
    (*eventvariables)["innerZ_upper0"] =  -999;
    (*eventvariables)["dtTofDirection_upper0"] =          -999;
    (*eventvariables)["dtTofNDof_upper0"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_upper0"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_upper0"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_upper0"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper0"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_upper0"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper0"] =   -999;
    (*eventvariables)["nRpcHits_upper0"] =                -999;
    (*eventvariables)["rpcBxPattern_upper0"] =            -999;
    (*eventvariables)["rpcBxAverage_upper0"] =            -999;
  }
  if(upper1_index!=999){
    (*eventvariables)["p_upper1"] =                         (tracks->at(upper1_index)).p();
    (*eventvariables)["pt_upper1"] =                        (tracks->at(upper1_index)).pt();
    (*eventvariables)["eta_upper1"] =                       (tracks->at(upper1_index)).eta();
    (*eventvariables)["phi_upper1"] =                       (tracks->at(upper1_index)).phi();
    (*eventvariables)["ndof_upper1"] =                      (tracks->at(upper1_index)).ndof();
    (*eventvariables)["normalizedChi2_upper1"] =            (tracks->at(upper1_index)).normalizedChi2();
    (*eventvariables)["charge_upper1"] =                    (tracks->at(upper1_index)).charge();
    (*eventvariables)["dxy_upper1"] =                       (tracks->at(upper1_index)).dxy();
    (*eventvariables)["dz_upper1"] =                        (tracks->at(upper1_index)).dz();
    (*eventvariables)["vx_upper1"] =                        (tracks->at(upper1_index)).vx();
    (*eventvariables)["vy_upper1"] =                        (tracks->at(upper1_index)).vy();
    (*eventvariables)["vz_upper1"] =                        (tracks->at(upper1_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_upper1"] =      (tracks->at(upper1_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_upper1"] =   (tracks->at(upper1_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_upper1"] =    (tracks->at(upper1_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_upper1"] =   (tracks->at(upper1_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_upper1"] =    (tracks->at(upper1_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_upper1"] = (tracks->at(upper1_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_upper1"] =  (tracks->at(upper1_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_upper1"] = (tracks->at(upper1_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_upper1"] =            (tracks->at(upper1_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_upper1"] =             (tracks->at(upper1_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_upper1"] =              (tracks->at(upper1_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_upper1"] =             (tracks->at(upper1_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_upper1"] = (tracks->at(upper1_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_upper1"] = (tracks->at(upper1_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_upper1"] = (tracks->at(upper1_index)).quality();
    (*eventvariables)["innerPx_upper1"] = (tracks->at(upper1_index)).innerPx();
    (*eventvariables)["innerPy_upper1"] = (tracks->at(upper1_index)).innerPy();
    (*eventvariables)["innerPz_upper1"] = (tracks->at(upper1_index)).innerPz();
    (*eventvariables)["innerOk_upper1"] = (tracks->at(upper1_index)).innerOk();
    (*eventvariables)["innerX_upper1"] =  (tracks->at(upper1_index)).innerX();
    (*eventvariables)["innerY_upper1"] =  (tracks->at(upper1_index)).innerY();
    (*eventvariables)["innerZ_upper1"] =  (tracks->at(upper1_index)).innerZ();
    (*eventvariables)["dtTofDirection_upper1"] =          (tracks->at(upper1_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_upper1"] =               (tracks->at(upper1_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_upper1"] =    (tracks->at(upper1_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_upper1"] = (tracks->at(upper1_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_upper1"] =      (tracks->at(upper1_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper1"] =   (tracks->at(upper1_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_upper1"] =      (tracks->at(upper1_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper1"] =   (tracks->at(upper1_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(upper1_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_upper1"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_upper1"] =            Rpc_Bx_Pattern(tracks,upper1_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_upper1"] =            Rpc_Bx_Average(tracks,upper1_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_upper1"] =                         -999;
    (*eventvariables)["pt_upper1"] =                        -999;
    (*eventvariables)["eta_upper1"] =                       -999;
    (*eventvariables)["phi_upper1"] =                       -999;
    (*eventvariables)["ndof_upper1"] =                      -999;
    (*eventvariables)["normalizedChi2_upper1"] =            -999;
    (*eventvariables)["charge_upper1"] =                    -999;
    (*eventvariables)["dxy_upper1"] =                       -999;
    (*eventvariables)["dz_upper1"] =                        -999;
    (*eventvariables)["vx_upper1"] =                        -999;
    (*eventvariables)["vy_upper1"] =                        -999;
    (*eventvariables)["vz_upper1"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_upper1"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_upper1"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_upper1"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_upper1"] =   -999;
    (*eventvariables)["nStationsWithValidHits_upper1"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_upper1"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_upper1"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_upper1"] = -999;
    (*eventvariables)["nValidMuonHits_upper1"] =            -999;
    (*eventvariables)["nValidCscHits_upper1"] =             -999;
    (*eventvariables)["nValidDtHits_upper1"] =              -999;
    (*eventvariables)["nValidRpcHits_upper1"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_upper1"] = -999;
    (*eventvariables)["outermostStationWithValidHits_upper1"] = -999;
    (*eventvariables)["quality_upper1"] = -999;
    (*eventvariables)["innerPx_upper1"] = -999;
    (*eventvariables)["innerPy_upper1"] = -999;
    (*eventvariables)["innerPz_upper1"] = -999;
    (*eventvariables)["innerOk_upper1"] = -999;
    (*eventvariables)["innerX_upper1"] =  -999;
    (*eventvariables)["innerY_upper1"] =  -999;
    (*eventvariables)["innerZ_upper1"] =  -999;
    (*eventvariables)["dtTofDirection_upper1"] =          -999;
    (*eventvariables)["dtTofNDof_upper1"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_upper1"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_upper1"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_upper1"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper1"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_upper1"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper1"] =   -999;
    (*eventvariables)["nRpcHits_upper1"] =                -999;
    (*eventvariables)["rpcBxPattern_upper1"] =            -999;
    (*eventvariables)["rpcBxAverage_upper1"] =            -999;
  }
  if(upper2_index!=999){
    (*eventvariables)["p_upper2"] =                         (tracks->at(upper2_index)).p();
    (*eventvariables)["pt_upper2"] =                        (tracks->at(upper2_index)).pt();
    (*eventvariables)["eta_upper2"] =                       (tracks->at(upper2_index)).eta();
    (*eventvariables)["phi_upper2"] =                       (tracks->at(upper2_index)).phi();
    (*eventvariables)["ndof_upper2"] =                      (tracks->at(upper2_index)).ndof();
    (*eventvariables)["normalizedChi2_upper2"] =            (tracks->at(upper2_index)).normalizedChi2();
    (*eventvariables)["charge_upper2"] =                    (tracks->at(upper2_index)).charge();
    (*eventvariables)["dxy_upper2"] =                       (tracks->at(upper2_index)).dxy();
    (*eventvariables)["dz_upper2"] =                        (tracks->at(upper2_index)).dz();
    (*eventvariables)["vx_upper2"] =                        (tracks->at(upper2_index)).vx();
    (*eventvariables)["vy_upper2"] =                        (tracks->at(upper2_index)).vy();
    (*eventvariables)["vz_upper2"] =                        (tracks->at(upper2_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_upper2"] =      (tracks->at(upper2_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_upper2"] =   (tracks->at(upper2_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_upper2"] =    (tracks->at(upper2_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_upper2"] =   (tracks->at(upper2_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_upper2"] =    (tracks->at(upper2_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_upper2"] = (tracks->at(upper2_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_upper2"] =  (tracks->at(upper2_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_upper2"] = (tracks->at(upper2_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_upper2"] =            (tracks->at(upper2_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_upper2"] =             (tracks->at(upper2_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_upper2"] =              (tracks->at(upper2_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_upper2"] =             (tracks->at(upper2_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_upper2"] = (tracks->at(upper2_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_upper2"] = (tracks->at(upper2_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_upper2"] = (tracks->at(upper2_index)).quality();
    (*eventvariables)["innerPx_upper2"] = (tracks->at(upper2_index)).innerPx();
    (*eventvariables)["innerPy_upper2"] = (tracks->at(upper2_index)).innerPy();
    (*eventvariables)["innerPz_upper2"] = (tracks->at(upper2_index)).innerPz();
    (*eventvariables)["innerOk_upper2"] = (tracks->at(upper2_index)).innerOk();
    (*eventvariables)["innerX_upper2"] =  (tracks->at(upper2_index)).innerX();
    (*eventvariables)["innerY_upper2"] =  (tracks->at(upper2_index)).innerY();
    (*eventvariables)["innerZ_upper2"] =  (tracks->at(upper2_index)).innerZ();
    (*eventvariables)["dtTofDirection_upper2"] =          (tracks->at(upper2_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_upper2"] =               (tracks->at(upper2_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_upper2"] =    (tracks->at(upper2_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_upper2"] = (tracks->at(upper2_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_upper2"] =      (tracks->at(upper2_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper2"] =   (tracks->at(upper2_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_upper2"] =      (tracks->at(upper2_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper2"] =   (tracks->at(upper2_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(upper2_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_upper2"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_upper2"] =            Rpc_Bx_Pattern(tracks,upper2_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_upper2"] =            Rpc_Bx_Average(tracks,upper2_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_upper2"] =                         -999;
    (*eventvariables)["pt_upper2"] =                        -999;
    (*eventvariables)["eta_upper2"] =                       -999;
    (*eventvariables)["phi_upper2"] =                       -999;
    (*eventvariables)["ndof_upper2"] =                      -999;
    (*eventvariables)["normalizedChi2_upper2"] =            -999;
    (*eventvariables)["charge_upper2"] =                    -999;
    (*eventvariables)["dxy_upper2"] =                       -999;
    (*eventvariables)["dz_upper2"] =                        -999;
    (*eventvariables)["vx_upper2"] =                        -999;
    (*eventvariables)["vy_upper2"] =                        -999;
    (*eventvariables)["vz_upper2"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_upper2"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_upper2"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_upper2"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_upper2"] =   -999;
    (*eventvariables)["nStationsWithValidHits_upper2"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_upper2"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_upper2"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_upper2"] = -999;
    (*eventvariables)["nValidMuonHits_upper2"] =            -999;
    (*eventvariables)["nValidCscHits_upper2"] =             -999;
    (*eventvariables)["nValidDtHits_upper2"] =              -999;
    (*eventvariables)["nValidRpcHits_upper2"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_upper2"] = -999;
    (*eventvariables)["outermostStationWithValidHits_upper2"] = -999;
    (*eventvariables)["quality_upper2"] = -999;
    (*eventvariables)["innerPx_upper2"] = -999;
    (*eventvariables)["innerPy_upper2"] = -999;
    (*eventvariables)["innerPz_upper2"] = -999;
    (*eventvariables)["innerOk_upper2"] = -999;
    (*eventvariables)["innerX_upper2"] =  -999;
    (*eventvariables)["innerY_upper2"] =  -999;
    (*eventvariables)["innerZ_upper2"] =  -999;
    (*eventvariables)["dtTofDirection_upper2"] =          -999;
    (*eventvariables)["dtTofNDof_upper2"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_upper2"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_upper2"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_upper2"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_upper2"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_upper2"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_upper2"] =   -999;
    (*eventvariables)["nRpcHits_upper2"] =                -999;
    (*eventvariables)["rpcBxPattern_upper2"] =            -999;
    (*eventvariables)["rpcBxAverage_upper2"] =            -999;
  }


  if(lower0_index!=999){
    (*eventvariables)["p_lower0"] =                         (tracks->at(lower0_index)).p();
    (*eventvariables)["pt_lower0"] =                        (tracks->at(lower0_index)).pt();
    (*eventvariables)["eta_lower0"] =                       (tracks->at(lower0_index)).eta();
    (*eventvariables)["phi_lower0"] =                       (tracks->at(lower0_index)).phi();
    (*eventvariables)["ndof_lower0"] =                      (tracks->at(lower0_index)).ndof();
    (*eventvariables)["normalizedChi2_lower0"] =            (tracks->at(lower0_index)).normalizedChi2();
    (*eventvariables)["charge_lower0"] =                    (tracks->at(lower0_index)).charge();
    (*eventvariables)["dxy_lower0"] =                       (tracks->at(lower0_index)).dxy();
    (*eventvariables)["dz_lower0"] =                        (tracks->at(lower0_index)).dz();
    (*eventvariables)["vx_lower0"] =                        (tracks->at(lower0_index)).vx();
    (*eventvariables)["vy_lower0"] =                        (tracks->at(lower0_index)).vy();
    (*eventvariables)["vz_lower0"] =                        (tracks->at(lower0_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_lower0"] =      (tracks->at(lower0_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_lower0"] =   (tracks->at(lower0_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_lower0"] =    (tracks->at(lower0_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_lower0"] =   (tracks->at(lower0_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_lower0"] =    (tracks->at(lower0_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_lower0"] = (tracks->at(lower0_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_lower0"] =  (tracks->at(lower0_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_lower0"] = (tracks->at(lower0_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_lower0"] =            (tracks->at(lower0_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_lower0"] =             (tracks->at(lower0_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_lower0"] =              (tracks->at(lower0_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_lower0"] =             (tracks->at(lower0_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_lower0"] = (tracks->at(lower0_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_lower0"] = (tracks->at(lower0_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_lower0"] = (tracks->at(lower0_index)).quality();
    (*eventvariables)["innerPx_lower0"] = (tracks->at(lower0_index)).innerPx();
    (*eventvariables)["innerPy_lower0"] = (tracks->at(lower0_index)).innerPy();
    (*eventvariables)["innerPz_lower0"] = (tracks->at(lower0_index)).innerPz();
    (*eventvariables)["innerOk_lower0"] = (tracks->at(lower0_index)).innerOk();
    (*eventvariables)["innerX_lower0"] =  (tracks->at(lower0_index)).innerX();
    (*eventvariables)["innerY_lower0"] =  (tracks->at(lower0_index)).innerY();
    (*eventvariables)["innerZ_lower0"] =  (tracks->at(lower0_index)).innerZ();
    (*eventvariables)["dtTofDirection_lower0"] =          (tracks->at(lower0_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_lower0"] =               (tracks->at(lower0_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_lower0"] =    (tracks->at(lower0_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_lower0"] = (tracks->at(lower0_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_lower0"] =      (tracks->at(lower0_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower0"] =   (tracks->at(lower0_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_lower0"] =      (tracks->at(lower0_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower0"] =   (tracks->at(lower0_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(lower0_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_lower0"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_lower0"] =            Rpc_Bx_Pattern(tracks,lower0_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_lower0"] =            Rpc_Bx_Average(tracks,lower0_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_lower0"] =                         -999;
    (*eventvariables)["pt_lower0"] =                        -999;
    (*eventvariables)["eta_lower0"] =                       -999;
    (*eventvariables)["phi_lower0"] =                       -999;
    (*eventvariables)["ndof_lower0"] =                      -999;
    (*eventvariables)["normalizedChi2_lower0"] =            -999;
    (*eventvariables)["charge_lower0"] =                    -999;
    (*eventvariables)["dxy_lower0"] =                       -999;
    (*eventvariables)["dz_lower0"] =                        -999;
    (*eventvariables)["vx_lower0"] =                        -999;
    (*eventvariables)["vy_lower0"] =                        -999;
    (*eventvariables)["vz_lower0"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_lower0"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_lower0"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_lower0"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_lower0"] =   -999;
    (*eventvariables)["nStationsWithValidHits_lower0"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_lower0"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_lower0"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_lower0"] = -999;
    (*eventvariables)["nValidMuonHits_lower0"] =            -999;
    (*eventvariables)["nValidCscHits_lower0"] =             -999;
    (*eventvariables)["nValidDtHits_lower0"] =              -999;
    (*eventvariables)["nValidRpcHits_lower0"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_lower0"] = -999;
    (*eventvariables)["outermostStationWithValidHits_lower0"] = -999;
    (*eventvariables)["quality_lower0"] = -999;
    (*eventvariables)["innerPx_lower0"] = -999;
    (*eventvariables)["innerPy_lower0"] = -999;
    (*eventvariables)["innerPz_lower0"] = -999;
    (*eventvariables)["innerOk_lower0"] = -999;
    (*eventvariables)["innerX_lower0"] =  -999;
    (*eventvariables)["innerY_lower0"] =  -999;
    (*eventvariables)["innerZ_lower0"] =  -999;
    (*eventvariables)["dtTofDirection_lower0"] =          -999;
    (*eventvariables)["dtTofNDof_lower0"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_lower0"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_lower0"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_lower0"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower0"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_lower0"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower0"] =   -999;
    (*eventvariables)["nRpcHits_lower0"] =                -999;
    (*eventvariables)["rpcBxPattern_lower0"] =            -999;
    (*eventvariables)["rpcBxAverage_lower0"] =            -999;
  }
  if(lower1_index!=999){
    (*eventvariables)["p_lower1"] =                         (tracks->at(lower1_index)).p();
    (*eventvariables)["pt_lower1"] =                        (tracks->at(lower1_index)).pt();
    (*eventvariables)["eta_lower1"] =                       (tracks->at(lower1_index)).eta();
    (*eventvariables)["phi_lower1"] =                       (tracks->at(lower1_index)).phi();
    (*eventvariables)["ndof_lower1"] =                      (tracks->at(lower1_index)).ndof();
    (*eventvariables)["normalizedChi2_lower1"] =            (tracks->at(lower1_index)).normalizedChi2();
    (*eventvariables)["charge_lower1"] =                    (tracks->at(lower1_index)).charge();
    (*eventvariables)["dxy_lower1"] =                       (tracks->at(lower1_index)).dxy();
    (*eventvariables)["dz_lower1"] =                        (tracks->at(lower1_index)).dz();
    (*eventvariables)["vx_lower1"] =                        (tracks->at(lower1_index)).vx();
    (*eventvariables)["vy_lower1"] =                        (tracks->at(lower1_index)).vy();
    (*eventvariables)["vz_lower1"] =                        (tracks->at(lower1_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_lower1"] =      (tracks->at(lower1_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_lower1"] =   (tracks->at(lower1_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_lower1"] =    (tracks->at(lower1_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_lower1"] =   (tracks->at(lower1_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_lower1"] =    (tracks->at(lower1_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_lower1"] = (tracks->at(lower1_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_lower1"] =  (tracks->at(lower1_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_lower1"] = (tracks->at(lower1_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_lower1"] =            (tracks->at(lower1_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_lower1"] =             (tracks->at(lower1_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_lower1"] =              (tracks->at(lower1_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_lower1"] =             (tracks->at(lower1_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_lower1"] = (tracks->at(lower1_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_lower1"] = (tracks->at(lower1_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_lower1"] = (tracks->at(lower1_index)).quality();
    (*eventvariables)["innerPx_lower1"] = (tracks->at(lower1_index)).innerPx();
    (*eventvariables)["innerPy_lower1"] = (tracks->at(lower1_index)).innerPy();
    (*eventvariables)["innerPz_lower1"] = (tracks->at(lower1_index)).innerPz();
    (*eventvariables)["innerOk_lower1"] = (tracks->at(lower1_index)).innerOk();
    (*eventvariables)["innerX_lower1"] =  (tracks->at(lower1_index)).innerX();
    (*eventvariables)["innerY_lower1"] =  (tracks->at(lower1_index)).innerY();
    (*eventvariables)["innerZ_lower1"] =  (tracks->at(lower1_index)).innerZ();
    (*eventvariables)["dtTofDirection_lower1"] =          (tracks->at(lower1_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_lower1"] =               (tracks->at(lower1_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_lower1"] =    (tracks->at(lower1_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_lower1"] = (tracks->at(lower1_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_lower1"] =      (tracks->at(lower1_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower1"] =   (tracks->at(lower1_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_lower1"] =      (tracks->at(lower1_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower1"] =   (tracks->at(lower1_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(lower1_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_lower1"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_lower1"] =            Rpc_Bx_Pattern(tracks,lower1_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_lower1"] =            Rpc_Bx_Average(tracks,lower1_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_lower1"] =                         -999;
    (*eventvariables)["pt_lower1"] =                        -999;
    (*eventvariables)["eta_lower1"] =                       -999;
    (*eventvariables)["phi_lower1"] =                       -999;
    (*eventvariables)["ndof_lower1"] =                      -999;
    (*eventvariables)["normalizedChi2_lower1"] =            -999;
    (*eventvariables)["charge_lower1"] =                    -999;
    (*eventvariables)["dxy_lower1"] =                       -999;
    (*eventvariables)["dz_lower1"] =                        -999;
    (*eventvariables)["vx_lower1"] =                        -999;
    (*eventvariables)["vy_lower1"] =                        -999;
    (*eventvariables)["vz_lower1"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_lower1"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_lower1"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_lower1"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_lower1"] =   -999;
    (*eventvariables)["nStationsWithValidHits_lower1"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_lower1"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_lower1"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_lower1"] = -999;
    (*eventvariables)["nValidMuonHits_lower1"] =            -999;
    (*eventvariables)["nValidCscHits_lower1"] =             -999;
    (*eventvariables)["nValidDtHits_lower1"] =              -999;
    (*eventvariables)["nValidRpcHits_lower1"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_lower1"] = -999;
    (*eventvariables)["outermostStationWithValidHits_lower1"] = -999;
    (*eventvariables)["quality_lower1"] = -999;
    (*eventvariables)["innerPx_lower1"] = -999;
    (*eventvariables)["innerPy_lower1"] = -999;
    (*eventvariables)["innerPz_lower1"] = -999;
    (*eventvariables)["innerOk_lower1"] = -999;
    (*eventvariables)["innerX_lower1"] =  -999;
    (*eventvariables)["innerY_lower1"] =  -999;
    (*eventvariables)["innerZ_lower1"] =  -999;
    (*eventvariables)["dtTofDirection_lower1"] =          -999;
    (*eventvariables)["dtTofNDof_lower1"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_lower1"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_lower1"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_lower1"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower1"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_lower1"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower1"] =   -999;
    (*eventvariables)["nRpcHits_lower1"] =                -999;
    (*eventvariables)["rpcBxPattern_lower1"] =            -999;
    (*eventvariables)["rpcBxAverage_lower1"] =            -999;
  }
  if(lower2_index!=999){
    (*eventvariables)["p_lower2"] =                         (tracks->at(lower2_index)).p();
    (*eventvariables)["pt_lower2"] =                        (tracks->at(lower2_index)).pt();
    (*eventvariables)["eta_lower2"] =                       (tracks->at(lower2_index)).eta();
    (*eventvariables)["phi_lower2"] =                       (tracks->at(lower2_index)).phi();
    (*eventvariables)["ndof_lower2"] =                      (tracks->at(lower2_index)).ndof();
    (*eventvariables)["normalizedChi2_lower2"] =            (tracks->at(lower2_index)).normalizedChi2();
    (*eventvariables)["charge_lower2"] =                    (tracks->at(lower2_index)).charge();
    (*eventvariables)["dxy_lower2"] =                       (tracks->at(lower2_index)).dxy();
    (*eventvariables)["dz_lower2"] =                        (tracks->at(lower2_index)).dz();
    (*eventvariables)["vx_lower2"] =                        (tracks->at(lower2_index)).vx();
    (*eventvariables)["vy_lower2"] =                        (tracks->at(lower2_index)).vy();
    (*eventvariables)["vz_lower2"] =                        (tracks->at(lower2_index)).vz();
    (*eventvariables)["nStationsWithAnyHits_lower2"] =      (tracks->at(lower2_index)).nStationsWithAnyHits();
    (*eventvariables)["nCscChambersWithAnyHits_lower2"] =   (tracks->at(lower2_index)).nCscChambersWithAnyHits();
    (*eventvariables)["nDtChambersWithAnyHits_lower2"] =    (tracks->at(lower2_index)).nDtChambersWithAnyHits();
    (*eventvariables)["nRpcChambersWithAnyHits_lower2"] =   (tracks->at(lower2_index)).nRpcChambersWithAnyHits();
    (*eventvariables)["nStationsWithValidHits_lower2"] =    (tracks->at(lower2_index)).nStationsWithValidHits();
    (*eventvariables)["nCscChambersWithValidHits_lower2"] = (tracks->at(lower2_index)).nCscChambersWithValidHits();
    (*eventvariables)["nDtChambersWithValidHits_lower2"] =  (tracks->at(lower2_index)).nDtChambersWithValidHits();
    (*eventvariables)["nRpcChambersWithValidHits_lower2"] = (tracks->at(lower2_index)).nRpcChambersWithValidHits();
    (*eventvariables)["nValidMuonHits_lower2"] =            (tracks->at(lower2_index)).nValidMuonHits();
    (*eventvariables)["nValidCscHits_lower2"] =             (tracks->at(lower2_index)).nValidCscHits();
    (*eventvariables)["nValidDtHits_lower2"] =              (tracks->at(lower2_index)).nValidDtHits();
    (*eventvariables)["nValidRpcHits_lower2"] =             (tracks->at(lower2_index)).nValidRpcHits();
    (*eventvariables)["innermostStationWithValidHits_lower2"] = (tracks->at(lower2_index)).innermostStationWithValidHits();
    (*eventvariables)["outermostStationWithValidHits_lower2"] = (tracks->at(lower2_index)).outermostStationWithValidHits();
    (*eventvariables)["quality_lower2"] = (tracks->at(lower2_index)).quality();
    (*eventvariables)["innerPx_lower2"] = (tracks->at(lower2_index)).innerPx();
    (*eventvariables)["innerPy_lower2"] = (tracks->at(lower2_index)).innerPy();
    (*eventvariables)["innerPz_lower2"] = (tracks->at(lower2_index)).innerPz();
    (*eventvariables)["innerOk_lower2"] = (tracks->at(lower2_index)).innerOk();
    (*eventvariables)["innerX_lower2"] =  (tracks->at(lower2_index)).innerX();
    (*eventvariables)["innerY_lower2"] =  (tracks->at(lower2_index)).innerY();
    (*eventvariables)["innerZ_lower2"] =  (tracks->at(lower2_index)).innerZ();
    (*eventvariables)["dtTofDirection_lower2"] =          (tracks->at(lower2_index)).dtTofDirection();
    (*eventvariables)["dtTofNDof_lower2"] =               (tracks->at(lower2_index)).dtTofNDof();
    (*eventvariables)["dtTofFreeInverseBeta_lower2"] =    (tracks->at(lower2_index)).dtTofFreeInverseBeta();
    (*eventvariables)["dtTofFreeInverseBetaErr_lower2"] = (tracks->at(lower2_index)).dtTofFreeInverseBetaErr();
    (*eventvariables)["dtTofTimeAtIpInOut_lower2"] =      (tracks->at(lower2_index)).dtTofTimeAtIpInOut();
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower2"] =   (tracks->at(lower2_index)).dtTofTimeAtIpInOutErr();
    (*eventvariables)["dtTofTimeAtIpOutIn_lower2"] =      (tracks->at(lower2_index)).dtTofTimeAtIpOutIn();
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower2"] =   (tracks->at(lower2_index)).dtTofTimeAtIpOutInErr();
    long unsigned int nRpcHits = tracks->at(lower2_index).rpcHitBx().size();
    (*eventvariables)["nRpcHits_lower2"] =                nRpcHits;
    (*eventvariables)["rpcBxPattern_lower2"] =            Rpc_Bx_Pattern(tracks,lower2_index,nRpcHits);
    (*eventvariables)["rpcBxAverage_lower2"] =            Rpc_Bx_Average(tracks,lower2_index,nRpcHits);
  }
  else{
    (*eventvariables)["p_lower2"] =                         -999;
    (*eventvariables)["pt_lower2"] =                        -999;
    (*eventvariables)["eta_lower2"] =                       -999;
    (*eventvariables)["phi_lower2"] =                       -999;
    (*eventvariables)["ndof_lower2"] =                      -999;
    (*eventvariables)["normalizedChi2_lower2"] =            -999;
    (*eventvariables)["charge_lower2"] =                    -999;
    (*eventvariables)["dxy_lower2"] =                       -999;
    (*eventvariables)["dz_lower2"] =                        -999;
    (*eventvariables)["vx_lower2"] =                        -999;
    (*eventvariables)["vy_lower2"] =                        -999;
    (*eventvariables)["vz_lower2"] =                        -999;
    (*eventvariables)["nStationsWithAnyHits_lower2"] =      -999;
    (*eventvariables)["nCscChambersWithAnyHits_lower2"] =   -999;
    (*eventvariables)["nDtChambersWithAnyHits_lower2"] =    -999;
    (*eventvariables)["nRpcChambersWithAnyHits_lower2"] =   -999;
    (*eventvariables)["nStationsWithValidHits_lower2"] =    -999;
    (*eventvariables)["nCscChambersWithValidHits_lower2"] = -999;
    (*eventvariables)["nDtChambersWithValidHits_lower2"] =  -999;
    (*eventvariables)["nRpcChambersWithValidHits_lower2"] = -999;
    (*eventvariables)["nValidMuonHits_lower2"] =            -999;
    (*eventvariables)["nValidCscHits_lower2"] =             -999;
    (*eventvariables)["nValidDtHits_lower2"] =              -999;
    (*eventvariables)["nValidRpcHits_lower2"] =             -999;
    (*eventvariables)["innermostStationWithValidHits_lower2"] = -999;
    (*eventvariables)["outermostStationWithValidHits_lower2"] = -999;
    (*eventvariables)["quality_lower2"] = -999;
    (*eventvariables)["innerPx_lower2"] = -999;
    (*eventvariables)["innerPy_lower2"] = -999;
    (*eventvariables)["innerPz_lower2"] = -999;
    (*eventvariables)["innerOk_lower2"] = -999;
    (*eventvariables)["innerX_lower2"] =  -999;
    (*eventvariables)["innerY_lower2"] =  -999;
    (*eventvariables)["innerZ_lower2"] =  -999;
    (*eventvariables)["dtTofDirection_lower2"] =          -999;
    (*eventvariables)["dtTofNDof_lower2"] =               -999;
    (*eventvariables)["dtTofFreeInverseBeta_lower2"] =    -999;
    (*eventvariables)["dtTofFreeInverseBetaErr_lower2"] = -999;
    (*eventvariables)["dtTofTimeAtIpInOut_lower2"] =      -999;
    (*eventvariables)["dtTofTimeAtIpInOutErr_lower2"] =   -999;
    (*eventvariables)["dtTofTimeAtIpOutIn_lower2"] =      -999;
    (*eventvariables)["dtTofTimeAtIpOutInErr_lower2"] =   -999;
    (*eventvariables)["nRpcHits_lower2"] =                -999;
    (*eventvariables)["rpcBxPattern_lower2"] =            -999;
    (*eventvariables)["rpcBxAverage_lower2"] =            -999;
  }

}//end of AddVariables()

int DelayedMuonsEventVariableProducer::Rpc_Bx_Pattern(edm::Handle<std::vector<CandidateDelayedMuonsTrack> > &tracks, long unsigned int& i, long unsigned int& nRpcHits) {

  bool all_bx_0 = true;
  bool all_bx_positive = true;
  bool all_bx_negative = true;
  bool all_bx_positiveOr0 = true;
  bool all_bx_negativeOr0 = true;
  bool all_bx_constant = true;
  bool all_bx_increasing = true;
  bool all_bx_decreasing = true;

  if(nRpcHits==0){
    all_bx_0 = false;
    all_bx_positive = false;
    all_bx_negative = false;
    all_bx_positiveOr0 = false;
    all_bx_negativeOr0 = false;
    all_bx_constant = false;
    all_bx_increasing = false;
    all_bx_decreasing = false;
  }

  //loop over Rpc hits
  for(unsigned int j = 0; j != nRpcHits; ++j) {
    //std::cout<<"  for rpc hit "<<j<<", BX is: "<<tracks->at(i).rpcHitBx().at(j)<<", Z is: "<<tracks->at(i).rpcHitZ().at(j)<<", Rho is: "<<tracks->at(i).rpcHitRho().at(j)<<", phi is: "<<tracks->at(i).rpcHitPhi().at(j)<<", region is: "<<tracks->at(i).rpcHitRegion().at(j)<<std::endl;
    if(tracks->at(i).rpcHitBx().at(j) != 0) all_bx_0 = false;
    if(tracks->at(i).rpcHitBx().at(j) <= 0) all_bx_positive = false;
    if(tracks->at(i).rpcHitBx().at(j) >= 0) all_bx_negative = false;
    if(tracks->at(i).rpcHitBx().at(j) < 0) all_bx_positiveOr0 = false;
    if(tracks->at(i).rpcHitBx().at(j) > 0) all_bx_negativeOr0 = false;
    unsigned int k=j+1;
    if(k<nRpcHits){
      if(tracks->at(i).rpcHitBx().at(k) != tracks->at(i).rpcHitBx().at(j)) all_bx_constant = false;
      if(tracks->at(i).rpcHitBx().at(k) < tracks->at(i).rpcHitBx().at(j)) all_bx_increasing = false;
      if(tracks->at(i).rpcHitBx().at(k) > tracks->at(i).rpcHitBx().at(j)) all_bx_decreasing = false;
    }
  }
  if(all_bx_constant) {
    all_bx_increasing = false;
    all_bx_decreasing = false;
  }

  if(nRpcHits<=0) return(-1);
  if(all_bx_0 && all_bx_constant){
    return(0);
    //cout<<"0BX"<<endl;
  }
  if(all_bx_positive && all_bx_constant){
    return(1);
    //cout<<"positiveConstantBX"<<endl;
  }
  if(all_bx_positiveOr0 && all_bx_increasing){
    return(2);
    //cout<<"positiveOr0IncreasingBX"<<endl;
  }
  if(all_bx_positiveOr0 && all_bx_decreasing){
    return(3);
    //cout<<"positiveOr0DecreasingBX"<<endl;
  }
  if(all_bx_positiveOr0 && !all_bx_decreasing && !all_bx_increasing && !all_bx_constant){
    return(4);
    //cout<<"positiveOr0StrangeBX"<<endl;
  }
  if(all_bx_negative && all_bx_constant){
    return(5);
    //cout<<"negativeConstantBX"<<endl;
  }
  if(all_bx_negativeOr0 && all_bx_increasing){
    return(6);
    //cout<<"negativeOr0IncreasingBX"<<endl;
  }
  if(all_bx_negativeOr0 && all_bx_decreasing){
    return(7);
    //cout<<"negativeOr0DecreasingBX"<<endl;
  }
  if(all_bx_negativeOr0 && !all_bx_decreasing && !all_bx_increasing && !all_bx_constant){
    return(8);
    //cout<<"negativeOr0StrangeBX"<<endl;
  }
  return(-1);
}//end of Rpc_Bx_Pattern

double DelayedMuonsEventVariableProducer::Rpc_Bx_Average(edm::Handle<std::vector<CandidateDelayedMuonsTrack> > &tracks, long unsigned int& i, long unsigned int& nRpcHits) {
  double rpc_bx_average = 0.;

  //loop over Rpc hits
  for(unsigned int j = 0; j != nRpcHits; ++j) {
    rpc_bx_average += tracks->at(i).rpcHitBx().at(j);
  }

  if(nRpcHits!=0) rpc_bx_average = 1.0*rpc_bx_average/nRpcHits;
  else rpc_bx_average = -999;

  return rpc_bx_average;
}//end of Rpc_Bx_Average
  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DelayedMuonsEventVariableProducer);

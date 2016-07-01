// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      RPCHits3DPlotter
// 
/**\class RPCHits3DPlotter RPCHits3DPlotter.cc StoppPtls/Collection/plugins/RPCHits3DPlotter.cc

 Description: [one line class summary]
 This EDProducer makes a 3D histogram of RPChits, which will be used in RPC masking procedure.

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Weifeng Ji
//         Created:  Wed, 22 Jun 2016 13:57:39 GMT
//
//
#ifndef RPCHitHist_H
#define RPCHitHist_H


// system include files
#include <memory>
#include <math.h>
#include <iostream>
#include <TVector3.h>

// user include files
#include <vector>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"


#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "StoppPtls/Collection/interface/CandidateRpcHit.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "StoppPtls/Collection/interface/CandidateCscSeg.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "TFile.h"
#include "TH1D.h"
#include "TH3.h"


using std::vector;
using namespace std;


//
// class declaration
//

class RPCHits3DPlotter : public edm::EDProducer {
   public:
      explicit RPCHits3DPlotter(const edm::ParameterSet&);
      ~RPCHits3DPlotter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      TH3D *RPCHitHist_;
      TH1D *RPCHitNumber_;

      TH3D *RPCHitInConeHist_;    // Plot of RPC hits that have a close neigbour inside a cone
      TH1D *RPCHitInConeNumber_;  // histo of density of RPC hits in regions of RPCHitInConeHist_

      TH1D *NOuterAllBarrelRPCPairsDeltaR0P2_;

      //TFile *ofile_;
      edm::InputTag candidateRpcHitsTag_;
      edm::EDGetTokenT<vector<CandidateRpcHit> > candidateRpcHitsToken_;
      edm::InputTag candidateDTSegsTag_;
      edm::EDGetTokenT<vector<CandidateDTSeg> > candidateDTSegsToken_;
      edm::InputTag candidateCscSegsTag_;
      edm::EDGetTokenT<vector<CandidateCscSeg> > candidateCscSegsToken_;
      bool noiseOnly = false;
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
RPCHits3DPlotter::RPCHits3DPlotter(const edm::ParameterSet& iConfig):
  candidateRpcHitsTag_ (iConfig.getParameter<edm::InputTag>("candidateRpcHitsTag")),
  candidateRpcHitsToken_(consumes<vector<CandidateRpcHit> >(candidateRpcHitsTag_)),
  candidateDTSegsTag_ (iConfig.getParameter<edm::InputTag>("candidateDTSegsTag")),
  candidateDTSegsToken_(consumes<vector<CandidateDTSeg> >(candidateDTSegsTag_)),
  candidateCscSegsTag_ (iConfig.getParameter<edm::InputTag>("candidateCscSegsTag")),
  candidateCscSegsToken_(consumes<vector<CandidateCscSeg> >(candidateCscSegsTag_)),
  noiseOnly(iConfig.getParameter<bool>("RPCNoiseOnly"))
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed
    if (noiseOnly == true) {
      cout << "Fill only noise RPC hits" << endl;
    }
    else {
      cout << "Fill all RPC hits" << endl;
    }
  
}


RPCHits3DPlotter::~RPCHits3DPlotter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
RPCHits3DPlotter::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  edm::Handle<vector<CandidateRpcHit> > rpchits;
  iEvent.getByToken(candidateRpcHitsToken_, rpchits);
  edm::Handle<vector<CandidateDTSeg> > dtsegs;
  iEvent.getByToken(candidateDTSegsToken_, dtsegs);
  edm::Handle<vector<CandidateCscSeg> > cscsegs;
  iEvent.getByToken(candidateCscSegsToken_, cscsegs);
// if noiseonly is ture, we only fill in the rpchits in events that have no dt or csc segments, so that the rpchits is just noise.
  if (noiseOnly == true) {
    if (dtsegs->size() == 0 && cscsegs->size() == 0) {
      unsigned nRPCPairDeltaR0p2 = 0;
      for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
        double x = (rpchits->at(i)).x();
        double y = (rpchits->at(i)).y();
        double z = (rpchits->at(i)).z();

        if (fabs(z) < 700 && sqrt(pow(x, 2) + pow(y, 2)) > 300){
          RPCHitHist_->Fill(x, y, z);
        }
      }
      for (unsigned i = 0; i != rpchits->size(); ++i) {
        if ((rpchits->at(i)).r() > 560) {
          for (unsigned j = i; j != rpchits->size(); ++j) {
            TVector3 tveci((rpchits->at(i)).x(), (rpchits->at(i)).y(), (rpchits->at(i)).z());
            TVector3 tvecj((rpchits->at(j)).x(), (rpchits->at(j)).y(), (rpchits->at(j)).z()); 
            double rpc_eta_i = tveci.Eta();
            double rpc_eta_j = tvecj.Eta();
            double deltaR = reco::deltaR(rpc_eta_i, (rpchits->at(i)).phi(), rpc_eta_j, (rpchits->at(j)).phi());
            if (deltaR < 0.2) {
              double x = (rpchits->at(i)).x();
              double y = (rpchits->at(i)).y();
              double z = (rpchits->at(i)).z();
              if (fabs(z) < 700 && sqrt(pow(x, 2) + pow(y, 2)) > 300){
                RPCHitInConeHist_->Fill(x, y, z);
                nRPCPairDeltaR0p2 += 1;
              }
            }
          }
          
        }
      }
      NOuterAllBarrelRPCPairsDeltaR0P2_->Fill(nRPCPairDeltaR0p2);
    }
  }
  else{
    for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
      double x = (rpchits->at(i)).x();
      double y = (rpchits->at(i)).y();
      double z = (rpchits->at(i)).z();

      if (fabs(z) < 700 && sqrt(pow(x, 2) + pow(y, 2)) > 300){
        RPCHitHist_->Fill(x, y, z);
      }
    }
  }


/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::unique_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(std::move(pOut));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
RPCHits3DPlotter::beginJob()
{
//RPCHitHist_ = new TH3D("RPCHits", "RPCHits", 100, -1000, 1000, 100, -1000, 1000, 100, -1200, 1200);
   //RPCHitNumber_ = new TH1D("RPCHitNumber", "RPCHitNumber", 5000, 0, 5000);
    edm::Service<TFileService> fs;
   //ofile_ = fs->make<TFile>("RPCHitHist.root", "RECREATE");
   RPCHitHist_ = fs->make<TH3D>("RPCHits", "RPCHits", 100, -1000, 1000, 100, -1000, 1000, 100, -1200, 1200);
   RPCHitNumber_ = fs->make<TH1D>("RPCHitNumber", "RPCHitNumber", 5000, 0, 5000);
   RPCHitInConeHist_ = fs->make<TH3D>("RPCHitsInCone", "RPCHitsInCone", 50, -1000, 1000, 50, -1000, 1000, 50, -1200, 1200);
   RPCHitInConeNumber_ = fs->make<TH1D>("RPCHitInConeNumber", "RPCHitInConeNumber", 5000, 0, 5000);
   NOuterAllBarrelRPCPairsDeltaR0P2_ = fs->make<TH1D>("NOuterAllBarrelRPCPairsDeltaR0P2", "NOuterAllBarrelRPCPairsDeltaR0P2", 20, 0, 20);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RPCHits3DPlotter::endJob() {
  for (unsigned i = 1; i < 101; i += 1) {
    for (unsigned j = 1; j < 101; j += 1) {
      for (unsigned k = 1; k < 101; k += 1) {
        if (RPCHitHist_->GetBinContent(i, j, k) != 0) {
          RPCHitNumber_->Fill(RPCHitHist_->GetBinContent(i, j, k));
        }
      }
    }
  }
  for (unsigned i = 1; i < 51; i += 1) {
    for (unsigned j = 1; j < 51; j += 1) {
      for (unsigned k = 1; k < 51; k += 1) {
        if (RPCHitInConeHist_->GetBinContent(i, j, k) != 0) {
          RPCHitInConeNumber_->Fill(RPCHitInConeHist_->GetBinContent(i, j, k));
        }
      }
    }
  }
  //ofile_->cd();
  //RPCHitHist_->Write("",TObject::kOverwrite);
  //RPCHitNumber_->Write("", TObject::kOverwrite);
  
}

// ------------ method called when starting to processes a run  ------------
/*
void
RPCHits3DPlotter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
RPCHits3DPlotter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
RPCHits3DPlotter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
RPCHits3DPlotter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
RPCHits3DPlotter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(RPCHits3DPlotter);
#endif

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

// user include files
#include <vector>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "StoppPtls/Collection/interface/CandidateRpcHit.h"
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
      TFile *ofile_;
      edm::InputTag candidateRpcHitsTag_;
      edm::EDGetTokenT<vector<CandidateRpcHit> > candidateRpcHitsToken_;
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
  candidateRpcHitsToken_(consumes<vector<CandidateRpcHit> >(candidateRpcHitsTag_))
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
   for (decltype(rpchits->size()) i = 0; i!= rpchits->size(); ++i) {
     double x = (rpchits->at(i)).x();
     double y = (rpchits->at(i)).y();
     double z = (rpchits->at(i)).z();

     if (fabs(z) < 700 && sqrt(pow(x, 2) + pow(y, 2)) > 300){
        RPCHitHist_->Fill(x, y, z);
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
   RPCHitHist_ = new TH3D("RPCHits", "RPCHits", 100, -1000, 1000, 100, -1000, 1000, 100, -1200, 1200);
   RPCHitNumber_ = new TH1D("RPCHitNumber", "RPCHitNumber", 5000, 0, 5000);
   ofile_ = new TFile("RPCHitHist.root", "RECREATE");
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
  ofile_->cd();
  RPCHitHist_->Write("",TObject::kOverwrite);
  RPCHitNumber_->Write("", TObject::kOverwrite);
  
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

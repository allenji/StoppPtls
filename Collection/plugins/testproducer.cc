// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      testproducer
// 
/**\class testproducer testproducer.cc StoppPtls/Collection/plugins/testproducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Weifeng Ji
//         Created:  Fri, 27 Nov 2015 13:41:35 GMT
//
//


// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "StoppPtls/Collection/interface/CandidateDTSeg.h"
#include "FWCore/Utilities/interface/InputTag.h"


//
// class declaration
//

class testproducer : public edm::EDProducer {
   public:
      explicit testproducer(const edm::ParameterSet&);
      ~testproducer();


   private:
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      
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
testproducer::testproducer(const edm::ParameterSet& iConfig)
{
   //register your products
   produces<std::vector<int> >();
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed
  
}


testproducer::~testproducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
testproducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   edm::Handle<std::vector<CandidateDTSeg> > candDT;
   edm::InputTag lbl("candidateStoppPtls");
   iEvent.getByLabel(lbl, candDT);
   std::cout << "data read" <<std::endl;
   for (auto &it : *candDT)
     std::cout << it.x() << std::endl;
   std::auto_ptr<std::vector<int> > ivec (new std::vector<int>());
   ivec->push_back(1);
   iEvent.put(ivec);
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

//define this as a plug-in
DEFINE_FWK_MODULE(testproducer);

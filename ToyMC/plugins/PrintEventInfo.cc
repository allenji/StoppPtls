// -*- C++ -*-
//
// Package:    StoppPtls/ToyMC
// Class:      PrintEventInfo
// 
/**\class PrintEventInfo PrintEventInfo.cc StoppPtls/ToyMC/plugins/PrintEventInfo.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Weifeng Ji
//         Created:  Tue, 19 Apr 2016 15:27:54 GMT
//
//


// system include files
#include <memory>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "StoppPtls/Livetime/interface/Constants.h"
#include "StoppPtls/Livetime/interface/LhcFills.h"


//
// class declaration
//

class PrintEventInfo : public edm::EDFilter {
   public:
      explicit PrintEventInfo(const edm::ParameterSet&);
      ~PrintEventInfo();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual bool filter(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      std::ofstream searchEventFile;
      std::ofstream lifetimeFile;
      LhcFills lhcFills;
      
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
PrintEventInfo::PrintEventInfo(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed

}


PrintEventInfo::~PrintEventInfo()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
PrintEventInfo::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  unsigned long id          = iEvent.id().event();
  unsigned long bx          = iEvent.bunchCrossing();
  unsigned long orbit       = iEvent.orbitNumber();
  unsigned long lb          = iEvent.luminosityBlock();
  unsigned long run         = iEvent.id().run();
  unsigned long fill        = lhcFills.getFillFromRun(run);
   searchEventFile << run << "," << lb << "," << orbit << "," << bx << ","
                    << id << std::endl;
    int bxAfter = 9999;
    int bxBefore = -9999;
    int bxLast=-1;
    int bxNext=-1;
    unsigned long bxPerOrbit  = 3564;
    auto currentColls_ = lhcFills.getCollisionsFromRun(run);
    if (currentColls_.size() > 0) {
      // special case if event is before first collision
      if (bx <= currentColls_.at(0)) {
    bxLast   = currentColls_.at(currentColls_.size() - 1);
    bxNext   = currentColls_.at(0);
    bxAfter  = (bx + bxPerOrbit) - bxLast;
    bxBefore = bx - bxNext;


      }
      // special case if event is after last collision
      else if (bx > currentColls_.at(currentColls_.size() - 1)) {
    bxLast   = currentColls_.at(currentColls_.size()-1);
    bxNext   = currentColls_.at(0);
    bxAfter  = bx - bxLast;
    bxBefore = (bx - bxPerOrbit) - bxNext;

    //LogDebug ("StoppedHSCPTreeProducer")  << bx << " : " << bxLast << " : " << bxNext << " : " << bxAfter << " : " << bxBefore;
      }
      // general case
      else {
    for (unsigned c=0; c<(currentColls_.size()-1) && currentColls_.at(c)<bx; ++c) {
      bxLast = currentColls_.at(c);
      bxNext = currentColls_.at(c+1);
      bxAfter = bx - bxLast;
      bxBefore = bx - bxNext;
    }
    //LogDebug ("StoppedHSCPTreeProducer")  << bx << " : " << bxLast << " : " << bxNext << " : " << bxAfter << " : " << bxBefore;
      }
    }
   lifetimeFile << ((bxAfter - 1) * TIME_PER_BX)/TIME_WINDOW << std::endl;
   lifetimeFile << (bxAfter * TIME_PER_BX)/TIME_WINDOW << std::endl;
   std::cout << fill<<bxBefore<< std::endl;
   
   return true;
}

// ------------ method called once each job just before starting event loop  ------------
void 
PrintEventInfo::beginJob()
{
    searchEventFile.open("searchEvents.txt");
    lifetimeFile.open("searchLifetimes.txt");
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PrintEventInfo::endJob() {
    searchEventFile.close();
    lifetimeFile.close();
}

// ------------ method called when starting to processes a run  ------------
/*
void
PrintEventInfo::beginRun(edm::Run const&, edm::EventSetup const&)
{ 
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
PrintEventInfo::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
PrintEventInfo::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
PrintEventInfo::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PrintEventInfo::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(PrintEventInfo);

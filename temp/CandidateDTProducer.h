// -*- C++ -*-
//
// Package:    StoppPtls/Collection
// Class:      CandidateDTProducer
// 
/**\class CandidateDTProducer CandidateDTProducer.cc StoppPtls/Collection/plugins/CandidateDTProducer.cc

 Description: retrive quantities of DTsegments for StoppedParticle analysis

 Implementation:
     Run this producer with RECO input, and produce slimmed output
*/
//
// Original Author:  Weifeng Ji
//         Created:  Fri, 20 Nov 2015 19:41:04 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ESHandle.h"


//
// class declaration
//

class CandidateDTProducer : public edm::EDProducer {
   public:
      explicit CandidateDTProducer(const edm::ParameterSet&);
      ~CandidateDTProducer();

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      
      // ----------member data ---------------------------
      edm::InputTag DTRecHitsTag_;
      edm::InputTag DT4DSegmentsTag_;
};

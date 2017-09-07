#include "IOMC/EventVertexGenerators/interface/StoppedParticleEvtVtxGenerator.h"

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <ios>

#include "HepMC/SimpleVector.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CLHEP/Random/RandFlat.h"
#include "CLHEP/Units/SystemOfUnits.h"
#include "CLHEP/Units/PhysicalConstants.h"

using namespace edm;
using namespace std;
using namespace CLHEP;

StoppedParticleEvtVtxGenerator::StoppedParticleEvtVtxGenerator(const edm::ParameterSet & pset) 
  : BaseEvtVtxGenerator(pset),
    verbose (pset.getUntrackedParameter<bool> ("verbose", false)),
    sourceToken(consumes<edm::HepMCProduct>(pset.getParameter<edm::InputTag>("src"))),
    readFromFile(pset.getUntrackedParameter<bool>("readFromFile", true)),
    fileName (pset.getParameter<std::string>("stoppedData")),
    stoppedParticlesName(consumes<std::vector<std::string> >(pset.getParameter<edm::InputTag>("StoppedParticlesName"))),
    stoppedParticlesX(consumes<std::vector<float> >(pset.getParameter<edm::InputTag>("StoppedParticlesX"))),
    stoppedParticlesY(consumes<std::vector<float> >(pset.getParameter<edm::InputTag>("StoppedParticlesY"))),
    stoppedParticlesZ(consumes<std::vector<float> >(pset.getParameter<edm::InputTag>("StoppedParticlesZ"))),
    stoppedParticlesTime(consumes<std::vector<float> >(pset.getParameter<edm::InputTag>("StoppedParticlesTime"))),
    stoppedParticlesPdgId(consumes<std::vector<int> >(pset.getParameter<edm::InputTag>("StoppedParticlesPdgId"))),
    timeMin (pset.getParameter<double>( "timeOffsetMin") * ns * c_light),
    timeMax (pset.getParameter<double>( "timeOffsetMax") * ns * c_light),
    putTwoStoppedInSameEvent(pset.getUntrackedParameter<bool>("PutTwoStoppedInSameEvent", false)),
    stoppedParticleNumber(pset.getUntrackedParameter<int>("StoppedParticleNumber", 0)),
    nStoppedParticles(0),
    vx_(0.),
    vy_(0.),
    vz_(0.),
    vt_(0.),
    ids_(0.),
    vx(0.),
    vy(0.),
    vz(0.),
    vt(0.),
    id(0.)
{
  LogDebug("StoppedParticleEvtVtxGenerator")<<"begining constructor of StoppedParticleEvtVtxGenerator"<<std::endl;

  if (readFromFile) {
    file = new std::ifstream (fileName.c_str());
  }
}

StoppedParticleEvtVtxGenerator::~StoppedParticleEvtVtxGenerator() {}


void StoppedParticleEvtVtxGenerator::produce(edm::Event& evt, const edm::EventSetup& ) {

  LogDebug("StoppedParticleEvtVtxGenerator")<<"starting produce of StoppedParticleEvtVtxGenerator"<<std::endl;

  edm::Service<RandomNumberGenerator> rng;
  if (!rng.isAvailable()) {
    throw cms::Exception("Configuration")
      << "Attempt to get a random engine when the RandomNumberGeneratorService is not configured.\n"
      "You must configure the service if you want an engine.\n";
  }
  CLHEP::HepRandomEngine* engine = &rng->getEngine(evt.streamID());
  
  LogDebug("StoppedParticleEvtVtxGenerator")<<"starting getStoppingPoint (StoppedParticleEvtVtxGenerator)"<<std::endl;
  getStoppingPoint(evt);

  Handle<HepMCProduct> HepUnsmearedMCEvt ;
  evt.getByToken( sourceToken, HepUnsmearedMCEvt ) ;
  HepMC::GenEvent * myGenEvent = new HepMC::GenEvent(*(HepUnsmearedMCEvt->GetEvent()));
  std::unique_ptr<edm::HepMCProduct> HepMCEvt(new edm::HepMCProduct(myGenEvent));
  
  if (isStoppedEvent) {
    LogDebug("StoppedParticleEvtVtxGenerator")<<"is StoppedEvent (StoppedParticleEvtVtxGenerator)"<<std::endl;

    for(int i=0; i<nStoppedParticles; i++){
      //EITHER: 
      //if there is more than 1 stopped particle, put them in the same event, and loop over all the particles
      //OR
      //if there is more than 1 stopped particle, look only at the one that matches stoppedParticleNumber
      if(putTwoStoppedInSameEvent || (!putTwoStoppedInSameEvent && i==stoppedParticleNumber)) {     
	
	LogDebug("StoppedParticleEvtVtxGenerator")<<"stopped particle #"<<i<<" (StoppedParticleEvtVtxGenerator)"<<std::endl;
	vx = vx_.at(i);
	vy = vy_.at(i);
	vz = vz_.at(i);
	vt = vt_.at(i);
	vt = (vt* ns * c_light) + CLHEP::RandFlat::shoot (engine,timeMin, timeMax);
	id = ids_.at(i);
	LogDebug("StoppedParticleEvtVtxGenerator") << "Vertex : " << vx << '/' << vy << '/' << vz << " cm" << '/' <<vt<< " ns" << std::endl; 

	HepMC::FourVector vtxShift = newVertex(engine);
	
	for ( HepMC::GenEvent::vertex_iterator vtx=myGenEvent->vertices_begin(); vtx!=myGenEvent->vertices_end(); ++vtx ) {
	  LogDebug("StoppedParticleEvtVtxGenerator")<<"loop over vertices initial: "<<(*vtx)->position().x()<<", "<<(*vtx)->position().y()<<", "<<(*vtx)->position().z()<<std::endl;
	  for ( HepMC::GenVertex::particle_iterator pt=(*vtx)->particles_begin(HepMC::ancestors); pt!=(*vtx)->particles_end(HepMC::ancestors); ++pt ) {
	    LogDebug("StoppedParticleEvtVtxGenerator")<<"loop over particles (ancestors): "<<(*pt)->pdg_id()<<std::endl;
	    //if ancestor of particles in vertex has the same pdg_id as the stopped particle (sign correct too),
	    //and if ancestor and stopped particle has the same vertex position,
	    //then shift the vertex
	    if( (*pt)->pdg_id()==id ){
	      if( (*pt)->production_vertex()->position().x()==vx && (*pt)->production_vertex()->position().y()==vy && (*pt)->production_vertex()->position().z()==vz ){
		//shift the vertex (see HepMCProduct::applyVtxGen())
		double x = (*vtx)->position().x() + vtxShift.x();
		double y = (*vtx)->position().y() + vtxShift.y();
		double z = (*vtx)->position().z() + vtxShift.z();
		double t = (*vtx)->position().t() + vtxShift.t();
		(*vtx)->set_position(HepMC::FourVector(x,y,z,t));
		LogDebug("StoppedParticleEvtVtxGenerator")<<"appliedVtxGen for "<<id<<std::endl;
	      }//end of if ancestor and stopped particle vertices match
	    }//end of if ancestor and stopped particle pdgid match
	  }//end of loop over ancestors
	  LogDebug("StoppedParticleEvtVtxGenerator")<<"loop over vertices final: "<<(*vtx)->position().x()<<", "<<(*vtx)->position().y()<<", "<<(*vtx)->position().z()<<std::endl;
	}//end of loop over vertices
      }//end of if put 2 stopped in same event or if decay only 1
    }//end of loop over stopped particles
      
    LogDebug("StoppedParticleEvtVtxGenerator")<<"isVtxGenApplied is: "<<HepMCEvt->isVtxGenApplied()<<", isVtxBoostApplied is: "<<HepMCEvt->isVtxBoostApplied()<<",  isPBoostApplied is: "<<HepMCEvt->isPBoostApplied()<<std::endl;    

    //could simply use applyVtxGen function if there was only 1 stopped particle. if we want to include the possibility of 
    //2 stopped particles, then need to apply separate vertex shifts, as above
    //HepMCEvt->applyVtxGen( newVertex(engine) ) ;

    //since no longer using applyVtxGen, adding a null vertex shift so that HepMCEvt->isVtxGenApplied() returns true
    HepMC::FourVector* const nullVertex = new HepMC::FourVector(0,0,0,0);
    HepMCEvt->applyVtxGen( nullVertex );

    HepMCEvt->boostToLab( GetInvLorentzBoost(), "vertex" );
    HepMCEvt->boostToLab( GetInvLorentzBoost(), "momentum" );

    if(nStoppedParticles == 2){
      const HepMC::GenEvent* mc = HepMCEvt->GetEvent();    
      mc->print(  std::cout );
    }
    
  }//end of if stopped event
  
  //add (modified) HepMCProduct into event (module label: VtxSmeared)
  evt.put(std::move(HepMCEvt));

  LogDebug("StoppedParticleEvtVtxGenerator")<<"ending produce of StoppedParticleEvtVtxGenerator"<<std::endl;
  return ;
  
}

void StoppedParticleEvtVtxGenerator::getStoppingPoint(edm::Event& iEvent) {
  nStoppedParticles = 0;
  isStoppedEvent = false;
  const char *initilize[] = {"none","none","none","none","none"};
  std::vector<std::string> name_(initilize, std::end(initilize));
  vx_={0.,0.,0.,0.,0.};
  vy_={0.,0.,0.,0.,0.};
  vz_={0.,0.,0.,0.,0.};
  vt_={0.,0.,0.,0.,0.};
  ids_={0,0,0,0,0};

  // get stopping point info
  if (readFromFile) {   // read stopping info from file
    
    char buf [1024];
    file->getline (buf, 1023);
    if (!file->good() || buf[0]=='\n') { // end file: rewind
      delete file;
      file = new std::ifstream (fileName.c_str());
      file->getline (buf, 1023);
      if (!file->good() || buf[0]=='\n') { // something wrong
	edm::LogError("StoppedParticles") << "Failed to open stopping points file" << std::endl;
      }
    }
    char nn[32];
    sscanf (buf, "%s %f %f %f", nn, &vx_.at(0), &vy_.at(0), &vz_.at(0));
    name_.at(0) = std::string(nn);
    isStoppedEvent = true;
    nStoppedParticles = 1;
   }
  else {  // or from the event

    edm::Handle<std::vector<std::string> > names;
    iEvent.getByToken (stoppedParticlesName, names);
    edm::Handle<std::vector<float> > xs;
    iEvent.getByToken (stoppedParticlesX, xs);
    edm::Handle<std::vector<float> > ys;
    iEvent.getByToken (stoppedParticlesY, ys);
    edm::Handle<std::vector<float> > zs;
    iEvent.getByToken (stoppedParticlesZ, zs);
    edm::Handle<std::vector<float> > ts;
    iEvent.getByToken (stoppedParticlesTime, ts);
    edm::Handle<std::vector<int> > ids;
    iEvent.getByToken (stoppedParticlesPdgId, ids);

    if (names->size() != xs->size() || xs->size() != ys->size() || ys->size() != zs->size()) {
      edm::LogError ("StoppedParticles") << "mismatch array sizes name/x/y/z:"
				       << names->size() << '/' << xs->size() << '/' << ys->size() << '/' << zs->size()
				       << std::endl;
    }
     else {

       nStoppedParticles = names->size();
       if (nStoppedParticles > 0) {
	 if(putTwoStoppedInSameEvent){ //if there is more than 1 stopped particle, put them in the same event    
	   isStoppedEvent = true;
	   if(nStoppedParticles==1) vt_.at(0) = 0.;
	   else if(nStoppedParticles==2) {
	     double deltaTime = TMath::Abs(ts->at(1)-ts->at(0));
	     if(ts->at(1) > ts->at(0)){
	       vt_.at(0) = 0.;
	       vt_.at(1) = deltaTime;
	     }
	     else{
	       vt_.at(0) = deltaTime;
	       vt_.at(1) = 0.;
	     }
	   }
	   else LogDebug("StoppedParticleEvtVtxGenerator")<<"3 or more stopped particles!!!!!!!!!!!!!!!"<<std::endl;
	 }//end of if put 2 stopped particles in same event
	 else{ //if put 2 stopped particles in separate events
	   for(int i=0; i<nStoppedParticles; i++){
	     if( i==stoppedParticleNumber) {
	       isStoppedEvent = true;
	       break;
	     }
	   }
	   vt_.at(stoppedParticleNumber) = 0.;
	 }
	  
	 for(int i=0; i<nStoppedParticles; i++){
	   //EITHER:
	   //if there is more than 1 stopped particle, put them in the same event, and loop over all the particles
	   //OR
	   //if there is more than 1 stopped particle, look only at the one that matches stoppedParticleNumber
	   if(putTwoStoppedInSameEvent || (!putTwoStoppedInSameEvent && i==stoppedParticleNumber)) {     
	     name_.at(i) = names->at(i);
	     vx_.at(i)  = xs->at(i);
	     vy_.at(i)  = ys->at(i);
	     vz_.at(i)  = zs->at(i);
	     ids_.at(i)  = ids->at(i);
	     LogDebug("StoppedParticleEvtVtxGenerator") << "StoppedParticleEvtVtxGenerator::generateEvent-> name/pid vertex: "
		       << name_.at(i) << '/' << ' '
		       << vx_.at(i) << '/' << vy_.at(i) << '/' << vz_.at(i) <<vt_.at(i)
		       << std::endl;    
	   }//end of if put 2 stopped in same event or if decay only 1
	 }//end of loop over stopped particles	 
       }//end of if nStoppedParticles>0
     }//end of if StoppedParticles arrays match
  }//end of else

}

HepMC::FourVector StoppedParticleEvtVtxGenerator::newVertex(CLHEP::HepRandomEngine* engine) const {

  if (verbose) {
    edm::LogInfo("StoppedParticles") << "Vertex : " << vx << '/' << vy << '/' << vz << " cm, " << vt / (ns * c_light) << " ns" << std::endl; 
  }

  return HepMC::FourVector(vx, vy, vz, vt);
}




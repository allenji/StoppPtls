#ifndef CANDIDATEEVENT_H
#define CANDIDATEEVENT_H

#include "FWCore/Framework/interface/ESHandle.h"

class CandidateEvent
{
 public:
 CandidateEvent():
  bx_(0),
    run_(0),
    fill_(0),
    bxWrtBunch_(0),
    instLumi_(0),
    nVtx_(0),
    l1Jet43NoBptx3BX_BXN2_(0),
    l1Jet43NoBptx3BX_BXN1_(0),
    l1Jet43NoBptx3BX_BX0_(0),
    l1Jet43NoBptx3BX_BXP1_(0),
    l1Jet43NoBptx3BX_BXP2_(0),
    l1Jet46NoBptx3BX_BXN2_(0),
    l1Jet46NoBptx3BX_BXN1_(0),
    l1Jet46NoBptx3BX_BX0_(0),
    l1Jet46NoBptx3BX_BXP1_(0),
    l1Jet46NoBptx3BX_BXP2_(0),
    noiseFilterResult_(0),
    numIsolatedNoiseChannels_(0),
    isolatedNoiseSumE_(0),
    isolatedNoiseSumEt_(0),
    cscTightHaloId2015_(0),
    globalTightHaloId2016_(0),
    globalSuperTightHaloId2016_(0),
    nTowerSameiPhi_(0),
    nTowerSameiRbx_(0),
    nAllTowerSameiPhi_(0),
    maxiEtaDiffSameiRbx_(0),
    nTowerDiffiEtaSameiRbx_(0),
    nTowerDiffRbxDeltaR0p6_(0),
    nTowerDiffRbxDeltaR0p5_(0),
    nTowerDiffRbxDeltaR0p4_(0),
    leadingRbxIndex_(0),
    leadingIPhiFractionValue_(0.),
    topHPD5PeakSample_(0),
    topHPD5Total_(-999.),
    topHPD5R1_(-999.),
    topHPD5R2_(-999.),
    topHPD5RPeak_(-999.),
    topHPD5ROuter_(-999.),
    stoppedParticleName_(""),
    stoppedParticleId_(-999),
    stoppedParticleMass_(-999),
    stoppedParticleCharge_(-999),
    stoppedParticleX_(-999),
    stoppedParticleY_(-999),
    stoppedParticleZ_(-999),
    stoppedParticleR_(-999),
    stoppedParticlePhi_(-999),
    stoppedParticleTime_(-999)
  {}
  public:
    void set_bx(ULong_t bx) {bx_ = bx;}
    void set_run(ULong_t run) {run_ = run;}
    void set_fill(ULong_t fill) {fill_ = fill;}
    void set_bxWrtBunch(int bxWrtBunch) {bxWrtBunch_ = bxWrtBunch;}
    void set_instLumi(double instLumi) {instLumi_ = instLumi;}
    void set_nVtx(unsigned nVtx) {nVtx_ = nVtx;}
    void set_l1Jet43NoBptx3BX_BXN2 (bool l1Jet43NoBptx3BX_BX0) {l1Jet43NoBptx3BX_BX0_ = l1Jet43NoBptx3BX_BX0;}
    void set_l1Jet43NoBptx3BX_BXN1 (bool l1Jet43NoBptx3BX_BX0) {l1Jet43NoBptx3BX_BX0_ = l1Jet43NoBptx3BX_BX0;}
    void set_l1Jet43NoBptx3BX_BX0 (bool l1Jet43NoBptx3BX_BX0) {l1Jet43NoBptx3BX_BX0_ = l1Jet43NoBptx3BX_BX0;}
    void set_l1Jet43NoBptx3BX_BXP1 (bool l1Jet43NoBptx3BX_BX0) {l1Jet43NoBptx3BX_BX0_ = l1Jet43NoBptx3BX_BX0;}
    void set_l1Jet43NoBptx3BX_BXP2 (bool l1Jet43NoBptx3BX_BX0) {l1Jet43NoBptx3BX_BX0_ = l1Jet43NoBptx3BX_BX0;}
    void set_l1Jet46NoBptx3BX_BXN2 (bool l1Jet46NoBptx3BX_BX0) {l1Jet46NoBptx3BX_BX0_ = l1Jet46NoBptx3BX_BX0;}
    void set_l1Jet46NoBptx3BX_BXN1 (bool l1Jet46NoBptx3BX_BX0) {l1Jet46NoBptx3BX_BX0_ = l1Jet46NoBptx3BX_BX0;}
    void set_l1Jet46NoBptx3BX_BX0 (bool l1Jet46NoBptx3BX_BX0) {l1Jet46NoBptx3BX_BX0_ = l1Jet46NoBptx3BX_BX0;}
    void set_l1Jet46NoBptx3BX_BXP1 (bool l1Jet46NoBptx3BX_BX0) {l1Jet46NoBptx3BX_BX0_ = l1Jet46NoBptx3BX_BX0;}
    void set_l1Jet46NoBptx3BX_BXP2 (bool l1Jet46NoBptx3BX_BX0) {l1Jet46NoBptx3BX_BX0_ = l1Jet46NoBptx3BX_BX0;}
    void set_noiseFilterResult(bool noiseFilterResult){noiseFilterResult_ = noiseFilterResult;}
    void set_numIsolatedNoiseChannels(int numIsolatedNoiseChannels){numIsolatedNoiseChannels_ = numIsolatedNoiseChannels;}
    void set_isolatedNoiseSumE(int isolatedNoiseSumE){isolatedNoiseSumE_ = isolatedNoiseSumE;}
    void set_isolatedNoiseSumEt(int isolatedNoiseSumEt){isolatedNoiseSumEt_ = isolatedNoiseSumEt;}

    void set_cscTightHaloId2015(bool cscTightHaloId2015){cscTightHaloId2015_ = cscTightHaloId2015;}

    void set_globalTightHaloId2016(bool globalTightHaloId2016){globalTightHaloId2016_ = globalTightHaloId2016;}
    void set_globalSuperTightHaloId2016(bool globalSuperTightHaloId2016){globalSuperTightHaloId2016_ = globalSuperTightHaloId2016;}
    void set_nTowerSameiPhi(unsigned nTowerSameiPhi) {nTowerSameiPhi_ = nTowerSameiPhi;}
    void set_nTowerSameiRbx(unsigned nTowerSameiRbx) {nTowerSameiRbx_ = nTowerSameiRbx;}
    void set_nAllTowerSameiPhi(unsigned nAllTowerSameiPhi) {nAllTowerSameiPhi_ = nAllTowerSameiPhi;}
    void set_maxiEtaDiffSameiRbx(int maxiEtaDiffSameiRbx) {maxiEtaDiffSameiRbx_ = maxiEtaDiffSameiRbx;}
    void set_nTowerDiffiEtaSameiRbx(unsigned nTowerDiffiEtaSameiRbx) {nTowerDiffiEtaSameiRbx_ = nTowerDiffiEtaSameiRbx;}
    void set_nTowerDiffRbxDeltaR0p6(int nTowerDiffRbxDeltaR0p6) {nTowerDiffRbxDeltaR0p6_ = nTowerDiffRbxDeltaR0p6;}
    void set_nTowerDiffRbxDeltaR0p5(int nTowerDiffRbxDeltaR0p5) {nTowerDiffRbxDeltaR0p5_ = nTowerDiffRbxDeltaR0p5;}
    void set_nTowerDiffRbxDeltaR0p4(int nTowerDiffRbxDeltaR0p4) {nTowerDiffRbxDeltaR0p4_ = nTowerDiffRbxDeltaR0p4;}
    void set_leadingRbxIndex(int leadingRbxIndex) {leadingRbxIndex_ = leadingRbxIndex;}
    void set_leadingIPhiFractionValue(double leadingIPhiFractionValue) {leadingIPhiFractionValue_ = leadingIPhiFractionValue;}
    void increment_nTowerSameiPhi() {++nTowerSameiPhi_;}
    void increment_nTowerSameiRbx() {++nTowerSameiRbx_;}
    void increment_nAllTowerSameiPhi() {++nAllTowerSameiPhi_;}
    
    void set_topHPD5PeakSample(unsigned topHPD5PeakSample) {topHPD5PeakSample_ = topHPD5PeakSample;}
    void set_topHPD5Total(double topHPD5Total) {topHPD5Total_ = topHPD5Total;}
    void set_topHPD5R1(double topHPD5R1) {topHPD5R1_ = topHPD5R1;}
    void set_topHPD5R2(double topHPD5R2) {topHPD5R2_ = topHPD5R2;}
    void set_topHPD5RPeak(double topHPD5RPeak) {topHPD5RPeak_ = topHPD5RPeak;}
    void set_topHPD5ROuter(double topHPD5ROuter) {topHPD5ROuter_ = topHPD5ROuter;}

    void set_stoppedParticleName(std::string stoppedParticleName) {stoppedParticleName_ = stoppedParticleName;}
    void set_stoppedParticleId(int stoppedParticleId) {stoppedParticleId_ = stoppedParticleId;}
    void set_stoppedParticleMass(float stoppedParticleMass) {stoppedParticleMass_ = stoppedParticleMass;}
    void set_stoppedParticleCharge(float stoppedParticleCharge) {stoppedParticleCharge_ = stoppedParticleCharge;}
    void set_stoppedParticleX(float stoppedParticleX) {stoppedParticleX_ = stoppedParticleX;}
    void set_stoppedParticleY(float stoppedParticleY) {stoppedParticleY_ = stoppedParticleY;}
    void set_stoppedParticleZ(float stoppedParticleZ) {stoppedParticleZ_ = stoppedParticleZ;}
    void set_stoppedParticleR(float stoppedParticleR) {stoppedParticleR_ = stoppedParticleR;}
    void set_stoppedParticlePhi(float stoppedParticlePhi) {stoppedParticlePhi_ = stoppedParticlePhi;}
    void set_stoppedParticleTime(float stoppedParticleTime) {stoppedParticleTime_ = stoppedParticleTime;}

    ULong_t bx() const {return bx_;}
    ULong_t run() const {return run_;}
    ULong_t fill() const {return fill_;}

    int bxWrtBunch() {return bxWrtBunch_;}

    double instLumi() const {return instLumi_;}

    unsigned nVtx() {return nVtx_;}

    bool l1Jet43NoBptx3BX_BXN2() {return l1Jet43NoBptx3BX_BXN2_;}
    bool l1Jet43NoBptx3BX_BXN1() {return l1Jet43NoBptx3BX_BXN1_;}
    bool l1Jet43NoBptx3BX_BX0() {return l1Jet43NoBptx3BX_BX0_;}
    bool l1Jet43NoBptx3BX_BXP1() {return l1Jet43NoBptx3BX_BXP1_;}
    bool l1Jet43NoBptx3BX_BXP2() {return l1Jet43NoBptx3BX_BXP2_;}
    bool l1Jet46NoBptx3BX_BXN2() {return l1Jet46NoBptx3BX_BXN2_;}
    bool l1Jet46NoBptx3BX_BXN1() {return l1Jet46NoBptx3BX_BXN1_;}
    bool l1Jet46NoBptx3BX_BX0() {return l1Jet46NoBptx3BX_BX0_;}
    bool l1Jet46NoBptx3BX_BXP1() {return l1Jet46NoBptx3BX_BXP1_;}
    bool l1Jet46NoBptx3BX_BXP2() {return l1Jet46NoBptx3BX_BXP2_;}


    bool noiseFilterResult() {return noiseFilterResult_;}

    int numIsolatedNoiseChannels() {return numIsolatedNoiseChannels_;}
    double isolatedNoiseSumE() {return isolatedNoiseSumE_;}
    double isolatedNoiseSumEt() {return isolatedNoiseSumEt_;}

    bool cscTightHaloId2015() {return cscTightHaloId2015_;}
    bool globalTightHaloId2016() {return globalTightHaloId2016_;}
    bool globalSuperTightHaloId2016() {return globalSuperTightHaloId2016_;}

    unsigned nTowerSameiPhi() {return nTowerSameiPhi_;}
    unsigned nTowerSameiRbx() {return nTowerSameiRbx_;}
    unsigned nAllTowerSameiPhi() {return nAllTowerSameiPhi_;}
    int maxiEtaDiffSameiRbx() {return maxiEtaDiffSameiRbx_;}
    unsigned nTowerDiffiEtaSameiRbx() {return nTowerDiffiEtaSameiRbx_;}
    int nTowerDiffRbxDeltaR0p6() {return nTowerDiffRbxDeltaR0p6_;}
    int nTowerDiffRbxDeltaR0p5() {return nTowerDiffRbxDeltaR0p5_;}
    int nTowerDiffRbxDeltaR0p4() {return nTowerDiffRbxDeltaR0p4_;}
    int leadingRbxIndex() {return leadingRbxIndex_;}
    double leadingIPhiFractionValue() {return leadingIPhiFractionValue_;}

    unsigned topHPD5PeakSample() {return topHPD5PeakSample_;}
    double topHPD5Total() {return topHPD5Total_;}
    double topHPD5R1() {return topHPD5R1_;}
    double topHPD5R2() {return topHPD5R2_;}
    double topHPD5RPeak() {return topHPD5RPeak_;}
    double topHPD5ROuter() {return topHPD5ROuter_;}
    
    std::string stoppedParticleName() const {return stoppedParticleName_;}
    int stoppedParticleId() const {return stoppedParticleId_;}
    float stoppedParticleMass() const {return stoppedParticleMass_;}
    float stoppedParticleCharge() const {return stoppedParticleCharge_;}
    float stoppedParticleX() const {return stoppedParticleX_/10.;} //convert mm to cm
    float stoppedParticleY() const {return stoppedParticleY_/10.;}
    float stoppedParticleZ() const {return stoppedParticleZ_/10.;}
    float stoppedParticleR() const {return stoppedParticleR_/10.;}
    float stoppedParticlePhi() const {return stoppedParticlePhi_;}
    float stoppedParticleTime() const {return stoppedParticleTime_;}


  private:
    // event info
    /*unsigned id;
    unsigned bx;
    unsigned orbit;
    unsigned lb;
    unsigned run;*/
    ULong_t bx_;
    ULong_t run_;
    ULong_t fill_;
    int bxWrtBunch_;
    double instLumi_;

    //number of vertex
    unsigned nVtx_;
    bool l1Jet43NoBptx3BX_BXN2_;
    bool l1Jet43NoBptx3BX_BXN1_;
    bool l1Jet43NoBptx3BX_BX0_;
    bool l1Jet43NoBptx3BX_BXP1_;
    bool l1Jet43NoBptx3BX_BXP2_;
    bool l1Jet46NoBptx3BX_BXN2_;
    bool l1Jet46NoBptx3BX_BXN1_;
    bool l1Jet46NoBptx3BX_BX0_;
    bool l1Jet46NoBptx3BX_BXP1_;
    bool l1Jet46NoBptx3BX_BXP2_;

    //noise
    bool noiseFilterResult_;

    int numIsolatedNoiseChannels_;
    double isolatedNoiseSumE_;
    double isolatedNoiseSumEt_;
    
    bool cscTightHaloId2015_;
    bool globalTightHaloId2016_;
    bool globalSuperTightHaloId2016_;
    //gobal calo
    unsigned nTowerSameiPhi_;
    unsigned nTowerSameiRbx_;
    unsigned nAllTowerSameiPhi_;
    int maxiEtaDiffSameiRbx_;
    unsigned nTowerDiffiEtaSameiRbx_;
    int nTowerDiffRbxDeltaR0p6_;
    int nTowerDiffRbxDeltaR0p5_;
    int nTowerDiffRbxDeltaR0p4_;
    int leadingRbxIndex_;
    double leadingIPhiFractionValue_;


    //bool noiseFilterResult_;

    // NoiseSummary pulse shape variables
    unsigned topHPD5PeakSample_;
    double   topHPD5Total_;
    double   topHPD5R1_;
    double   topHPD5R2_;
    double   topHPD5RPeak_;
    double   topHPD5ROuter_;

    std::string stoppedParticleName_;
    int stoppedParticleId_;
    float stoppedParticleMass_;
    float stoppedParticleCharge_;
    float stoppedParticleX_;
    float stoppedParticleY_;
    float stoppedParticleZ_;
    float stoppedParticleR_;
    float stoppedParticlePhi_;
    float stoppedParticleTime_;

};

#endif

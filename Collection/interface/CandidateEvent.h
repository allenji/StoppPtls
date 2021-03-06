#ifndef CANDIDATEEVENT_H
#define CANDIDATEEVENT_H
class CandidateEvent
{
 public:
 CandidateEvent():
  bx_(0),
    run_(0),
    fill_(0),
    bxWrtBunch_(0),
    nVtx_(0),
    noiseFilterResult_(0),
    nTowerSameiPhi_(0),
    leadingIPhiFractionValue_(0.),
    topHPD5PeakSample_(0),
    topHPD5Total_(-999.),
    topHPD5R1_(-999.),
    topHPD5R2_(-999.),
    topHPD5RPeak_(-999.),
    topHPD5ROuter_(-999.),
    stoppedParticleName_(""),
    stoppedParticleId_(-999),
    stoppedParticleMass_(-999.),
    stoppedParticleCharge_(-999.),
    stoppedParticleX_(-999.),
    stoppedParticleY_(-999.),
    stoppedParticleZ_(-999.),
    stoppedParticleR_(-999.),
    stoppedParticlePhi_(-999.),
    stoppedParticleTime_(-999.)
  {}
  public:
    void set_bx(ULong_t bx) {bx_ = bx;}
    void set_run(ULong_t run) {run_ = run;}
    void set_fill(ULong_t fill) {fill_ = fill;}
    void set_bxWrtBunch(int bxWrtBunch) {bxWrtBunch_ = bxWrtBunch;}
    void set_nVtx(unsigned nVtx) {nVtx_ = nVtx;}
    void set_noiseFilterResult(bool noiseFilterResult){noiseFilterResult_ = noiseFilterResult;}
    void set_nTowerSameiPhi(unsigned nTowerSameiPhi) {nTowerSameiPhi_ = nTowerSameiPhi;}
    void set_leadingIPhiFractionValue(double leadingIPhiFractionValue) {leadingIPhiFractionValue_ = leadingIPhiFractionValue;}
    void increment_nTowerSameiPhi() {++nTowerSameiPhi_;}
    
    void set_topHPD5PeakSample(unsigned topHPD5PeakSample) {topHPD5PeakSample_ = topHPD5PeakSample;}
    void set_topHPD5Total(double topHPD5Total) {topHPD5Total_ = topHPD5Total;}
    void set_topHPD5R1(double topHPD5R1) {topHPD5R1_ = topHPD5R1;}
    void set_topHPD5R2(double topHPD5R2) {topHPD5R2_ = topHPD5R2;}
    void set_topHPD5RPeak(double topHPD5RPeak) {topHPD5RPeak_ = topHPD5RPeak;}
    void set_topHPD5ROuter(double topHPD5ROuter) {topHPD5ROuter_ = topHPD5ROuter;}

    void set_stoppedParticleName(std::string stoppedParticleName) {stoppedParticleName_ = stoppedParticleName;}
    void set_stoppedParticleId(int stoppedParticleId) {stoppedParticleId_ = stoppedParticleId;}
    void set_stoppedParticleMass(double stoppedParticleMass) {stoppedParticleMass_ = stoppedParticleMass;}
    void set_stoppedParticleCharge(double stoppedParticleCharge) {stoppedParticleCharge_ = stoppedParticleCharge;}
    void set_stoppedParticleX(double stoppedParticleX) {stoppedParticleX_ = stoppedParticleX;}
    void set_stoppedParticleY(double stoppedParticleY) {stoppedParticleY_ = stoppedParticleY;}
    void set_stoppedParticleZ(double stoppedParticleZ) {stoppedParticleZ_ = stoppedParticleZ;}
    void set_stoppedParticleR(double stoppedParticleR) {stoppedParticleR_ = stoppedParticleR;}
    void set_stoppedParticlePhi(double stoppedParticlePhi) {stoppedParticlePhi_ = stoppedParticlePhi;}
    void set_stoppedParticleTime(double stoppedParticleTime) {stoppedParticleTime_ = stoppedParticleTime;}

    ULong_t bx() const {return bx_;}
    ULong_t run() const {return run_;}
    ULong_t fill() const {return fill_;}

    int bxWrtBunch() {return bxWrtBunch_;}

    unsigned nVtx() {return nVtx_;}

    bool noiseFilterResult() {return noiseFilterResult_;}

    unsigned nTowerSameiPhi() {return nTowerSameiPhi_;}
    double leadingIPhiFractionValue() {return leadingIPhiFractionValue_;}

    unsigned topHPD5PeakSample() {return topHPD5PeakSample_;}
    double topHPD5Total() {return topHPD5Total_;}
    double topHPD5R1() {return topHPD5R1_;}
    double topHPD5R2() {return topHPD5R2_;}
    double topHPD5RPeak() {return topHPD5RPeak_;}
    double topHPD5ROuter() {return topHPD5ROuter_;}
    
    std::string stoppedParticleName() const {return stoppedParticleName_;}
    int stoppedParticleId() const {return stoppedParticleId_;}
    double stoppedParticleMass() const {return stoppedParticleMass_;}
    double stoppedParticleCharge() const {return stoppedParticleCharge_;}
    double stoppedParticleX() const {return 1.0*stoppedParticleX_/10;} //convert mm to cm
    double stoppedParticleY() const {return 1.0*stoppedParticleY_/10;}
    double stoppedParticleZ() const {return 1.0*stoppedParticleZ_/10;}
    double stoppedParticleR() const {return 1.0*stoppedParticleR_/10;}
    double stoppedParticlePhi() const {return stoppedParticlePhi_;}
    double stoppedParticleTime() const {return stoppedParticleTime_;}


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

    //number of vertex
    unsigned nVtx_;

    //noise
    bool noiseFilterResult_;
    //gobal calo
    unsigned nTowerSameiPhi_;
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
    double stoppedParticleMass_;
    double stoppedParticleCharge_;
    double stoppedParticleX_;
    double stoppedParticleY_;
    double stoppedParticleZ_;
    double stoppedParticleR_;
    double stoppedParticlePhi_;
    double stoppedParticleTime_;

};

#endif

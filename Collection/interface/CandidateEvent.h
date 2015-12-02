#ifndef CANDIDATEEVENT_H
#define CANDIDATEEVENT_H
class CandidateEvent
{
  public:
    CandidateEvent():nTowerSameiPhi_(0) {}
  public:
    void set_nTowerSameiPhi(unsigned nTowerSameiPhi) {nTowerSameiPhi_ = nTowerSameiPhi;}
    //void set_leadingIPhiFractionValue(double leadingIPhiFractionValue) {leadingIPhiFractionValue_ = leadingIPhiFractionValue;}
    void increment_nTowerSameiPhi() {++nTowerSameiPhi_;}

    unsigned nTowerSameiPhi() {return nTowerSameiPhi_;}
    //double leadingIPhiFractionValue() {return leadingIPhiFractionValue_;}


  private:
    unsigned nTowerSameiPhi_;
    //double leadingIPhiFractionValue_;


    /*bool noiseFilterResult_;

    // NoiseSummary pulse shape variables
    unsigned topHPD5PeakSample_;
    double   topHPD5Total_;
    double   topHPD5R1_;
    double   topHPD5R2_;
    double   topHPD5RPeak_;
    double   topHPD5ROuter_;*/

};

#endif

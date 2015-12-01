#ifndef CANDIDATEEVENT_H
#define CANDIDATEEVENT_H
class CandidateEvent
{

  private:
    ULong_t id_;
    ULong_t bx_;
    ULong_t orbit_;
    ULong_t lb_;
    ULong_t run_;
    ULong_t fill_;
    ULong_t fillFromL1_;
    ULong64_t time_;   // timestamp from EvF
    ULong64_t time2_;  // calculated from run start + L1 counters for LS, orbit, BX
    ULong64_t time3_;  // timestamp from LHC info in L1 data
    Long_t bxAfterCollision_;
    Long_t bxBeforeCollision_;
    Long_t bxWrtCollision_;
    Long_t bxAfterBunch_;
    Long_t bxBeforeBunch_;
    Long_t bxWrtBunch_;
    //global calo quantities
    unsigned nTowerSameiPhi_;
    double leadingIPhiFractionValue_;

    bool noiseFilterResult_;

    // NoiseSummary pulse shape variables
    std::vector<double> topHPD5TimeSamples;
    unsigned topHPD5PeakSample_;
    double   topHPD5Total_;
    double   topHPD5R1_;
    double   topHPD5R2_;
    double   topHPD5RPeak_;
    double   topHPD5ROuter_;

};

#endif

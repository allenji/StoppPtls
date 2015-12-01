#ifndef CANDIDATECSCSEG_H
#define CANDIDATECSCSEG_H
class CandidateCscSeg {
  public:
    void set_endcap(int endcap) {endcap_ = endcap;}
    void set_ring(int ring) {ring_ = ring;}
    void set_station(int station) {station_ = station;}
    void set_chamber(int chamber) {chamber_ = chamber;}
    void set_nHits(int nHits) {nHits_ = nHits;}
    void set_phi(double phi) {phi_ = phi;}
    void set_z(double z) {z_ = z;}
    void set_r(double r) {r_ = r;}
    void set_dirPhi(double dirPhi) {dirPhi_ = dirPhi;}
    void set_dirTheta(double dirTheta) {dirTheta_ = dirTheta;}
    void set_time(double time) {time_ = time;}

    const int endcap() const {return endcap_;}
    const int ring() const {return ring_;}
    const int station() const {return station_;}
    const int chamber() const {return chamber_;}
    const int nHits() const {return nHits_;}
    const double phi() const {return phi_;}
    const double z() const {return z_;}
    const double r() const {return r_;}
    const double dirPhi() const {return dirPhi_;}
    const double dirTheta() const {return dirTheta_;}
    const double time() const {return time_;}

  private:
    int endcap_;
    int ring_;
    int station_;
    int chamber_;
    int nHits_;
    double phi_;
    double z_;
    double r_;
    double dirPhi_;
    double dirTheta_;
    double time_;
};
#endif//CANDIDATECSCSEG_H
    

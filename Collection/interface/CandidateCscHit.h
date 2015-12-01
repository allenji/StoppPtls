#ifndef CANDIDATECSCHIT_H
#define CANDIDATECSCHIT_H
class CandidateCscHit {
  public:
    void set_z(double z) {z_ = z;}
    void set_rho(double rho) {rho_ = rho;}
    void set_phi(double phi) {phi_ = phi;}
    void set_time(double time) {time_ = time;}
    const double z() const {return z_;}
    const double rho() const {return rho_;}
    const double phi() const {return phi_;}
    const double time() const {return time_;}
  private:
    double z_;
    double rho_;
    double phi_;
    double time_;
};
#endif //CANDIDATECSCHIT_H

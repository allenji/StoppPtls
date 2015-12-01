#ifndef CANDIDATERPCHIT_H
#define CANDIDATERPCHIT_H
class CandidateRpcHit {
  public:
    void set_x(double x) {x_ = x;}
    void set_y(double y) {y_ = y;}
    void set_r(double r) {r_ = r;}
    void set_z(double z) {z_ = z;}
    void set_rho(double rho) {rho_ = rho;}
    void set_phi(double phi) {phi_ = phi;}
    void set_region(int region) {region_ = region;}

    const double x() const {return x_;}
    const double y() const {return y_;}
    const double z() const {return z_;}
    const double r() const {return r_;}
    const double rho() const {return rho_;}
    const double phi() const {return phi_;}
    const int region() const {return region_;}
  private:
    double x_;
    double y_;
    double r_;
    double z_;
    double rho_;
    double phi_;
    int region_;
};
#endif //CANDIDATERPCHIT_H

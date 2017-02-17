#ifndef CANDIDATEDTSEG_H
#define CANDIDATEDTSEG_H

class CandidateDTSeg
{
  public:
    void set_wheel(int wheel) {wheel_ = wheel;}
    void set_station(int station) {station_ = station;}
    void set_sector(int sector) {sector_ = sector;}
    void set_localX(double localX) {localX_ = localX;}
    void set_localY(double localY) {localY_ = localY;}
    void set_x(double x) {x_ = x;}
    void set_y(double y) {y_ = y;}
    void set_r(double r) {r_ = r;}
    void set_z(double z) {z_ = z;}
    void set_rho(double rho) {rho_ = rho;}
    void set_phi(double phi) {phi_ = phi;}
    void set_xdir(double xdir) {xdir_ = xdir;}
    void set_ydir(double ydir) {ydir_ = ydir;}
    void set_phidir(double phidir) {phidir_ = phidir;}
    void set_zdir(double zdir) {zdir_ = zdir;}
    void set_nPhiHits(double nPhiHits) {nPhiHits_ = nPhiHits;}
    void set_nZHits(double nZHits) {nZHits_ = nZHits;}
    void set_nHits(double nHits) {nHits_ = nHits;}

    const int wheel () const {return wheel_;}
    const int station () const {return station_;}
    const int sector () const {return sector_;}
    const double localX () const {return localX_;}
    const double localY () const {return localY_;}
    const double x () const {return x_;}
    const double y () const {return y_;}
    const double r () const {return r_;}
    const double z () const {return z_;}
    const double rho () const {return rho_;}
    const double phi () const {return phi_;}
    const double xdir () const {return xdir_;}
    const double ydir () const {return ydir_;}
    const double phidir () const {return phidir_;}
    const double zdir () const {return zdir_;}
    const int nPhiHits () const {return nPhiHits_;}
    const int nZHits () const {return nZHits_;}
    const int nHits() const {return nHits_;}

  private:
    int wheel_;
    int station_;
    int sector_;
    double localX_;
    double localY_;
    double x_;
    double y_;
    double r_;
    double z_;
    double rho_;
    double phi_;
    double xdir_;
    double ydir_;
    double phidir_;
    double zdir_;
    int nPhiHits_;
    int nZHits_;
    int nHits_;

};
#endif//CANDIDATEDTSEG_H

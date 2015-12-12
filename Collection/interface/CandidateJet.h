#ifndef CANDIDATEJET_H 
#define CANDIDATEJET_H 
class CandidateJet {
  public:
    void set_energy(double energy) {energy_ = energy;}
    void set_et(double et) {et_ = et;}
    void set_eta(double eta) {eta_ = eta;}
    void set_phi(double phi) {phi_ = phi;}
    void set_n60(double n60) {n60_ = n60;}
    void set_n90(double n90) {n90_ = n90;}

    const double energy() const {return energy_;}
    const double et() const {return et_;}
    const double eta() const {return eta_;}
    const double phi() const {return phi_;}
    const double n60() const {return n60_;}
    const double n90() const {return n90_;}
  private:
    double energy_;
    double et_;
    double eta_;
    double phi_;
    double n60_;
    double n90_;
};


#endif



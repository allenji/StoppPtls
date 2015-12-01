#include "StoppPtls/Collection/interface/CandidateDT.h"

CandidateDT::CandidateDT ():
  wheel_      (0),
  station_    (0),
  sector_     (0),
  localX_     (0.),
  localY_     (0.),
  x_          (0.),
  y_          (0.),
  r_          (0.),
  z_          (0.),
  rho_        (0.),
  phi_        (0.),
  xdir_       (0.),
  ydir_       (0.),
  phidir_     (0.),
  zdir_       (0.)
{

}

CandidateDT::CandidateDT (const DTChamber *&dc, const LocalPoint &lp, const GlobalPoint &gp, const GlobalVector &gv) :
  wheel_      ((dc->id()).wheel()),
  station_    ((dc->id()).station()),
  sector_     ((dc->id()),sector()),
  localX_     (lp.x()),
  localY_     (lp.y()),
  x_          (gp.x()),
  y_          (gp.y()),
  r_          (sqrt(gp.x()*gp.x() + gp.y()*gp.y())),
  z_          (gp.z()),
  rho_        (gp.perp()),
  phi_        (gp.phi()),
  xdir_       (gv.x()),
  ydir_       (gv.y()),
  phidir_     (gv.phi()),
  zdir_       (gv.z())
{
}

CandidateDT::~CandidateDT ()
{
}

import ROOT
import ROOT.ROOT as rr

##############################################################################################

find_idx_code ='''
using namespace ROOT::VecOps;
std::vector<int> find_idx(const RVec<int> &charge, const RVec<double> &phi, const RVec<double> &eta)
{
    std::vector<int> idx {-1,-1,-1};
    
    if(charge[0]==charge[1] && charge[1]!=charge[2]){
        
        idx[0] = 2;
        
        double dr_1 = DeltaR(eta[1], eta[2], phi[1], phi[2]);
        double dr_2 = DeltaR(eta[0], eta[2], phi[0], phi[2]);
        
        if(dr_1 < dr_2){
            idx[1] = 1;
            idx[2] = 0;
        }else{
            idx[1] = 0;
            idx[2] = 1;     
        }
      }
      
    if(charge[0]!=charge[1] && charge[1]!=charge[2]){
          
        idx[0] = 1;
        
        double dr_1 = DeltaR(eta[1], eta[2], phi[1], phi[2]);
        double dr_2 = DeltaR(eta[0], eta[1], phi[0], phi[1]);
        
        if(dr_1 < dr_2){
            idx[1] = 2;
            idx[2] = 0;
        }else{
            idx[1] = 0;
            idx[2] = 2;     
        }
      }
    
    if(charge[0]!=charge[1] && charge[1]==charge[2]){
          
          idx[0] = 0;
          
        double dr_1 = DeltaR(eta[0], eta[2], phi[0], phi[2]);
        double dr_2 = DeltaR(eta[0], eta[1], phi[0], phi[1]);
        
        if(dr_1 < dr_2){
            idx[1] = 2;
            idx[2] = 1;
        }else{
            idx[1] = 1;
            idx[2] = 2;     
        }
      }
      
    return idx;
};
'''

ROOT.gInterpreter.Declare(find_idx_code)

##############################################################################################

compute_m_code = '''
auto compute_m(const float &p1, const float &p2, const float &phi1, const float &phi2, const float &eta1, const float &eta2)
{
    //const auto dphi = Helper::DeltaPhi(phi1, phi2);
    return std::sqrt(2.0 * p1 * p2 * (std::cosh(eta1-eta2) - std::cos(phi1-phi2)));
};
'''

ROOT.gInterpreter.Declare(compute_m_code)

##############################################################################################

InvMass2_code = '''
using namespace ROOT::VecOps;

auto InvMass2(const float &p1, const float &p2, const float &phi1, const float &phi2, const float &eta1, const float &eta2, const float &m1, const float &m2)
{
    RVec<float> p = {p1, p2};
    RVec<float> eta = {eta1, eta2};
    RVec<float> phi = {phi1, phi2};
    RVec<float> mass = {m1, m2};

    return InvariantMass(p, eta, phi, mass);
};
'''

ROOT.gInterpreter.Declare(InvMass2_code)

##############################################################################################

InvMass3_code = '''
using namespace ROOT::VecOps;

auto InvMass3(const RVec<float> &p, const RVec<float> &phi, const RVec<float> &eta, const RVec<float> &m)
{
    return InvariantMass(p, eta, phi, m);
};
'''

ROOT.gInterpreter.Declare(InvMass3_code)

##############################################################################################

dR_code = '''
using namespace ROOT::VecOps;

auto dR(const float &eta1, const float &eta2, const float &phi1, const float &phi2)
{
    return DeltaR(eta1, eta2, phi1, phi2);
};
'''

ROOT.gInterpreter.Declare(dR_code)

##############################################################################################

# Zcandidate_code = '''
# using namespace ROOT::VecOps;

# auto Zcandidate(const float &inv_m01, const float &inv_m02)
# {
#     return InvariantMass(p, eta, phi, m);
# };
# '''

# ROOT.gInterpreter.Declare(Zcandidate_code)

##############################################################################################
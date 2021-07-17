import ROOT
import ROOT.ROOT as rr
import cpp

dirOutPath = '/data/Skim/'

# - Dictionary for iSkim variables and labels #####################################

default_nbins = 30

SkimRanges = {
     1 : 
                {'Muon_pt15':(default_nbins, 0, 200),
                 'lep_pt0': (default_nbins, 0, 200),
                 'lep_pt1': (default_nbins, 0, 200),
                 'max_eta': (default_nbins, 0, 4),
                 'lep_eta0': (default_nbins, -4, 4),
                 'lep_eta1': (default_nbins, -4, 4),
                 'inv_m': (default_nbins, 0, 200),
                 'MET_pt': (default_nbins, 0, 200),
                 'dRHJ': (default_nbins, 0, 4),
                 'dRLJ': (default_nbins, 0, 4),
                 'dRLep': (default_nbins, 0, 4),
                 'ST': (default_nbins, 0, 2000),
                 'dPhi0': (default_nbins, -4, 4),
                 'dPhi1': (default_nbins, -4, 4),},
    2 : 
                {'Muon_pt15':(default_nbins, 0, 200),
                 'lep_pt0': (default_nbins, 0, 200),
                 'lep_pt1': (default_nbins, 0, 200),
                 'max_eta': (default_nbins, 0, 4),
                 'lep_eta0': (default_nbins, -4, 4),
                 'lep_eta1': (default_nbins, -4, 4),
                 'inv_m': (default_nbins, 0, 200),
                 'MET_pt': (default_nbins, 0, 200),
                 'dRHJ': (default_nbins, 0, 4),
                 'dRLJ': (default_nbins, 0, 4),
                 'dRLep': (default_nbins, 0, 4),
                 'ST': (default_nbins, 0, 2000),
                 'dPhi0': (default_nbins, -4, 4),
                 'dPhi1': (default_nbins, -4, 4),},
    3 :
                {'Muon_pt15':(default_nbins, 0, 200),
                 'lep_pt0': (default_nbins, 0, 200),
                 'lep_pt1': (default_nbins, 0, 200),
                 'lep_pt2': (default_nbins, 0, 200),
                 'lep_eta0': (default_nbins, -4, 4),
                 'lep_eta1': (default_nbins, -4, 4),
                 'lep_eta2': (default_nbins, -4, 4),
                 'inv_m01': (default_nbins, 0, 200),
                 'inv_m12': (default_nbins, 0, 200),
                 'inv_m02': (default_nbins, 0, 200),   
                 'inv_m3': (default_nbins, 0, 300),
                 'ST': (default_nbins, 200, 2000),
                 'Jet_pt0': (default_nbins, 0, 200),
                 'Jet_pt1': (default_nbins, 0, 200),
                 'bJet_pt0': (default_nbins, 0, 200),
                 'MET_pt': (default_nbins, 0, 200),
                 'dPhi0': (default_nbins, -4, 4),
                 'dPhi1': (default_nbins, -4, 4),
                 'dPhi2': (default_nbins, -4, 4),
                 'dR01' : (default_nbins, 0, 4),
                 'dR02' : (default_nbins, 0, 4),
                 'dR1J' : (default_nbins, 0, 4),
                 'dR0bJ' : (default_nbins, 0, 4),},  
    4 :
                {'Muon_pt15':(default_nbins, 0, 200),
                 'lep_pt0': (default_nbins, 0, 200),
                 'lep_pt1': (default_nbins, 0, 200),
                 'lep_pt2': (default_nbins, 0, 200),
                 'lep_eta0': (default_nbins, -4, 4),
                 'lep_eta1': (default_nbins, -4, 4),
                 'lep_eta2': (default_nbins, -4, 4),
                 'inv_m01': (default_nbins, 0, 200),
                 'inv_m12': (default_nbins, 0, 200),
                 'inv_m02': (default_nbins, 0, 200),   
                 'inv_m3': (default_nbins, 0, 300),
                 'ST': (default_nbins, 200, 2000),
                 'Jet_pt0': (default_nbins, 0, 200),
                 'Jet_pt1': (default_nbins, 0, 200),
                 'bJet_pt0': (default_nbins, 0, 200),
                 'MET_pt': (default_nbins, 0, 200),
                 'dPhi0': (default_nbins, -4, 4),
                 'dPhi1': (default_nbins, -4, 4),
                 'dPhi2': (default_nbins, -4, 4),
                 'dR01' : (default_nbins, 0, 4),
                 'dR02' : (default_nbins, 0, 4),
                 'dR1J' : (default_nbins, 0, 4),
                 'dR0bJ' : (default_nbins, 0, 4),}
        }

SkimLabels = { 
    1 : 
                {'Muon_pt15': 'Muon p_{T} 15 / GeV',
                 'lep_pt0': 'Muon p^{T}_{0} / GeV',
                 'lep_pt1': 'Muon p^{T}_{1} / GeV',
                 'max_eta': '#eta_{max}',
                 'lep_eta0': '#eta_{l_{0}}',
                 'lep_eta1': '#eta_{l_{1}}',
                 'inv_m': 'm_{inv} / GeV',
                 'MET_pt': 'E_{miss} / GeV',
                 'dRHJ': 'dRHJ',
                 'dRLJ': 'dRLJ',
                 'dRLep': 'dRLep',
                 'ST': 'ST',
                 'dPhi0': '#Delta#phi_{0}',
                 'dPhi1': '#Delta#phi_{1}',},
    2 : 
                {'Muon_pt15': 'Muon p_{T} 15 / GeV',
                 'lep_pt0': 'Muon p_{T} / GeV',
                 'lep_pt1': 'Electron p_{T} / GeV',
                 'max_eta': '#eta_{max}',
                 'lep_eta0': '#eta_{l_{0}}',
                 'lep_eta1': '#eta_{l_{1}}',
                 'inv_m': 'm_{inv} / GeV',
                 'MET_pt': 'E_{miss}',
                 'dRHJ': 'dRHJ',
                 'dRLJ': 'dRLJ',
                 'dRLep': 'dRLep',
                 'ST': 'ST',
                 'dPhi0': '#Delta#phi_{0}',
                 'dPhi1': '#Delta#phi_{1}',},
    
    3 :
                {'Muon_pt15': 'Muon p_{T} 15 / GeV',
                'lep_pt0': 'Muon p^{T}_{0} / GeV',
                'lep_pt1': 'Muon p^{T}_{1} / GeV',
                'lep_pt2': 'Muon p^{T}_{2} / GeV',
                'lep_eta0': '#eta_{l_{0}}',
                'lep_eta1': '#eta_{l_{1}}',
                'lep_eta2': '#eta_{l_{2}}',
                'inv_m01': 'm_{inv} 01 / GeV',
                'inv_m12': 'm_{inv} 12 / GeV',
                'inv_m02': 'm_{inv} 02 / GeV',
                'inv_m3': 'm_{inv} 3 / GeV',
                'ST': 'ST',
                'Jet_pt0': 'Jet p_{T}',
                'Jet_pt1': 'Jet p_{T}',
                'bJet_pt0': 'b-Jet p_{T}',
                'MET_pt': 'Missing E / GeV',
                'dPhi0': '#Delta#phi_{0}',   
                'dPhi1': '#Delta#phi_{1}',   
                'dPhi2': '#Delta#phi_{2}',
                'dR01' : 'dR01',
                'dR02' : 'dR02',
                'dR1J' : 'dR1J',
                'dR0bJ' : 'dR0bJ',},
    4 :
                {'Muon_pt15': 'Muon p_{T} 15 / GeV',
                'lep_pt0': 'Lepton p_{T} / GeV',
                'lep_pt1': 'Lepton p_{T} / GeV',
                'lep_pt2': 'Lepton p_{T} / GeV',
                'lep_eta0': '#eta_{l_{0}}',
                'lep_eta1': '#eta_{l_{1}}',
                'lep_eta2': '#eta_{l_{2}}',
                'inv_m01': 'm_{inv} 01 / GeV',
                'inv_m12': 'm_{inv} 12 / GeV',
                'inv_m02': 'm_{inv} 02 / GeV',
                'inv_m3': 'm_{inv} 3 / GeV',
                'ST': 'ST',
                'Jet_pt0': 'Jet p_{T}',
                'Jet_pt1': 'Jet p_{T}',
                'bJet_pt0': 'b-Jet p_{T}',
                'MET_pt': 'E_{miss} / GeV',
                'dPhi0': '#Delta#phi_{0}',   
                'dPhi1': '#Delta#phi_{1}',   
                'dPhi2': '#Delta#phi_{2}',
                'dR01' : 'dR01',
                'dR02' : 'dR02',
                'dR1J' : 'dR1J',
                'dR0bJ' : 'dR0bJ',}
        }

                #'di_Jet_invm': 'di_Jet_invm',}

# - iSkim1 ########################################################################
def FSkim1(df):
    fdf = df.Filter('iSkim == 1', 'iSkim1')\
            .Define('maskMu', 'Muon_pfRelIso03_all < 0.15 && Muon_pt > 15 && abs(Muon_eta)<2.5')\
            .Define('nGoodMu', 'Sum(maskMu)')\
            .Define('Muon_pt15', 'Muon_pt[maskMu]')\
            .Define('maskEl', 'Electron_pfRelIso03_all < 0.15')\
            .Define('nGoodEl', 'Sum(maskEl)')\
            .Filter('nGoodMu == 2 && nGoodEl == 0', 'GoodEvent')\
            .Define('maskJpt','Jet_pt>30')\
            .Define('maskJClean', 'prod(maskJpt, cleanJ(Jet_eta, Muon_eta[maskMu], Jet_phi, Muon_phi[maskMu]))')\
            .Define('maskBjet', 'Jet_btagDeepB > 0.6')\
            .Define('nJClean', 'Sum(maskJClean)')\
            .Define('maskBJClean', 'prod(maskJClean,maskBjet)')\
            .Define('nBJ', 'Sum(maskBJClean)')\
            .Filter('nJClean >= 4 && nBJ > 0 && nBJ < 2', 'GoodJet') 
            
    return fdf
# .Filter('nCleanJet >= 4 && nBJet > 0 && nBJet <= 2', 'GoodJet')

# - iSkim2 ########################################################################
def FSkim2(df):
    fdf = df.Filter('iSkim == 2', 'iSkim2')\
            .Define('maskMu', 'Muon_pfRelIso03_all < 0.1 && Muon_pt > 27 && abs(Muon_eta)<2.4')\
            .Define('nGoodMu', 'Sum(maskMu)')\
            .Define('Muon_pt15', 'Muon_pt[maskMu]')\
            .Define('maskEl', 'Electron_pfRelIso03_all < 0.1 && Electron_pt > 20 && abs(Electron_eta)<2.4 \
                     && Electron_cutBased>2')\
            .Define('nGoodEl', 'Sum(maskEl)')\
            .Define('Electron_pt15', 'Electron_pt[maskEl]')\
            .Filter('nGoodMu == 1 && nGoodEl == 1', 'GoodEvent')\
            .Define('maskJpt','Jet_pt>30')\
            .Define('maskJClean', 'prod(maskJpt, cleanJ(Jet_eta, Merge(Muon_eta[maskMu], Electron_eta[maskEl]),\
                    Jet_phi,Merge(Muon_phi[maskMu], Electron_phi[maskEl])))')\
            .Define('maskBjet', 'Jet_btagDeepB > 0.6')\
            .Define('nJClean', 'Sum(maskJClean)')\
            .Define('maskBJClean', 'prod(maskJClean,maskBjet)')\
            .Define('nBJ', 'Sum(maskBJClean)')\
            .Filter('nJClean >= 4 && nBJ > 0 && nBJ <= 2', 'GoodJet')
            
    return fdf
#.Filter('nCleanJet >= 4 && nBJet > 0 && nBJet <= 2', 'GoodJet')\

# - iSkim3 ########################################################################
def FSkim3(df):
    fdf = df.Filter('iSkim == 3', 'iSkim3')\
            .Define('maskMu', 'Muon_pfRelIso03_all < 0.15 && Muon_pt > 15 && abs(Muon_eta)<2.5')\
            .Define('nGoodMu', 'Sum(maskMu)')\
            .Define('maskEl', 'Electron_pfRelIso03_all < 0.15')\
            .Define('nGoodEl', 'Sum(maskEl)')\
            .Filter('nGoodMu == 3 && nGoodEl == 0', 'GoodEvent')\
            .Filter('abs(Sum(Muon_charge[maskMu])) != 3', 'GoodCharge')\
            .Define('Muon_pt15', 'Muon_pt[maskMu]')\
            .Define('maskJpt','Jet_pt>30')\
            .Define('maskJClean', 'prod(maskJpt, cleanJ(Jet_eta, Muon_eta[maskMu], Jet_phi, Muon_phi[maskMu]))')\
            .Define('maskBjet', 'Jet_btagDeepB > 0.6')\
            .Define('nJClean', 'Sum(maskJClean)')\
            .Define('maskBJClean', 'prod(maskJClean,maskBjet)')\
            .Define('nBJ', 'Sum(maskBJClean)')\
            .Filter('nJClean >= 2 && nBJ >= 1', 'GoodJet')
    
    return fdf
#.Filter('nCleanJet >= 2 && nBJet >= 1', 'GoodJet')\

# - iSkim4 ########################################################################
def FSkim4(df):
    fdf = df.Filter('iSkim == 4', 'iSkim4')\
            .Define('maskMu', 'Muon_pfRelIso03_all < 0.15 && Muon_pt > 15 && abs(Muon_eta)<2.5')\
            .Define('nGoodMu', 'Sum(maskMu)')\
            .Define('Muon_pt15', 'Muon_pt[maskMu]')\
            .Define('maskEl', 'Electron_pfRelIso03_all < 0.15 && Electron_pt > 15 && abs(Electron_eta)<2.5')\
            .Define('nGoodEl', 'Sum(maskEl)')\
            .Define('Electron_pt15', 'Electron_pt[maskEl]')\
            .Filter('nGoodMu == 2 && nGoodEl == 1', 'GoodEvent')\
            .Define('ChargeMus', 'Muon_charge[maskMu][0] * Muon_charge[maskMu][1]')\
            .Filter('ChargeMus < 0', 'GoodCharge')\
            .Define('maskJpt','Jet_pt>30')\
            .Define('maskJClean', 'prod(maskJpt, cleanJ(Jet_eta, Merge(Muon_eta[maskMu], Electron_eta[maskEl]),\
                    Jet_phi,Merge(Muon_phi[maskMu], Electron_phi[maskEl])))')\
            .Define('maskBjet', 'Jet_btagDeepB > 0.6')\
            .Define('nJClean', 'Sum(maskJClean)')\
            .Define('maskBJClean', 'prod(maskJClean,maskBjet)')\
            .Define('nBJ', 'Sum(maskBJClean)')\
            .Filter('nJClean >= 2 && nBJ >= 1', 'GoodJet')
            
    return fdf
#.Filter('nCleanJet >= 2 && nBJet >= 1', 'GoodJet')\

# - iSkim dictionary ##############################################################

FSkim ={1 : FSkim1, 2 : FSkim2, 3 : FSkim3, 4 : FSkim4}

# - Declare Variables ####################################################################

def DeclareVariables1(df, title, save=True):
    finalVariables1 = {'lep_mass0','lep_mass1','max_eta','lep_eta1',
                       'inv_m','dRHJ','dRLJ','dRLep','dPhi0','dPhi1','eventWeightLumi'}
    
    define =  FSkim1(df).Define('lep_pt0', 'Muon_pt[maskMu][0]')\
                        .Define('lep_pt1', 'Muon_pt[maskMu][1]')\
                        .Define('lep_eta0', 'Muon_eta[maskMu][0]')\
                        .Define('lep_eta1', 'Muon_eta[maskMu][1]')\
                        .Define('max_eta', 'max(abs(lep_eta0), abs(lep_eta1))')\
                        .Define('lep_phi0', 'Muon_phi[maskMu][0]')\
                        .Define('lep_phi1', 'Muon_phi[maskMu][1]')\
                        .Define('lep_mass0', '0.1057')\
                        .Define('lep_mass1', '0.1057')\
                        .Define('lep_q0', 'Muon_charge[maskMu][0]')\
                        .Define('lep_q1', 'Muon_charge[maskMu][1]')\
                        .Define('inv_m', 'InvMass2(lep_pt0, lep_pt1, lep_eta0, lep_eta1, lep_phi0, lep_phi1, lep_mass0, lep_mass1)')\
                        .Filter('inv_m > 15', 'GoodMass')\
                        .Filter('!(abs(inv_m - 91.2) < 10 && lep_q0 * lep_q1 < 0)', 'rmZ')\
                        .Define('dRHJ', 'closest_Jet(Jet_eta[maskJClean],lep_eta0,Jet_phi[maskJClean],lep_phi0)')\
                        .Define('dRLJ', 'closest_Jet(Jet_eta[maskJClean],lep_eta1,Jet_phi[maskJClean],lep_phi1)')\
                        .Define('dRLep', 'dR(lep_eta0, lep_eta1, lep_phi0, lep_phi1)')\
                        .Define('ST', 'lep_pt0 + lep_pt1 + Sum(Jet_pt[maskJClean]) + MET_pt')\
                        .Define('dPhi0', 'dPhi(MET_phi, lep_phi0)')\
                        .Define('dPhi1', 'dPhi(MET_phi, lep_phi1)')\
                        .Define('notBJet','prod(maskJClean, (-1*maskBJClean)+1)')\
                        .Define('di_Jet_invm', 'diJ_invm(Jet_pt[notBJet], Jet_eta[notBJet], Jet_phi[notBJet],\
                                Jet_mass[notBJet])')\
                        .Filter('lep_q0 * lep_q1 > 0', 'ss')
    
    if save: define.Snapshot('Events', dirOutPath + title + 'Flat1.root', finalVariables1)
    
    return define

##############################################################################################

def DeclareVariables2(df, title, save=True):
    finalVariables2 = {'lep_mass0','lep_mass1','max_eta','lep_eta1',
                       'inv_m','dRHJ','dRLJ','dRLep','dPhi0','dPhi1','eventWeightLumi'}

    define =  FSkim2(df).Define('lep_pt0', 'Muon_pt[maskMu][0]')\
                        .Define('lep_pt1', 'Electron_pt[maskEl][0]')\
                        .Define('lep_eta0', 'Muon_eta[maskMu][0]')\
                        .Define('lep_eta1', 'Electron_eta[maskEl][0]')\
                        .Define('max_eta', 'max(abs(lep_eta0), abs(lep_eta1))')\
                        .Define('lep_phi0', 'Muon_phi[maskMu][0]')\
                        .Define('lep_phi1', 'Electron_phi[maskEl][0]')\
                        .Define('lep_mass0', '0.1057')\
                        .Define('lep_mass1', '0.000511')\
                        .Define('lep_q0', 'Muon_charge[maskMu][0]')\
                        .Define('lep_q1', 'Electron_charge[maskEl][0]')\
                        .Define('inv_m', 'InvMass2(lep_pt0, lep_pt1, lep_eta0, lep_eta1, lep_phi0, lep_phi1,\
                                lep_mass0,lep_mass1)')\
                        .Filter('inv_m > 15', 'GoodMass')\
                        .Define('maxELepton', 'higherELepton(Merge(Muon_pt[maskMu],Electron_pt[maskEl]),Merge(Muon_eta[maskMu],\
                                Electron_eta[maskEl]),Merge(Muon_phi[maskMu], Electron_phi[maskEl]))')\
                        .Define('minELepton', 'higherELepton(Merge(Muon_pt[maskMu],Electron_pt[maskEl]),Merge(Muon_eta[maskMu],\
                                Electron_eta[maskEl]),Merge(Muon_phi[maskMu], Electron_phi[maskEl]), 1)')\
                        .Define('dRHJ', 'closest_Jet(Jet_eta[maskJClean],maxELepton[0],Jet_phi[maskJClean],maxELepton[1])')\
                        .Define('dRLJ', 'closest_Jet(Jet_eta[maskJClean],minELepton[0],Jet_phi[maskJClean],minELepton[1])')\
                        .Define('dRLep', 'dR(lep_eta0, lep_eta1, lep_phi0, lep_phi1)')\
                        .Define('ST', 'lep_pt0 + lep_pt1 + Sum(Jet_pt[maskJClean]) + MET_pt')\
                        .Define('dPhi0', 'dPhi(MET_phi, lep_phi0)')\
                        .Define('dPhi1', 'dPhi(MET_phi, lep_phi1)')\
                        .Define('notBJet','prod(maskJClean, (-1*maskBJClean)+1)')\
                        .Define('di_Jet_invm', 'diJ_invm(Jet_pt[notBJet], Jet_eta[notBJet], Jet_phi[notBJet],\
                                Jet_mass[notBJet])')\
                        .Filter('lep_q0 * lep_q1 > 0', 'ss')
                        
    if save: define.Snapshot('Events', dirOutPath + title + 'Flat2.root', finalVariables2)
    
    return define

##############################################################################################

def DeclareVariables3(df, title, save=True):
    finalVariables3 = {'lep_pt0','lep_mass0','lep_mass1','lep_mass2','inv_m01','lep_eta1','lep_eta2',
                       'inv_m12','inv_m02','dR1J','dR0bJ','dR01','dR02','dPhi0','dPhi1','dPhi2','eventWeightLumi'}

    define =  FSkim3(df).Define('lep_idx', 'find_idx(Muon_charge[maskMu], Muon_phi[maskMu], Muon_eta[maskMu])')\
                        .Define('lep_pt0', 'Muon_pt[maskMu][lep_idx[0]]')\
                        .Define('lep_pt1', 'Muon_pt[maskMu][lep_idx[1]]')\
                        .Define('lep_pt2', 'Muon_pt[maskMu][lep_idx[2]]')\
                        .Define('lep_eta0', 'Muon_eta[maskMu][lep_idx[0]]')\
                        .Define('lep_eta1', 'Muon_eta[maskMu][lep_idx[1]]')\
                        .Define('lep_eta2', 'Muon_eta[maskMu][lep_idx[2]]')\
                        .Define('lep_phi0', 'Muon_phi[maskMu][lep_idx[0]]')\
                        .Define('lep_phi1', 'Muon_phi[maskMu][lep_idx[1]]')\
                        .Define('lep_phi2', 'Muon_phi[maskMu][lep_idx[2]]')\
                        .Define('lep_mass0', '0.1057')\
                        .Define('lep_mass1', '0.1057')\
                        .Define('lep_mass2', '0.1057')\
                        .Define('lep_q0', 'Muon_charge[maskMu][lep_idx[0]]')\
                        .Define('lep_q1', 'Muon_charge[maskMu][lep_idx[1]]')\
                        .Define('lep_q2', 'Muon_charge[maskMu][lep_idx[2]]')\
                        .Define('inv_m01', 'InvMass2(lep_pt0, lep_pt1, lep_eta0, lep_eta1, lep_phi0, lep_phi1,\
                                lep_mass0,lep_mass1)')\
                        .Define('inv_m12', 'InvMass2(lep_pt1, lep_pt2, lep_eta1, lep_eta2, lep_phi1, lep_phi2,\
                                lep_mass1,lep_mass2)')\
                        .Define('inv_m02', 'InvMass2(lep_pt0, lep_pt2, lep_eta0, lep_eta2, lep_phi0, lep_phi2,\
                                lep_mass0, lep_mass2)')\
                        .Define('inv_m3', 'InvMass3(Muon_pt[maskMu], Muon_eta[maskMu], Muon_phi[maskMu],\
                                RVec<float>({0.1057,0.1057,0.1057}))')\
                        .Filter('inv_m01 > 15')\
                        .Filter('inv_m02 > 15')\
                        .Filter('inv_m12 > 15')\
                        .Filter('abs(inv_m01 - 91.2) > 10 && abs(inv_m02 - 91.2) > 10', 'rmZ')\
                        .Define('dR01', 'dR(lep_eta0, lep_eta1, lep_phi0, lep_phi1)')\
                        .Define('dR02', 'dR(lep_eta0, lep_eta2, lep_phi0, lep_phi2)')\
                        .Define('Jet_pt0', 'Jet_pt[maskJClean][0]')\
                        .Define('Jet_pt1', 'Jet_pt[maskJClean][1]')\
                        .Define('bJet_pt0', 'Jet_pt[maskBJClean][0]')\
                        .Define('dR1J', 'closest_Jet(Jet_eta[maskJClean],lep_eta1,Jet_phi[maskJClean],lep_phi1)')\
                        .Define('dR0bJ', 'closest_Jet(Jet_eta[maskBJClean],lep_eta0,Jet_phi[maskBJClean],lep_phi0)')\
                        .Define('ST', 'lep_pt0 + lep_pt1  + lep_pt2 + Sum(Jet_pt[maskJClean]) + MET_pt')\
                        .Define('dPhi0', 'dPhi(MET_phi, lep_phi0)')\
                        .Define('dPhi1', 'dPhi(MET_phi, lep_phi1)')\
                        .Define('dPhi2', 'dPhi(MET_phi, lep_phi2)')\
                        .Define('notBJet','prod(maskJClean, (-1*maskBJClean)+1)')\
                        .Define('di_Jet_invm', 'diJ_invm(Jet_pt[notBJet], Jet_eta[notBJet], Jet_phi[notBJet],\
                                Jet_mass[notBJet])')
    
    if save: define.Snapshot('Events', dirOutPath + title + 'Flat3.root', finalVariables3)
    
    return define

#.Filter('abs(inv_m02 - 91.2) > 10', 'other Z contamination with one lepton not reconstructed')\
#.Define('WJ','abs(di_Jet_invm - 80) < 5')\
#.Filter('Sum(WJ) < 1', 'cutting W')

##############################################################################################

def DeclareVariables4(df, title, save=True):    
    finalVariables4 = {'lep_pt0','lep_mass0','lep_mass1','lep_mass2','inv_m01','lep_eta1','lep_eta2',
                       'inv_m12','inv_m02','dR1J','dR0bJ','dR01','dR02','dPhi0','dPhi1','dPhi2','eventWeightLumi'}

    define =  FSkim4(df).Define('lep_pt', 'Merge(Muon_pt[maskMu], Electron_pt[maskEl])')\
                        .Define('lep_eta', 'Merge(Muon_eta[maskMu], Electron_eta[maskEl])')\
                        .Define('lep_phi', 'Merge(Muon_phi[maskMu], Electron_phi[maskEl])')\
                        .Define('lep_mass', 'RVec<float> {0.1057, 0.1057, 0.000511}')\
                        .Define('lep_charge', 'Merge(Muon_charge[maskMu], Electron_charge[maskEl])')\
                        .Define('lep_idx', 'find_idx(lep_charge, lep_phi, lep_eta)')\
                        .Define('lep_pt0', 'lep_pt[lep_idx[0]]')\
                        .Define('lep_pt1', 'lep_pt[lep_idx[1]]')\
                        .Define('lep_pt2', 'lep_pt[lep_idx[2]]')\
                        .Define('lep_eta0', 'lep_eta[lep_idx[0]]')\
                        .Define('lep_eta1', 'lep_eta[lep_idx[1]]')\
                        .Define('lep_eta2', 'lep_eta[lep_idx[2]]')\
                        .Define('lep_phi0', 'lep_phi[lep_idx[0]]')\
                        .Define('lep_phi1', 'lep_phi[lep_idx[1]]')\
                        .Define('lep_phi2', 'lep_phi[lep_idx[2]]')\
                        .Define('lep_mass0', 'lep_mass[lep_idx[0]]')\
                        .Define('lep_mass1', 'lep_mass[lep_idx[1]]')\
                        .Define('lep_mass2', 'lep_mass[lep_idx[2]]')\
                        .Define('lep_q0', 'lep_charge[lep_idx[0]]')\
                        .Define('lep_q1', 'lep_charge[lep_idx[1]]')\
                        .Define('lep_q2', 'lep_charge[lep_idx[2]]')\
                        .Define('inv_m01', 'InvMass2(lep_pt0, lep_pt1, lep_eta0, lep_eta1, lep_phi0, lep_phi1, lep_mass0,\
                        lep_mass1)')\
                        .Define('inv_m12', 'InvMass2(lep_pt1, lep_pt2, lep_eta1, lep_eta2, lep_phi1, lep_phi2, lep_mass1,\
                        lep_mass2)')\
                        .Define('inv_m02', 'InvMass2(lep_pt0, lep_pt2, lep_eta0, lep_eta2, lep_phi0, lep_phi2, lep_mass0,\
                        lep_mass2)')\
                        .Define('inv_m3', 'InvMass3(lep_pt, lep_eta, lep_phi, lep_mass)')\
                        .Filter('inv_m01 > 15')\
                        .Filter('inv_m02 > 15')\
                        .Filter('inv_m12 > 15')\
                        .Filter('abs(inv_m01 - 91.2) > 10 && abs(inv_m02 - 91.2) > 10', 'rmZ')\
                        .Define('dR01', 'dR(lep_eta0, lep_eta1, lep_phi0, lep_phi1)')\
                        .Define('dR02', 'dR(lep_eta0, lep_eta2, lep_phi0, lep_phi2)')\
                        .Define('Jet_pt0', 'Jet_pt[maskJClean][0]')\
                        .Define('Jet_pt1', 'Jet_pt[maskJClean][1]')\
                        .Define('bJet_pt0', 'Jet_pt[maskBJClean][0]')\
                        .Define('dR1J', 'closest_Jet(Jet_eta[maskJClean],lep_eta1,Jet_phi[maskJClean],lep_phi1)')\
                        .Define('dR0bJ', 'closest_Jet(Jet_eta[maskBJClean],lep_eta0,Jet_phi[maskBJClean],lep_phi0)')\
                        .Define('ST', 'lep_pt0 + lep_pt1  + lep_pt2 + Sum(Jet_pt[maskJClean]) + MET_pt')\
                        .Define('dPhi0', 'dPhi(MET_phi, lep_phi0)')\
                        .Define('dPhi1', 'dPhi(MET_phi, lep_phi1)')\
                        .Define('dPhi2', 'dPhi(MET_phi, lep_phi2)')\
                        .Define('notBJet','prod(maskJClean, (-1*maskBJClean)+1)')\
                        .Define('di_Jet_invm', 'diJ_invm(Jet_pt[notBJet], Jet_eta[notBJet], Jet_phi[notBJet],\
                                Jet_mass[notBJet])')\
                        .Filter('!TMath::IsNaN(inv_m12)', 'NaNCut')
    
    if save: define.Snapshot('Events', dirOutPath + title + 'Flat4.root', finalVariables4)
    
    return define

##############################################################################################

DeclareVariables = {1 : DeclareVariables1, 2 : DeclareVariables2, 3 : DeclareVariables3, 4 : DeclareVariables4}
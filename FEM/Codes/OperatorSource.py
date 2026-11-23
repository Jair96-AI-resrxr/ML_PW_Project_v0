import numpy as np
from Parameters import dof_node
from NShiEtaElement import Nfunc
from DetJacobian import detJ
from HeatSource import HeatSource

def SourceTerm(l, xvec, yvec, shi, eta):
    x = 0.0
    y = 0.0
    for i in range(len(xvec)):
        x += Nfunc(i, shi, eta) * xvec[i]
        y += Nfunc(i, shi, eta) * yvec[i]

    Q = HeatSource(x, y)
    
    vec = np.zeros(dof_node)
    vec[0] = Nfunc(l, shi, eta)
    vec[0] = Q * detJ(xvec, yvec, shi, eta) * vec[0]
    return vec
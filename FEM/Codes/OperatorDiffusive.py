import numpy as np
from Parameters import dof_node, k_diffusive
from NShiEtaElement import Nfunc
from LaplacianOperator import OperatorL
from DetJacobian import detJ

def DiffusiveTerm(l, m, xvec, yvec, shi, eta):
    Laplacian_Nl = OperatorL(l, xvec, yvec, shi, eta)
    Laplacian_Nm = OperatorL(m, xvec, yvec, shi, eta)

    Nl = Nfunc(l, shi, eta)
    Nm = Nfunc(m, shi, eta)
    NlNm = Nl * Nm

    mat = k_diffusive * np.matmul(np.transpose(Laplacian_Nl), Laplacian_Nm) * detJ(xvec, yvec, shi, eta)

    return mat

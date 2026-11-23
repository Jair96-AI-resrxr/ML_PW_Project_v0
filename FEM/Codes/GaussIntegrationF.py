import numpy as np
from Parameters import e_type, dof_node
from CuadraturePoints import GaussPoints
from OperatorSource import SourceTerm


def CuadratureGaussF(l, xvec, yvec):

    # gaussk --> Cuadrature Gauss integration of the diffusive term
    # gaussf --> Cuadrature Gauss integration of the source term
    # a --> Second sub-index of l
    # b --> Second sub-index of m

    shi, eta, w = GaussPoints()
    p = len(shi)

    gaussf = np.zeros(dof_node)

    if e_type == 1:  # Triangle

        for i in range(p):
            vectorSource = SourceTerm(l, xvec, yvec, shi[i], eta[i])

            gaussf = gaussf + 0.5 * w[i] * vectorSource

    elif e_type == 2:  # Quadrangule

        for i in range(p):
            for j in range(p):
                vectorSource = SourceTerm(l, xvec, yvec, shi[i], eta[j])

                gaussf = gaussf + w[i] * w[j] * vectorSource

    return gaussf

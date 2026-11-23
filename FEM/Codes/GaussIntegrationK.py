import numpy as np
from Parameters import e_type, dof_node
from CuadraturePoints import GaussPoints
from OperatorDiffusive import DiffusiveTerm


def CuadratureGaussK(l, m, xvec, yvec):

    # gaussk --> Cuadrature Gauss integration of the diffusive term
    # gaussf --> Cuadrature Gauss integration of the source term
    # a --> Second sub-index of l
    # b --> Second sub-index of m

    shi, eta, w = GaussPoints()
    p = len(shi)

    gaussk = np.zeros((dof_node, dof_node))

    if e_type == 1:  # Triangle

        for i in range(p):
            matrixDiffusiveTerm = DiffusiveTerm(
                l, m, xvec, yvec, shi[i], eta[i]
            )

            gaussk = gaussk + 0.5 * w[i] * matrixDiffusiveTerm

    elif e_type == 2:  # Quadrangule

        for i in range(p):
            for j in range(p):
                matrixDiffusiveTerm = DiffusiveTerm(
                    l, m, xvec, yvec, shi[i], eta[j]
                )

                gaussk = gaussk + w[i] * w[j] * matrixDiffusiveTerm

    return gaussk
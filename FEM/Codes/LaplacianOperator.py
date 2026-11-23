import numpy as np
from DerivativesDiffusive import dxydshieta
from dNdShiElement import dNdshi
from dNdEtaElement import dNdeta
from DetJacobian import detJ


def OperatorL(n, xvec, yvec, shi, eta):

    dxdshi = dxydshieta(0, xvec, shi, eta)
    dxdeta = dxydshieta(1, xvec, shi, eta)

    dydshi = dxydshieta(0, yvec, shi, eta)
    dydeta = dxydshieta(1, yvec, shi, eta)

    dNdx = dydeta * dNdshi(n, shi, eta) - dydshi * dNdeta(n, shi, eta)
    dNdy = -dxdeta * dNdshi(n, shi, eta) + dxdshi * dNdeta(n, shi, eta)

    Laplacian_N = np.zeros((2, 1))

    Laplacian_N[0, 0] = dNdx / detJ(xvec, yvec, shi, eta)
    Laplacian_N[1, 0] = dNdy / detJ(xvec, yvec, shi, eta)

    return Laplacian_N

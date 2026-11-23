from Derivatives import dxydshieta

def detJ(xvec, yvec, shi, eta):

    dxdshi = dxydshieta(0, xvec, shi, eta)
    dxdeta = dxydshieta(1, xvec, shi, eta)

    dydshi = dxydshieta(0, yvec, shi, eta)
    dydeta = dxydshieta(1, yvec, shi, eta)

    detJ = dxdshi * dydeta - dxdeta * dydshi

    if detJ < 0.0:
        raise ValueError("warning: DetJ < 0")

    return detJ

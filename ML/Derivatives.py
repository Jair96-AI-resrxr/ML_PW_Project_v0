from NShiEta import dNdshi
from NShiEta import dNdeta


def dxydshieta(n, cvec, shi, eta):
    dxydshieta = 0.0
    # ci cj ck --> coordenada x o y
    # n=1 --> dxdshi o dydshi
    # n=2 --> dxdeta o dydeta

    if n == 0:
        for i in range(len(cvec)):
            dxydshieta += cvec[i] * dNdshi(i, shi, eta)

    else:
        for i in range(len(cvec)):
            dxydshieta += cvec[i] * dNdeta(i, shi, eta)

    return dxydshieta
def Nfunc(n, shi, eta):
    #Base functions for an unitary Triangle
    if n == 0:
        Nfunc = shi
    elif n == 1:
        Nfunc = eta
    else:
        Nfunc = 1.0 - shi - eta
    return Nfunc


def dNdshi(n, shi, eta):
    # Derivatives with respect to shi of the base functions for an unitary Triangle
    if n == 0:
        dNdshi = 1.0
    elif n == 1:
        dNdshi = 0.0
    else:
        dNdshi = -1.0
    return dNdshi


def dNdeta(n, shi, eta):
    # Derivatives with respect to eta of the base functions for an unitary Triangle
    if n == 0:
        dNdeta = 0.0
    elif n == 1:
        dNdeta = 1.0
    else:
        dNdeta = -1.0
    return dNdeta
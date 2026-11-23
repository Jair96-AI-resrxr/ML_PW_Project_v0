from Parameters import e_type
from CuadraturePoints import GaussPoints
from NShiEtaElement import Nfunc
from DetJacobian import detJ

def Average(xvec, yvec, fi_element):

    shi, eta, w = GaussPoints()
    p = len(shi)
    mean_phi = 0.0

    if e_type == 1:  # Triangle

        for g in range(p):
            phi = 0.0

            for a in range(len(fi_element)):
                phi += 0.5 * Nfunc(a, shi[g], eta[g]) * fi_element[a] * detJ(xvec, yvec, shi[g], eta[g])

            mean_phi += w[g] * phi

    elif e_type == 2:  # Square

        for i in range(p):
            for j in range(p):

                phi = 0.0

                for a in range(len(fi_element)):
                    phi += Nfunc(a, shi[i], eta[j]) * fi_element[a] * detJ(xvec, yvec, shi[i], eta[j])

                mean_phi += w[i] * w[j] * phi

    return mean_phi
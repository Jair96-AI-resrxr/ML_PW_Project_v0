from Parameters import e_type
from CuadraturePoints import GaussPoints
from DetJacobian import detJ

def Area(xvec, yvec):
    shi, eta, w = GaussPoints()
    p = len(shi)
    area = 0

    if e_type == 1:  # Triangle

        for g in range(p):
            area += 0.5 * w[g] * detJ(xvec, yvec, shi[g], eta[g])

    elif e_type == 2:  # Square

        for i in range(p):
            for j in range(p):
                area += w[i] * w[j] * detJ(xvec, yvec, shi[i], eta[j])

    return area
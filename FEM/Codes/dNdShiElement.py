from Parameters import e_type, order


def dNdshi(n, shi, eta):

    if e_type == 1:

        # Derivatives with respect to shi of the base functions for an unitary Triangle
        if order == 1:
            if n == 0:
                dNdshi = 1.0
            elif n == 1:
                dNdshi = 0.0
            else:
                dNdshi = -1.0

        elif order == 2:
            if n == 0:
                dNdshi = (4.0 * shi) - 1.0
            elif n == 1:
                dNdshi = 0.0
            elif n == 2:
                dNdshi = -3.0 + 4.0 * eta + 4.0 * shi
            elif n == 3:
                dNdshi = 4.0 * eta
            elif n == 4:
                dNdshi = -4.0 * eta
            else:
                dNdshi = 4.0 - 4.0 * eta - 8.0 * shi

    elif e_type == 2:

        # Derivatives with respect to shi of the base functions for an unitary Square
        if order == 1:
            if n == 0:
                dNdshi = -0.25 * (1.0 - eta)
            elif n == 1:
                dNdshi = 0.25 * (1.0 - eta)
            elif n == 2:
                dNdshi = 0.25 * (1.0 + eta)
            else:
                dNdshi = -0.25 * (1.0 + eta)

        elif order == 2:
            if n == 0:
                dNdshi = 0.25 * eta * (eta - 1.0) * ((2.0 * shi) - 1.0)
            elif n == 1:
                dNdshi = 0.25 * eta * (eta - 1.0) * ((2.0 * shi) + 1.0)
            elif n == 2:
                dNdshi = 0.25 * eta * (eta + 1.0) * ((2.0 * shi) + 1.0)
            elif n == 3:
                dNdshi = 0.25 * eta * (eta + 1.0) * ((2.0 * shi) - 1.0)
            elif n == 4:
                dNdshi = -shi * eta * (eta - 1.0)
            elif n == 5:
                dNdshi = -0.5 * ((2.0 * shi) + 1.0) * (eta**2.0 - 1.0)
            elif n == 6:
                dNdshi = -shi * eta * (eta + 1.0)
            elif n == 7:
                dNdshi = -0.5 * (eta**2.0 - 1.0) * ((2.0 * shi) - 1.0)
            else:
                dNdshi = 2.0 * shi * (eta**2.0 - 1.0)

    return dNdshi
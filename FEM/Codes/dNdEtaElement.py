from Parameters import e_type, order

def dNdeta(n, shi, eta):

    if e_type == 1:

        # Derivatives with respect to eta of the base functions for an unitary Triangle
        if order == 1:
            if n == 0:
                dNdeta = 0.0
            elif n == 1:
                dNdeta = 1.0
            else:
                dNdeta = -1.0

        elif order == 2:
            if n == 0:
                dNdeta = 0.0
            elif n == 1:
                dNdeta = (4.0 * eta) - 1.0
            elif n == 2:
                dNdeta = -3.0 + 4.0 * shi + 4.0 * eta
            elif n == 3:
                dNdeta = 4.0 * shi
            elif n == 4:
                dNdeta = 4.0 - 8.0 * eta - 4.0 * shi
            else:
                dNdeta = -4.0 * shi

    elif e_type == 2:

        # Derivatives with respect to eta of the base functions for an unitary Square
        if order == 1:
            if n == 0:
                dNdeta = -0.25 * (1.0 - shi)
            elif n == 1:
                dNdeta = -0.25 * (1.0 + shi)
            elif n == 2:
                dNdeta = 0.25 * (1.0 + shi)
            else:
                dNdeta = 0.25 * (1.0 - shi)

        elif order == 2:
            if n == 0:
                dNdeta = 0.25 * shi * (shi - 1.0) * ((2.0 * eta) - 1.0)
            elif n == 1:
                dNdeta = 0.25 * shi * (shi + 1.0) * ((2.0 * eta) - 1.0)
            elif n == 2:
                dNdeta = 0.25 * shi * (shi + 1.0) * ((2.0 * eta) + 1.0)
            elif n == 3:
                dNdeta = 0.25 * shi * (shi - 1.0) * ((2.0 * eta) + 1.0)
            elif n == 4:
                dNdeta = -0.5 * ((2.0 * eta) - 1.0) * (shi**2.0 - 1.0)
            elif n == 5:
                dNdeta = -shi * eta * (shi + 1.0)
            elif n == 6:
                dNdeta = -0.5 * (shi**2.0 - 1.0) * ((2.0 * eta) + 1.0)
            elif n == 7:
                dNdeta = -shi * eta * (shi - 1.0)
            else:
                dNdeta = 2.0 * eta * (shi**2.0 - 1.0)

    return dNdeta
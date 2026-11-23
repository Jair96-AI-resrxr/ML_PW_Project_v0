from Parameters import e_type, order

def Nfunc(n, shi, eta):
    if e_type == 1:

        #Base functions for an unitary Triangle
        if order == 1:
            if n == 0:
                Nfunc = shi
            elif n == 1:
                Nfunc = eta
            else:
                Nfunc = 1.0 - shi - eta
        elif order == 2:
            if n == 0:
                Nfunc = shi * (2.0 * shi - 1.0)
            elif n == 1:
                Nfunc = eta * (2.0 * eta - 1.0)
            elif n == 2:
                Nfunc = (-1.0 + eta + shi) * (-1.0 + 2.0 * eta + 2.0 * shi)
            elif n == 3:
                Nfunc = 4.0 * shi * eta
            elif n == 4:
                Nfunc = -4.0 * eta * (-1.0 + eta + shi)
            else:
                Nfunc = -4.0 * shi * (-1.0 + eta + shi)

    elif e_type == 2:

        #Base functions for an unitary Square
        if order == 1:
            if n == 0:
                Nfunc = 0.25 * (1.0 - shi) * (1.0 - eta)
            elif n == 1:
                Nfunc = 0.25 * (1.0 + shi) * (1.0 - eta)
            elif n == 2:
                Nfunc = 0.25 * (1.0 + shi) * (1.0 + eta)
            else:
                Nfunc = 0.25 * (1.0 - shi) * (1.0 + eta)
        elif order == 2:
            if n == 0:
                Nfunc = 0.25 * shi * eta * (eta - 1.0) * (shi - 1.0)
            elif n == 1:
                Nfunc = 0.25 * shi * eta * (eta - 1.0) * (shi + 1.0)
            elif n == 2:
                Nfunc = 0.25 * shi * eta * (eta + 1.0) * (shi + 1.0)
            elif n == 3:
                Nfunc = 0.25 * shi * eta * (eta + 1.0) * (shi - 1.0)
            elif n == 4:
                Nfunc = -0.50 * eta * (eta - 1.0) * (shi**2.0 - 1.0)
            elif n == 5:
                Nfunc = -0.50 * shi * (eta**2.0 - 1.0) * (shi + 1.0)
            elif n == 6:
                Nfunc = -0.50 * eta * (eta + 1.0) * (shi**2.0 - 1.0)
            elif n == 7:
                Nfunc = -0.50 * shi * (eta**2.0 - 1.0) * (shi - 1.0)
            else:
                Nfunc = (shi**2.0 - 1.0) * (eta**2.0 - 1.0)

    return Nfunc

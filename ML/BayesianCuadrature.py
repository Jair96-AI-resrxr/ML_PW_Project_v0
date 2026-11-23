import numpy as np
from Parameters import nodes,nelements,elements,coords,nod_e,shi,eta,w,area
from NShiEta import Nfunc
from DetJacobian import detJ

def PosteriorAvg(y_pos,var_pos):
    # y_pos: The GP posterior
    # var_pos: Posterior covariance matrix 

    # Coordinates x,y of the 3 nodes of one element
    xvec = np.zeros(nod_e) 
    yvec = np.zeros(nod_e)

    # Initialize vector b (useful to compute mu_yref and var_yref)
    b = np.zeros(nodes)

    for i in range(nelements):
    # Get the coords of the 3 nodes of one element
        for j in range(nod_e):
            xvec[j] = coords[elements[i,j], 0]
            yvec[j] = coords[elements[i,j], 1]

        # Calculate the area of the element
        area_e = 0.5 * w[0] * detJ(xvec, yvec, shi[0], eta[0])

        # Compute the integral of each basis function
        for j in range(nod_e):
            piv = elements[i,j]
            b[piv] += area_e / 3.0

    # Normalise by the total domain area
    b /= area
    #print("Sum of b =", np.sum(b))
    
    # Calculate the posterior mean of the average temperature
    mu_yref = np.dot(b.T,y_pos)

    # Calculate the posterior covariance of the average temperature
    var_yref = np.dot(b.T,np.dot(var_pos,b))

    return mu_yref,var_yref,b
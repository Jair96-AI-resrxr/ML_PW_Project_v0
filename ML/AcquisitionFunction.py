import numpy as np
from Parameters import nodes

def Acquisition(b,var_pos,obs):
    # b: Integral vector from Bayesian cuadrature
    # var_pos: GP posterior of output field
    # obs: indices of nodes already observed

    # Initialize
    cov_yref = np.zeros(nodes) # Covariance between the average output and the nodal outputs  
    red = np.zeros(nodes) # Expected reduction in posterior variance of the average output

    # Compute the covariance
    cov_yref = np.dot(b.T,var_pos)

    # Compute the variace (diag. of cov. matrix)
    variance = np.maximum(np.diag(var_pos),0.0)

    # Standard check to prevent mathematical errors
    valid = variance > 1e-12

    # Compute expected reduction
    red[valid] = cov_yref[valid]**2 / variance[valid]

    # Exclude previously observed nodes
    obs = np.asarray(obs, dtype=int)
    red[obs] = -np.inf

    # Index of the node with the largest expected reduction
    return np.argmax(red)
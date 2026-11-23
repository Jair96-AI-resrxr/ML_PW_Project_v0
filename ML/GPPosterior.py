import numpy as np
from Parameters import theta
from CovarianceKernels import Kernel

def MyGP_pos(k_type,x,y,x_star):
    # x --> training inputs
    # y --> training outputs
    # x_star --> test inputs
    # theta --> [var,l,noise_std]
    # k_type: "rbf", "linear", "white", "periodic"

    # Covariance matrices
    k_xx = Kernel(k_type,x,x)
    k_star_x = Kernel(k_type,x_star,x)
    k_x_star = Kernel(k_type,x,x_star)
    k_star_star = Kernel(k_type,x_star,x_star)

    # Include observation noise in the training covariance
    k_mod = k_xx + theta[2]**2 * np.eye(len(x))
    # Small numerical jitter helps stabilise the matrix inversion
    k_mod = k_mod + 1e-6 * np.eye(k_mod.shape[0])

    # posterior mean
    mu_star = np.dot(k_star_x,np.linalg.solve(k_mod,y))

    # posterior covariance
    K_star = k_star_star - np.dot(k_star_x,np.linalg.solve(k_mod, k_x_star))

    # Remove small numerical asymmetries
    K_star = (K_star + K_star.T) / 2

    return mu_star, K_star
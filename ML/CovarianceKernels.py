import numpy as np
from scipy.spatial.distance import cdist
from Parameters import theta

def Kernel(k_type,x1,x2):
    # k_type: "rbf", "linear", "white", "periodic"
    # theta --> [var,l,noise_std]
    match k_type:
        case "rbf":
            d = cdist(x1, x2)
            return theta[0] * np.exp(-0.5 * (d / theta[1])**2)
        case "linear":
            if x2 is None:
                return theta[0]*x1.dot(x1.T)
            else:
                return theta[0]*x1.dot(x2.T)
        case "white":
            if x2 is None:
                return theta[0]*np.eye(x1.shape[0])
            else:
                return theta[0] * np.zeros((x1.shape[0], x2.shape[0]))
        case "periodic":
            period = 2.0*np.pi
            if x2 is None:
                d = cdist(x1, x1)
            else:
                d = cdist(x1, x2)
            return theta[0]*np.exp(-(2*np.sin((np.pi/period)*d)**2)/theta[1]**2)

        case "matern32":
              if x2 is None:
                  d = cdist(x1, x1)
              else:
                  d = cdist(x1, x2)
              return theta[0]*(1+np.sqrt(3)*d/theta[1])*np.exp(-np.sqrt(3)*d/theta[1])
        case "matern52":
            if x2 is None:
                d = cdist(x1, x1)
            else:
                d = cdist(x1, x2)
            return theta[0]*(1+np.sqrt(5)*d/theta[1] + 5*d**2/(3*theta[1]**2))*np.exp(-np.sqrt(5)*d/theta[1])

from Parameters import Q_gen,xs,ys,sigma
import numpy as np

def HeatSource(x,y):
    Q = Q_gen*np.exp(-((x-xs)**2.0 + (y-ys)**2.0)/(2.0*sigma))
    return Q
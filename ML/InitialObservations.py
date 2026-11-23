import numpy as np
import random

def InitialData(n):
    # n is the number of initial observations
    # x --> Input poitns
    # xs --> Space of search
    # ys --> Outputs of the whole space
    # obs --> indices of initial observations

    # Read the number of nodes
    with open("../FEM/output_mesh/num_nodes.dat", "r") as f:
        nodes = int(f.readline().strip())

    random_vals = np.zeros(n)
    x = []
    y = []
    xs = []
    ys = []

    random_vals = random_vals.astype(int)

    # Choose n random inputs
    for i in range(n):
        random_vals[i] = random.randint(0,nodes)

    # Sort the random integers
    random_vals.sort()

    # Find the random n Initial Observations in T.dat
    # Save all coords in xs
    j = 0
    with open("../FEM/Result/T.dat") as f:
        for i, line in enumerate(f):
            parts = line.strip().split()  # Use .split(",") if comma-separated
            coord_x,coord_y,T = [float(x) for x in parts]
            xs.append([coord_x,coord_y])
            ys.append(T)
            if(j<n):
                if i == random_vals[j]:
                    y.append(T)
                    x.append([coord_x,coord_y])
                    j += 1
    return xs,ys,x,y,random_vals


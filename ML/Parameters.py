import numpy as np
# You can PLAY with the parameters at the bottom of this file

# Nodes per element (Triangles first order)
nod_e = 3

# Type of element according ParaView (Triangles first order)
typeE_Paraview = 5

# Gaussian points
shi = np.array([1.0 / 3.0])
eta = np.array([1.0 / 3.0])
w = np.array([1.0])

# Read the number of nodes and elements
with open("../FEM/output_mesh/num_nodes.dat", "r") as f:
    nodes = int(f.readline().strip())
with open("../FEM/output_mesh/num_elements.dat", "r") as f:
    nelements = int(f.readline().strip())

# Read the mean temperature from FEM simulation
with open("../FEM/Result/Tmean.dat", "r") as f:
    yrefFEM = float(f.readline().strip())

# Read the matrix of elements
elements = np.loadtxt('../FEM/output_mesh/elements.dat', dtype=int)
elements = np.atleast_2d(elements)

# Read the matrix of coordinates
coords = np.loadtxt('../FEM/output_mesh/coords.dat')
coords = np.atleast_2d(coords)

# Total area of domain
area = 0.1**2 

# --------------------------------
# --------------------------------
# You can PLAY with this parameters!

# Input points (Initial observations)
p_input = 10 # Number of random points in the domain 

# theta --> [var,l,noise_std]
# var: variance of the data 
# l: Length Scale of the kernels (has to do with the dimensions of the square!)
# noise_std: The noise we add when we compute the GP posterior
theta = np.array([1.0,0.03,1e-4])

# Kernel: You can choose these names
         # rbf
         # linear
         # white
         # periodic
         # matern32
         # matern552
KernelName = "matern32"

# Convergence criteria
# The loop in Main is going to stop when std_yref (see Main) reaches this value
# std_yref: standard deviation of the reference output (mean temperature)
tolerance = 0.003


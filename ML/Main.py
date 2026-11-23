"""
To RUN this code you can type the following on the ML folder location:

rm -r Results/GPpos*

python Main.py

paraview
"""
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from Parameters import p_input,coords,yrefFEM,KernelName,tolerance
from InitialObservations import InitialData
from GPPosterior import MyGP_pos
from VTKFile import WriteVTK
from BayesianCuadrature import PosteriorAvg
from AcquisitionFunction import Acquisition


x_star,y_star,x,y,obs = InitialData(p_input)
# p_input: Number of initial observations
# x: Initial observations (x,y)
# y: Output of the initial observations (T)
# x_star: Complete input space (x,y)
# y_star: Complete output space (T)
# obs: Indices of initial observations

x = np.vstack((x))
print("Initial set of inputs")
print(x)

print("Indices of inicial values")
print(obs)

error_yref = []

# Initialise the standard deviation of the reference output
std_yref = 1.0

i = 0
while(std_yref > tolerance):
    i += 1
    print("Iteration number : ",i)
    # Compute the posterior and the x-coord minima of each sample
    mu,var = MyGP_pos(KernelName,x,y,x_star)

    VTKfilename = f"Results/GPpos{i}.vtk"

    # Write the posterior in a VTK file
    WriteVTK(x_star,mu,VTKfilename)

    # Compute the posterior mean and variance of the integral of the output
    mu_yref,var_yref,b = PosteriorAvg(mu,var)

    # Posterior Standard deviation of the integral of the output
    std_yref = np.sqrt(var_yref)
    print("posterior mean and std of the integral: ",mu_yref,std_yref)

    # Compute index with the largest expected reduction in the posterior var. of the reference output
    next_index = Acquisition(b,var,obs)
    obs = np.append(obs,next_index)

    print("Total of new inputs: ",len(obs))
    print("x-coord :",coords[next_index,0])
    print("y-coord :",coords[next_index,1])
    print("Temperature :",y_star[next_index])

    # Add the next value to the initial observations
    x = np.vstack((x,x_star[next_index]))
    y = np.append(y,y_star[next_index])

    # Quantify confidence in the estimated average
    std_yref = np.sqrt(var_yref)
    lower = mu_yref - 1.96 * std_yref
    upper = mu_yref + 1.96 * std_yref
    print(f"Average temperature: {mu_yref:.4f}")
    print(f"95% credible interval: [{lower:.4f}, {upper:.4f}]")

    # Compute the absolute error of the reference output
    error_yref.append(abs(mu_yref - yrefFEM))
    

# Let's plot the error
plt.plot(error_yref)
plt.xlabel('Iterations')
plt.ylabel('Absolute Error')
plt.title('Absolute error of the mean temperature from ML with respect to FEM')
plt.show()
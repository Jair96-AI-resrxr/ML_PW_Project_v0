import numpy as np
from Parameters import dof_node

def BoundaryConditions():
    #f saves the external force x-direction and y-direction from BC file
    with open('../output_mesh/num_dirichlet.dat', 'r') as file:
        BC_Dirichlet = int(file.readline().strip())

    with open('../output_mesh/num_newmann.dat', 'r') as file:
        BC_Newmann = int(file.readline().strip())

    with open('../output_mesh/bordes.dat', 'r') as file:
        bordes = int(file.readline().strip())

    f = np.empty((BC_Newmann, dof_node))
    U = np.empty((BC_Dirichlet, dof_node))
    BC_val = np.empty(dof_node)

    with open('../Input/BC.dat', 'r') as file:
        file.readline()
        file.readline()
        file.readline()

        for i in range(bordes):
            values = file.readline().split()
            surface = int(values[0])
            condition = int(values[1])
            BC_val = np.array([
                float(value.replace('d', 'e').replace('D', 'E'))
                for value in values[2:2 + dof_node]
            ])

            if condition > BC_Dirichlet:
                for j in range(dof_node):
                    f[condition - BC_Dirichlet - 1, j] = BC_val[j]
            else:
                for j in range(dof_node):
                    U[condition - 1, j] = BC_val[j]

    return BC_Dirichlet, BC_Newmann, U, f

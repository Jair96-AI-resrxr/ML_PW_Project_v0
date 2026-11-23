import numpy as np
from scipy.linalg import cho_factor, cho_solve

from Parameters import dof_node, order, e_type, kappa, th, NodesPerElement
from ReadMeshElements import InfoMesh
from ReadBC import BoundaryConditions
from GaussIntegrationF import CuadratureGaussF
from GaussIntegrationK import CuadratureGaussK
from MeanPhi import Average
from ElementArea import Area


print("=========================================================================")
print(" This program solves the poisson equation in 2D steady-state")
print(" Applies crank-Nicolson to integrate the time")
print(" ")
print(" K is the stiffness matrix (Diffusive)")
print(" ")
print(" Differential equation: -∇.(k∇Φ) = Q_gen")
print(" ")
print(" Newmann BC: dΦ/dn = q_flux")
print("=========================================================================")

typeE_Paraview, nodes, nfaces, nelements = InfoMesh()
BC_Dirichlet, BC_Newmann, fixedCondition, externalForce = BoundaryConditions()
nod_e, nod_f, e_name = NodesPerElement(order, e_type)

print("")
print("")
print(" Dirichlet conditions: ", BC_Dirichlet)
print(" Newmann conditions d(phi)/dn>0: ", BC_Newmann)
print(" Number of faces in the boundaries: ", nfaces)
print(" Type of elements: ", e_name)
print(" Number of elements: ", nelements)
print(" Number of nodes: ", nodes)
print("")
print("")


#mat_K --> Diffusive matrix

dof = dof_node * nodes

xvec = np.zeros(nod_e)
yvec = np.zeros(nod_e)

coords = np.zeros((nodes, 3))
faces = np.zeros((nfaces, nod_f + 1), dtype=int)
elements = np.zeros((nelements, nod_e), dtype=int)

mat_K = np.zeros((dof, dof))
vec_b = np.zeros(dof)
vec_fi = np.zeros(dof)
vec_force = np.zeros(dof)

gaussf = np.zeros(dof_node)
gaussk = np.zeros((dof_node, dof_node))

print("Reading the matrix of coordinates")
coords = np.loadtxt('../output_mesh/coords.dat')

print("Reading the matrix of faces      ")
faces = np.loadtxt('../output_mesh/faces.dat', dtype=int)

print("Reading the matrix of elements   ")
elements = np.loadtxt('../output_mesh/elements.dat', dtype=int)

coords = np.atleast_2d(coords)
faces = np.atleast_2d(faces)
elements = np.atleast_2d(elements)

mat_K = 0.0
vec_force = 0.0

mat_K = np.zeros((dof, dof))
vec_force = np.zeros(dof)

print("")
print("Building the stiffness matrix and the force vector")

for i in range(nelements):
    print(f"\r Element {i + 1}/{nelements}", end="", flush=True)

    for ii in range(nod_e):
        xvec[ii] = coords[elements[i, ii], 0]
        yvec[ii] = coords[elements[i, ii], 1]

    for j in range(nod_e):
        piv1 = elements[i, j] * dof_node

        gaussf = CuadratureGaussF(j, xvec, yvec)

        for jj in range(dof_node):
            piv3 = piv1 + jj
            vec_force[piv3] = vec_force[piv3] + gaussf[jj]

        for k in range(nod_e):
            #Filling the upper triangle of the matrix

            if elements[i, k] >= elements[i, j]:
                piv2 = elements[i, k] * dof_node

                gaussk = CuadratureGaussK(j, k, xvec, yvec)

                for jj in range(dof_node):
                    piv3 = piv1 + jj

                    for kk in range(dof_node):
                        piv4 = piv2 + kk
                        mat_K[piv3, piv4] = mat_K[piv3, piv4] + gaussk[jj, kk]

print("")
print("")

print("")
print("Filling the lower triangle of the diffusive matrix")

for i in range(dof):
    for j in range(i + 1, dof):
        mat_K[j, i] = mat_K[i, j]

print("")
print("Penalizing the accumulative matrix and the force vector")

#Coords of the vertices of the surfaces in the boundaries
x = np.zeros(2)
y = np.zeros(2)

for i in range(nfaces):
    print(f"\r Face {i + 1}/{nfaces}", end="", flush=True)

    #Penalization of Dirichlet conditions
    if faces[i, 0] <= BC_Dirichlet:
        for j in range(nod_f):
            piv1 = faces[i, j + 1] * dof_node

            for ii in range(dof_node):
                piv2 = piv1 + ii
                mat_K[piv2, piv2] = mat_K[piv2, piv2] + kappa
                vec_force[piv2] = (
                    vec_force[piv2]
                    + kappa * fixedCondition[faces[i, 0] - 1, ii]
                )

    #Newmann dphi/dn
    elif faces[i, 0] <= (BC_Dirichlet + BC_Newmann):
        for j in range(2):
            x[j] = coords[faces[i, j + 1], 0]
            y[j] = coords[faces[i, j + 1], 1]

        tam = np.sqrt((x[0] - x[1])**2.0 + (y[0] - y[1])**2.0)

        for j in range(nod_f):
            piv1 = faces[i, j + 1] * dof_node

            for ii in range(dof_node):
                piv2 = piv1 + ii
                vec_force[piv2] = (
                    vec_force[piv2]
                    + externalForce[faces[i, 0] - BC_Dirichlet - 1, ii]
                    * tam * th / nod_f
                )

print("")
print("")
print("Penalizing the trash nodes")

#Penalization of the trash nodes
with open('../Input/trash_nodes.dat', 'r') as file:
    file.readline()
    j = int(file.readline().strip())
    file.readline()

    for i in range(j):
        trash_node = int(file.readline().strip())

        piv1 = (trash_node - 1) * dof_node - (dof_node - 1)

        for ii in range(dof_node):
            piv2 = piv1 + ii
            mat_K[piv2, piv2] = mat_K[piv2, piv2] + kappa

print("")
print("")

print(
    " Computing the Cholesky factorization of the accumulative matrix of "
    + str(dof) + " nodes x " + str(dof) + " nodes"
)

#computes the Cholesky factorization of a real symmetric positive definite matrix.
mat_K, info = cho_factor(mat_K, lower=False)

print("info", 0)

print("")
print("")
print("Computing the temperature")

#Solves a system of linear equations A*X = B with a symmetric
#positive definite matrix A using the Cholesky factorization
vec_b = vec_force.copy()

vec_b = cho_solve((mat_K, False), vec_b)
vec_fi = vec_b.copy()

# Calculate the mean fi
fi_avg = 0.0
area_total = 0.0
fi_element = np.zeros(nod_e)

for i in range(nelements):
    for ii in range(nod_e):
        xvec[ii] = coords[elements[i, ii], 0]
        yvec[ii] = coords[elements[i, ii], 1]
        fi_element[ii] = vec_fi[elements[i, ii]]

    fi_avg += Average(xvec, yvec, fi_element)
    area_total += Area(xvec, yvec)

fi_avg = fi_avg / area_total
print("")
print("The average of fi is:", fi_avg)

with open("../Result/Tmean.dat", 'w') as file:
    file.write(f"{fi_avg:15.8f}")

VTKFile = "../Result/malla.vtk"
phiFile = "../Result/T.dat"

with open(phiFile, 'w') as file:
    for i in range(nodes):
        file.write(
                    f"{coords[i, 0]:15.8f}"
                    f"{coords[i, 1]:15.8f}"
                    f"{vec_fi[i]:20.10f}\n"
                )

with open(VTKFile, 'w') as file:
    file.write("# vtk DataFile Version 2.0\n")
    file.write("Datos Jair\n")
    file.write("ASCII\n")
    file.write("DATASET UNSTRUCTURED_GRID\n")
    file.write(f"POINTS {nodes} float\n")

    for i in range(nodes):
        file.write(
            f"{coords[i, 0]:15.8f}"
            f"{coords[i, 1]:15.8f}"
            f"{coords[i, 2]:15.8f}\n"
        )

    file.write(f"CELLS {nelements} {nelements * (nod_e + 1)}\n")

    for i in range(nelements):
        file.write(
            f"{nod_e:2d}"
            + ''.join(f"{elements[i, j]:6d}" for j in range(nod_e))
            + "\n"
        )

    file.write(f"CELL_TYPES {nelements}\n")

    for i in range(nelements):
        file.write(f"{typeE_Paraview:2d}\n")

    file.write(f"CELL_DATA {nelements}\n")
    file.write(f"POINT_DATA {nodes}\n")
    file.write("FIELD Temperature 1\n")
    file.write(f"T 1 {nodes} float\n")

    for i in range(nodes):
        file.write(f"{vec_fi[i]:20.10f}\n")

print("")

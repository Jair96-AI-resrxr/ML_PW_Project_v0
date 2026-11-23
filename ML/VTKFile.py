import numpy as np
from Parameters import nod_e,typeE_Paraview,nodes,nelements,elements

def WriteVTK(x,fi,VTKfile):
    # Write the VTK file
    with open(VTKfile, 'w') as file:
        file.write("# vtk DataFile Version 2.0\n")
        file.write("Datos Jair\n")
        file.write("ASCII\n")
        file.write("DATASET UNSTRUCTURED_GRID\n")
        file.write(f"POINTS {nodes} float\n")

        for i in range(nodes):
            file.write(
                f"{x[i][0]:15.8f}"
                f"{x[i][1]:15.8f}"
                f"{0.0:15.8f}\n"
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
            file.write(f"{fi[i]:20.10f}\n")

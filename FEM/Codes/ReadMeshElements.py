from Parameters import order, e_type, NodesPerElement

def InfoMesh():
    nod_e, nod_f, e_name = NodesPerElement(order, e_type)

    if e_type == 1:
        if order == 1:
            typeE_Gmsh = [1, 2]
            typeE_Paraview = 5
        elif order == 2:
            typeE_Gmsh = [8, 9]
            typeE_Paraview = 22

    elif e_type == 2:
        if order == 1:
            typeE_Gmsh = [1, 3]
            typeE_Paraview = 9
        elif order == 2:
            typeE_Gmsh = [8, 10]
            typeE_Paraview = 23

    with open('../Input/mesh.msh', 'r') as file:
        for i in range(4):
            file.readline()

        nBC = int(file.readline().strip())

        BC_Dirichlet = 0
        BC_Newmann = 0

        for i in range(nBC):
            values = file.readline().split()
            BC = values[2].strip('"')

            if BC[0] == "D":
                BC_Dirichlet += 1
            elif BC[0] == "N":
                BC_Newmann += 1

        file.readline()
        file.readline()

        nodos = int(file.readline().strip())

        node_index = {}

        with open('../output_mesh/coords.dat', 'w') as coords_file:
            for i in range(nodos):
                values = file.readline().split()
                node_id = int(values[0])
                x = float(values[1])
                y = float(values[2])
                z = float(values[3])

                node_index[node_id] = i

                coords_file.write(
                    f"{x:20.8f}{y:20.8f}{z:20.8f}\n"
                )

        file.readline()
        file.readline()

        elementsGmsh = int(file.readline().strip())

        elements = []

        for i in range(elementsGmsh):
            values = file.readline().split()
            elements.append(values)

    val1 = 0
    val2 = 0

    for i in range(elementsGmsh):
        type_element = int(elements[i][1])

        if type_element == typeE_Gmsh[0] and val1 == 0:
            val1 = 1
            ne_faces = i + 1

        if type_element == typeE_Gmsh[1] and val2 == 0:
            val2 = 1
            ne_elements = i + 1

    nfaces = ne_elements - ne_faces
    nelements = elementsGmsh - ne_elements + 1

    with open('../Input/BC.dat', 'r') as file:
        file.readline()
        bordes = int(file.readline().strip())
        file.readline()

        mat_BC = []

        for i in range(bordes):
            values = file.readline().split()
            mat_BC.append([int(values[0]), int(values[1])])

    with open('../output_mesh/faces.dat', 'w') as faces_file:
        piv = 0

        for i in range(ne_faces - 1, ne_elements - 1):
            values = elements[i]

            boundary = int(values[4])
            nodesFace = [
                node_index[int(node)]
                for node in values[5:5 + nod_f]
            ]

            if boundary != mat_BC[piv][0]:
                piv += 1

            faces_file.write(
                ''.join(f"{value:6d}" for value in [mat_BC[piv][1]] + nodesFace)
                + "\n"
            )

    with open('../output_mesh/elements.dat', 'w') as elements_file:
        for i in range(ne_elements - 1, elementsGmsh):
            values = elements[i]

            nodesElement = [
                node_index[int(node)]
                for node in values[5:5 + nod_e]
            ]

            #To match the order of the nodes
            if nod_e == 3:
                nodesElement = [
                    nodesElement[1],
                    nodesElement[2],
                    nodesElement[0]
                ]
            elif nod_e == 6:
                nodesElement = [
                    nodesElement[1],
                    nodesElement[2],
                    nodesElement[0],
                    nodesElement[4],
                    nodesElement[5],
                    nodesElement[3]
                ]

            elements_file.write(
                ''.join(f"{value:6d}" for value in nodesElement)
                + "\n"
            )

    with open('../output_mesh/num_dirichlet.dat', 'w') as file:
        file.write(f"{BC_Dirichlet:6d}\n")

    with open('../output_mesh/num_newmann.dat', 'w') as file:
        file.write(f"{BC_Newmann:6d}\n")

    with open('../output_mesh/bordes.dat', 'w') as file:
        file.write(f"{bordes:6d}\n")

    with open('../output_mesh/num_elements.dat', 'w') as file:
            file.write(f"{nelements:6d}\n")

    with open('../output_mesh/num_nodes.dat', 'w') as file:
            file.write(f"{nodos:6d}\n")

    return typeE_Paraview, nodos, nfaces, nelements

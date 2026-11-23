#Element type --> Triangle=1 ; Square=2
#Element order --> Triangle: 3nodes=1 ; 6nodes=2
#Element order -->   Square: 4nodes=1 ; 9nodes=2

#Parameters for the steady-state
k_diffusive = 70.0  #......................... Conductivity
th = 0.01  #......................... Thickness
kappa = 1.0e+12  #.........................kappa (penalization)

#Parameters for the heat source
Q_gen = 1.0e7 #......................... Heat generation
xs = 0.01 #......................... x-coord of source
ys = 0.01 #......................... y-coord of source
sigma = 0.001 #......................... variance of the source
#decrease sigma to decrease source

#Parameters for the elements
dof_node = 1  #..............................DoF per node
order = 1 #..............................Element order
e_type = 1  #..............................Element type

def NodesPerElement(order, e_type):
    #nod_e --> Nodes per element
    #nod_f --> Nodes per face
    if e_type == 1:
        if order == 1:
            nod_e = 3
            nod_f = 2
            e_name = "Triangles of first order "
        elif order == 2:
            nod_e = 6
            nod_f = 3
            e_name = "Triangles of second order"
    elif e_type == 2:
        if order == 1:
            nod_e = 4
            nod_f = 2
            e_name = "Quadrangles of first order  "
        elif order == 2:
            nod_e = 9
            nod_f = 3
            e_name = "Quadrangles of second order "

    return nod_e, nod_f, e_name

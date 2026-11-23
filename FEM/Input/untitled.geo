//+
Point(1) = {0, 0, 0, 0.005};
//+
Point(2) = {0.1, 0, 0, 0.006};
//+
Point(3) = {0.1, 0.1, 0, 0.006};
//+
Point(4) = {0, 0.1, 0, 0.0055};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Line Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Physical Line("D1") = {1,2};
//+
Physical Line("D2") = {3};
//+
Physical Line("N1") = {4};




M1
vector<int> v;
v.push_back(1); v.push_back(1); v.push_back(1);

M2
vector<int> v = {1, 1, 1};

M3    //doesn't work for global vectors
int n = 3;
vector<int> v(n, 1);    //Gives a vector having 3 1s

Example for 2D vector:-
vector<vector<int>> v(m, vector<int>(n, 0));    //m x n matrix initialized with 0s

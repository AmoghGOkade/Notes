#include <algorithm>

vector<int> v = {10, 20, 30, 40, 50};
int item = 30;
//v has to be sorted

auto it = upper_bound(v.begin(), v.end(), item);      //first value that is strictly greater than item
cout << *it;    //gives 40
cout << it - v.begin();     //gives the index number of the found element

auto it = lower_bound(v.begin(), v.end(), item);      //first value that is >= item, i.e., the first value that is not less than the given value

bool binary_search(v.begin(), v.end(), item);         //to see whether an element is present or not in a vector

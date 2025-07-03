#include <vector>
vector<int> v = {1, 2, 3};

auto it = v.begin();    //points to the element 1
cout << *it;            //prints 1

auto it_ = v.end();     //points to an element after 3
cout << *it_;           //prints garbage

cout << *(--it_);       //does it_ = it_ --; and then prints 3
cout << *(it_--);       //prints 3 and does it_ = it_ --;
cout << *it_;           //prints 2

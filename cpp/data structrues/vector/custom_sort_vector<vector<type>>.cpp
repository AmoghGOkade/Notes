static bool compare(vector<int>& a, vector<int>& b)       //static imperative
{
  //function that sorts
  //if true is returned based on some if condition, the corresponding vector of 'a' will be placed before 'b'
  //if false is returned, 'b' will come before 'a'

  if (a[3] < b[3]) return true;    //if a's 3rd element is smaller, a comes before b. So it will sort in ascending order of 3rd element
  else if (a[3] == b[3])
  {
    if (a[0] > b[0]) return true;  //if a's and b's 3rd element are the same, the one with the higher first element will be placed first
  }
  return false;
}

vector<vector<int>> v;    //say [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
sort(v.begin(), v.end(), compare);

//see leetcode - 2545. Sort the Students by Their Kth Score (simple)
//3433. Count Mentions Per User (slightly complex)

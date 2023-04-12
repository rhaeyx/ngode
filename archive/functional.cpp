#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
  int A[] = {0, 1, 2, 3, 3, 4};
  int n = sizeof(A) / sizeof(A[0]);

  vector<int> repeated;

  for (int i = 0; i < n; i++)
  {
    int j = count(A, A + n, A[i]);
    if (j > 1)
    {
      auto it = find(repeated.begin(), repeated.end(), A[i]);
      if (it == repeated.end())
      {
        repeated.push_back(A[i]);
      }
    }
  }

  cout << "Using Functional Programming:" << endl;
  for (int i : repeated)
  {
    cout << i << " ";
  }
  cout << endl;

  return 0;
}

#include <iostream>
#include <vector>

using namespace std;

class Array
{
private:
  int *arr;
  int size;

public:
  Array(int *a, int s) : arr(a), size(s) {}

  vector<int> findRepeated()
  {
    vector<int> repeated;
    for (int i = 0; i < size; i++)
    {
      int count = 0;
      for (int j = 0; j < size; j++)
      {
        if (arr[i] == arr[j])
        {
          count++;
        }
      }
      if (count > 1)
      {
        bool found = false;
        for (int k : repeated)
        {
          if (k == arr[i])
          {
            found = true;
            break;
          }
        }
        if (!found)
        {
          repeated.push_back(arr[i]);
        }
      }
    }
    return repeated;
  }
};

int main()
{
  int A[] = {0, 1, 2, 3, 3, 4};
  int n = sizeof(A) / sizeof(A[0]);

  Array arr(A, n);
  vector<int> repeated = arr.findRepeated();

  cout << "Using Object Oriented Programming:" << endl;
  for (int i : repeated)
  {
    cout << i << " ";
  }
  cout << endl;

  return 0;
}

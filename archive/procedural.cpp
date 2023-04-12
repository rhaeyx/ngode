#include <iostream>
#include <vector>

using namespace std;

void findRepeated(int *arr, int size)
{
  cout << "Using Procedural Programming" << endl;
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
  for (int i : repeated)
  {
    cout << i << " ";
  }
  cout << endl;
}

int main()
{
  int A[] = {0, 1, 2, 3, 3, 4};
  int n = sizeof(A) / sizeof(A[0]);

  findRepeated(A, n);

  return 0;
}

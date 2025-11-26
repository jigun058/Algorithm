#include <iostream>
using namespace std;

void swap(int &a, int &b) {
  int temp;
  temp = a;
  a = b;
  b = temp;
}

int main(){
  int i=1, j=2;
  swap(i,j);

  cout << "i=" << i << ", j=" << j << endl;

  return 0;
}



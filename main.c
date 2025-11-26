#include <stdio.h>

int main(){
  int true = 1;
  int false = 0;
  
  if(false || printf("false evaluated\n")){}
  if(true || printf("true evaluated\n")){}

  return 0;
}



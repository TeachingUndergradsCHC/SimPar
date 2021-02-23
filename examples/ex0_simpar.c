#include<omp.h>

int add() {
  int x, y, result;
#PARALLEL {
    x = 17;
    y = 13; 
  }
  result = x + y;
  return result;
}

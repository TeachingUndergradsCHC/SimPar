#include<omp.h>

int add() {
  int x, y, result;
  #pragma omp paralell
  {
    #pragma omp sections
    {
      #pragma omp section
      x = 17;
      #pragma omp section
      y = 13;
    }
  }
  result = x + y;
  return result;
}

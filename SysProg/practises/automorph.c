#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main(void) {
  int a, b;
  bool check = false;

  printf("Enter an integer a: ");
  scanf("%d", &a);  
  printf("Enter an integer b: ");
  scanf("%d", &b);  

  for (int i = a; i <= b; i++) {
    int n_digits = ceil(log10(i));
    int length = pow(10, n_digits);
    
    if ((i * i) % length == i) {
      check = true;
      printf("%d is amorph %d", i, i * i);
    }
  }

  if (!check) {
    printf("There is no amorph numbers");
  }

  return 0;
}
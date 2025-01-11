#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a, b;

  printf("Enter an integer a: ");
  scanf("%d", &a);  
  printf("Enter an integer b: ");
  scanf("%d", &b); 

  if (a == b) {
    printf("GCD is %d\n", a);
    return 0;
  }

  while(a != 0 && b != 0) {
    if (a > b) {
      a %= b;
    } else if (b > a) {
      b %= a;
    }
  }

  printf("GCD is %d\n", a < b ? b : a);

  return 0;
}
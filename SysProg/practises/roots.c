#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(void) {
  int a, b, c;
  float d, x0, x1;

  printf("Enter an integer a: ");
  scanf("%d", &a);
  printf("Enter an integer b: ");
  scanf("%d", &b);
  printf("Enter an integer c: ");
  scanf("%d", &c);

  d = b * b - 4 * a * c;

  if (d > 0) {
    x0 = (-b + sqrt(d)) / (2 * a);
    x1 = (-b - sqrt(d)) / (2 * a);

    printf("x0 = %f, x1 = %f", x0, x1);
  } else if (d == 0) {
    x0 = -b / (2 * a);
    
    printf("x0 = %f", x0);
  } else {
    printf("I've got no roots");
  }

  return 0;
}
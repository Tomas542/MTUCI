#include <stdlib.h>
#include <stdio.h>

int main(void) {
  int a, b, c;
  int buf;
  printf("Enter an integer a: ");
  scanf("%d", &a);
  printf("Enter an integer b: ");
  scanf("%d", &b);
  printf("Enter an integer c: ");
  scanf("%d", &c);

  if (a > b) {
    buf = a;
    a = b;
    b = buf;
  }

  if (b > c) {
    buf = b;
    b = c;
    c = buf;
  }

  if (a > b) {
    buf = a;
    a = b;
    b = buf;
  }

  printf("Min number is %d, mid number is %d, max number is %d", a, b, c);

  return 0;
}
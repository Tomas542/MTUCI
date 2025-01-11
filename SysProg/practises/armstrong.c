#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
  int a, b;
  bool check = false;

  printf("Enter an integer a: ");
  scanf("%d", &a);  
  printf("Enter an integer b: ");
  scanf("%d", &b);  

  int n_digits = ceil(log10(a));
  if (n_digits < 3) {
    printf("There is no armstrong number\n");
    return 0;
  }

  int num, sum, j, loop;
  
  for (int i = a; i <= b; i++) {
    sum = 0;
    j = i;
    loop = 0;
    n_digits = ceil(log10(j));

    do {
      num = j % 10;
      sum += pow(num, n_digits);
      loop++;
      j /= 10;
    } while (loop < n_digits);
    if (sum == i) {
      check = true;
      printf("%d is armstrong \n", i);};
  }

  if (!check) {printf("There is no armstrong number\n");}

  return 0;
}
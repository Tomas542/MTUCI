// resheto erotosphen
#include <stdlib.h>
#include <stdio.h>

int main(void) {
  int a;

  printf("Enter an integer a: ");
  scanf("%d", &a);  

  int arr[a - 2];

  for (int i = 0; i <= a; i++) {
    arr[i] = i;
  }

  int i = 2;
  while (i * i <= arr[a]) {
    int j = 2;
    if (arr[i] == 0) {continue;}

    while (i * j <= arr[a]) {
      arr[i * j] = 0;
      j++;
    }
    i++;
  }

  for (int j = 0; j <= a; j++) {
    if (arr[j] != 0 && arr[j] != 1) {
      printf("%d ", arr[j]);
    }
  }

  return 0;
}
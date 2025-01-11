#include <iostream>
#include <math.h>

int main(void) {
  int a{}, b{};
  bool check = false;

  std::cout << "Enter integers a: ";
  std::cin >> a;
  std::cout << "Enter integers b: ";
  std::cin >> b;

  int num, sum, j, loop, n_digits;

  for (int i {a}; i <= b; i++) {
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
      std::cout << i << " is armstrong" << std::endl;};
  }

  if (!check) {std::cout << "There is no armstrong number" << std::endl;}

  return 0;
}
#include <iostream>
#include <math.h>

int main(void) {
  int a{}, b{};
  bool check = false;

  std::cout << "Enter integers a: ";
  std::cin >> a;
  std::cout << "Enter integers b: ";
  std::cin >> b;

  for (int i {a}; i <= b; i++) {
    int n_digits = ceil(log10(i));
    int length = pow(10, n_digits);

    if ((i * i) % length == i) {
      check = true;
      std::cout << i << " is amorph " << i * i << std::endl;
    } 
  }

  if (!check) {
    std::cout << "There is no amorph numbers" << std::endl;
  }
  return 0;
}
#include <iostream>

int main(void) {
  int a{}, b{};
  std::cout << "Enter an integer a: ";
  std::cin >> a;
  std::cout << "Enter an integer b: ";
  std::cin >> b;

  if (a == b) {
    std::cout << "GCD is " << a << std::endl;
    return 0;
  }

  while (a != 0 && b != 0) {
    if (a > b) {
      a %= b;
    } else if (b > a) {
      b %= a;
    }
  }

  int min = a < b ? b : a;
  std::cout << "GCD is " << min << std::endl;

  return 0;
}
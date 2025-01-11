#include <iostream>

int main(void) {
  int a{}, b{}, c{};

  std::cout << "Enter an integer a: ";
  std::cin >> a;
  std::cout << "Enter an integer b: ";
  std::cin >> b;
  std::cout << "Enter an integer c: ";
  std::cin >> c;

  if (a > b) {std::swap(a, b);}
  if (b > c) {std::swap(b, c);}
  if (a > b) {std::swap(a, b);}

  std::cout << "Min number is" << a << ", mid number is " << b <<  ", max number is " << c << std::endl;

  return 0;
}
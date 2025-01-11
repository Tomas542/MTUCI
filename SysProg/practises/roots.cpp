#include <iostream>
#include <math.h>

int main(void) {
  int a, b, c;
  float d, x0, x1;

  std::cout << "Enter integers a" << std::endl;
  std::cin >> a;
  std::cout << "Enter integers b" << std::endl;
  std::cin >> b;
  std::cout << "Enter integers c" << std::endl;
  std::cin >> c;
  
  d = b * b - 4 * a * c;

  if (d > 0) {
    x0 = (-b + sqrt(d)) / (2 * a);
    x1 = (-b - sqrt(d)) / (2 * a);
    std::cout << "X0 is " << x0 << std::endl;
    std::cout << "X1 is " << x1 << std::endl;
  } else if (d == 0) {
    x0 = (-b) / (2 * a);
  } else {
    std::cout << "I've got no roots";
  }

  return 0;
}
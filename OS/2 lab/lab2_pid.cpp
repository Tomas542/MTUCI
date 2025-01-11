#include <iostream>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <string>

void currTime() {
  time_t lt;
  lt = time(NULL);
  std::string s = ctime(&lt);
  std::cout << s.substr(s.find('Oct')+5) << std::endl;
}

int main(void) {
  pid_t pid1, pid2;
  (pid1 = fork()) && (pid2 = fork());

  if (pid1 == 0) {
    std::cout << "Child's process 1 pid = " << getpid() << std::endl;
    std::cout << "Parent's pid = " << getppid() << std::endl;
    currTime();
    system("ls -lt");
    std::cout<<""<<std::endl;
  } else if (pid2 == 0) {
    sleep(1);
    std::cout << "Child's process 2 pid = " << getpid() << std::endl;
    std::cout << "Parent's pid = " << getppid() << std::endl;
    currTime();
    execl("lab2_thread", NULL);
    std::cout<<""<<std::endl;
  } else {
    sleep(10);
    std::cout << "Parent's process pid = " << getpid() << std::endl;
    currTime();
    system("findmnt");
  }

  return 0;
}
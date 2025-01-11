#include <iostream>
#include <signal.h>

int main(void) {
  pid_t pid1;
  pid1 = fork();

  if (pid1 == 0) {
    while(1) {printf("Child's messange\n");}
  } else {
    sleep(0.1);
    kill(pid1, SIGQUIT);
    printf("Child was teminated\n");
  }
  return 0;
}

#include <iostream>
#include <time.h>
#include <unistd.h>
#include <pthread.h>

void currTime() {
  time_t lt;
  lt = time(NULL);
  std::string s = ctime(&lt);
  std::cout << s.substr(s.find('Oct')+5) << std::endl;
}

void* threadFunc(void* args) {
  std::cout << "Thread id: " << pthread_self() << std::endl;
  std::cout << "Pred process pid: " << getpid() << std::endl;
  currTime();
  std::cout << std::endl;
  return 0;
}

int main(void) {
  pthread_t thread1, thread2;

  pthread_create(&thread1, NULL, threadFunc, NULL);
  sleep(1);
  pthread_create(&thread2, NULL, threadFunc, NULL);

  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);
}
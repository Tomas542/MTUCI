#include <iostream>

#include <pthread.h>

#define THREAD_NUM 4
pthread_barrier_t barrier;

void* threadFunc(void* argv) {
  std::cout << "Waiting for a barrier" << std::endl;
  pthread_barrier_wait(&barrier);
  std::cout << "Barrier passed" << std::endl;
}

int main(void) {
  pthread_t th[THREAD_NUM];
  pthread_barrier_init(&barrier, NULL, 2);
  int i;
  for (i = 0; i < THREAD_NUM; i++) {
    if (pthread_create(&th[i], NULL, &threadFunc, NULL) != 0) {
      std::cout << "Can't create a thread!" << std::endl;
    }
  }

  for (i = 0; i < THREAD_NUM; i++) {
    if (pthread_join(th[i], NULL) != 0) {
      std::cout << "can't join threads" << std::endl;
    }
  }
  pthread_barrier_destroy(&barrier);
  return 0;
}
#include <iostream>

#include <semaphore.h>
#include <pthread.h>
#include <unistd.h>

#define THREAD_NUM 4

sem_t semaphore;

void* threadFunc(void* args) {
  sem_wait(&semaphore);
  sleep(1);
  std::cout << "Hi, i'm thread: " << pthread_self() << std::endl;
  sem_post(&semaphore);
  free(args);
}

int main(void) {
  pthread_t th[THREAD_NUM];

  sem_init(&semaphore, 0, 2);

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
  sem_destroy(&semaphore);
  return 0;
}
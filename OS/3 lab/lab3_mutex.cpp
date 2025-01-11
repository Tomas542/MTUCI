#include <iostream>

#include <pthread.h>

#define THREAD_NUM 4

int counter {0};
pthread_mutex_t mutex;

void* threadFunc(void* argv) {
  for (int j = 0; j < 1000000; j++) {
    pthread_mutex_lock(&mutex);
    counter++;
    pthread_mutex_unlock(&mutex);
  }
}

int main(void) {
  pthread_t th[THREAD_NUM];
  pthread_mutex_init(&mutex, NULL);

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
  pthread_mutex_destroy(&mutex);
  std::cout << counter/THREAD_NUM << std::endl;
  return 0;
}
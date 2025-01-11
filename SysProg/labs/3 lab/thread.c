#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int a = 0;

void *myThread(void *dummy) {
	pthread_t mythid;
	mythid = pthread_self();
	a++;
	printf("Thread %d, res is %d\n", mythid, a);
	return NULL;
}

int main() {
	pthread_t thid, mythid;
	int result;

	result = pthread_create(&thid, (pthread_attr_t *)NULL, myThread, NULL);

	if (result != 0) {
		printf("Thread error");
		return 1;
	}

	printf("Thread created %d\n", thid);
	mythid = pthread_self();
	a++;
	printf("Thread %d, res is %d\n", mythid, a);
	pthread_join(thid, (void **)NULL);
	return 0;
}

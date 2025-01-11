#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <fcntl.h>
#include <pthread.h>

char message[1024];

void *myThread(void *dummy) {
	sleep(1);
	pthread_t mythid;
	printf("Thread %d is writing\n", mythid);
	FILE *out = fopen("./output/res2.txt", "w");
	fprintf(out, message);
	fclose(out);
	return NULL;
}

int helper(char file_name[]) {
	char ch;
	int letter = 0;
	int reader;

	int in = open(file_name, O_RDONLY);
	while((reader = read(in, &ch, 1)) > 0) {
		if (isalpha(ch) != 0) {
			letter++;
		}
	}

	return letter;
}

int main(void) {
	pthread_t thid, mythid;
	int result;

	result = pthread_create(&thid, (pthread_attr_t *)NULL, myThread, NULL);

	if (result != 0) {
		printf("Thread error");
		return 1;
	}

	printf("Thread created\n p");

	int l1 = helper("input/text1.txt");
	int l2 = helper("input/text2.txt");

	sprintf(message, "letters in text1: %d, letters in text2: %d", l1, l2);
	pthread_join(thid, (void **)NULL);
	return 0;
}

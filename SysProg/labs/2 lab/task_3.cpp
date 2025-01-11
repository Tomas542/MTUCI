#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(void) {
	pid_t child1, child2;
	child1 = fork();
	wait(NULL);

	if (child1 < 0) {
		perror("fork 1");
	} else if (child1 == 0) {
		execl("./calc", NULL);
	} else {
		child2 = fork();
		wait(NULL);
		if (child2 < 0) {
			perror("fork2");
		} else if (child2 == 0) {
			execl("../lab1/main", NULL);
		}
	}
	return 0;
}

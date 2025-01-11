#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <fcntl.h>
#include <sys/types.h>

int helper(char file_name[]){
        char ch;
        int lowe_case = 0;
        int reader;

        int in = open(file_name, O_RDONLY);
        while((reader = read(in, &ch, 1)) > 0) {
                if(islower(ch) != 0) {
                        lowe_case++;
                }
        }
	return lowe_case;
}

int main(void){
	int fd[2], result, func_ans_one, func_ans_two;
	size_t size;
	char message[1024];
	char ans[1024];

	if(pipe(fd) < 0) {
		printf("Can't create a pipe");
		return 1;
	}

	result = fork();
	if (result < 0) {
		printf("Can't fork");
		return 1;
	} else if (result > 0) {
		close(fd[0]);
		func_ans_one = helper("input/text1.txt");
		func_ans_two = helper("input/text2.txt");
		sprintf(message, "text1 lower case is %d, text2 lower case is %d", func_ans_one, func_ans_two);
		size = write(fd[1], message, 1024);
		close(fd[1]);
		wait(NULL);
	} else {
		close(fd[1]);
		size = read(fd[0], ans, 1024);

		if (size < 0) {
			printf("Can't read string");
		}

		FILE *out = fopen("./output/res.txt", "w");
		fprintf(out, ans);
		fclose(out);
		close(fd[0]);
	}
	return 0;
}

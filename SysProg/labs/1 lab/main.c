#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <fcntl.h>

void helper(char file_name[]){
	char ch;
	int lowe_case = 0;
	int reader;
	FILE *out = fopen("output/res.txt", "a");
	
	int in = open(file_name, O_RDONLY);
	while((reader = read(in, &ch, 1)) > 0) {
		if(islower(ch) != 0) {
			lowe_case++;
		}
	}
	printf("Total number of lower case letters is %d\n", lowe_case);
	fprintf(out, "Total number of lower case letters is %d\n", lowe_case);
	fclose(out);
}

int main(void) {
	char path1[] = "input/text1.txt";
	char path2[] = "input/text2.txt";
	helper(path1);
	helper(path2);
	printf("Files read:\n %s\n %s\nWrote into /out/res.txt\n", path1, path2);
	return 0;
}

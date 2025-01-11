#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <fcntl.h>

int helper(char file_name[]){
        char ch;
        int letter = 0;
        int reader;

        int in = open(file_name, O_RDONLY);
        while((reader = read(in, &ch, 1)) > 0) {
                if(isalpha(ch) != 0) {
                        letter++;
                }
        }

        printf("Total number of letters is %d\n", letter);
	return letter;
}

int main(void) {
        char path1[] = "input/text1.txt";
        char path2[] = "input/text2.txt";
	int arr[2];

        arr[0] = helper(path1);
        arr[1] = helper(path2);
	FILE *out = fopen("output/res2.txt", "w");
	if (arr[0] < arr[1]) {
		fprintf(out, "Letters: %d, file: %s\n", arr[0], path1);
	} else {
		fprintf(out, "Letters: %d, file: %s\n", arr[1], path2);
	}
	fclose(out);
        printf("Files read:\n %s\n %s\nWrote into /out/res.txt\n", path1, path2);
        return 0;
}

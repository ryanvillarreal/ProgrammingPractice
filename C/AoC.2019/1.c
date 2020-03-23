#include <stdio.h>


// initialize global variables
// creates a variable CHUNK with the value of 1024 and passes it into the buf buffer
#define CHUNK 1024 /* read 1024 bytes at a time */
char buf[CHUNK];
FILE* file; // initialize variable file as a FILE
size_t nread;


// Gotta have a main
int main() {
    read_in(); // start the chain of functions
}

void mafs(){
	//fwrite(buf, 1, nread, stdout);
	
}

void read_in() {
    // open the file and read in 1024 bytes at a time.
    file = fopen("1.input.txt", "r");
    if (file) {
        while ((nread = fread(buf, 1, sizeof buf, file)) > 0)
	    mafs();
        if (ferror(file)) {
            /* deal with error */
            printf("Error");
        }
        fclose(file);
    }
}

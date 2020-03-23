#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

/*
AoC - 2019 - Day 1 - Question 1
At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
For example:
For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
What is the sum of the fuel requirements for all of the modules on your spacecraft?
*/


/*
Finished!  finall answer is: 3178783
*/

// initialize global variables
FILE * file;
char * line = NULL;
size_t len = 0;
ssize_t read;
int total = 0; 

// Gotta have a main
int main() {
    read_in(); // start the chain of functions
}

void mafs(char * line){
	int line_int; 
	int result; 
	//printf(line);
	// line holds the char * line  which is the value of the current line
	// need to convert it to a int
	line_int = atoi(line);
	result = (line_int / 3) - 2; 
	// keep a running total of the values
	total = total + result;
	printf("the running total is: %d \n", total);
}


void read_in() {
    file = fopen("1.input.txt", "r");
    if (file == NULL)
	exit(EXIT_FAILURE);
    while((read = getline(&line, &len, file)) != -1){
	mafs(line);
	}

    fclose(file);
    if (line)
	free(line);
    exit(EXIT_SUCCESS);
}

// Build with: gcc -m32 -no-pie -g -o plt plt.c
// https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  puts("Hello world!");
  exit(0);
}

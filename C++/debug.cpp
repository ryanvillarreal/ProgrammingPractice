// debug.cpp 
// https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/
// https://github.com/TartanLlama/minidbg

// meant to be a debugger written in c++ to learn the language
// and how memory stuff works. 
#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <sys/ptrace.h>

// import the debugger header file
#include "debugger.hpp"

// use the namespace provided
using namespace minidbg;


void execute_debugee (const std::string& prog_name) {
    if (ptrace(PTRACE_TRACEME, 0, 0, 0) < 0) {
        std::cerr << "Error in ptrace\n";
        return;
    }
    execl(prog_name.c_str(), prog_name.c_str(), nullptr);
}

void debugger::run() {
    
}


int main(int argc, char* argv[]){
	// main 
	if (argc < 2){
		std::cout << "Specify file to open\n";
		return -1;
	}

	auto prog = argv[1];
	auto pid = fork();

	printf("Starting the program -------\n");

	if (pid == 0){
		// child process
		std::cout << "We are inside the child\n";
		

	}
	else if (pid >= 1){
		// parent process
		std::cout << "We are inside the parent\n";
        debugger dbg{prog, pid};
        dbg.run();

	}

	else{
		// error forking
		std::cout << "error here.\n";
	}
}

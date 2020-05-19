// more c++ learning along side of ELF format parsing
// https://github.com/finixbit/elf-parser
#include <iostream>

int main(int argc, char* argv[]) {
    char usage_banner[] = "usage: ./sections [<executable>]\n";
    if(argc < 2) {
        std::cerr << usage_banner;
        return -1;
    }

       std::string program((std::string)argv[1]);
 }
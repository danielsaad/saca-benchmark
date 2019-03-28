#include <chrono>
#include <cstring>
#include <fstream>
#include <iostream>
#include "divsufsort.h"

using namespace std;
using namespace std::chrono;
using timer = std::chrono::high_resolution_clock;

void load_string_from_file(char *&str, char *filename) {
    std::ifstream f(filename, std::ios::binary);
    f.seekg(0, std::ios::end);
    uint64_t size = f.tellg();
    f.seekg(0, std::ios::beg);
    str = new char[size + 1];
    f.read(str, size);
    str[size] = 0;
    f.close();
};


int main(int argc, char *argv[]) {

    if (argc != 2) {
        std::cerr << "Usage: ./divsufsort_saca <input_file>"
                  << std::endl;
        exit(EXIT_FAILURE);
    }
    auto start = timer::now();
    char *str;
    load_string_from_file(str, argv[1]);
    size_t n = strlen(str);
    saidx_t *SA = new saidx_t[n];


    std::cout << "Building SA with Divsufsort." << std::endl;
    divsufsort((sauchar_t*) str, SA, n);
    auto stop = timer::now();

    cout << "time: " << (double)duration_cast<milliseconds>(stop - start).count()/1000.0
         << " seconds" << endl;
    return 0;
}
#include "sais.h"
#include <cstring>
#include <fstream>
#include <iostream>

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
        std::cerr << "Usage: ./sais_yuta <input_file>"
                  << std::endl;
        exit(EXIT_FAILURE);
    }

    char *str;
    load_string_from_file(str, argv[1]);

    size_t n = strlen(str) + 1;
    sa_int32_t *SA = new sa_int32_t[n];
    sa_int32_t k = 256;

    std::cout << "Building SA with SAIS-YUTA." << std::endl;
    auto start = timer::now();
    sais_u8((sa_uint8_t *)str, SA, n, k);
    auto stop = timer::now();

    cout << "input:\t" << strlen(str) << " bytes" << endl;

    cout << "time: "
         << (double)duration_cast<milliseconds>(stop - start).count() / 1000.0
         << " seconds" << endl;
    return 0;
}

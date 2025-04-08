#include "real_solve.h"
#include <iostream>
#include <cstring>
#include <cassert>
using namespace std;

int main() {
    for (size_t i = 0; i < KEYS; i++) {
        for (size_t j = 0; j < FLAG_LENGTH; j++) {
            const char *key = keys[i];
            encrypted_flag[j] ^= key[j];
        }
    }
    
    cout << encrypted_flag << endl;

    return 0;
}
// #include "gl.h"
#include "kmeans.h"

void anyKey() {
    cout << "press any key to continue";
    cin.ignore();
    cin.get();
}

void work() {
    try {
        kmeans_work();
    } catch (const std::exception &e) {
        std::cerr << "Exception: " << e.what() << '\n';
    }
    // anyKey();
}

int main(int argc, char const *argv[]) {
    work();
    return 0;
}
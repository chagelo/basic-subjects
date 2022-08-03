#include <iostream>
#include <algorithm>
#include <vector>

#include <gmpxx.h>


int a[53]={41, 2, 1, 2, 1, 13, 16, 2 ,8, 
            1, 2, 2, 2, 2, 2, 1, 8, 2, 16,
            13, 1, 2, 1, 2, 82};
int N = 1711, k = 1;
// factor base
//std::set<int>FB = {-1, 2, 3, 5};
std::vector<int>FB = {-1, 2, 3, 5};
int main() {
    int p0 = a[0], p1 = a[0] * a[1] + 1;
    int q0 = 1, q1 = a[1];
    long long p2, q2;
    for (int i = 2;i < 13; ++i) {
        // iterate continued fraction, \sqrt{kn} converges to P/Q
        p2 = 1ll * a[i] * p1 + p0;
        p0 = p1, p1 = p2;
        q2 = a[i] * q1 + q0;
        q0 = q1, q1 = q2;
        //P^-kNQ^2=W, P^2\equiv w\pmod{N}
        long long w = p2 * p2 - N * q2 * q2;
        std::cout << p2 <<'\t'<< w <<'\t';
        if (w < 0) {
            std::cout << -1 <<",";
            w = -w;
        }
        for (int j = 1;j < 4; ++j) {
            while (w % FB[j]==0) {
                w /= FB[j];
                std::cout << FB[j] <<",";
            }
        }
        if (w != 1)
            std::cout << w << std::endl;
        else
            std::cout << std::endl;
    }

}
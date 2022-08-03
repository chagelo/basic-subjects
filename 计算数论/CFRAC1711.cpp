#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <set>
#include <gmpxx.h>

const int a[53]={41, 2, 1, 2, 1, 13, 16, 2 ,8, 
            1, 2, 2, 2, 2, 2, 1, 8, 2, 16,
            13, 1, 2, 1, 2, 82};
const int N = 1711, k = 1;
// factor base
//std::set<int>FB = {-1, 2, 3, 5};
const int FB[5] = {-1, 2, 3, 5};
// congruence equation, P, (-1), 2, 3, 5
std::vector<std::array<long long , 5>>coneq;

// factorization w-> FB, return 0 means failure
int factorzi(long long w, std::array<long long, 5> & temp){
    if (w < 0) {
        temp[1] = 1;
        w = -w;
    }
    for (int i = 2; i < 5; ++i) {
        int cnt = 0;
        while (w % FB[i - 1]) {
            cnt++;
            w /= FB[i - 1];
        }
        temp[i] = cnt;
        std::cout << FB[i - 1] <<"^" << cnt <<",";
    }
    std::cout << std::endl;
    return w == 1? 1: 0;
}

long long gcd(long long a, long long b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

bool check(std::array<long long, 5>e) {
    for (int i = 1; i < 5; ++i) {
        if (e[i] % 2)
            return false;
    }
    return true;
}

int dfs(int dep, std::array<long long, 5>e) {
    if (dep >= coneq.size())  {
        return 1;
    }
    if (check(e)) {
        if (gcd())
    }
}

int main() {
    int p0 = a[0], p1 = a[0] * a[1] + 1;
    int q0 = 1, q1 = a[1];
    long long p2, q2;
    std::array<int, 5> temp;
    for (int i = 2;i < 13; ++i) {
        // iterate continued fraction, \sqrt{kn} converges to P/Q
        p2 = 1ll * a[i] * p1 + p0;
        p0 = p1, p1 = p2;
        q2 = a[i] * q1 + q0;
        q0 = q1, q1 = q2;
        //P^-kNQ^2=W, P^2\equiv w\pmod{N}
        long long w = p2 * p2 - N * q2 * q2;
        // std::cout << p2 <<'\t'<< w <<'\t';
        // if (w < 0) {
        //     std::cout << -1 <<",";
        //     w = -w;
        // }
        // for (int j = 1;j < 4; ++j) {
        //     while (w % FB[j]==0) {
        //         w /= FB[j];
        //         std::cout << FB[j] <<",";
        //     }
        // }
        // if (w != 1)
        //     std::cout << w << std::endl;
        // else
        //     std::cout << std::endl;
        temp[0] = p2;
        std::cout << p2 << "同余于";
        if (factorzi(long long w, temp) == 0)
            continue;
        coneq.push_back(temp)
        std::array<long long , 5> e = {1, 0, 0, 0, 0};
        dfs(0, e);
    }

}
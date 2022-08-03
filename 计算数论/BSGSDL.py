from math import floor,sqrt

from matplotlib.contour import QuadContourSet

def quickPow(a, b, n):
    """
    return a^b % n, using binary factorization of b

    parameters
    ==========

    a: integer
    b: integer
    n: modular
    """

    res = 1
    while b > 0:
        if (b & 1):
            res = res * a % n
        a = a * a % n
        b >>= 1
    return res

def BSGS(a, b, N):
    """
    Baby-step giant-step algorithm
    """
    s = floor(sqrt(N))

    X = {}
    
    # Baby-step
    for i in range(s):
        t = b * quickPow(a, i, N) % N
        X[b * quickPow(a, i, N) % N] = i
    
    # Giant-step

    Y = {}
    for i in range(1, s + 1):
        val = quickPow(a, i * s, N)
        Y[val] = i * s
        if val in X:
            print(i * s - X[val])

    # sort by key
    X = [(k,X[k]) for k in sorted(X.keys())] 
    Y = [(k,Y[k]) for k in sorted(Y.keys())]

    print(X)
    print(Y)
def main():
    N = 123
    a = 37
    b = 15

    # for i in range(N):
    #     if quickPow(37, i, N) == 15:
    #         print(i) 
    X = BSGS(a, b, N)
    print("X = \log_", a," ",b, " = ", X, sep='')


if __name__ == "__main__":
    main()
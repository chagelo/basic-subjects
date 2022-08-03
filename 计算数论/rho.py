
from math import ceil,log2, gcd

def f(x):
    """
    selected funciotn f(x) = x^3 + x + 1, x0 = 1
    """ 
    return pow(x, 3) + x + 1


# def f(x):
#     """
#     selected funciotn f(x) = x^2 + 1, x0 = 1
#     """
#     return pow(x, 2) + 1

def quickPow(a, b):
    """
    return a^b, using binary factorization of b

    parameters
    ==========

    a: integer
    b: integer
    n: modular
    """

    res = 1
    while b > 0:
        if (b & 1):
            res = res * a
        a = a * a
        b >>= 1
    return res

def lbh(k):
    """
    2^{h+1}-2^{h-1}<=k<=2^{h+1}-1
    return lower bound of h
    """
    return ceil(log2(k + 1)) - 1

def main():
    #N = 8051
    N = 2701
    x = 1

    X = [0]
    X.append(x)
    dic = {x % N: 1}
    t = x
    while True:
        t = f(t) % N
        if t % N in dic:
            break
        dic[t % N] = 1
        X.append(t % N)
    print(X)

    k = 1

    while True:
        h = lbh(k)
        while quickPow(2, h + 1) - quickPow(2, h - 1) <= k:
            _gcd = gcd(X[quickPow(2, h) - 1] - X[k], N)
            h += 1
            print("gcd(X[", quickPow(2, h) - 1, "]", " - X[",k, "], ", "N) = ", _gcd, sep='')
            if _gcd != 1 and _gcd != N:
                print("sucessful!")
                print(N, "=", _gcd, "x", N // _gcd)
                return
        k += 1

if __name__ == "__main__":
    main()
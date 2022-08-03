from copy import deepcopy
from math import ceil, sqrt
from sympy import sieve
from sympy.ntheory import sqrt_mod_iter
import random, math

def faczi(p, w, FB):
    """
    using FB to factorize w, and combine p and factorization expoent 
    """
    temp = [p]
    for i in range(len(FB)):
        cnt = 0
        while w % FB[i] == 0:
            cnt += 1
            w /= FB[i]
        temp.append(cnt)
    if w == 1:
        return True, temp
    else:
        return False, None

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

def isprime(n):
    """
    Miller-Rabin primality test implemention

    parameter
    =========

    n: number to be tested whether prime or not
    """
    if n < 3 or n % 2 == 0:
        return n == 2
    a, b = n - 1, 0
    while a % 2 == 0:
        a = a // 2
        b = b + 1

    test_time = 8    
    # test_time is times for testing, recommand to set to be less than 8
    # to ensure accuracy, but should not be too large so that lower the efficiency

    for i in range(1, test_time + 1):
        x = random.randint(0, 32767) % (n - 2) + 2
        v = quickPow(x, a, n)
        if v == 1:
            continue
        j = 0
        while j < b:
            if v == n - 1:
                break
            v = v * v % n
            j = j + 1
        if j >= b:
            return False
    return True

def legendre_symbol(a, p):
    """
    Returns the Legendre symbol (a / p).
    
    Parameters
    ==========
    a : integer
    p : odd prime
    """

    if not isprime(p) or p == 2:
        print(isprime(p))
        raise ValueError("p should be an odd prime")
    a = a % p
    if not a:
        return 0
    if pow(a, (p - 1) // 2, p) == 1:
        return 1
    return -1


def getFB(P: int, N: int):
    """
    return all quadratic residue less than which is also prime

    parameters
    ==========

    P: upper prime bound of FactorBase
    N: number to be factored
    """
    # get all primes less than P
    sieve._reset
    sieve.extend(P)
    primeslist = list(sieve._list)

    # sieve primes that N is a quadratic residue modulo less than P
    FB = []
    for x in primeslist:
        if quickPow(N, (x - 1) // 2, x) == 1:
            FB.append(x)
    return FB
    

def csqrt(x: int):
    """
    return ceil(sqrt(x))
    
    parameter
    =========

    x: integer
    """
    
    return ceil(sqrt(x))

def Q(x, N):
    r"""
    Q(x) = (x + \lceil \sqrt{N} \rceil)^2 - N
    
    parameter
    =========
    x: list, sieve interval
    N: number to be factorized
    """
    qx = []
    for e in x:
        qx.append(pow(e + csqrt(N), 2) - N)
    return qx

def seve(A, FB, N):
    r"""
    sieve interval P, return Q(x) and sieved Q(x), x in range A
    fisrt find solution of Z^2 = N mod p, then find X that X + ceil(N) = Z mod p, so X = a mod p, then sieve a, a + p, a + 2p ... 
    
    """
    Qx = Q(list(range(A + 1)), N)
    tempQx = deepcopy(Qx)
    
    cN = csqrt(N)

    for p in FB:

        sol = list(sqrt_mod_iter(N, p))
        for i in range(len(sol)):
            a = (sol[i] - cN % p + p) % p
            for i in range(a, A + 1, p):
                while tempQx[i] % p == 0:
                    tempQx[i] //= p
    
    return Qx, tempQx

def sieveconeq(Q, V, FB, cN):
    """
    return a list of congruence equations p^2 = q mod N
    parameter
    =========
    Q: Q(x), list
    V: sieved Q(x), list
    """
    coneq = []

    for i in range(len(V)):
        if V[i] == 1:
            # print(Q[i])
            coneq.append(faczi(i + cN, Q[i], FB)[1])

    return coneq

def check(x: list, FB, N):
    """
    check whether combination x is p^2 = q^2 mod N, and return gcd
    """
    a = x[0]
    b = 1

    for i in range(len(FB)):
        if x[i + 1] % 2:
            return 1, None
        b *= pow(FB[i], x[i + 1] // 2)
    _gcd = math.gcd(a + b, N)
    if _gcd != 1 and _gcd != N:
        print([a, b])
    return _gcd,[a, b, _gcd]

def combine(a: list, b: list):
    """
    conbine two congruence eqations
    """
    temp = []
    temp.append(a[0] * b[0])
    for i in range(1, len(a)):
        temp.append(a[i] + b[i])
    return temp

def bfs(alconeq, N, FB):
    """
    return answer, use bfs to combine all congruence equations

    parameter
    =========

    alconeq: all congruence equations,list[list], each element of alconeq is a list, has length len(FB) + 1, last len(FB) elements are exponent of FB
    N: number to be factorized
    FB: factor base
    """
    temp = [1] + [0] * len(FB)
    # 1 = FB^0
    total = [temp]
    idx = [-1]
    record = []
    while len(idx) != 0:
        i = idx[0]
        idx.pop(0)
        coneq = total[0]
        total.pop(0)

        _gcd, comb = check(coneq, FB, N)
        if comb != None:
            record.append(comb)
        if _gcd != 1 and _gcd != N:
            return _gcd

        c = combine(coneq, alconeq[i + 1])
        total.append(c)
        idx.append(i + 1)
        total.append(coneq)
        idx.append(i + 1)

        # debug, recording gcd(a+b, N), a, b
        # print(record)

    return 1

def main():
    P = 50
    A = 500
    #N = 998771
    N = 1046603


    cN = csqrt(N)
    FB = getFB(P, N)
    print("selected Factor Base: ", FB)
    Qx, Vx = seve(A, FB, N)
    print("sieved interval P: ", Vx)
    coneq = sieveconeq(Qx, Vx, FB, cN)
    print("all congruences eqations: ", coneq)
    p = bfs(coneq, N, FB)
    # p is a nontrivial divisor
    print(N, "=", p, "x", N // p)


if __name__ == '__main__':
    main()

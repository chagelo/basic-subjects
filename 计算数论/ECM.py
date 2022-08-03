from copy import deepcopy
from math import gcd

def chooseab(a, b, N, P):
    """
    find a, b so that gcd(4 * a^3 + 27 * b ^ 2) = 1, then return a, b    
    """
    while gcd(4 * pow(a, 3) + 27 * pow(b, 2), N) != 1:
        a += 1
        x = P[0]
        y = P[1]
        b = pow(y, 2) - pow(x, 3) - a * x
    return a, b

def Qgpow():
    """
    Quick generalized power, use binary to factorize exponent
    """
    pass

def exgcd(a, b):
    """
    extend euclid algorithm to find inverse of a
    """
    if(b == 0):
        return 1,0
    y, x = exgcd(b, a % b)
    y = y - x * (a // b)
    return x, y

def add(a, b, P, Q, N):
    """
    add operation on Elliptic Curve
    """
    if P == None:
        return Q, 1

    if P == Q:
        # Denominator
        dom = 2 * P[1]
        # numerator
        num = 3 * pow(P[0], 2) + a
    else:
        # Denominator
        dom = P[0] - Q[0]
        # numerator
        num = P[1] - Q[1]

    _gcd = gcd(dom, N)
    if _gcd != 1:
        return None, _gcd
    
    invdom, b = exgcd(dom, N)
    invdom = (invdom + N) % N

    slope = num * invdom % N

    x = (pow(slope, 2, N) - P[0]- Q[0] + N) % N
    y = (slope * (P[0] - x) - P[1] + N) % N 

    return [x, y], _gcd



def ecm(a, b, K, N, P):

    Q = deepcopy(P)
    for i in range(2, K + 1):
        Q, p = add(a, b, Q, P, N)
        if Q == None:
            print("when k =", i, " successfully!")
            return p


    # tol = 0
    # c = 1
    # res = None
    # while K > 0:
    #     if K & 1:
    #         tol = tol + c
    #         res, p = add(a, b, res, P, N)
    #         if p != 1 and p != N:
    #             return p

    #     P, p = add(a, b, P, P, N)
    #     print(res, tol, c)
    #     c = c + c
    #     if p != 1 and p != N:
    #             return p

    #     K >>= 1

    # print(tol, c)
    # return None
        

def main():
    N = 199843247
    k = 19296
    a = 53
    b = -53
    P = [1, 1]

    a, b = chooseab(a, b, N, P)

    p = ecm(a, b, k, N, P)
    print(N, "=", p, "x", N // p)


if __name__ == "__main__":
    main()
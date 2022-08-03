import math
def faczi(p, w, FB):
    temp = [p]
    if w < 0:
        w = -w
        temp.append(1)
    else:
        temp.append(0)
    for i in range(1, len(FB)):
        cnt = 0
        while w % FB[i] == 0:
            cnt += 1
            w /= FB[i]
        temp.append(cnt)
    if w == 1:
        return True, temp
    else:
        return False, None

def combine(a: list, b: list):
    temp = []
    temp.append(a[0] * b[0])
    for i in range(1, len(a)):
        temp.append(a[i] + b[i])
    return temp

def check(x: list, FB, N):
    a = x[0]
    b = 1
    # (-1)^{2m}=(-1)^0
    if x[1] % 2 == 0:
        x[1] = 0
    for i in range(len(FB)):
        if x[i + 1] % 2:
            return 1, None
        b *= pow(FB[i], x[i + 1] // 2)
    _gcd = math.gcd(a + b, N)

    return _gcd,[a, b, _gcd]

# search result by bfs
def bfs(alconeq: list, N: int, FB: list):
    total = [[1, 0, 0, 0, 0]]
    idx = [-1]
    ans = alconeq[0]
    record = []
    while True:
        i = idx[0]
        idx.pop(0)
        coneq = total[0]
        total.pop(0)

        _gcd, comb = check(coneq, FB, N)
        if comb != None:
            record.append(comb)
        if _gcd != 1 and _gcd != N:
            return _gcd

        if i + 1 == len(alconeq):
            continue

        c = combine(coneq, alconeq[i + 1])
        total.append(c)
        idx.append(i + 1)
        total.append(coneq)
        idx.append(i + 1)

        # debug, recording gcd(a+b, N), a, b
        # print(record)

    return 1
    

def main():
    a = [41, 2, 1, 2, 1, 13, 16, 2 ,8, 
        1, 2, 2, 2, 2, 2, 1, 8, 2, 16,
        13, 1, 2, 1, 2, 82]

    N = 1711

    FB = [-1, 2, 3, 5]

    solve(N, FB, a)
    
def solve(N, FB, a):
    p0 = a[0]
    p1 = a[0] * a[1] + 1
    q0 =  1
    q1 = a[1]

    coneq = []
    coneq.append(faczi(p0, p0 * p0 - N * q0 * q0, FB)[1])
    coneq.append(faczi(p1, p1 * p1 - N * q1 * q1, FB)[1])
    for i in range(2,100001,1):
        p2 = p1 * a[i] + p0
        p0 = p1
        p1 = p2
        q2 = q1 * a[i] + q0
        q0 = q1
        q1 = q2
        
        w = p2 * p2 - N * q2 * q2 
        # 
        
        f, temp = faczi(p2, w, FB)
        if f == False:
            continue
        coneq.append(temp)
        
        if len(coneq) % 10 == 0:
            print("first", len(coneq), "congruence equations: ", coneq)
            _gcd = bfs(coneq, N, FB)
            if _gcd == 1 or _gcd == N:
                print("failure! continue to find more congruence equations.")
            else:
                print(N, "=", _gcd, "x", N // _gcd)
                return 


if __name__ == "__main__":
    main()
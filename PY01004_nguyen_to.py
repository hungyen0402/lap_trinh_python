import math 
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b) 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = 1 # 1 và n là cặp số nguyên tố rồi 
        for i in range(2, n, 1):
            if ucln(n, i) == 1:
                k += 1
        if isPrime(k):
            print('YES')
        else:
            print('NO')
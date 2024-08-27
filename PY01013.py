def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)  
def snt(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6 
    return True
def solve(n):
    sum = 0
    while n > 0:
        x = n % 10
        sum += x
        n //= 10
    if snt(sum):
        return True
    else:
        return False 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        x = gcd(a, b) 
        if solve(x):
            print('YES')
        else:
            print('NO')
 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b) 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        s1 = s[::-1]
        n = int(s)
        m = int(s1)
        if n < m:
            n, m = m, n
        if gcd(n, m) == 1:
            print("YES")
        else:
            print("NO")

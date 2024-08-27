def gcd(a, b):
    if a < b:
        a, b = b, a 
    if b == 0:
        return a
    return gcd(b, a%b) 
if __name__ == '__main__':
    n, k = map(int, input().split())
    x = 10**(k-1)
    y = 10**k
    cnt = 0
    while x < y:
        if gcd(x, n) == 1:
            print(x, end = ' ') 
            cnt += 1
            if cnt % 10 == 0:
                print()
        x+=1
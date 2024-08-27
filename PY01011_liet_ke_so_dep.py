def solve(n):
    if n % 2 != 0:
        return False
    x = n 
    m = 0
    dem = 0 
    while n>1:
        m = m * 10 + n % 10
        n //= 10 
        if n % 2 != 0:
            return False
        dem += 1
    if dem % 2 == 1:
         return False 
    return m == x 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) # 22 < n < 10**6 
        s = []
        for i in range(22, n):
            if solve(i):
                s.append(i)
        print(' '.join(map(str, s)))
        
a = [1]*10001
a[0] = a[1] = 0
i = 2
primes = [] 
while i <= 10000:
    if a[i]:
        primes.append(i)
        for j in range(i*i, 10000, i):
            a[j] = 0
    i += 1
if __name__ == '__main__':
    n, x = map(int, input().split())
    lst = []
    lst.append(x)
    for i in range(n):
        x += primes[i]
        lst.append(x)
    print(' '.join(map(str, lst)))
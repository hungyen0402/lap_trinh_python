prime = [1]*(10**6+1)
prime[0] = prime[1] = 0
p = 2
while p * p <= 10**6:
    if prime[p]:
        for j in range(p*p, 10**6, p):
            prime[j] = 0
    p += 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(n-5):
            if prime[i] and prime[i+6]:
                if prime[i+2] or prime[i+4]:
                    cnt += 1 
        print(cnt) 

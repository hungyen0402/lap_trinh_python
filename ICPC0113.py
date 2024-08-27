prime = [1]*(10**6+1)
prime[0] = prime[1] = 0
p = 2 
while p * p <= 10**6:
    if prime[p]:
        for j in range(p*p, 10**6, p):
            prime[j] = 0
    p += 1

def dao(a):
    x = 0  
    while a > 0:
        x *= 10
        x += a% 10 
        a //= 10
    return x 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n <= 11:
            print('')
            break
        else:
            lst = []
            for i in range(13, n):
                if prime[i] and i not in lst: 
                    x = dao(i)
                    if x < n and x != i and prime[x]:
                        lst.append(i)
                        lst.append(x) 
            print(' '.join(map(str, lst)))
            

                        

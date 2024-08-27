from math import sqrt
def phan_tich(n, s):
    i = 2
    for i in range(2, int(sqrt(n))+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            s += f" * {i}^{cnt}"
        if n == 1:
            break
    if n != 1:
        s += f" * {n}^1" 
    print(s)
    

    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = '1'
        phan_tich(n, s) 


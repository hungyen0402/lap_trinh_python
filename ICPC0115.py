def giai_thua(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans 
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = n 
        sum = 0
        while n >0:
            x = n % 10
            n //= 10
            sum += giai_thua(x) 
        if sum == m:
            print('Yes')
        else:
            print('No')
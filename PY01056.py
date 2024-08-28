def snt(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6 
    return True
def solve(s):
    sum = 0 
    for i in range(len(s)):
        if (i % 2 == 0 and int(s[i]) % 2 != 0) or (i % 2 != 0 and int(s[i]) % 2 == 0):
            print("NO")
            return 
        sum += int(s[i]) 
    print('YES' if snt(sum) else 'NO')
        
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        solve(s)
        

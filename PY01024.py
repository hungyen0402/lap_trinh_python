def check(s):
    Sum = int(s[0])
    for i in range(1, len(s)):
        if abs(s[i]-s[i-1]) != 2:
            print("NO")
            return 
        Sum += s[i]
    if Sum % 10 == 0:
        print('YES')
    else:
        print('NO')
     
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = list(map(int, input().strip()))
        check(s)

        
        

            
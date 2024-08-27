def solve(s):
    for x in s:
        if x != '0' and x != '1' and x != '2':
            print('NO')
            return 
    print('YES')
    return     
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = set(input())
        solve(s)
        
        
        
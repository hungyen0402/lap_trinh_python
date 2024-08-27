def solve(b):
    if len(b) <= 2:
        for x in b:
            if x != 4 and x != 7:
                print('NO')
                return
    else:
        print('NO')
        return
    print('YES')
    return 

t = int(input())
for _ in range(t):
    a = list(map(int, input()))
    l1 = len(a)
    b = set(a)
    solve(b) 


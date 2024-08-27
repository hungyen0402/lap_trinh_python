def solve(a):
    l = len(a)
    if l < 3:
            print('NO')
            return 
    else:
        i = 0
        while i < l-1:
            if a[i] == a[i+1]:
                print('NO')
                return 
            elif a[i] > a[i+1]:
                i += 1
                break 
            i += 1
        while i < l-1:
            if a[i] > a[i+1]:
                i += 1
            else:
                print('NO')
                return 
        print('YES')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)
        
        
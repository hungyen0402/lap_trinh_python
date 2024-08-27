def solve(s):
    if s[0] != s[1]:
            x, y = s[0], s[1]
            for i in range(2, len(s), 1):
                if (i % 2 == 0 and s[i] != x) or (i % 2 != 0 and s[i] != y):
                    print("NO")
                    return 
            print('YES')
            return 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)
        
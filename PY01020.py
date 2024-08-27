if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        x = len(s)
        if s[x-1] == '6' and s[x-2] == '8':
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, m = map(float, input().split())
        a = (1+x/100)
        y = 1
        while 1:
            if (a**y)*n >= m:
                 print(y)
                 break
            y += 1
        
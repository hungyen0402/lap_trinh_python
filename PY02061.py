import numpy as np

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            row = list(map(int, input().split()))
            a.append(row)
        b = []
        for _ in range(3):
            row = list(map(int, input().split()))
            b.append(row)
        c = np.dot(a, b)
        ans = c.sum()
        print(ans)
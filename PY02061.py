if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            row = list(map(int, input().split()))
            a.append(row)
        h = []
        for _ in range(3):
            x = list(map(int, input().split()))
            h.append(x)
        sum = 0 
        for i in range(n-3+1):
            for j in range(m-3+1):
                for u in range(3):
                    for v in range(3):
                        z = h[u][v] * a[i+u][j+v]
                        sum += z
        print(sum)
                     
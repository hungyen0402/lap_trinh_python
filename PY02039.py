if __name__ == '__main__':
    n = int(input()) # n < 50
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    k = int(input())
    nua_tren = 0
    nua_duoi = 0
    for i in range(n):
        for j in range(i+1, n):
            nua_tren += a[i][j]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            nua_duoi += a[i][j]
    x = abs(nua_duoi - nua_tren)
    if x <= k:
        print("YES")
    else:
        print("NO")
    print(x)
    
    
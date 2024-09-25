
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)   
    k = int(input())
    nua_tren = 0
    nua_duoi = 0
    for i in range(0, n):
        for j in range(0, n-i):
            nua_tren += a[i][j]
    for i in range(n-1, -1, -1):
        for j in range(n-i-1, n, 1):
            nua_duoi += a[i][j]
    hieu = abs(nua_tren-nua_duoi)
    if (hieu <= k): print(f'YES\n{hieu}')
    else: print(f'NO\n{hieu}')
      
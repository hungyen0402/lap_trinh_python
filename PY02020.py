if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    max = a[n-1]
    min = a[0]
    sum = 0
    dem = 0 
    for i in range(1, n-1):
        if a[i] != max and a[i] != min:
            sum += a[i]
            dem += 1
    tb = sum / dem
    print('{:.2f}'.format(tb))
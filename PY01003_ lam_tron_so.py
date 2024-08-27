t = int(input())
for _ in range(t):
    a = list(map(int, input()))
    if len(a) < 2:
        print(a[0])
    else:
        for i in range(len(a)-1, 0, -1):
            if a[i] >= 5:
                a[i-1] += 1
            a[i] = 0
        print(''.join(map(str, a)))    

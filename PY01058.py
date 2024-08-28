a = [1]*10000
a[0] = a[1] = 0
i = 2
while i * i <= 10000:
    if a[i] > 0:
        for j in range(i*i, 10000, i):
            a[j] = 0
    i += 1
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        x = int(s[len(s)-4:])
        if a[x] == 1:
            print('YES')
        else:
            print('NO')

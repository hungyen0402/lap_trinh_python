def tich_chu_so(n):
    mul = 1
    while n > 0:
        x = n % 10
        mul *= x
        n //= 10
    return mul

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = []
        for i in range(n):
            mul = tich_chu_so(a[i])
            b.append([mul, a[i]])
        b = sorted(b, key = lambda item : (item[0], item[1]))

        for [k, v] in b:
            print(v, end = " ")
        print()

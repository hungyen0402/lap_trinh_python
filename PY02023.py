def tong_chu_so(n : int):
    sum = 0
    while n > 0:
        x = n % 10
        sum += x
        n //= 10
    return sum
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        d = []
        b = list(map(int, input().split()))
        for x in b:
            sum = tong_chu_so(x)
            d.append([x, sum])

        d = sorted(d, key=lambda item : (item[1], item[0]))

        for [k, v] in d:
            print(k, end=" ")
        print()
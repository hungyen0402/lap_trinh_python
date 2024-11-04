a = [1]*10000
i = 2
a[0] = 0 
while i * i <= 10000:
    if a[i] != 0: 
        for j in range(i+i, 10000, i):
            a[j] = 0 
    i += 1

def xuly(x):
    cnt = 1
    m = x - 1
    n = x + 1
    while a[m] != 1 and a[n] != 1:
        m -= 1
        n += 1
        cnt+= 1
    return cnt 
if __name__ == '__main__':
    n = int(input())
    count = 0
    lst = list(map(int, input().split()))
    for x in lst:
        if a[x] != 1:
            count = max(count, xuly(x))
            # print(f"lan {count}")
    print(count)
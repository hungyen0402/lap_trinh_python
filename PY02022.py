prime = [1]*1000001
prime[0] = prime[1] = 0
i = 2
while i * i <= 1000000:
    if prime[i]:
        for j in range(i*i, 1000000, i):
            prime[j] = 0
    i += 1
# n < 500
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n-1, -1, -1):
        if prime[a[i]]:
            prime[a[i]] += 1
        else:
            a.pop(i)
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
    for i in range(len(b)):
        print(b[i], prime[b[i]]-1)
# code này giải thuần list, bài này có thể kết hợp với dict để giải sẽ đơn giản hơn 
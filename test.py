def sieve_divisors(limit):
    divisors = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            divisors[j] += 1
    return divisors

def tim_so_phan_nguyen_to(x, l, max_limit):
    while x <= max_limit:
        if l[x] > l[x - 1]:
            return x
        x += 1
    return 10000061

def main():
    max_limit = 10000000
    divisors = sieve_divisors(max_limit)

    t = int(input())
    for _ in range(t):
        x = int(input())
        if x == max_limit:
            print('10000061')
        else:
            print(tim_so_phan_nguyen_to(x, divisors, max_limit))

if __name__ == '__main__':
    main()

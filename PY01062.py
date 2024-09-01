def snt(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
lst = ['2', '3', '5', '7']
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        l = len(s)
        if snt(l):
            cnt = 0
            for i in s:
                if i in lst:
                    cnt += 1
            if cnt > l - cnt:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')


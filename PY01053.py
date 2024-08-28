if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        sum = 0
        for x in s:
            sum += int(x)
        if sum % 3 == 0:
            print('YES')
        else:
            print('NO')
        
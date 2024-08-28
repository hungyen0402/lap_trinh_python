if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        res = 1
        for i in s:
            if int(i) != 0:
                res *= int(i)
        print(res)
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        a.append(s)
    a = set(a)
    print(len(a))
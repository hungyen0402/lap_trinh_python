if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        b = a[:d]
        print(' '.join(map(str, a[d:])), ' '.join(map(str, a[:d])))
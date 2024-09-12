if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    for i in range(1, n + 1):
        if i not in a:
            print(i)
            break
    else:
        print(n + 1)
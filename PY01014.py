if __name__ == '__main__':
    a, k, n = map(int, input().split())
    if n <= a:
        print(-1)
    else:
        id = 0
        x = k - a % k # số b thỏa mãn đầu tiên 
        for b in range(a+x, n+1, k):
            print(b-a, end = ' ') 
            id = 1 
        if id == 0:
            print(-1)
        else:
            print('') 
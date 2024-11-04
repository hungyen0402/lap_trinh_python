if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        id = True 
        for i in range(n):
            if a[i] > b[i]:
                print("NO")
                id = False
                break
        if id == True:
            print("YES")
        
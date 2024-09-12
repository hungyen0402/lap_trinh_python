if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input()) # n <= 100000 
        a = list(map(int, input().split())) # a[i] <= 1 000 000 
        compare_x = n // 2
        b = {}
        for x in a:
            if b.get(x): 
                b[x] += 1
            else:
                b[x] = 1
        x = 0 
        y = 0
        for key in b:
            if x < b[key] and b[key] > compare_x:
                y = key
                x = b[key]
            elif x == b[key] and x > compare_x and y < key:
                y = key
        print(y) if y > 0 else print("NO")




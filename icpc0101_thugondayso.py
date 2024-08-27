if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    i = 0 # 2 5 4 4 5 6 7 7 
    b = []
    for num in a:
        if b and (b[-1] + num) % 2 == 0:
            b.pop()
        else: 
            b.append(num)
    print(len(b))
    
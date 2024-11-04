if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = float('inf')
    value = 0
    b = []
    
    while n > 0 and len(a) != 0:
        n -= 1
        if len(a) != 0:
            x = a.pop()
        sum = 0 
        for i in a:
            sum += abs(x-i)
        if len(b) != 0:
            for i in b:
                sum += abs(x-i)
        if count >= sum:
            value = x
            count = sum
        b.append(x)
    print(f"{count} {value}")

        

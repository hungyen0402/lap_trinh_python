if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0 
        a.sort()
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                x = a[i] + a[left] + a[right]
                if not x: # tổng bằng 0 
                    count += 1
                    left += 1
                    #right -= 1 
                elif x < 0:
                    left += 1
                else:
                    right -= 1
        print(count)

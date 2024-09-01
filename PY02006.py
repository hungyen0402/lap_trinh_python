def xl(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")
# sau khi sắp xếp, nếu a[i] > b[i] thì a[i+1] > b[i] do đó không tồn tại cách sắp xếp các phần tử để thỏa mãn đề bài
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        xl(a, b, n) 
        
        

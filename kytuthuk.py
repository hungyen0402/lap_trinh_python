a = [1]*26 # 0 - 25 
for i in range(2, 26): # 0 - 25 
    a[i] = a[i-1] * 2 + 1
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] 

def solve(n, k):
    if k == 0 or n == 1: 
        print('A')
        return 
    if k == a[n-1] or k == a[n]:
        print('A')
        return  
    x = a[n]//2 + 1
    # print(f"x la {x}")
    if k == x:
        print(letters[n-1])
        return
    if k < a[n-1]:
        return solve(n-1, k)
    if k > a[n-1]:
        return solve(n-1, k - x)
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        solve(n, k)

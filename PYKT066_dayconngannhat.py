import math 
import sys
# quá tốn thời gian 
# def uocchungcuadayso(s, k):
#     uoc = s[0]
#     for i in range(1, len(s)):
#         uoc = math.gcd(uoc, s[i])
#         if uoc == 1:
#             break
#     if uoc == k:
#         return True 
#     else:
#         return False 


# def solve(a, n, k):
#     length = float('inf')
#     sign = False
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if uocchungcuadayso(a[i:j+1], k) == True:
#                 length = min(length, j-i+1)
#                 sign = True
#     if sign == False:
#         print("-1")
#         return 
#     else:
#         print(length)
#         return 
def check(a, l, r, len):
    for i in range(l, r-len+2):
        x = a[i]
        for j in range(i+1, i+len): 
            x = math.gcd(x, a[j])
        if x == 1: return True
    return False 
def find_min(a, l, r): # dùng binary 
    oke = False
    L, R = 0, r-l+2
    while L < R:
        len = (L+R) >> 1
        if check(a, l, r, len):
            oke = True
            R = len # set R bằng len để thu gọn phạm vi tìm kiếm
        else: L = len+1
    return (oke, L)
def solve(a, n, k):
    for i in range(n):
        # lọc phần tử, các phần tử mà có ước là k thì sẽ chia cho k
        # lát sẽ kiểm tra có chung uscln = 1 không
        if a[i] % k == 0:
            a[i] //= k
            if a[i] == 1: # trường hợp dãy có độ dài bằng 1 luôn
                print(1)
                return
        else:
            a[i] = -1 # đánh dấu để loại đi luôn
    l, r, ans, oke = 0, 0, 10**9, False
    while l < n and r < n:
        while l < n and a[l] == -1: l += 1
        if l == n: break # không có dãy nào 
        r = l
        while r < n-1 and a[r] != - 1: r += 1
        res = find_min(a, l, r)
        if res[0] == True:
            oke = True
            ans = min(ans, res[1])
        l = r + 1 # tiếp tục tìm dãy con mới
    if oke: print(ans)
    else: print(-1)
if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    # print(t)
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())
        #print(n, k)
        a = []
        while len(a) < n:
            a.extend(map(int, sys.stdin.readline().strip().split()))
        solve(a, n, k)
        
        

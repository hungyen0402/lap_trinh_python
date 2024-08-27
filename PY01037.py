from math import sqrt

def dem_uoc(n):
    cnt = 0 
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    return cnt

a = 10000000
l = [0] * (a + 1)  # Khởi tạo danh sách l với kích thước a+1
for i in range(1, a):
    l[i] = dem_uoc(i)
pref = [0] * (a + 1)  # Khởi tạo danh sách pref với kích thước a+1
pref[1] = 0 
pref[2] = 1 
for i in range(1, a):
    pref[i] = pref[i - 1] + l[i-1] 
# 10000061
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        if x == 10000000:
            print('10000061')
        else:
            x += 1
            while True:
                if x == 10000000:
                    print('10000061')
                    break
                if l[x] > pref[x]:
                    print(x)
                    break
                x += 1
        

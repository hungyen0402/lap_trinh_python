import math 
def check(a):
    if a[0] == a[1] == a[2] == a[3]:
        return True
    return False 
if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        cnt = 0
        if a[0] == a[1] == a[2] == a[3] == 0:
            break 
        while check(a) == False:
            x = abs(a[3]-a[0])
            for i in range(3):
                a[i] = abs(a[i]-a[i+1])
            a[3] = x
            cnt += 1
            #print(a)
        print(cnt)


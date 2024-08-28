from math import sqrt 

a = [1] * 501
a[0] = a[1] = 0
i = 2

while i * i <= 500:
    if a[i] == 1:
        for j in range(i * i, 501, i):
            a[j] = 0
    i += 1

lst = ['2', '3', '5', '7']
    
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        id = 1
        for i in range(len(s)):
            if (a[i] == 1 and s[i] not in lst) or (a[i] == 0 and s[i] in lst):
                print('NO')
                id = 0
                break
        if id:
            print('YES')
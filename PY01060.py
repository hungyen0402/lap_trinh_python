def solve(s):
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    tich = 1
    ans = 0
    for i in range(0, len(s),2):
        if int(s[i]):
            tich *= s[i]
            ans = 1
    if ans == 0:
        tich = 0
    print(tich, sum, end = ' ')
    print()
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        solve(s)

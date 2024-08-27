p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
if __name__ == '__main__':
    while True:
        str = input()
        if str == '0':
            break
        k, s = str.split()
        k = int(k)
        lst = ''
        for i in range(len(s)):
            j = p.find(s[i])
            x = p[(j+k)%28]
            lst += x     
        print(lst[::-1])

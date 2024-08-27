if __name__ == '__main__':
    s = input()
    l = len(s)
    x = l % 3
    if x > 0:
        s1 = s[:x]
        s1 += ','
    else:
        s1 = ''
    while x < l:
        s1 += s[x:x+3]
        if x < l - 3:
            s1 += ','
        x += 3
    print(s1)

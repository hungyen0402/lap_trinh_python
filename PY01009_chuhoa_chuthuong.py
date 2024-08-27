if __name__ == '__main__':
    s = input() # xâu chỉ gồm các ký tự chữ cái 
    id = 1 # sẽ là upper 
    x1 = 0 # số lượng chữ cái viết thường 
    x2 = 0 # số lượng chữ cái viết hoa
    for c in s:
        if c.isupper():
            x2 += 1 
        else:
            x1 += 1
    if x1 >= x2:
        s1 = s.lower()
        print(s1)
    else:
        s1 = s.upper()
        print(s1)

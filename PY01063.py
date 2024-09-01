if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        n = input()
        cnt = 0
        l1 = len(s)
        l2 = len(n)
        if l1 >= l2: 
            for i in range(0, l1-l2+1):
                if s[i:i+l2] == n:
                    cnt += 1
                    for j in range(i, i+l2):
                        s[i] = 'y' 
            print(cnt)
        else:
            print(cnt)
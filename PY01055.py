if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        if len(s) % 2 != 0 and s[0] != s[1]:
            x = s[0] 
            id = 1
            for i in range(0, len(s), 2):
                if x != s[i]:
                    print('NO')
                    id = 0
                    break
            if id > 0:
                print('YES') 
        else:
            print('NO')


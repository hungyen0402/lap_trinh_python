if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        cnt = 1 
        for i in range(0, len(s)):
            if i != len(s)-1:
                if s[i] == s[i+1]:
                    cnt += 1
                else:
                    print(f'{cnt}{s[i]}', end = '') 
                    cnt = 1
            else:
                print(f'{cnt}{s[i]}', end = '') 
        print('')
            
            

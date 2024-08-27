if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p, q = map(int, input().split())
        if p > q:
            p, q = q, p
        ip = input().split()
        if len(ip) == 1:
            x1 = list(map(int, ip[0]))
            x2 = list(map(int, input()))
        else:
            x1 = list(map(int, ip[0]))
            x2 = list(map(int, ip[1]))
        
        Min1 = 0
        Max1 = 0
        Min2 = 0
        Max2 = 0
        
        l1 = len(x1) - 1
        l2 = len(x2) - 1
        
        # Xử lý X1
        for i in range(len(x1)):
            if x1[i] == p or x1[i] == q:
                Min1 += (10**(l1-i)) * p
                Max1 += (10**(l1-i)) * q
            else:
                Min1 += (10**(l1-i)) * x1[i]
                Max1 += (10**(l1-i)) * x1[i]
        
        # Xử lý X2
        for i in range(len(x2)):
            if x2[i] == p or x2[i] == q:
                Min2 += (10**(l2-i)) * p
                Max2 += (10**(l2-i)) * q
            else:
                Min2 += (10**(l2-i)) * x2[i]
                Max2 += (10**(l2-i)) * x2[i]
        
        print(Min1 + Min2, Max1 + Max2)

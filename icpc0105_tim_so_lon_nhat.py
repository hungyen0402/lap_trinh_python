def char_num(c):
    if ord('0') <= ord(c) <= ord('9'):
        return True
    else:
        return False 
def chuyen(a):
    ans = 0 
    for i in range(len(a)):
        ans += a[i] * pow(10, len(a)-i-1)
    return ans 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        stack = []
        ans = 0 
        for c in s:
            if char_num(c):
                stack.append(int(c))
            elif stack:
                x = chuyen(stack)
                if ans < x:
                    ans = x
                stack.clear() 
        if stack: # ví dụ: 12ab29cd34 
            x = chuyen(stack)
            if ans < x:
                ans = x 
        print(ans)
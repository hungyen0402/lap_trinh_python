lst = []
def check(s):
    for x in s:
        if int(x) & 1 == 1:
            return False
    return s == s[::-1] 
def add(a, b):
    for i in range(a, b, 2):
        if (check(str(i))):
            lst.append(i)
add(22, 100)
add(1000, 10000)
add(100000, 1000000)

def solve(n):
    n = int(n)
    for i in lst:
        if (i >= n):
            break
        print(i, end = ' ')
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        solve(input())
# l = ['0', '2', '4', '6', '8']
# def solve(s):
#     s1 = s[::-1]
#     if s1 != s:
#         return False
#     s1 = set(s)
#     for c in s1:
#         if c not in l:
#             return False
#     if s[0] == '0':
#         return False
#     return True

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         for x in range(22, n, 2):
#             s = str(x)
#             if len(s) % 2 == 0:
#                 if solve(s):
#                     print(x, end = ' ') 
#         print()
                
        
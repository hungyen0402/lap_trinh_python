import sys

# if __name__ == '__main__':
    # data = sys.stdin.read.splitlines()   # Đọc toàn bộ đầu vào vào data và chia theo dòng
    # t = int(data[0].strip())
    # line_index = 1
    # for _ in range(t):
    #     n, k = map(int, data[line_index].strip().split())
    #     line_index += 1
    #     a = []
    #     while len(a) < n:
    #         a.extend(map(int, data[line_index].strip().split()))  # Dùng extend vì không biết số phần tử trên mỗi dòng
    #         line_index += 1
    #     for x in a:
    #         print(x)
    
if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    # print(t)
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())
        #print(n, k)
        a = []
        while len(a) < n:
            a.extend(map(int, sys.stdin.readline().strip().split()))
        for x in a:
            print(x)
        


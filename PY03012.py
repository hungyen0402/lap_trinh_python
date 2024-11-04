if __name__ == '__main__':
    n = int(input())
    my_list = []
    for _ in range(n):
        s = input() # tên sinh viên 
        c, t = map(int, input().split())
        l = []
        l.append(s)
        l.append(c)
        l.append(t)
        my_list.append(l)
    my_list.sort(key = lambda x: (-x[1], x[2], x[0]))
    for l in my_list:
        for x in l:
            print(x, end = ' ')
        print('\n')
    
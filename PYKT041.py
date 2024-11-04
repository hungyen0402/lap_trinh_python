
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        a.append(s)
    cnt = 0 
    for i in range(n):
        x = 0 
        y = 0
        for j in range(n):
            if a[i][j] == 'C':
                x += 1
            if a[j][i] == 'C':
                y += 1
        sum = x*(x-1)/2 + y*(y-1)/ 2
        cnt += sum
        # print(f"hang cot {i}: {sum}")
    print(int(cnt))

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        dict = {}
        for _ in range(n):
            x = int(input())
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        max_cnt = max(dict.values())
        ans = 1000
        for key, value in dict.items():
            if value == max_cnt and key < ans:
                ans = key
        print(ans)
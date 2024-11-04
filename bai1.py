def min_time_to_create_n_chars(n, x, y, z):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    dp[1] = x  # Chỉ cần 1 thao tác insert để có 1 ký tự

    for i in range(2, n + 1):
        # Thêm một ký tự
        dp[i] = min(dp[i], dp[i - 1] + x)

        # Copy tất cả và paste (áp dụng nếu i là số chẵn hoặc là bội số)
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + z * (i // j - 1))

    return dp[n]


t = int(input().strip())
for _ in range(t):
    n = int(input())
    x, y, z = map(int, input().split())
    result = min_time_to_create_n_chars(n, x, y, z)
    print(result)


# for t in range(int(input())):
#     n = int(input())
#     x, y, z = map(int, input().split())
#     dp = [10**5 for i in range(n+1)]
#     dp[0]=0
#     for i in range(1, n+1):
#         dp[i] = min(dp[i], dp[i-1] + x)
#         if i%2==0:
#             dp[i] = min(dp[i], dp[i//2] + z)
#             dp[i] = min(dp[i], dp[(i//2)+1] + y + z)
#         else: 
#             dp[i] = min(dp[i], dp[(i-1)//2] + z + x)
#             dp[i] = min(dp[i], dp[(i+1)//2] + y + z)
#     print(dp[n])
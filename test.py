def solve():
    t = int(input())  # số lượng bộ test
    for _ in range(t):
        n = int(input())  # số phần tử của mảng
        A = list(map(int, input().split()))  # mảng A
        
        # Kết quả sẽ lưu ở đây
        result = [0] * n
        stack = []
        
        for i in range(n):
            # Loại bỏ các phần tử nhỏ hơn A[i] khỏi stack
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
                
            # Tính độ dài đoạn liên tiếp nhỏ hơn hoặc bằng A[i]
            if stack:
                result[i] = i - stack[-1]
            else:
                result[i] = i + 1
                
            # Đẩy chỉ số hiện tại vào stack
            stack.append(i)
        
        # In kết quả cho test case này
        print(' '.join(map(str, result)))

# Chạy chương trình
solve()
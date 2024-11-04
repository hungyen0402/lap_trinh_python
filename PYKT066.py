import sys
import math

# Hàm tính GCD của một dãy các số
def gcd_of_subarray(arr):
    result = arr[0]
    for num in arr[1:]:
        result = math.gcd(result, num)
        if result == 1:  # Nếu GCD đã là 1 thì không cần kiểm tra tiếp
            break
    return result

# Hàm chính để giải quyết từng bộ test
def find_min_length_subarray_with_gcd_k(N, K, A):
    min_length = float('inf')
    found = False
    
    # Duyệt qua từng vị trí bắt đầu của dãy con
    for i in range(N):
        current_gcd = A[i]
        
        # Kiểm tra các dãy con bắt đầu từ vị trí i
        for j in range(i, N):
            current_gcd = math.gcd(current_gcd, A[j])
            
            # Nếu GCD bằng K, cập nhật độ dài nhỏ nhất
            if current_gcd == K:
                min_length = min(min_length, j - i + 1)
                found = True
                break  # Dừng lại vì dãy con đã thỏa mãn
            
            # Nếu GCD nhỏ hơn K, không cần kiểm tra thêm vì các phần tử sau sẽ không làm tăng GCD
            if current_gcd < K:
                break
    
    return min_length if found else -1

# Đọc dữ liệu từ input
input = sys.stdin.read
data = input().splitlines()
T = int(data[0].strip())  # Số lượng bộ test
result = []

line_index = 1
for _ in range(T):
    N, K = map(int, data[line_index].strip().split())
    line_index += 1
    A = list(map(int, data[line_index].strip().split()))
    line_index += 1
    
    # Tìm độ dài nhỏ nhất của dãy con thỏa mãn điều kiện
    result.append(str(find_min_length_subarray_with_gcd_k(N, K, A)))

# In kết quả cho từng bộ test
print("\n".join(result))

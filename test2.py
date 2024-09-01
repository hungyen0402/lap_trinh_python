import sys
from array import array

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đọc đầu vào
input = sys.stdin.read
data = input().split()

# Lấy kích thước của ma trận
N, M = int(data[0]), int(data[1])

# Xử lý ma trận và lưu vào array
result = array('i')
idx = 2  # Bắt đầu từ phần tử thứ 3 trong danh sách data
for i in range(N):
    for j in range(M):
        value = int(data[idx])
        result.append(1 if is_prime(value) else 0)
        idx += 1

# In kết quả (cắt ma trận thành các hàng để in)
for i in range(N):
    print(' '.join(map(str, result[i*M:(i+1)*M])))

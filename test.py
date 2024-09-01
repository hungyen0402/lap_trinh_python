from math import sqrt
from array import array
N, M = 1 + 2*10**6, 2*10**6
U = array('i', [0]*N)
for i in range(2, int(sqrt(M))+1):
    if U[i] == 0:
        U[i] = i
        for u in range(i, M//i+1): U[i*u]=i
del M 
del u
for i in range(4,N): U[i] += U[i//U[i]] if U[i] else i
from sys import stdin
n, s = int(stdin.readline()), 0
while 1:
    try:
        x = int(stdin.readline())
        s += U[x]
    except: break
print(s)


from math import sqrt        # Nhập hàm tính căn bậc hai
from array import array      # Nhập module array để sử dụng mảng tối ưu bộ nhớ

# Khởi tạo các biến và mảng cần thiết
N, M = 1 + 2*10**6, 2*10**6  # N là giá trị tối đa cần xử lý, M là giới hạn số nguyên tố cần tính
U = array('i', [0]*N)        # Tạo mảng U với kích thước N và gán tất cả các phần tử bằng 0

# Đánh dấu các số nguyên tố và tìm ước số nguyên tố nhỏ nhất cho mỗi số
for i in range(2, int(sqrt(M))+1):  # Duyệt qua các số từ 2 đến căn bậc hai của M
    if U[i] == 0:                   # Nếu U[i] bằng 0, tức là i là số nguyên tố
        U[i] = i                    # Đánh dấu U[i] bằng chính giá trị i
        for u in range(i, M//i+1):  # Duyệt qua các bội số của i
            U[i*u] = i              # Gán giá trị U[i*u] bằng i (i là ước số nhỏ nhất của i*u)

# Xóa các biến tạm không cần thiết để tiết kiệm bộ nhớ
del M 
del u

# Tính tổng các ước số nguyên tố cho mỗi số từ 4 đến N
for i in range(4,N): 
    U[i] += U[i//U[i]] if U[i] else i  # Nếu U[i] khác 0, cộng U[i//U[i]] vào U[i]. Nếu U[i] bằng 0 (số nguyên tố), gán U[i] bằng i

# Đọc đầu vào và tính tổng các ước số nguyên tố cho các số được nhập vào
from sys import stdin         # Nhập module sys để sử dụng stdin (tối ưu tốc độ đọc)
n, s = int(stdin.readline()), 0  # Đọc số lượng số nguyên N, khởi tạo biến s để lưu tổng các ước số nguyên tố

while 1:                      # Vòng lặp vô hạn để đọc các số nguyên từ đầu vào
    try:
        x = int(stdin.readline())  # Đọc từng số nguyên x
        s += U[x]                  # Cộng giá trị U[x] (tổng các ước số nguyên tố của x) vào s
    except: 
        break                    # Khi không còn dữ liệu đầu vào, thoát vòng lặp

print(s)  # In ra kết quả là tổng các ước số nguyên tố của tất cả các số được nhập vào

mod = 1000000007  # Định nghĩa hằng số mod là 10^9 + 7 để sử dụng cho các phép toán modulo.

def pow(a: int, b: int):
    # Hàm để tính a^b modulo mod bằng cách sử dụng lũy thừa nhanh (exponentiation by squaring).
    if b == 1:
        return a  # Trường hợp cơ bản: nếu b là 1, trả về a.
    if b & 1:
        # Nếu b là lẻ, sử dụng đệ quy để tính a^(b-1) và nhân với a.
        return pow(a, b - 1) * a % mod
    # Nếu b là chẵn, tính a^(b//2) và bình phương kết quả.
    p = pow(a, b >> 1)  # Dịch phải b một bit tương đương với chia b cho 2.
    return p * p % mod  # Trả về p^2 modulo mod.

def cal(n: int, k: int):
    # Hàm để tính số đặc biệt thứ k của n.
    if k <= 1:
        return k  # Nếu k <= 1, trả về k (k có thể là 0 hoặc 1).
    
    ex = 0  # Khởi tạo biến để lưu trữ chỉ số bit.
    # Tìm chỉ số của bit cao nhất có giá trị là 1 trong k - 1.
    while (k >> ex) ^ 1:
        ex += 1  # Tăng ex cho đến khi tìm thấy bit cao nhất là 1.
    
    # Tính lũy thừa n^ex và gọi đệ quy cal với k đã được thay đổi.
    return pow(n, ex) + cal(n, k ^ (1 << ex))  # Tính n^ex cộng với kết quả của cal.

# Vòng lặp đọc đầu vào và xử lý cho từng bộ test case.
for t in range(int(input())):  # Nhập số lượng test case.
    n, k = map(int, input().split())  # Nhập n và k cho mỗi test case.
    print(cal(n, k) % mod)  # Tính số đặc biệt thứ k của n và in kết quả theo modulo.

def find_zodiac(d, m):
    # Danh sách các khoảng thời gian và tên cung hoàng đạo
    zodiac_dates = [
        ((21, 3), (19, 4), "Bach Duong"),
        ((20, 4), (20, 5), "Kim Nguu"),
        ((21, 5), (20, 6), "Song Tu"),
        ((21, 6), (22, 7), "Cu Giai"),
        ((23, 7), (22, 8), "Su Tu"),
        ((23, 8), (22, 9), "Xu Nu"),
        ((23, 9), (22, 10), "Thien Binh"),
        ((23, 10), (22, 11), "Thien Yet"),
        ((23, 11), (21, 12), "Nhan Ma"),
        ((22, 12), (19, 1), "Ma Ket"),
        ((20, 1), (18, 2), "Bao Binh"),
        ((19, 2), (20, 3), "Song Ngu")
    ]
    
    # Duyệt qua danh sách để tìm cung hoàng đạo tương ứng
    for start, end, zodiac in zodiac_dates:
        if (m == start[1] and d >= start[0]) or (m == end[1] and d <= end[0]):
            return zodiac

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    d, m = map(int, input().split())
    print(find_zodiac(d, m))

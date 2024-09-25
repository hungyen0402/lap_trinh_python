class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color_str = color
    
    def perimeter(self):
        # Tính chu vi hình chữ nhật
        return 2 * (self.length + self.width)
    
    def area(self):
        # Tính diện tích hình chữ nhật
        return self.length * self.width
    
    def color(self):
        # Chuyển đổi màu sắc về dạng chuẩn: chữ cái đầu viết hoa, các chữ cái sau viết thường
        return self.color_str.capitalize()
    
    def is_valid(self):
        # Kiểm tra xem hình chữ nhật có hợp lệ hay không (các cạnh phải nguyên dương)
        return self.length > 0 and self.width > 0

if __name__ == '__main__':
    # Đọc và tách chuỗi đầu vào thành các phần tử riêng lẻ
    arr = input().split()
    length = int(arr[0])
    width = int(arr[1])
    color = arr[2]

    # Tạo đối tượng Rectangle
    r = Rectangle(length, width, color)
    
    # Kiểm tra tính hợp lệ
    if r.is_valid():
        # In chu vi, diện tích và màu sắc theo đúng định dạng yêu cầu
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        # In ra INVALID nếu dữ liệu không hợp lệ
        print('INVALID')

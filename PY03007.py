import re

def process_text():
    # Đọc dữ liệu đầu vào
    input_text = ""
    try:
        while True:
            line = input().strip()
            if not line:
                break
            input_text += line + " "
    except EOFError:
        pass

    # Xử lý, tách câu dựa vào các dấu câu . ? !
    sentences = re.split(r'[.?!]', input_text)
    
    my_dict = {}
    sentence_id = 1
    
    # Duyệt qua từng câu và xử lý
    for sentence in sentences:
        sentence = sentence.strip()  # Loại bỏ khoảng trắng thừa
        if sentence:  # Nếu câu không rỗng
            # Chuẩn hóa câu: chữ cái đầu viết hoa, các ký tự còn lại viết thường
            words = sentence.split()
            normalized_sentence = words[0].capitalize() + " " + " ".join(word.lower() for word in words[1:])
            
            # Lưu câu vào dictionary
            my_dict[sentence_id] = normalized_sentence
            sentence_id += 1
    
    # In ra các câu theo định dạng yêu cầu
    for i in range(1, sentence_id):
        print(my_dict[i])

# Gọi hàm để chạy chương trình
process_text()

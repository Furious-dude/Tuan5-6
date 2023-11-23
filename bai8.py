def count_characters(input_string):
    # Tạo từ điển ban đầu
    char_dict = {}

    # Duyệt qua từng kí tự trong chuỗi
    for char in input_string:
        # Cập nhật từ điển: tăng giá trị của key nếu đã tồn tại, hoặc thêm key mới với giá trị là 1
        char_dict[char] = char_dict.get(char, 0) + 1

    # In từ điển ra màn hình
    print("Từ điển kí tự và số lần xuất hiện:")
    for char, count in char_dict.items():
        print(f"Kí tự: {char}, Số lần xuất hiện: {count}")

    # Trả về từ điển
    return char_dict

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Đếm số lần xuất hiện của các kí tự và in kết quả
character_count_dict = count_characters(input_string)
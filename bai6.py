def find_lucky_number_pairs(input_set, lucky_number):
    # Kiểm tra và thêm số 11 vào set nếu chưa có
    if 11 not in input_set:
        input_set.add(11)

    # In set ra màn hình
    print("Set sau khi thêm số 11:")
    print(input_set)

    # Tạo danh sách các cặp số có tổng bằng con số may mắn
    number_pairs = []
    for num1 in input_set:
        for num2 in input_set:
            if num1 + num2 == lucky_number:
                number_pairs.append((num1, num2))

    # Tạo tuple chứa các cặp số
    number_pairs_tuple = tuple(number_pairs)

    # Tính tổng của tuple
    total = sum([sum(pair) for pair in number_pairs_tuple])

    # In kết quả ra màn hình
    print("Các cặp số có tổng bằng con số may mắn:")
    print(number_pairs_tuple)
    print("Tổng của các cặp số:")
    print(total)

# Nhập set từ người dùng
print("Nhập set (các số cách nhau bằng dấu cách):")
input_set = set(map(int, input().split()))

# Nhập con số may mắn từ người dùng
lucky_number = int(input("Nhập con số may mắn: "))

# Tìm cặp số và tính tổng
find_lucky_number_pairs(input_set, lucky_number)
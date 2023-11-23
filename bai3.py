def find_most_frequent_words(text):
    # Tách chuỗi thành danh sách các từ
    words = text.split()

    # Đếm số lần xuất hiện của từng từ
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Tìm giá trị tối đa trong từ điển
    max_count = max(word_count.values())

    # Lọc các từ xuất hiện nhiều nhất
    most_frequent_words = [word for word, count in word_count.items() if count == max_count]

    # Trả về tuple chứa danh sách các từ xuất hiện nhiều nhất và số lần xuất hiện
    return tuple((most_frequent_words, max_count))

# Nhập đoạn văn bản từ người dùng
text = input("Nhập đoạn văn bản: ")

# Tìm các từ xuất hiện nhiều nhất
result = find_most_frequent_words(text)

# In kết quả
print("Các từ xuất hiện nhiều nhất và số lần xuất hiện:")
print(result)
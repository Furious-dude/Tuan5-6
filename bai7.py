def process_student_records(student_records):
    # Tạo từ điển ban đầu
    student_dict = student_records

    # Đếm số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]
    count = sum(2.5 <= score <= 3.5 for score in student_dict.values())

    # Bổ sung thêm một sinh viên vào từ điển
    new_student_id = input("Nhập mã sinh viên mới: ")
    new_student_score = float(input("Nhập điểm tổng kết của sinh viên mới: "))
    student_dict[new_student_id] = new_student_score

    # Xóa các sinh viên có điểm tổng kết nhỏ hơn 2.0
    student_dict = {student_id: score for student_id, score in student_dict.items() if score >= 2.0}

    # In toàn bộ từ điển ra màn hình
    print("Từ điển sinh viên:")
    for student_id, score in student_dict.items():
        print(f"Mã sinh viên: {student_id}, Điểm tổng kết: {score}")

    # Trả về số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]
    return count

# Tạo từ điển ban đầu với các khóa và giá trị
student_records = {
    "SV001": 2.8,
    "SV002": 3.2,
    "SV003": 1.5,
    "SV004": 3.6,
    "SV005": 2.9
}

# Xử lý thông tin sinh viên và in kết quả
count_within_range = process_student_records(student_records)
print(f"Số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]: {count_within_range}")
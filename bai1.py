def process_registration_lists(set1, set2):
    
    common_students = set1.intersection(set2)
    print("Sinh viên đăng ký tại cả hai bàn:", common_students)

    
    all_students = set1.union(set2)
    print("Danh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn:", all_students)

    
    exclusive_to_table1 = set1.difference(set2)
    print("Danh sách sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2:", exclusive_to_table1)

    
    exclusive_to_one_table = set1.symmetric_difference(set2)
    print("Danh sách sinh viên đăng ký ở duy nhất 1 bàn:", exclusive_to_one_table)


print("Nhập danh sách sinh viên đăng ký tại bàn 1 (cách nhau bởi dấu cách):")
registration_list1 = set(input().split())


print("Nhập danh sách sinh viên đăng ký tại bàn 2 (cách nhau bởi dấu cách):")
registration_list2 = set(input().split())


process_registration_lists(registration_list1, registration_list2)
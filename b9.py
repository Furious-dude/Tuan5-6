def build_champion_dictionary(champion_list, data_list):
    # Tạo từ điển ban đầu
    champion_dict = {}

    # Duyệt qua danh sách championLOL và dataLOL để tạo từ điển
    for i in range(len(champion_list)):
        champion_name = champion_list[i]
        champion_data = data_list[i]
        champion_dict[champion_name] = champion_data

    return champion_dict

# Xây dựng từ điển dựa trên hai danh sách championLOL và dataLOL
champion_dictionary = build_champion_dictionary(champion_list, data_list)

# Kiểm tra sự tồn tại của champion nhập từ bàn phím
champion_name = input("Nhập tên champion: ")
if champion_name in champion_dictionary:
    champion_price = champion_dictionary[champion_name]["price"]
    print(f"Giá của champion {champion_name}: {champion_price}")
else:
    print("Champion không tồn tại trong danh sách.")
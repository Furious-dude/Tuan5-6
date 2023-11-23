def find_largest_subset(input_set, target_sum):
    largest_subset = set()
    current_subset = set()

    def backtrack(subset, remaining_sum, start_index):
        nonlocal largest_subset

        if remaining_sum == 0:
            if len(subset) > len(largest_subset):
                largest_subset = subset.copy()
            return

        if remaining_sum < 0 or start_index >= len(input_set):
            return

        for i in range(start_index, len(input_set)):
            num = input_set[i]
            subset.add(num)
            backtrack(subset, remaining_sum - num, i + 1)
            subset.remove(num)

    backtrack(current_subset, target_sum, 0)
    return largest_subset


n = int(input("Nhập số lượng phần tử của set: "))
input_set = set()
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    input_set.add(num)


target_sum = int(input("Nhập tổng mục tiêu: "))


largest_subset = find_largest_subset(input_set, target_sum)


print("Tập hợp con lớn nhất thỏa mãn điều kiện:")
print(largest_subset)
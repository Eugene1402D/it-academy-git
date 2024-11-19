def count_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
    return count


my_list = [1, 2, 1, 1]
print("Количество пар:",count_pairs(my_list))

def count_deep_list(lst, level=1):
    max_level = level
    for i in lst:
        if type(i) is list:
            max_level = max(max_level, count_deep_list(i, level + 1))

    return max_level


my_list = [1, 3, [4, [6, 9, 10, [12, 13], 11], 7, 8], 5]
res = count_deep_list(my_list)
print("Максимальная глубина вложенности списков:", res)

def increment_number(number_list: list) -> list:
    str_num = ""
    for i in number_list:
        str_num += str(i)
    int_num = int(str_num) + 1
    return list(str(int_num))


list_num = [1, 9, 9]
result = increment_number(list_num)
print(result)

def count_dif(lst1, lst2):
    change_list = int(input("Выберите список для проверки (1 или 2): "))
    if change_list == 1:
        res = [x for x in lst1 if x not in lst2]
    else:
        res = [y for y in lst2 if y not in lst1]
    return len(res)


list_1 = [1, 7, 3, 6, 1]  # как учитывать дубли внутри списка?
list_2 = [2, 3, 4, 5, 4, 9]
result = count_dif(list_1, list_2)
print("Количество чисел, отличающихся от чисел другого списка:", result)

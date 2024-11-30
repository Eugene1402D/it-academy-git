def count_dif(lst_1, lst_2):
    res = [x for x in lst_1 if x not in lst_2] + [y for y in lst_2 if y not in lst_1]
    return len(res)


list_1 = [1, 2, 3, 1]
list_2 = [2, 3, 4, 5, 4]
result = count_dif(list_1, list_2)
print("Количество различных чисел в обеих списках:", result)

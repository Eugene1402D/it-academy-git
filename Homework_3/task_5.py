def filter_list(lst):
    new_list = []
    for i in lst:
        if lst.count(i) == 1:
            new_list.append(i)
    return new_list


my_list = [1, 'a', 2, 'abc', 1, False]
print("new_list:", filter_list(my_list))

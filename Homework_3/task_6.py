def sort_list(lst):
    count = 0
    for index, value in enumerate(lst):
        if value != 0:
            lst[count], lst[index] = lst[index], lst[count]
            count += 1
    return lst


list_of_numbers = [0, 3, 0, 0, 12, 6, 0, 1, 0]
print("sort_list:", sort_list(list_of_numbers))

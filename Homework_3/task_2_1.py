def create_new_list(list_1, list_2):
    new_list = [i + j for i in list_1 for j in list_2]
    print("new_list:", new_list)
    slice_from_new_list = new_list[::2]
    return slice_from_new_list


first_char = ['a', 'b']
second_char = ['b', 'c', 'd']
print("slice_from_new_list", create_new_list(first_char, second_char))

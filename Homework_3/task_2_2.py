def create_new_list(list_1, list_2):
    new_list = [str(i) + j for i in first_char for j in second_char]
    return new_list

def del_elem_from_list(my_list):
    del_elem = my_list.pop(1)
    return del_elem

def copy_add(other_list):
    last_list = other_list[:]
    last_list.append('2a')
    return last_list

first_char = [1, 2, 3, 4]
second_char = ['a']
my_list = create_new_list(first_char, second_char)
print("new_list:", my_list)

del_elem = del_elem_from_list(my_list)
print("Удаленный элемент:", del_elem)
print("my_list:", my_list)

last_list = copy_add(my_list)
print("Модифицированный список:", last_list)

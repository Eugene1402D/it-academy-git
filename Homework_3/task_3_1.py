def tuple_from_list(my_list):
    my_tuple = tuple(my_list)
    return my_tuple


my_list = ["a", "b", "c"]
print("my_tuple:", tuple_from_list(my_list))


def list_from_tuple(my_tuple):
    new_list = list(my_tuple)
    return new_list


my_tuple = ("a", "b", "c")
print("new_list:", list_from_tuple(my_tuple))

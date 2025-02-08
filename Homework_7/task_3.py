def check_list(lst: list, aim: int) -> list:
    my_dict = {}
    for i_elem, value in enumerate(lst):
        if aim - value in my_dict:
            return [my_dict[aim - value], i_elem]
        my_dict[value] = i_elem
    return []


nums = [2, 15, 7, 11]
target = 9
print(check_list(nums, target))

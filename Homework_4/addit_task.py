def create_dict():
    count = 0
    my_dict = {}

    def inner(obj):
        nonlocal count
        count += 1
        my_dict[count] = obj
        return my_dict

    return inner


f_1 = create_dict()
print(f_1("hello"))
print(f_1(100))
print(f_1([1, 2, 3]))
f_2 = create_dict()
print(f_2("PoweR"))

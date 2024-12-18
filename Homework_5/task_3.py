def my_decor(valid_func):
    def inner(func):
        def wrapper(args):
            if not valid_func(args):
                raise ValueError(
                    f"Аргумент {args} {type(args)} не соответствует проверяемому типу данных.")
            return func(args), args

        return wrapper

    return inner


def check_arg(x):
    return isinstance(x, list)


def return_type_func(x):
    return type(x)


try:
    res = my_decor(check_arg)(return_type_func)
    result, arg = res([1, 2, 3])
    print(f"Аргумент {arg} соответствует проверяемому типу данных:", result)
except ValueError as e:
    print(e)

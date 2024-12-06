def my_func():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return counter, get_count


call_func, get_count = my_func()
call_func()
call_func()
call_func()
call_func()
call_func()
res = get_count()
print(f"Функция my_func() была вызвана {res} раз.")

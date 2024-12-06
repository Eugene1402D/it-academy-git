import time


def my_decorator(seconds):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(1)
            my_res = func(*args, **kwargs)
            finish = time.time()
            if seconds:
                print(f"Функция - {func.__name__} отработала за {round(finish - start, 4)} сек.")
            else:
                print(f"Функция - {func.__name__} отработала за {round((finish - start) / 60, 4)} мин.")
            return my_res, args

        return wrapper

    return inner


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


res = my_decorator(seconds=False)(fibonacci)
result, arg = res(25)
print("Результат работы функции:", result)
print("Аргумент функции:", *arg)

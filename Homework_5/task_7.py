def check_zero(func, max_time):
    count = 0

    def wrapper(num_1, num_2):
        nonlocal count
        while count < max_time:
            count += 1
            print(f"Функция divide() вызвана {count} раз.")
            if num_2 == 0:
                print("Делить на 0 нельзя.")
                return None
            return func(num_1, num_2)
        else:
            print("Достигнут лимит использования функции divide().")
            return None

    return wrapper

number = 3  # int(input("Введите лимит по использованию функции: "))
def divide(num_1, num_2):
    return num_1 / num_2


result = check_zero(divide, number)
print("Результат:", result(15, 3))
print("Результат:", result(3, 0))
print("Результат:", result(7, 2))
print("Результат:", result(9, 4))

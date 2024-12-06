def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) * num


number = 5  # int(input("Введите целое положительное число: ")
print(f"Факториал числа {number}: {fact(number)}")

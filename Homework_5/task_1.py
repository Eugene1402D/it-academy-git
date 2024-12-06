import random


def random_string_generator(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "<", ">", "^", "?"]

    all_char = letters + numbers + symbols
    for i in range(length):
        yield random.choice(all_char)


num = 12  # int(input("Введите длину генерируемой строки: "))
random_string = "".join(random_string_generator(num))


def writing_to_file(string):
    with open("task_1.2.txt", "a+") as file:
        file.write(string + " ")
        return file


new_string = writing_to_file(random_string)
with open("task_1.2.txt", "r") as f:
    print(f.read())

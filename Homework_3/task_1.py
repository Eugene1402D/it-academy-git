def fizz_buzz(my_list):
    new_list = [
        ("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)
        for i in my_list]
    for item in new_list:
        print(item)


list_of_numbers = list(range(1, 101))
fizz_buzz(list_of_numbers)

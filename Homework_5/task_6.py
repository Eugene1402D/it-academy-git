def my_function(num_1):

    def mult(num_2):
        nonlocal num_1
        result = num_1 * num_2
        return f"Число {num_1} * {num_2} = {result}"

    return mult


mult_calc = my_function(3)
print(mult_calc(1))
print(mult_calc(2))
print(mult_calc(3))
print(mult_calc(4))
print(mult_calc(5))
